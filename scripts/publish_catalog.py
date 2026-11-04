"""Promote current full-text-supported discoveries into the main English catalog."""
from __future__ import annotations
import json
import hashlib
from pathlib import Path
from scripts.build_catalog import norm
from scripts.catalog_editorial import annotate
from scripts.literature_pipeline.analysis import fetch_evidence, review_fingerprint
from scripts.render_catalog import main as render_catalog


def same_record(left, right):
    return norm(left['title']) == norm(right['title']) or any(
        left.get(key) and right.get(key) and str(left[key]).lower() == str(right[key]).lower()
        for key in ('doi', 'arxiv_id', 'pmid'))


def sync_catalog(db, root, approval_file=None):
    if approval_file is None:
        raise ValueError('An explicit human-reviewed approval file is required')
    from scripts.review_workflow import read_decisions
    approvals=read_decisions(approval_file)
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
        eligible = fp == review_fingerprint(paper, result.get('model',''), result.get('provider',''))
        eligible = eligible and result.get('decision') == 'suggest_include' and result.get('evidence_level') == 'full_text'
        eligible = eligible and all(result.get('criteria',{}).get(key,{}).get('met') for key in ('medical','algorithm','fairness','groups','evaluation'))
        if not eligible:
            failures += 1
            notes += ['## '+paper['title'],'','人工已通过，但当前全文或范围证据尚不齐全／已更新，需补核后再收录。','']
            continue
        try:
            evidence = fetch_evidence(paper)
            if evidence['level'] != 'full_text': raise ValueError('Primary full text unavailable for catalog annotation')
            annotation = annotate(paper, evidence['text'])
            publication_date = str(paper.get('published') or paper['year'])[:10]
            metadata = {key:list(value) for key,value in result['metadata'].items()}
            metadata['Assets'] = ['Paper only']
            metadata['Stage'] = ['Evaluation' if annotation['method']=='Fairness Evaluation' else 'Not verified' if annotation['method']=='Stage pending' else annotation['method']]
            record = {key:paper[key] for key in ('title','doi','arxiv_id','pmid','authors') if paper.get(key)}
            record.update(year=publication_date[:4], publication_date=publication_date,
                          venue='arXiv' if paper.get('arxiv_id') else 'Paper', kind='main',
                          links={'Paper':paper['url']}, metadata=metadata, method=annotation['method'],
                          tldr_en=annotation['tldr_en'], verified=True,
                          sources=[{'url':evidence['url'], 'section':'Automated full-text screening'}])
            records.append(record);added += 1
            record['human_review']={'decision':'approve','review_fingerprint':fp,'note':approval.get('note','')}
            notes += ['## '+paper['title'], '', annotation['reason_zh'], '',
                      '初筛理由：'+result['reason_zh'], '', '证据：']
            notes += ['- '+name+'：'+item['quote'] for name,item in result['criteria'].items()]
            notes += ['', '[全文]('+evidence['url']+')', '']
        except Exception as exc:
            failures += 1
            notes += ['## '+paper['title'], '', '英文条目生成未完成，保留待重试：'+type(exc).__name__, '']
    # Render/validate before the wrapper stages any files for publication.
    from scripts.render_catalog import validate_records
    validate_records(records)
    path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
    render_catalog(root)
    if notes:
        report = root/'reports/catalog-screening.md'
        previous = report.read_text() if report.exists() else '# 主目录人工审核与收录证据\n\n仅将明确通过且证据版本匹配的文章加入 README。\n\n'
        report.write_text(previous+'\n'.join(notes)+'\n')
    return {'added':added, 'failures':failures}
