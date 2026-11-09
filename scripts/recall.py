"""Generate supplementary searches and check approved-paper recall fixtures."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_config(path=None):
    return json.loads(Path(path or ROOT/'config/recall.json').read_text())


def _match(term, text):
    words = re.findall(r'[a-z0-9]+', term.casefold())
    return bool(re.search(r'\b'+r'[\W_]+'.join(map(re.escape, words))+r'\b', text.casefold()))


def matching_groups(paper, config):
    text = paper.get('title','')+' '+paper.get('abstract','')
    contexts = config['medical_context']+config['dataset_aliases']
    if not any(_match(term,text) for term in contexts):
        return []
    if not any(_match(term,text) for term in config.get('algorithm_context',[])+config['dataset_aliases']):
        return []
    return [group['name'] for group in config['groups']
            if any(_match(term,text) for term in group['terms'])]


def _clause(term, source):
    if source == 'pubmed':
        # Avoid PubMed's phrase-index substitution: keep every word explicit.
        return '('+' AND '.join(word+'[Title/Abstract]' for word in re.findall(r'[A-Za-z0-9]+',term))+')'
    escaped=term.replace('"','')
    if source == 'arxiv':
        return f'(ti:"{escaped}" OR abs:"{escaped}")'
    return f'TITLE_ABS:"{escaped}"'


def queries(config):
    result={}
    for source in ('arxiv','europepmc','pubmed'):
        omitted=config.get('source_omitted_dataset_aliases',{}).get(source,[])
        contexts=config['medical_context']+[t for t in config['dataset_aliases'] if t not in omitted]
        context='('+' OR '.join(_clause(t,source) for t in contexts)+')'
        computational='('+' OR '.join(_clause(t,source) for t in config.get('algorithm_context',[])+[t for t in config['dataset_aliases'] if t not in omitted])+')'
        result[source]=['('+' OR '.join(_clause(t,source) for t in group['terms'])+') AND '+context+' AND '+computational
                        for group in config['groups']]
    return result


def check(config=None, sentinels=None):
    config=config or load_config()
    sentinels=sentinels or json.loads((ROOT/'config/recall-sentinels.json').read_text())
    rows=[]
    for item in sentinels['cases']:
        groups=matching_groups(item,config)
        passed=bool(groups)==item['expected_recall']
        if item.get('expected_group'):passed=passed and item['expected_group'] in groups
        rows.append({'id':item['id'],'title':item['title'],'matched_groups':groups,'passed':passed})
    return {'passed':all(row['passed'] for row in rows),'cases':rows,
            'basis':sentinels['basis'],
            'limitation':'Local query-vocabulary regression; not proof of API/index completeness or final relevance.'}


def report(output, result):
    path=Path(output);path.mkdir(parents=True,exist_ok=True)
    (path/'recall-regression.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    lines=['# 召回回归检查','','本检查使用已批准条目的公开题名和目录摘要，验证补漏词表与医疗语境匹配。',
           '它不代表接口已成功执行、索引穷尽或文章已经符合最终准入规则。','','| 样例 | 匹配通道 | 结果 |','|---|---|---|']
    for row in result['cases']:
        lines.append('| '+row['title'].replace('|','\\|')+' | '+', '.join(row['matched_groups'])+' | '+('通过' if row['passed'] else '失败')+' |')
    (path/'recall-regression.md').write_text('\n'.join(lines)+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args();result=check()
    if args.output:report(args.output,result)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    raise SystemExit(0 if result['passed'] else 1)
