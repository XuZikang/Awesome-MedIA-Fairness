"""Promote current full-text-supported discoveries into the main English catalog."""
from __future__ import annotations
import argparse
import json
import os
import tempfile
import hashlib
from pathlib import Path
from scripts.build_catalog import norm
from scripts.catalog_editorial import annotate, verify_public_code
from scripts.literature_pipeline.analysis import fetch_evidence, review, review_fingerprint
from scripts.render_catalog import main as render_catalog
from scripts.screening_policy import paper_version, content_version


def same_record(left, right):
    return norm(left['title']) == norm(right['title']) or any(
        left.get(key) and right.get(key) and str(left[key]).lower() == str(right[key]).lower()
        for key in ('doi', 'arxiv_id', 'pmid'))


def sync_catalog(db, root, approval_file=None):
    if approval_file is None:
        raise ValueError('An explicit human-reviewed approval file is required')
    from scripts.review_workflow import read_decisions
    approvals=read_decisions(approval_file)
    from scripts.venue_policy import assess_venue,load_policy
    venue_policy=load_policy()
    root = Path(root)
    path = root/'data/catalog.json'
    records = json.loads(path.read_text())
    approval_text=Path(approval_file).read_text()
    archive=root/'reports'/('review-approval-'+hashlib.sha256(approval_text.encode()).hexdigest()[:12]+'.md')
    archive.parent.mkdir(parents=True,exist_ok=True)
    archive.write_text(approval_text)
    analyses = {pid: (fp, json.loads(payload)) for pid, fp, payload in db.execute('SELECT paper_id,fingerprint,payload FROM analyses')}
    added = failures = 0
    notes = []
    for (payload,) in db.execute('SELECT payload FROM papers ORDER BY id'):
        paper = json.loads(payload)
        if any(same_record(paper, existing) for existing in records): continue
        approval=approvals.get(paper['id'],{})
        if approval.get('decision')!='approve':continue
        venue=assess_venue(paper,venue_policy)
        if paper.get('conference_status') in {'accepted', 'accepted-main'}:
            failures += 1
            notes += ['## '+paper['title'], '', '人工已通过，会议已录用，等待正式论文集条目。', '']
            continue
        if venue['status'] not in {'eligible','preprint'}:
            failures+=1
            notes += ['## '+paper['title'],'','人工已通过，但出版渠道门槛尚未满足：'+venue['reason_zh'],'']
            continue
        previous = analyses.get(paper['id'])
        if not previous:
            failures += 1
            notes += ['## '+paper['title'],'','人工已通过，但尚缺有效分析，需先补核原文。','']
            continue
        fp, result = previous
        if approval.get('fingerprint')!=fp:
            failures += 1
            notes += ['## '+paper['title'],'','审核对应的证据版本已变化，需重新确认。','']
            continue
        if result.get('content_version'):
            current = result['content_version'] == content_version(paper)
        elif result.get('paper_version'):
            current = result['paper_version'] == paper_version(paper)
        else:
            current = fp == review_fingerprint(paper, result.get('model', ''), result.get('provider', ''))
        if not current:
            failures += 1
            notes += ['## '+paper['title'],'','人工审核后模型或证据版本已更新，需核对后再收录。','']
            continue
        try:
            evidence = fetch_evidence(paper)
            if evidence['level'] != 'full_text' or not evidence['text'].strip():
                failures += 1
                notes += ['## '+paper['title'], '', '人工已通过，等待可获取的原文全文。', '']
                continue
            final = review(paper, evidence, os.environ.get('LITERATURE_LLM_ENDPOINT', ''),
                           os.environ.get('LITERATURE_LLM_MODEL', ''),
                           os.environ.get('LITERATURE_LLM_API_KEY', ''))
            if final['decision'] != 'suggest_include':
                failures += 1
                notes += ['## '+paper['title'], '', '人工已通过，全文精读后仍有证据待核：'+final['reason_zh'], '']
                continue
            annotation = annotate(paper, evidence['text'])
            if annotation['method'] == 'Stage pending':
                failures += 1
                notes += ['## '+paper['title'], '', '人工已通过，全文尚不足以确定干预阶段：'+annotation['reason_zh'], '']
                continue
            code = verify_public_code(paper, annotation.get('code_urls', []), evidence['text'])
            if code['status'] == 'retry_pending':
                failures += 1
                notes += ['## '+paper['title'], '', '人工已通过，公开代码链接暂无法核验。', '']
                continue
            publication_date = str(paper.get('published') or paper['year'])[:10]
            metadata = {key:list(value) for key,value in final['metadata'].items()}
            # Preserve an explicitly approved legacy analysis without inventing a modality.
            metadata['Domain'] = ['Medical imaging (modality unspecified)' if v == 'Medical imaging' else v for v in metadata['Domain']]
            metadata['Assets'] = ['Code'] if code.get('url') else ['Paper only']
            metadata['Evidence'] = ['Primary full text']
            links = {'Paper': paper['url']}
            if code.get('url'):
                links['Code'] = code['url']
            metadata['Stage'] = ['Evaluation' if annotation['method']=='Fairness Evaluation' else 'Not verified' if annotation['method']=='Stage pending' else annotation['method']]
            record = {key:paper[key] for key in ('title','doi','arxiv_id','pmid','authors','journal_title','journal_issns','conference','publication_kind','formal_publications','source') if paper.get(key)}
            record.update(year=publication_date[:4], publication_date=publication_date,
                          venue='arXiv' if paper.get('arxiv_id') else (paper.get('journal_title') or paper.get('conference') or ('medRxiv' if paper.get('source')=='medrxiv' else 'Paper')), kind='survey' if final.get('article_type') in {'review','commentary'} else 'main',
                          links=links, metadata=metadata, method=annotation['method'],
                          tldr_en=annotation['tldr_en'], verified=True,
                          sources=[{'url':evidence['url'], 'section':'Human-approved full-text review'}],
                          code_verification=code)
            if final.get('article_type')=='commentary':record['publication_type']='Commentary'
            record['venue_assessment']=venue
            records.append(record);added += 1
            record['human_review']={'decision':'approve','review_fingerprint':fp,'note':approval.get('note',''),
                                    'overrides_machine_screening':result.get('decision')!='suggest_include'}
            notes += ['## '+paper['title'], '', annotation['reason_zh'], '',
                      '初筛理由：'+result['reason_zh'], '', '精读判断：'+final['reason_zh'], '',
                      '公开代码：'+(code['url']+'（'+code['evidence']+'）' if code.get('url') else '在所读证据中未核实到公开实现'), '', '证据：']
            notes += ['- '+name+'：'+item['quote'] for name,item in final['criteria'].items()]
            notes += ['', '[全文]('+evidence['url']+')', '']
        except Exception as exc:
            failures += 1
            notes += ['## '+paper['title'], '', '英文条目生成未完成，保留待重试：'+type(exc).__name__, '']
    # Render/validate before the wrapper stages any files for publication.
    from scripts.render_catalog import validate_records
    validate_records(records)
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    if added:render_catalog(root)
    if notes:
        report = root/'reports/catalog-screening.md'
        previous = report.read_text() if report.exists() else '# 主目录人工审核与收录证据\n\n仅将明确通过且证据版本匹配的文章加入 README。\n\n'
        new_notes = '\n'.join(notes).rstrip() + '\n'
        if new_notes not in previous:
            report.write_text(previous + new_notes)
    return {'added':added, 'failures':failures}


def apply_review(root, approval_file, state_file=None):
    """Apply human decisions from a Markdown packet, without running discovery."""
    from scripts.literature_pipeline.cli import connect, import_state
    from scripts.review_workflow import import_human_decisions, write_review_packet

    root = Path(root)
    state_file = Path(state_file) if state_file else root / 'data/literature-state.json'
    import_human_decisions(approval_file, state_file, root / 'data/curation-decisions.json')
    with tempfile.TemporaryDirectory() as directory:
        db = connect(Path(directory) / 'editorial.sqlite3')
        try:
            import_state(db, state_file)
            result = sync_catalog(db, root, approval_file)
            run_status = root / 'reports/run-status.json'
            from datetime import date
            day = json.loads(run_status.read_text()).get('date', date.today().isoformat()) if run_status.exists() else date.today().isoformat()
            write_review_packet(db, root / 'reports', day, root / 'README.md', archive=False)
            return result
        finally:
            db.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--approval-file', required=True, type=Path)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args(argv)
    result = apply_review(args.root, args.approval_file)
    print(f"Catalog additions: {result['added']}; approved items pending: {result['failures']}")
    return 2 if result['failures'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
