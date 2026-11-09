"""Run with python3 -m scripts.literature_pipeline.cli --help (Python 3.9+)."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import urllib.error
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

from scripts.literature_pipeline.analysis import fetch_evidence, normalize, review, review_fingerprint, route
from scripts.validate_catalog import CatalogValidator

ROOT = Path(__file__).resolve().parents[2]


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def write_atomic(path, text):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def source_transport_unavailable(exc):
    """A host timeout/rate limit is different from a rejected query expression."""
    seen=set()
    while exc is not None and id(exc) not in seen:
        seen.add(id(exc))
        if isinstance(exc,TimeoutError) or getattr(exc,'code',None)==429:return True
        if isinstance(exc,urllib.error.URLError) and isinstance(exc.reason,(TimeoutError,ConnectionError)):return True
        exc=exc.__cause__
    return False


def aliases(paper):
    values = []
    for field in ("doi", "arxiv_id", "pmid", "pmcid"):
        value = str(paper.get(field, "")).strip()
        if value:
            value = unquote(value).lower()
            if field == "doi":
                value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
            if field == "arxiv_id":
                value = re.sub(r"v\d+$", "", value)
            values.append(field + ":" + value)
    # Exact normalized titles only. Fuzzy similarity must never silently merge papers.
    title = re.sub(r"[^\w]", "", paper["title"].casefold())
    if title:
        values.append("title:" + title)
    return values


def connect(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute("PRAGMA foreign_keys=ON")
    db.executescript("""
      CREATE TABLE IF NOT EXISTS papers (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS aliases (alias TEXT PRIMARY KEY, paper_id TEXT NOT NULL REFERENCES papers(id));
      CREATE TABLE IF NOT EXISTS analyses (paper_id TEXT PRIMARY KEY REFERENCES papers(id), fingerprint TEXT NOT NULL, payload TEXT NOT NULL);
      CREATE TABLE IF NOT EXISTS checkpoints (key TEXT PRIMARY KEY, value TEXT NOT NULL);
    """)
    return db


def import_state(db, path):
    if db.execute("SELECT count(*) FROM papers").fetchone()[0] or not Path(path).exists():
        return
    state = json.loads(Path(path).read_text(encoding="utf-8"))
    if state.get("format_version") != 1:
        raise ValueError("unsupported state format")
    with db:
        for item in state["papers"]:
            db.execute("INSERT INTO papers VALUES (?, ?)", (item["id"], stable_json(item)))
        for alias, paper_id in state["aliases"]:
            db.execute("INSERT INTO aliases VALUES (?, ?)", (alias, paper_id))
        for paper_id, fingerprint, payload in state["analyses"]:
            db.execute("INSERT INTO analyses VALUES (?, ?, ?)", (paper_id, fingerprint, stable_json(payload)))
        for key, value in state["checkpoints"].items():
            db.execute("INSERT INTO checkpoints VALUES (?, ?)", (key, value))


def export_state(db, path):
    papers = []
    for (payload,) in db.execute("SELECT payload FROM papers ORDER BY id"):
        paper = json.loads(payload)
        # Full abstracts and full article bodies are not published to GitHub.
        paper.pop("abstract", None)
        papers.append(paper)
    state = {"format_version": 1, "papers": papers,
             "aliases": list(db.execute("SELECT alias,paper_id FROM aliases ORDER BY alias")),
             "analyses": [(pid, fp, json.loads(payload)) for pid, fp, payload in db.execute(
                 "SELECT paper_id,fingerprint,payload FROM analyses ORDER BY paper_id")],
             "checkpoints": dict(db.execute("SELECT key,value FROM checkpoints ORDER BY key"))}
    write_atomic(path, stable_json(state))


def ingest(db, incoming, day, seeded=False):
    paper = dict(incoming)
    if not isinstance(paper.get("title"), str) or not paper["title"].strip():
        raise ValueError("record title missing")
    if not isinstance(paper.get("url"), str) or not paper["url"].startswith("https://"):
        raise ValueError("record requires canonical HTTPS URL")
    ids = aliases(paper)
    strong_matches={row[0] for alias in ids if not alias.startswith('title:')
                    for row in db.execute('SELECT paper_id FROM aliases WHERE alias=?',(alias,))}
    if len(strong_matches)>1:
        raise ValueError("identifier conflict; requires manual reconciliation")
    matches=strong_matches or {row[0] for alias in ids if alias.startswith('title:')
                              for row in db.execute('SELECT paper_id FROM aliases WHERE alias=?',(alias,))}
    if matches and not strong_matches and any(not alias.startswith('title:') for alias in ids):
        # A common title is only a counterpart lead when identifiers differ.
        # In particular it must not silently fuse a preprint with a journal DOI.
        paper['publication_tracking']={'status':'needs_identity_review','issues':[
            {'other_paper_id':next(iter(matches)), 'reason':'Same title but no shared verified identifier; requires manual publication-identity reconciliation'}]}
        matches=set()
    paper_id = next(iter(matches), "p-" + hashlib.sha256(ids[0].encode()).hexdigest()[:20])
    row = db.execute("SELECT payload FROM papers WHERE id=?", (paper_id,)).fetchone()
    old = json.loads(row[0]) if row else {}
    if old:
        merged = dict(old)
        if old.get("discovery_lanes") or paper.get("discovery_lanes"):
            merged["discovery_lanes"] = sorted(set(old.get("discovery_lanes",[])) | set(paper.get("discovery_lanes",[])))
        for field, value in paper.items():
            if value and field not in {"id", "first_seen", "last_changed", "seeded", "abstract", "sources", "version", "updated", "discovery_lanes"}:
                if field in {"title", "url", "authors", "published", "year"} and merged.get(field):
                    continue
                merged[field] = value
        priority = {"arxiv": 3, "europepmc": 2, "pubmed": 1}
        owner = old.get("abstract_source", "")
        source = incoming.get("source", "")
        newer = str(incoming.get("updated", "")) >= old.get("abstract_updated", "")
        if paper.get("abstract") and (not owner or priority.get(source, 0) > priority.get(owner, 0) or (source == owner and newer)):
            merged["abstract"] = normalize(paper["abstract"])
            merged["abstract_source"] = source
            merged["abstract_updated"] = str(incoming.get("updated", ""))
        for field in ("updated", "version"):
            a, b = str(old.get(field, "")), str(paper.get(field, ""))
            merged[field] = str(max(int(a or 0), int(b or 0))) if field == "version" and (a or b) and (a or "0").isdigit() and (b or "0").isdigit() else max(a, b)
        paper = merged
    paper["id"] = paper_id
    if paper.get("abstract") and not paper.get("abstract_source"):
        paper["abstract_source"] = incoming.get("source", "")
        paper["abstract_updated"] = str(incoming.get("updated", ""))
    paper.setdefault("updated", "")
    paper.setdefault("version", "")
    paper["first_seen"] = old.get("first_seen", day)
    paper["seeded"] = old.get("seeded", seeded)
    paper["sources"] = sorted(set(old.get("sources", [])) | {incoming.get("source", "catalog")})
    if paper.get("abstract"):
        paper["abstract_hash"] = hashlib.sha256(normalize(paper["abstract"]).encode()).hexdigest()
    paper.setdefault("abstract_hash", old.get("abstract_hash", ""))
    significant = ("title", "abstract_hash", "updated", "version", "doi", "pmcid")
    changed = not old or any(paper.get(key, "") != old.get(key, "") for key in significant)
    paper["last_changed"] = day if changed else old["last_changed"]
    with db:
        db.execute("INSERT OR REPLACE INTO papers VALUES (?, ?)", (paper_id, stable_json(paper)))
        for alias in ids:
            db.execute("INSERT OR IGNORE INTO aliases VALUES (?, ?)", (alias, paper_id))
    return paper_id, changed


def seed_catalog(db, path, day):
    structured = Path(path).parent / 'data/catalog.json'
    if structured.exists():
        for record in json.loads(structured.read_text()):
            paper = {key:record[key] for key in ('title','year','doi','arxiv_id','pmid','authors') if record.get(key)}
            paper.update(url=record['links']['Paper'], source='catalog', published=record.get('publication_date',record['year']))
            ingest(db, paper, day, seeded=True)
        return
    text = Path(path).read_text(encoding="utf-8")
    if '## 📝 Papers' in text:
        main = text.split('## 📝 Papers',1)[1].split('## 🧰 Datasets, Benchmarks and Toolkits',1)[0]
    else:
        main = text.split("## 📝 Fairness Papers", 1)[1].split("## 🧭 By Topic", 1)[0]
    for entry in CatalogValidator.entries(main):
        urls = re.findall(r"\]\((https://.*?)(?:\)\]|\)(?=\s|$))", entry.block)
        def find(pattern):
            match = re.search(pattern, entry.block, re.I)
            return match.group(1) if match else ""
        paper = {"title": entry.title, "url": urls[0], "source": "catalog", "year": entry.section,
                 "arxiv_id": find(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})"),
                 "doi": find(r"doi\.org/(10\.[^\s]+?)(?:\)\]|\)(?=\s|$))"), "pmid": find(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)")}
        ingest(db, paper, day, seeded=True)


def review_pending(db, day, limit, full_text, decisions=None, catalog_records=None):
    endpoint = os.environ.get("LITERATURE_LLM_ENDPOINT", "")
    model = os.environ.get("LITERATURE_LLM_MODEL", "")
    key = os.environ.get("LITERATURE_LLM_API_KEY", "")
    if not endpoint or not model:
        return {"mode": "metadata_only", "reviewed": 0, "failures": 0}
    parsed = urlsplit(endpoint)
    if parsed.scheme != "https" and not (parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1", "::1"}):
        raise ValueError("model endpoint must use HTTPS (HTTP only allowed on localhost)")
    if parsed.username or parsed.password or parsed.query:
        raise ValueError("model endpoint must not contain embedded credentials/query parameters")
    provider = os.environ.get("LITERATURE_LLM_CACHE_NAMESPACE") or hashlib.sha256(endpoint.encode()).hexdigest()[:16]
    papers = [json.loads(row[0]) for row in db.execute("SELECT payload FROM papers")]
    papers.sort(key=lambda paper: (-route(paper)["priority"], paper["first_seen"], paper["id"]))
    count = failures = 0
    for paper in papers:
        if paper.get("seeded") or not paper.get("abstract") or paper.get('venue_assessment',{}).get('status')=='ineligible':
            continue
        from scripts.publish_catalog import same_record
        if any(same_record(paper,record) for record in (catalog_records or [])):
            continue
        from scripts.screening_policy import current_human_decision
        if current_human_decision(paper,decisions or {}).get('decision') in {'reject','approve'}:
            continue
        fingerprint = review_fingerprint(paper, model, provider)
        previous = db.execute("SELECT fingerprint,payload FROM analyses WHERE paper_id=?", (paper["id"],)).fetchone()
        if previous and previous[0] == fingerprint:
            previous_result = json.loads(previous[1])
            retry_days = 1 if previous_result.get("warning") else 7
            retry_after = (date.fromisoformat(previous_result["reviewed_on"]) + timedelta(days=retry_days)).isoformat()
            if previous_result.get("evidence_level") == "full_text" or day < retry_after:
                continue
        if count + failures >= limit:
            break
        try:
            evidence = fetch_evidence(paper) if full_text else {"text": normalize(paper["abstract"]), "level": "abstract", "url": paper["url"], "warning": ""}
            result = review(paper, evidence, endpoint, model, key)
            result["reviewed_on"] = day
            result["provider"] = provider
            with db:
                db.execute("INSERT OR REPLACE INTO analyses VALUES (?, ?, ?)", (paper["id"], fingerprint, stable_json(result)))
            count += 1
            print(f"Reviewed {paper['id']}: {result['decision']} ({result['evidence_level']})", flush=True)
        except Exception as exc:
            # Never log provider exception messages: they can contain endpoint credentials.
            detail = str(exc) if isinstance(exc, ValueError) else type(exc).__name__
            print(f"Review failed for {paper['id']}: {detail}", file=sys.stderr)
            failures += 1
            # A hard provider quota/configuration failure cannot improve on the
            # next paper. Preserve the queue rather than spending every budget slot.
            if getattr(exc,'code',None) in {400,429}:
                try:provider_error=exc.read(8192).decode('utf-8',errors='replace').casefold()
                except Exception:provider_error=''
                if any(term in provider_error for term in ('usage limit','quota','insufficient balance','unknown or disabled model','model_not_found')):
                    print('Provider unavailable; remaining candidates retained for retry.',flush=True)
                    return {"mode":"model","reviewed":count,"failures":failures,"provider_status":"unavailable"}
    return {"mode": "model", "reviewed": count, "failures": failures}


def markdown(text):
    return str(text).replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;").replace("[", "\\[").replace("]", "\\]")


def enrich_run_status(db, output, decisions, records, tracking, recall):
    from collections import Counter
    from scripts.publish_catalog import same_record
    from scripts.screening_policy import current_human_decision
    papers=[json.loads(row[0]) for row in db.execute('SELECT payload FROM papers')]
    active=[p for p in papers if not p.get('seeded') and not any(same_record(p,r) for r in records)
            and current_human_decision(p,decisions).get('decision')!='reject']
    counts=Counter(p.get('venue_assessment',{}).get('status','pending') for p in active)
    status_path=Path(output)/'run-status.json';status=json.loads(status_path.read_text())
    status['publication_tracking']=tracking
    status['recall_regression']={'passed':recall['passed'],'cases':len(recall['cases'])} if recall else {'enabled':False}
    status['venue_policy']=dict(counts)
    status['human_review']={'pending':sum(current_human_decision(p,decisions).get('decision')!='approve'
                                         and p.get('venue_assessment',{}).get('status')!='ineligible' for p in active),
                            'catalog_total':len(records),'automatic_inclusion':False}
    status['retrieval_progress']='Complete' if all(s['complete'] for s in status['sources']) else 'Partial; failed query watermarks retained'
    write_atomic(status_path,stable_json(status))
    lines=['# 出版渠道资格检查','','仅依据可核实的中科院大类1/2区或CCF A/B会议规则；渠道资格不替代主题证据或人工批准。',
           '未核实渠道保留待办；已确认不达门槛者保存在候选库并列于下方，不自动删除。','',
           '| 候选 | 渠道状态 | 原因 |','|---|---|---|']
    for p in active:
        assessment=p.get('venue_assessment',{})
        lines.append('| ['+markdown(p['title'])+']('+p['url']+') | '+assessment.get('status','pending')+' | '+markdown(assessment.get('reason_zh','待核实'))+' |')
    write_atomic(Path(output)/'venue-policy.md','\n'.join(lines)+'\n')


def render(db, output, day, statuses, review_status, decisions=None, catalog_records=None):
    output = Path(output)
    papers = [json.loads(row[0]) for row in db.execute("SELECT payload FROM papers")]
    analyses = {pid: (fp, json.loads(payload)) for pid, fp, payload in db.execute("SELECT paper_id,fingerprint,payload FROM analyses")}
    candidates = sorted((p for p in papers if not p.get("seeded")), key=lambda p: (-route(p)["priority"], p["id"]))
    from scripts.screening_policy import current_human_decision
    from scripts.publish_catalog import same_record
    candidates=[p for p in candidates if current_human_decision(p,decisions or {}).get('decision')!='reject'
                and not any(same_record(p,q) for q in (catalog_records or []))
                and p.get('venue_assessment',{}).get('status')!='ineligible']
    def current_analysis(paper):
        entry = analyses.get(paper["id"])
        if entry and entry[0] == review_fingerprint(paper, entry[1].get("model", ""), entry[1].get("provider", "")):
            return entry[1]
        return None
    today = [p for p in candidates if p["last_changed"] == day or (current_analysis(p) or {}).get("reviewed_on") == day]
    reviewed_count = sum(current_analysis(p) is not None for p in candidates)
    review_status["available_reviews"] = reviewed_count
    review_status["pending"] = len(candidates) - reviewed_count
    header = [f"# 医疗算法公平性文献摘要 · {day}", "", "机器整理的候选与收录建议；未代表人工审核或实验复现。", "",
              f"候选库：{len(candidates)} 篇；当日发现、更新或完成分析：{len(today)} 篇。", "",
              f"已有有效中文分析：{reviewed_count} 篇；待分析或缺少摘要证据：{len(candidates) - reviewed_count} 篇。", "",
              "## 检索覆盖", ""]
    for status in statuses:
        suffix = "完整" if status.get("complete") else "不完整，进度未推进"
        header.append(f"- {status['source']} / 查询 {status['query_id']}：{status.get('records', 0)} 条；{suffix}" + ("；" + status["error"] if status.get("error") else ""))
    if review_status["mode"] == "metadata_only":
        header += ["", "未配置模型接口：以下仅为检索元数据与规则路由，中文解读和语义筛选待完成。"]
    if review_status["failures"]:
        header += ["", f"模型分析失败 {review_status['failures']} 次，保留候选并等待重试。"]
    lines = header + ["", "## 当日候选", ""]
    decision_labels = {"suggest_include": "建议纳入，待审核", "related": "相关，待核实是否纳入", "hold": "待核验", "exclude": "机器建议排除，待抽查"}
    for paper in today:
        result = current_analysis(paper)
        topics = result["topics"] if result else route(paper)["topics"]
        lines += [f"### [{markdown(paper['title'])}]({paper['url']})", "",
                  f"- 标识：`{paper['id']}`；发表：{markdown(paper.get('published') or paper.get('year') or '未知')}；发现：{paper['first_seen']}",
                  "- 主题：" + ("、".join(topics) or "待分类") + ("" if result else "（规则建议）"),
                  "- 状态：" + (decision_labels[result["decision"]] if result else "待模型分析／人工核验")]
        if result:
            lines += ["", markdown(result["summary_zh"]), "", "限制：" + markdown(result["limitations_zh"]),
                      "", "判断：" + markdown(result["reason_zh"]), "",
                      f"证据层级：{result['evidence_level']}；[来源]({result['evidence_url']})；模型：{markdown(result['model'])}。"]
            if result.get("warning"):
                lines += ["", markdown(result["warning"])]
        lines += [""]
    if not today:
        lines += ["本日没有新增或实质更新的候选。", ""]
    write_atomic(output / "daily" / f"{day}.md", "\n".join(lines))
    write_atomic(output / "latest.md", "\n".join(lines))
    week_start = (date.fromisoformat(day) - timedelta(days=6)).isoformat()
    weekly = [f"# 文献候选七日汇总 · {week_start}—{day}", "", "主题为规则建议或机器分析结果；候选不等同于正式收录。", ""]
    week_papers = [p for p in candidates if week_start <= max(p["last_changed"], (current_analysis(p) or {}).get("reviewed_on", "")) <= day]
    for topic in sorted(set(topic for p in week_papers for topic in ((current_analysis(p) or {}).get("topics", route(p)["topics"]) or ["待分类"]))):
        weekly += ["## " + topic, ""]
        for paper in week_papers:
            result = current_analysis(paper)
            if topic not in ((result or {}).get("topics", route(paper)["topics"]) or ["待分类"]):
                continue
            label = decision_labels[result["decision"]] if result else "待分析／证据不足"
            weekly += [f"- [{markdown(paper['title'])}]({paper['url']}) · {label} · `{paper['id']}`"]
            if result:
                weekly += ["  " + markdown(result["summary_zh"])]
        weekly += [""]
    write_atomic(output / "weekly.md", "\n".join(weekly))
    proposals = ["# 主目录筛选判断证据", "", "机器建议及中文证据，仅供审核；必须由维护者明确通过后才加入主 README。请填写 review-latest.md 或按文章编号回复助手。", ""]
    for paper in candidates:
        result = current_analysis(paper)
        if not result or result["decision"] != "suggest_include":
            continue
        metadata = result["metadata"]
        year = str(paper.get("year") or paper.get("published", "")[:4])
        if not re.fullmatch(r"\d{4}", year):
            continue
        venue = "arXiv" if paper.get("arxiv_id") else "Paper"
        proposals += [f"## {markdown(paper['title'])}", "", f"年度：{year}；主题：{'、'.join(result['topics'])}", "", "```markdown",
            f"- (*{venue}'{year[-2:]}*) **{markdown(paper['title'])}**", f"  [[📝 Paper]({paper['url']})]",
            "  **Metadata:** " + " · ".join(f"`{field}: {' + '.join(metadata[field])}`" for field in ("Domain", "Focus", "Stage", "Attributes")) + " · `Assets: Paper only` · `Evidence: Primary full text`",
            "  > **Why it qualifies:** " + markdown(result["reason_zh"]), "```", "", "### 方法证据", ""]
        proposals += [f"- {name}：{markdown(value['quote'])}" for name, value in result["criteria"].items()]
        proposals += ["", f"[全文证据]({result['evidence_url']})", ""]
    write_atomic(output / "catalog-proposals.md", "\n".join(proposals))
    write_atomic(output / "run-status.json", stable_json({"date": day, "sources": statuses, "analysis": review_status,
                  "candidates": len(candidates), "changed_today": len(today)}))
    return len(candidates), len(today)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=ROOT / "config/literature.json")
    parser.add_argument("--db", type=Path, default=ROOT / ".local/literature.sqlite3")
    parser.add_argument("--state", type=Path, default=ROOT / "data/literature-state.json")
    parser.add_argument("--output", type=Path, default=ROOT / "reports")
    parser.add_argument("--catalog", type=Path, default=ROOT / "README.md")
    parser.add_argument("--publish-root", type=Path, help="Render eligible discoveries directly into this checkout's English README and catalog")
    parser.add_argument("--approval-file", type=Path, help="Markdown review packet with explicit human approvals and matching evidence versions")
    parser.add_argument("--since", type=date.fromisoformat)
    parser.add_argument("--until", type=date.fromisoformat, default=datetime.now(timezone.utc).date()-timedelta(days=1))
    parser.add_argument("--sources", nargs="+", choices=["arxiv", "europepmc", "pubmed"])
    parser.add_argument("--max-records", type=int)
    parser.add_argument("--review-limit", type=int)
    parser.add_argument("--no-full-text", action="store_true")
    parser.add_argument("--no-publication-tracking", action="store_true", help="Skip bounded publication identity metadata checks")
    parser.add_argument("--fixture", type=Path, help="Offline JSON record list; skips all literature API calls")
    parser.add_argument("--metadata-only", action="store_true", help="Never call the model or full-text endpoints")
    parser.add_argument("--require-model", action="store_true", help="Fail rather than silently producing metadata-only output")
    args = parser.parse_args(argv)
    if args.publish_root and not args.approval_file:
        parser.error('--publish-root requires --approval-file with explicit human decisions')
    if args.since and args.since > args.until:
        parser.error("--since must be <= --until")
    if args.require_model and (args.metadata_only or not os.environ.get("LITERATURE_LLM_ENDPOINT") or not os.environ.get("LITERATURE_LLM_MODEL")):
        parser.error("--require-model needs a configured endpoint/model and cannot be combined with --metadata-only")
    config = json.loads(args.config.read_text(encoding="utf-8"))
    maximum = args.max_records if args.max_records is not None else config["max_records_per_query"]
    limit = args.review_limit if args.review_limit is not None else config["max_analyses_per_run"]
    if maximum < 1 or limit < 0:
        parser.error("--max-records must be positive; --review-limit must be nonnegative")
    if args.require_model and limit == 0:
        parser.error("--require-model cannot use a zero review budget")
    recall_config=None;recall_result=None
    if config.get('recall_config'):
        from scripts.recall import load_config,check,queries as recall_queries
        recall_config=load_config(args.config.parent/config['recall_config'])
        recall_result=check(recall_config)
        if not recall_result['passed']:
            raise ValueError('Recall regression failed; fix missing approved-paper sentinels before retrieval')
    day = args.until.isoformat()
    db = connect(args.db)
    try:
        import_state(db, args.state)
        seed_catalog(db, args.catalog, day)
        statuses = []
        if args.fixture:
            for record in json.loads(args.fixture.read_text(encoding="utf-8")):
                ingest(db, record, day)
            statuses.append({"source": "fixture", "query_id": "offline", "complete": True, "records": len(json.loads(args.fixture.read_text()))})
        else:
            from scripts.literature_pipeline.sources import fetch_source
            source_queries={source:[(q,'methodology') for q in queries] for source,queries in config['sources'].items()}
            supplements=config.get('supplementary_sources',{})
            for source,queries in supplements.items():
                source_queries.setdefault(source,[]).extend((q,'review_supplement') for q in queries)
            if recall_config:
                for source,queries in recall_queries(recall_config).items():
                    source_queries.setdefault(source,[]).extend((q,'recall') for q in queries)
            for source, queries in source_queries.items():
                if args.sources and source not in args.sources:
                    continue
                source_unavailable=False
                for query,lane in queries:
                    query_id = hashlib.sha256(query.encode()).hexdigest()[:12]
                    checkpoint_key = source + ":" + query_id
                    previous = db.execute("SELECT value FROM checkpoints WHERE key=?", (checkpoint_key,)).fetchone()
                    since = args.since or (date.fromisoformat(previous[0]) - timedelta(days=config["overlap_days"]) if previous and previous[0] <= day else args.until - timedelta(days=config["initial_days"]))
                    pending_key = "pending-start:" + checkpoint_key
                    pending_end_key = "pending-end:" + checkpoint_key
                    pending = db.execute("SELECT value FROM checkpoints WHERE key=?", (pending_key,)).fetchone()
                    pending_end = db.execute("SELECT value FROM checkpoints WHERE key=?", (pending_end_key,)).fetchone()
                    if pending and not args.since:
                        since = min(since, date.fromisoformat(pending[0]))
                    # Pin an unfinished initial window even if the next run is a week later.
                    with db:
                        db.execute("INSERT OR REPLACE INTO checkpoints VALUES (?, ?)", (pending_key, min(since.isoformat(), pending[0] if pending else since.isoformat())))
                        db.execute("INSERT OR REPLACE INTO checkpoints VALUES (?, ?)", (pending_end_key, max(day, pending_end[0] if pending_end else day)))
                    status = {"source": source, "query_id": query_id, "since": since.isoformat(), "until": day, "complete": False,'lane':lane}
                    print(f"Searching {source}/{query_id}: {since.isoformat()} to {day}", flush=True)
                    try:
                        if source_unavailable:
                            status['attempted']=False
                            status['error']='Source unavailable after exhausted transport retries; this query was not attempted, window retained'
                            statuses.append(status)
                            continue
                        status['attempted']=True
                        result = fetch_source(source, query, since.isoformat(), day, max_records=maximum, email=os.environ.get("NCBI_EMAIL", ""))
                        for record in result["records"]:
                            record['discovery_lanes']=[lane]
                            ingest(db, record, day)
                        status.update(complete=result["complete"], records=len(result["records"]), total=result["total"])
                        if result["complete"]:
                            # Explicit historical runs must not rewind an existing watermark.
                            checkpoint = max(day, previous[0] if previous else day)
                            with db:
                                db.execute("INSERT OR REPLACE INTO checkpoints VALUES (?, ?)", (checkpoint_key, checkpoint))
                                if (not pending or since.isoformat() <= pending[0]) and (not pending_end or day >= pending_end[0]):
                                    db.execute("DELETE FROM checkpoints WHERE key IN (?, ?)", (pending_key, pending_end_key))
                    except Exception as exc:
                        status["error"] = type(exc).__name__ + ": source query failed; retry retained"
                        source_unavailable=source_transport_unavailable(exc)
                    statuses.append(status)
                    print(f"  {status.get('records', 0)} records; complete={status['complete']}" + (f"; {status['error']}" if status.get("error") else ""), flush=True)
        tracking_status={'checked':0,'failures':0,'formal_links':0,'identity_conflicts':0,'pending_checks':0}
        tracking_config=config.get('publication_tracking',{})
        if tracking_config.get('enabled') and not args.fixture and not args.no_publication_tracking:
            from scripts.publication_tracking import track,crossref_candidates
            from scripts.literature_pipeline.sources import fetch_arxiv_identities
            tracking_status=track(db,day,tracking_config,arxiv_fetch=lambda ids:fetch_arxiv_identities(ids,tracking_config.get('timeout_seconds',25)),search=crossref_candidates if tracking_config.get('title_search',True) else None)
        from scripts.venue_policy import load_policy,assess_venue
        venue_policy=load_policy()
        for pid,payload in db.execute('SELECT id,payload FROM papers').fetchall():
            paper=json.loads(payload);paper['venue_assessment']=assess_venue(paper,venue_policy)
            db.execute('UPDATE papers SET payload=? WHERE id=?',(stable_json(paper),pid))
        db.commit()
        ledger_file=args.catalog.parent/'data/curation-decisions.json'
        decisions=json.loads(ledger_file.read_text()) if ledger_file.exists() else {}
        catalog_data=args.catalog.parent/'data/catalog.json'
        records=json.loads(catalog_data.read_text()) if catalog_data.exists() else []
        review_status = {"mode": "metadata_only", "reviewed": 0, "failures": 0} if args.metadata_only else review_pending(db, day, limit, not args.no_full_text, decisions, records)
        export_state(db, args.state)
        candidates, changed = render(db, args.output, day, statuses, review_status, decisions, records)
        publication = {"added": 0, "failures": 0}
        if args.publish_root:
            from scripts.publish_catalog import sync_catalog
            publication = sync_catalog(db, args.publish_root, args.approval_file)
            marker = args.output / 'run-status.json'
            status = json.loads(marker.read_text())
            status['catalog_publication'] = publication
            write_atomic(marker, stable_json(status))
        from scripts.review_workflow import write_review_packet
        write_review_packet(db, args.output, day, args.catalog)
        from scripts.publication_tracking import write_report as tracking_report
        tracking_report(db,args.output,day,tracking_status)
        if recall_result:
            from scripts.recall import report as recall_report
            recall_report(args.output,recall_result)
        enrich_run_status(db,args.output,decisions,records,tracking_status,recall_result)
        print(f"Literature run: {candidates} candidates; {changed} changed/reviewed today; mode={review_status['mode']}.")
        print(f"Reports: {args.output.resolve()}")
        return 2 if any(not status["complete"] for status in statuses) or review_status["failures"] or publication['failures'] or tracking_status['failures'] else 0
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
