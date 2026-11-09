"""Track explicit publication relationships without changing catalog membership."""
from __future__ import annotations
import hashlib
import json
import re
import urllib.parse
import urllib.request
from datetime import date, timedelta
from pathlib import Path

USER_AGENT='Awesome-MedIA-Fairness publication-identity-check/1.0 (+https://github.com/XuZikang/Awesome-MedIA-Fairness)'


def doi(value):
    return re.sub(r'^https?://(?:dx\.)?doi\.org/','',str(value).strip(),flags=re.I).lower()


def normal(value):
    return re.sub(r'[^a-z0-9]','',str(value).casefold())


def crossref_record(identifier, timeout=25):
    url='https://api.crossref.org/works/'+urllib.parse.quote(doi(identifier),safe='')
    request=urllib.request.Request(url,headers={'User-Agent':USER_AGENT})
    with urllib.request.urlopen(request,timeout=timeout) as response:data=json.load(response)
    record=data.get('message',{})
    if doi(record.get('DOI',''))!=doi(identifier):raise ValueError('Crossref DOI mismatch')
    return record


def crossref_candidates(paper, timeout=25):
    """Find possible counterparts; a search match alone never confirms identity."""
    url='https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':paper['title'],'rows':3})
    request=urllib.request.Request(url,headers={'User-Agent':USER_AGENT})
    with urllib.request.urlopen(request,timeout=timeout) as response:data=json.load(response)
    items=data.get('message',{}).get('items')
    if not isinstance(items,list):raise ValueError('Invalid Crossref search response')
    return items


def _first_author(value):
    if isinstance(value,dict):return normal(value.get('family',''))
    # Source adapters emit either full names or PubMed's family + initials.
    parts=re.findall(r'[^\W\d_]+',str(value),re.U)
    if len(parts)>1 and len(parts[-1])<=3 and parts[-1].isupper():return normal(parts[0])
    return normal(parts[-1]) if parts else ''


def formal_record(record, evidence, confidence):
    container=record.get('container-title') or []
    title=record.get('title') or []
    parts=(record.get('published') or record.get('published-online') or {}).get('date-parts') or [[]]
    published='-'.join(str(n).zfill(2) if i else str(n) for i,n in enumerate(parts[0]))
    return {'doi':doi(record['DOI']),'title':title[0] if title else '',
            'journal_title':container[0] if container and record.get('type')=='journal-article' else '',
            'conference':(record.get('event',{}).get('name') or (container[0] if container else '')) if record.get('type')=='proceedings-article' else '',
            'journal_issns':record.get('ISSN',[]),'publication_kind':record.get('type',''),
            'published':published,'url':'https://doi.org/'+doi(record['DOI']),
            'evidence':[evidence],'confidence':confidence}


def resolve(paper, fetch=crossref_record):
    """Exact explicit relations, or an explicit arXiv DOI with corroborating identity.

    No title search, fuzzy matching, or same-author-only merging is performed.
    """
    found=[];issues=[]
    explicit=doi(paper.get('formal_publication_doi',''))
    original=doi(paper.get('doi',''))
    if paper.get('arxiv_id') and original and not original.startswith('10.48550/'):
        explicit=explicit or original
    identifiers=list(dict.fromkeys(x for x in [original,explicit] if x and not x.startswith('10.48550/')))
    for identifier in identifiers:
        record=fetch(identifier)
        evidence='https://api.crossref.org/works/'+urllib.parse.quote(identifier,safe='')
        is_formal=record.get('type') in {'journal-article','proceedings-article'}
        if paper.get('arxiv_id') and is_formal and identifier==explicit:
            same_title=normal((record.get('title') or [''])[0])==normal(paper['title'])
            source_author=_first_author((paper.get('authors') or [''])[0])
            target_author=_first_author((record.get('author') or [{}])[0])
            if same_title and source_author and source_author==target_author:
                found.append(formal_record(record,evidence,'explicit_arxiv_doi_and_corroborated_metadata'))
            else:
                issues.append({'doi':identifier,'reason':'arXiv DOI link requires manual identity confirmation; title/first author differ or are missing','evidence':evidence})
        elif is_formal and not paper.get('arxiv_id'):
            # Looking up the article's own DOI enriches venue metadata only.
            found.append(formal_record(record,evidence,'own_registered_doi'))
        for relation in record.get('relation',{}).get('is-preprint-of',[]):
            target=doi(relation.get('id',''))
            if relation.get('id-type')!='doi' or not re.match(r'^10\.\d{4,9}/\S+$',target):continue
            formal=fetch(target)
            if formal.get('type') not in {'journal-article','proceedings-article'}:
                issues.append({'doi':target,'reason':'Registered relation target is not a formal article','evidence':evidence});continue
            found.append(formal_record(formal,evidence,'registered_is_preprint_of'))
        # A formal record may preserve an explicit predecessor even if renamed.
        if is_formal:
            predecessors=[doi(item.get('id','')) for item in record.get('relation',{}).get('has-preprint',[]) if item.get('id-type')=='doi']
            if predecessors:
                current=formal_record(record,evidence,'registered_has_preprint')
                current['preprint_dois']=predecessors
                if current not in found:found.append(current)
    unique={entry['doi']:entry for entry in found}
    return list(unique.values()),issues


def confirmed_aliases(paper):
    result=[]
    for item in paper.get('formal_publications',[]):
        if item.get('confidence') not in {'registered_is_preprint_of','explicit_arxiv_doi_and_corroborated_metadata','own_registered_doi','registered_has_preprint'}:continue
        if item.get('doi'):result.append('doi:'+doi(item['doi']))
        for identifier in item.get('preprint_dois',[]):
            if identifier.startswith('10.48550/arxiv.'):
                result.append('arxiv_id:'+re.sub(r'v\d+$','',identifier.split('arxiv.',1)[1]))
            else:result.append('doi:'+doi(identifier))
    return list(dict.fromkeys(result))


def track(db, day, config, fetch=crossref_record, arxiv_fetch=None, search=None):
    """Bounded durable checks; a failure never means no formal publication exists."""
    maximum=config.get('max_records_per_run',20);age=config.get('recheck_days',7)
    rows=[json.loads(row[0]) for row in db.execute('SELECT payload FROM papers')]
    cutoff=(date.fromisoformat(day)-timedelta(days=age)).isoformat()
    due=[p for p in rows if (p.get('doi') or p.get('arxiv_id')) and p.get('publication_tracking',{}).get('checked_on','')<=cutoff]
    due.sort(key=lambda p:(max(p.get('publication_tracking',{}).get('checked_on',''),p.get('publication_tracking',{}).get('last_attempt','')),not bool(p.get('arxiv_id')),p['id']))
    due_count=len(due)
    due=due[:maximum];fresh={};arxiv_error=None
    arxiv_ids=[p['arxiv_id'] for p in due if p.get('arxiv_id')]
    if arxiv_ids and arxiv_fetch:
        try:fresh={p['arxiv_id']:p for p in arxiv_fetch(arxiv_ids)}
        except Exception as exc:arxiv_error=type(exc).__name__
    stats={'checked':0,'failures':0,'formal_links':0,'identity_conflicts':0,'pending_checks':max(0,due_count-len(due))}
    for paper in due:
        pid=paper['id'];old=paper.get('publication_tracking',{})
        try:
            if paper.get('arxiv_id') and arxiv_fetch:
                if arxiv_error or paper['arxiv_id'] not in fresh:raise ValueError('arXiv identity metadata unavailable')
                incoming=fresh[paper['arxiv_id']]
                if incoming.get('doi') and not doi(incoming['doi']).startswith('10.48550/'):
                    paper['formal_publication_doi']=doi(incoming['doi'])
                if incoming.get('journal_ref'):paper['journal_ref']=incoming['journal_ref']
            formal,issues=resolve(paper,fetch)
            # Existing cross-record identity conflicts require explicit reconciliation.
            issues += [r for r in old.get("issues",[]) if r.get("other_paper_id") and r not in issues]
            if paper.get('arxiv_id') and not formal and not issues and search is not None:
                candidates=[]
                for hit in search(paper):
                    if hit.get('type') not in {'journal-article','proceedings-article'}:continue
                    if normal((hit.get('title') or [''])[0])!=normal(paper['title']):continue
                    identifier=doi(hit.get('DOI',''))
                    if not identifier:continue
                    predecessors=[doi(r.get('id','')) for r in hit.get('relation',{}).get('has-preprint',[]) if r.get('id-type')=='doi']
                    arxiv_doi='10.48550/arxiv.'+paper['arxiv_id']
                    if any(re.sub(r'v\d+$','',value)==arxiv_doi for value in predecessors):
                        confirmed=fetch(identifier)
                        item=formal_record(confirmed,'https://api.crossref.org/works/'+urllib.parse.quote(identifier,safe=''),'registered_has_preprint')
                        item['preprint_dois']=predecessors;formal.append(item)
                    else:
                        candidates.append(formal_record(hit,'https://api.crossref.org/works?'+urllib.parse.urlencode({'query.title':paper['title'],'rows':3}),'unconfirmed_title_match'))
                if candidates:
                    paper['formal_publication_candidates']=candidates
                    issues.extend({'doi':r['doi'],'reason':'Title-search counterpart is unconfirmed; verify primary publication identity before merging or applying its rank','evidence':r['evidence'][0]} for r in candidates)
            if formal:
                confirmed_dois={r['doi'] for r in formal}
                paper['formal_publication_candidates']=[r for r in paper.get('formal_publication_candidates',[]) if r['doi'] not in confirmed_dois]
            # Preserve confirmed historical links if a later response lacks relations.
            combined={x['doi']:x for x in paper.get('formal_publications',[])}
            combined.update({x['doi']:x for x in formal});paper['formal_publications']=list(combined.values())
            paper['publication_tracking']={'checked_on':day,'status':'needs_identity_review' if issues else 'checked','issues':issues}
            for alias in confirmed_aliases(paper):
                other=db.execute('SELECT paper_id FROM aliases WHERE alias=?',(alias,)).fetchone()
                if other and other[0]!=pid:
                    stats['identity_conflicts']+=1
                    paper['publication_tracking']['issues'].append({'alias':alias,'other_paper_id':other[0],'reason':'Existing separate records require manual reconciliation'})
                    paper['publication_tracking']['status']='needs_identity_review'
                else:db.execute('INSERT OR IGNORE INTO aliases VALUES (?,?)',(alias,pid))
            stats['checked']+=1;stats['formal_links']+=len(formal)
        except Exception as exc:
            stats['failures']+=1
            paper['publication_tracking']={**old,'last_attempt':day,'status':'retry_pending','error':type(exc).__name__}
        db.execute('UPDATE papers SET payload=? WHERE id=?',(json.dumps(paper,ensure_ascii=False),pid))
    db.commit()
    return stats


def write_report(db, output, day, stats):
    lines=['# 预印本与正式版本追踪 · '+day,'','身份关系与出版渠道检查不自动更改README、题名、日期或收录决定。',
           '仅凭同名或相同作者不会自动合并；有冲突的现存记录保留并送人工核实。','',
           f"本轮完成 {stats['checked']} 次检查；失败 {stats['failures']} 次；发现／确认正式身份 {stats['formal_links']} 条；身份冲突 {stats['identity_conflicts']} 条。",'']
    for pid,payload in db.execute('SELECT id,payload FROM papers ORDER BY id'):
        p=json.loads(payload)
        if not p.get('formal_publications') and not p.get('publication_tracking',{}).get('issues'):continue
        lines+=['## '+pid,'',p['title'],'']
        for item in p.get('formal_publications',[]):
            lines+=['- [正式记录]('+item['url']+')：'+item['title']+'；'+item.get('journal_title',item.get('conference',''))+'；'+item['confidence']]
        for issue in p.get('publication_tracking',{}).get('issues',[]):lines+=['- 待核实：'+issue['reason']]
        for item in p.get('formal_publication_candidates',[]):lines+=['- [待核实的可能正式版本]('+item['url']+')：'+item['title']+'；不自动合并']
        lines+=['']
    path=Path(output);path.mkdir(parents=True,exist_ok=True)
    (path/'publication-tracking.md').write_text('\n'.join(lines).rstrip()+'\n')
