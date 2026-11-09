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
    analyses={pid:fp for pid,fp,result in state['analyses']}
    ledger_path=Path(ledger_file)
    ledger=json.loads(ledger_path.read_text()) if ledger_path.exists() else {}
    source_hash=hashlib.sha256(Path(review_file).read_bytes()).hexdigest()
    for pid,decision in decisions.items():
        if pid not in papers:raise ValueError('Unknown paper ID in human review: '+pid)
        if decision['decision']=='approve' and pid not in analyses:
            raise ValueError('Approved paper has no reviewed evidence version: '+pid)
        if decision['decision']!='pending' and pid in analyses and decision['fingerprint']!=analyses[pid]:
            raise ValueError('Human decision refers to a different analysis version: '+pid)
    for pid,decision in decisions.items():
        ledger[pid]={**decision,'paper_version':paper_version(papers[pid]),'content_version':content_version(papers[pid]),'title':papers[pid]['title'],
                     'source_review_sha256':source_hash}
    ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
    return ledger


def write_review_packet(db, output, day, catalog):
    from scripts.publish_catalog import same_record
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    source=Path(catalog).parent/'data/catalog.json'
    records=json.loads(source.read_text()) if source.exists() else []
    ledger_file=source.parent/'curation-decisions.json'
    ledger=json.loads(ledger_file.read_text()) if ledger_file.exists() else {}
    analyses={pid:(fp,json.loads(payload)) for pid,fp,payload in db.execute('SELECT paper_id,fingerprint,payload FROM analyses')}
    path=output/('review-'+day+'.md')
    prior=read_decisions(path) if path.exists() else {}
    lines=['# 每周文献人工审核单 · '+day,'',
           '请只修改每篇的“审核决定”和“审核备注”：待审核 / 通过 / 排除 / 暂缓。编号和证据版本请保留。',
           '填写后将此 Markdown 文件交给助手，或在聊天中按编号给出决定；只有明确通过的文章才会进入 README。',
           '模型建议不是你的审核决定；证据不足的通过项仍需补核原文。','']
    shortlist=output/('methodology-priority-'+day+'.md')
    if shortlist.exists():lines += ['优先阅读：[方法学候选导读]('+shortlist.name+')（基于原始摘要的辅助整理，待你审核）。','']
    papers=[json.loads(payload) for payload, in db.execute('SELECT payload FROM papers')]
    papers.sort(key=lambda p:(-route(p)['priority'],p['first_seen'],p['id']))
    for p in papers:
        if p.get('seeded') or any(same_record(p,q) for q in records):continue
        human=current_human_decision(p,ledger)
        if human.get('decision')=='reject':continue
        old=analyses.get(p['id']);result=None
        if old and old[0]==review_fingerprint(p,old[1].get('model',''),old[1].get('provider','')):result=old[1]
        fp=old[0] if result else '待取得有效分析'
        saved=human or prior.get(p['id'],{})
        decision=saved.get('decision','pending') if saved.get('fingerprint')==fp else 'pending'
        if human.get('decision')=='hold':decision='hold'
        labels={'pending':'待审核','approve':'通过','reject':'排除','hold':'暂缓'}
        lines += ['## '+p['id'],'',
                  '文章：['+p['title'].replace('\n',' ')+']('+p['url']+')','',
                  '审核决定：'+labels[decision], '审核备注：'+saved.get('note',''), '证据版本：'+fp,'',
                  '模型建议：'+(result['decision'] if result else '待分析／原分析已过期'),'']
        if result:
            lines += ['中文概述：'+result['summary_zh'],'','纳入判断：'+result['reason_zh'],'','限制：'+result['limitations_zh'],'',
                      '建议分类：'+', '.join(result['metadata']['Stage']),'', '证据：']
            lines += ['- '+name+'：'+item['quote'] for name,item in result['criteria'].items()]
            lines += ['', '[分析原文]('+result['evidence_url']+')','']
        if human.get('followup_zh'):
            lines += ['人工原文补查：'+human['followup_zh'],'']
    path.write_text('\n'.join(lines).rstrip()+'\n')
    (output/'review-latest.md').write_text('\n'.join(lines).rstrip()+'\n')
    return path
