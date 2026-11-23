"""Human-editable Markdown review packets and explicit approval loading."""
from __future__ import annotations
import json
import re
import hashlib
from pathlib import Path
from scripts.literature_pipeline.analysis import review_fingerprint, route
from scripts.screening_policy import paper_version, content_version, current_human_decision

DECISIONS = {'待审核':'pending','通过':'approve','纳入':'approve','排除':'reject','暂缓':'hold',
             'pending':'pending','approve':'approve','reject':'reject','hold':'hold'}


def read_decisions(path):
    text = Path(path).read_text()
    decisions = {}
    for match in re.finditer(r'^## (p-[a-f0-9]+)\s*\n(.*?)(?=^## |\Z)', text, re.M|re.S):
        pid, block = match.groups()
        decision = re.search(r'^审核决定[：:][ \t]*([^\n]+)', block, re.M)
        fingerprint = re.search(r'^证据版本[：:][ \t]*([^\n]+)', block, re.M)
        note = re.search(r'^审核备注[：:][ \t]*([^\n]*)', block, re.M)
        if not decision or decision.group(1).strip() not in DECISIONS:raise ValueError('Invalid review decision: '+pid)
        if pid in decisions:raise ValueError('Duplicate review ID: '+pid)
        decisions[pid] = {'decision':DECISIONS[decision.group(1).strip()],
                          'fingerprint':fingerprint.group(1).strip() if fingerprint else '',
                          'note':note.group(1).strip() if note else ''}
    return decisions


def import_human_decisions(review_file, state_file, ledger_file):
    """Explicitly import a maintainer-submitted packet; never called by the timer."""
    decisions=read_decisions(review_file)
    state=json.loads(Path(state_file).read_text())
    papers={p['id']:p for p in state['papers']}
    analyses={pid:(fp,result) for pid,fp,result in state['analyses']}
    ledger_path=Path(ledger_file)
    ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
    source_hash=hashlib.sha256(Path(review_file).read_bytes()).hexdigest()
    for pid,decision in decisions.items():
        if pid not in papers:raise ValueError('Unknown paper ID in human review: '+pid)
        if decision['decision']=='approve' and pid not in analyses:
            raise ValueError('Approved paper has no reviewed evidence version: '+pid)
        if decision['decision']!='pending' and pid in analyses and decision['fingerprint']!=analyses[pid][0]:
            raise ValueError('Human decision refers to a different analysis version: '+pid)
        if decision['decision']=='approve':
            result=analyses[pid][1]
            paper=papers[pid]
            if result.get('content_version') and result['content_version'] != content_version(paper):
                raise ValueError('Human approval refers to a previous article version: '+pid)
            if not result.get('content_version') and result.get('paper_version') and result['paper_version'] != paper_version(paper):
                raise ValueError('Human approval refers to a previous article version: '+pid)
    for pid,decision in decisions.items():
        if decision['decision']=='pending':
            continue
        ledger[pid]={**decision,'paper_version':paper_version(papers[pid]),'content_version':content_version(papers[pid]),'title':papers[pid]['title'],
                     'source_review_sha256':source_hash}
    ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    return ledger


def write_review_packet(db, output, day, catalog, *, archive=True):
    from scripts.publish_catalog import same_record

    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    source = Path(catalog).parent / 'data/catalog.json'
    records = json.loads(source.read_text()) if source.exists() else []
    ledger_file = source.parent / 'curation-decisions.json'
    ledger = json.loads(ledger_file.read_text()) if ledger_file.exists() else {}
    analyses = {pid: (fp, json.loads(payload)) for pid, fp, payload in
                db.execute('SELECT paper_id,fingerprint,payload FROM analyses')}
    path = output / ('review-' + day + '.md')
    prior = read_decisions(path) if path.exists() else {}
    lines = [f'# 文献人工审核单 · {day}', '',
             '初筛推荐且渠道符合条件的候选，方法学优先。预印本单独标注。',
             '可按编号回复通过／排除／暂缓，也可填写审核决定与备注并保留编号、证据版本。通过后进入全文精读。',
             '[排除抽查](screening-exclusions.md) · [证据、渠道与已通过的待办](screening-pending.md)', '']
    exclusions = ['# 初筛排除抽查', '', '保留机器判断和渠道依据。人工排除由审核台账单独保存。', '']
    pending = ['# 初筛与收录待办', '', '等待分析、证据、渠道核验、人工暂缓或通过后处理的候选。', '']
    papers = [json.loads(payload) for payload, in db.execute('SELECT payload FROM papers')]

    def sort_key(paper):
        result = analyses.get(paper['id'], ('', {}))[1]
        kind = result.get('article_type')
        return (kind != 'methodology', kind in {'review', 'commentary'},
                -route(paper)['priority'], paper['first_seen'], paper['id'])

    papers.sort(key=sort_key)
    count = 0
    for paper in papers:
        if paper.get('seeded') or any(same_record(paper, record) for record in records):
            continue
        human = current_human_decision(paper, ledger)
        if human.get('decision') == 'reject':
            continue
        pid = paper['id']
        old = analyses.get(pid)
        if old and old[0] != review_fingerprint(paper, old[1].get('model', ''), old[1].get('provider', '')):
            old = None
        fp, result = old if old else ('待取得有效分析', {})
        venue = paper.get('venue_assessment', {})
        status = venue.get('status', 'pending')
        model = result.get('decision', '待分析')
        title = ' '.join(paper['title'].split()).replace('[', r'\[').replace(']', r'\]')
        link = f'[{title}]({paper["url"]})'
        reason = result.get('reason_zh', '')
        channel = venue.get('reason_zh', '渠道待核')
        if human.get('decision') in {'approve', 'hold'}:
            label = '人工通过后待处理' if human['decision'] == 'approve' else '人工暂缓'
            pending += [f'- `{pid}` {link} · {label} · {channel}']
        elif status == 'ineligible' or model == 'exclude':
            basis = channel if status == 'ineligible' else reason
            exclusions += [f'- `{pid}` {link} · {basis} · [证据]({result.get("evidence_url") or paper["url"]})']
        elif model != 'suggest_include' or status not in {'eligible', 'preprint'}:
            pending += [f'- `{pid}` {link} · {model} · {channel}' + (f' · {reason}' if reason else '')]
        else:
            saved = prior.get(pid, {})
            decision = saved.get('decision') if saved.get('fingerprint') == fp else 'pending'
            label = {'pending': '待审核', 'approve': '通过', 'reject': '排除', 'hold': '暂缓'}[decision]
            rank = next((item for item in venue.get('evidence', []) if item.get('rank')), {})
            rank_text = (f'CAS {rank["rank"]} 区' if rank.get('source') == 'cas' else f'CCF {rank["rank"]}') if rank else ''
            if paper.get('conference_status') in {'accepted', 'accepted-main'}:
                rank_text = (rank_text or channel) + '，会议已列录用，正式出版待核'
            lines += [f'## {pid}', '', f'文章：{link}', '',
                      f'审核决定：{label}', '审核备注：' + (saved.get('note', '') if saved.get('fingerprint') == fp else ''), f'证据版本：{fp}', '',
                      f'渠道：{rank_text or channel} · 类型：{result.get("article_type", "待定")} · 证据：{result["evidence_level"]}',
                      '', result['summary_zh'], '', f'判断：{reason}', '',
                      f'[初筛证据]({result["evidence_url"]})', '']
            count += 1
    lines.insert(2, f'共 {count} 篇。')
    for name, content in [('review-latest.md', lines), ('screening-exclusions.md', exclusions),
                          ('screening-pending.md', pending)]:
        (output / name).write_text('\n'.join(content).rstrip() + '\n')
    if archive:
        path.write_text('\n'.join(lines).rstrip() + '\n')
    return path
