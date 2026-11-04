"""Rebuild the traceable medical fairness catalog from archived source inventories."""
from __future__ import annotations
import concurrent.futures
import hashlib
import html
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

from scripts.catalog_schema import ALLOWED, TOPICS

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.local/sources'
SURVEY_URL = 'https://www.nature.com/articles/s41746-024-01276-5'
FAIMI_URL = 'https://faimi-workshop.github.io/resources/'

def text(node):
    return ' '.join(' '.join(node.itertext()).split()) if node is not None else ''

def norm(value):
    return re.sub(r'[^a-z0-9]', '', value.casefold())

def fetch(url):
    name = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = CACHE / name
    CACHE.mkdir(parents=True,exist_ok=True)
    if path.exists(): return path.read_bytes()
    req=urllib.request.Request(url,headers={'User-Agent':'Awesome-MedIA-Fairness catalog/1.0'})
    with urllib.request.urlopen(req, timeout=30) as r: body=r.read()
    path.write_bytes(body)
    return body

def identity(p):
    links=' '.join(p.get('links',{}).values())
    doi_value = ''
    for url in p.get('links', {}).values():
        parsed = urllib.parse.urlsplit(url)
        if parsed.hostname in {'doi.org', 'dx.doi.org'}:
            doi_value = urllib.parse.unquote(parsed.path.lstrip('/'))
            break
        match = re.search(r'(10\.\d{4,}/[^?#]+)', parsed.path)
        if match:
            doi_value = urllib.parse.unquote(match.group(1)).removesuffix('.short') if hasattr(str, 'removesuffix') else match.group(1)
            break
    arxiv=re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})',links,re.I)
    pmid=re.search(r'pubmed\.ncbi\.nlm\.nih\.gov/(\d+)',links)
    if doi_value: p['doi']=doi_value.rstrip('.').lower()
    if arxiv: p['arxiv_id']=arxiv.group(1)
    if pmid: p['pmid']=pmid.group(1)
    if p.get('doi','').startswith('10.48550/arxiv.'):
        p['arxiv_id']=p.pop('doi').split('arxiv.',1)[1]
    return p

def metadata(title, labels=''):
    s=(title+' '+labels).lower()
    domain='Medical imaging'
    if re.search(r'language model|medical text|clinical text|clinical nlp',s):domain='Clinical NLP and foundation models'
    elif re.search(r'\behr\b|electronic health|clinical prediction|health of populations',s):domain='EHR and clinical prediction'
    elif re.search(r'\beeg\b|\becg\b|electroencephal|electrocardio',s):domain='Physiological signals'
    focus=['Evaluation'];stage=['Evaluation']
    if re.search(r'mitigat|debias|improv.*fair|fairprune|fairtune|fairadabn|circle|fairdisco|um-',s):focus=['Mitigation'];stage=['Not verified']
    if re.search(r'pre-processing|data resampling|data synthesis|data aggregation|embellish|um-pre',s):stage=['Pre-processing']
    if re.search(r'in-processing|adversarial|disentangle|contrastive|federated|universal learning|um-in',s):stage=['In-processing']
    if re.search(r'post-processing|prun|um-post',s):stage=['Post-processing']
    if re.search(r'benchmark|medfair|fairmedfm',s):focus=sorted(set(focus+['Benchmark']))
    if re.search(r'fairness dataset|harvard glaucoma|fairseg|diverse dermatology',s):focus=sorted(set(focus+['Dataset']))
    if re.search(r'encoding|shortcut|causes|source|mechanism|understanding|fe-under',s):focus=sorted(set(focus+['Bias mechanisms']))
    attributes=[]
    for pattern,label in [(r'\bsex|gender','Sex and gender'),(r'\bage|elder','Age'),(r'rac[ei]|ethnic','Race and ethnicity'),(r'skin tone|skin colo','Skin tone'),(r'socioeconomic|income','Socioeconomic status'),(r'intersection','Intersectional')]:
        if re.search(pattern,s):attributes.append(label)
    return {'Domain':[domain],'Focus':focus,'Stage':stage,'Attributes':attributes or ['Not specified'],'Assets':['Paper only'],'Evidence':['Reviewed source']}

def topics(meta):
    result=[]
    if set(meta['Focus']) & {'Evaluation','Benchmark','Dataset'}:result.append(TOPICS[0])
    if set(meta['Focus']) & {'Bias mechanisms','Theory and measurement'}:result.append(TOPICS[1])
    for stage,topic in zip(['Pre-processing','In-processing','Post-processing'],TOPICS[2:5]):
        if stage in meta['Stage'] or 'Multi-stage' in meta['Stage']:result.append(topic)
    if 'Mitigation' in meta['Focus'] and not set(meta['Stage']) & {'Pre-processing','In-processing','Post-processing','Multi-stage'}:result.append(TOPICS[-1])
    if meta['Domain']==['Clinical NLP and foundation models']:result.append(TOPICS[5])
    elif meta['Domain']!=['Medical imaging']:result.append(TOPICS[6])
    return result or [TOPICS[0]]

def legacy():
    result=[];heading=''
    for line in (ROOT/'docs/legacy-catalog.md').read_text().splitlines():
        if line.startswith('#'):heading=line.lstrip('# ').strip()
        match=re.search(r'^(?:\d+\.\s*)?(.+?)\.\s*(.*?)\(\[paper\]\(([^)]+)\)',line)
        if not match:continue
        title,venue,url=match.groups(); links={'Paper':url.replace('http://','https://')}
        for kind,dest in re.findall(r'\[(code|dataset)\]\(([^)]+)\)',line):links['Code' if kind=='code' else 'Data']=dest
        years=re.findall(r'20\d{2}',venue)
        p={'title':title.strip(),'year':years[-1] if years else '2021','venue':venue.strip(' .,'),'links':links,'sources':[{'url':'docs/legacy-catalog.md','section':heading}],'metadata':metadata(title,heading),'origin':'legacy'}
        p['metadata']['Evidence']=['Legacy unverified'];result.append(identity(p))
    return result

def expanded_rows(table):
    spans={}
    for row in table.findall('.//tr')[1:]:
        values={};next_spans={}
        for i,(value,left) in spans.items():
            values[i]=value
            if left>1:next_spans[i]=(value,left-1)
        i=0
        for cell in row:
            while i in values:i+=1
            value=text(cell);values[i]=value
            if int(cell.get('rowspan','1'))>1:next_spans[i]=(value,int(cell.get('rowspan'))-1)
            i+=1
        spans=next_spans
        yield [values.get(i,'') for i in range(8)],row

def survey():
    root=ET.parse(CACHE/'review.xml').getroot();result=[]
    for cols,row in expanded_rows(root.find(".//table-wrap[@id='Tab2']")):
        for xref in row.findall('.//xref'):
            rid=xref.get('rid','')
            if not rid.startswith('CR'):continue
            ref=root.find(".//ref[@id='"+rid+"']")
            title=text(ref.find('.//article-title'))
            if not title:
                mc=ref.find('.//mixed-citation');prefix=(mc.text or '') if mc is not None else ''
                if 'et al.' in prefix:prefix=prefix.split('et al.',1)[1]
                choices=re.split(r'(?<=\.)\s+',prefix)
                choices=[c for c in choices if len(re.findall(r'\b[a-z][a-z-]+\b',c))>=2 and not c.startswith('In ')]
                title=choices[0].strip(' .') if choices else ''
                title=re.sub(r'\s+In$', '', title).rstrip(' .')
            if not title:raise ValueError('Cannot extract review reference '+rid)
            doi=next((text(n) for n in ref.findall('.//pub-id') if n.get('pub-id-type')=='doi'),'')
            pmid=next((text(n) for n in ref.findall('.//pub-id') if n.get('pub-id-type')=='pmid'),'')
            urls=[n.get('{http://www.w3.org/1999/xlink}href','') for n in ref.findall('.//ext-link')]
            url=('https://doi.org/'+doi) if doi else ('https://pubmed.ncbi.nlm.nih.gov/'+pmid+'/' if pmid else next((u for u in urls if 'arxiv' in u or 'openreview' in u),SURVEY_URL+'#ref-'+rid))
            meta=metadata(title,cols[0]);meta['Attributes']=metadata('',cols[6])['Attributes']
            result.append(identity({'title':title,'year':text(ref.find('.//year')) or (re.findall(r'\((20\d{2})\)',text(ref)) or [cols[1]])[-1],'venue':text(ref.find('.//source')) or 'Referenced study','doi':doi.lower(),'pmid':pmid,'links':{'Paper':url},'sources':[{'url':SURVEY_URL+'/tables/2','section':cols[0],'reference':rid}],'metadata':meta,'origin':'review'}))
    return result

class Node:
    def __init__(self,tag='',attrs=None):self.tag=tag;self.attrs=dict(attrs or []);self.children=[]
    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child,Node):yield from child.walk()
    def text(self):return ''.join(c.text() if isinstance(c,Node) else c for c in self.children)

class DOM(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.root=Node();self.stack=[self.root]
    def handle_starttag(self,tag,attrs):
        node=Node(tag,attrs);self.stack[-1].children.append(node)
        if tag=='br':node.children.append('\n')
        if tag not in {'br','img','meta','link','input','hr','source','wbr'}:self.stack.append(node)
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag:self.stack=self.stack[:i];break
    def handle_data(self,data):self.stack[-1].children.append(data)

def faimi():
    dom=DOM();dom.feed(fetch(FAIMI_URL).decode());section='';area='';papers=[];related=[]
    for n in dom.root.walk():
        if n.tag=='h2':area=n.text().strip()
        if n.tag in {'h3','h4'}:section=n.text().strip()
        if n.tag!='li' or area!='Literature':continue
        body=n.text();years=re.findall(r'\b20\d{2}\b',body);year=years[0] if years else '2019'
        for a in n.walk():
            title=' '.join(a.text().split());url=a.attrs.get('href','')
            if a.tag!='a' or len(title)<28 or not url.startswith('http') or title.lower() in {'propublica'}:continue
            url=url.replace('http://dx.doi.org/','https://doi.org/').replace('http://','https://')
            meta=metadata(title,section)
            p=identity({'title':title,'year':year,'venue':'FAIMI resource','links':{'Paper':url},'sources':[{'url':FAIMI_URL,'section':section}],'metadata':meta,'origin':'faimi'})
            p['kind']='survey' if 'review' in section.lower() or 'Perspectives' in section else 'main'
            if section in {'Seminal works on AI fairness','Miscellaneous'} and not re.search(r'medic|health|clinical|chest|calibration biases',title,re.I):
                p['kind']='foundation';related.append(p)
            else:papers.append(p)
    return papers,related

def workshops():
    result=[]
    for year,path in [(2023,'2023-miccai'),(2024,'2024-miccai'),(2025,'2025-miccai-workshop'),(2026,'2026-miccai')]:
        url='https://faimi-workshop.github.io/'+path+'/'
        dom=DOM();dom.feed(fetch(url).decode());active=False
        for n in dom.root.walk():
            if n.tag=='h2':active=n.text().strip()==('Poster Session' if year==2026 else 'Accepted Papers')
            if not active or n.tag not in ({'li'} if year==2026 else {'p'}):continue
            for value in n.text().split('\n'):
                value=' '.join(value.split()).strip()
                if year<2026:
                    if ':' not in value:continue
                    value=value.split(':',1)[1].strip(' ,')
                value=re.sub(r'\s*Link\s*$','',value).strip()
                if len(value)<25:continue
                links=[a.attrs.get('href','') for a in n.walk() if a.tag=='a' and 'arxiv.org' in a.attrs.get('href','')]
                result.append(identity({'title':value,'year':str(year),'venue':f'FAIMI {year} listing','links':{'Paper':links[0] if len(links)==1 else url},'sources':[{'url':url,'section':'Tentative poster programme' if year==2026 else 'Accepted papers'}],'metadata':metadata(value),'origin':'workshop','kind':'workshop'}))
    return result

def merge(records):
    groups=[]
    for p in records:
        match=None
        for old in groups:
            if norm(p['title'])==norm(old['title']) or any(p.get(k) and p.get(k)==old.get(k) for k in ['doi','arxiv_id','pmid']):match=old;break
        if not match:groups.append(p);continue
        match['sources']+=p['sources'];match['links'].update({k:v for k,v in p['links'].items() if k!='Paper' or 'nature.com/articles/s41746-024-01276-5#' in match['links'].get(k,'')})
        for key in ['doi','arxiv_id','pmid']:
            if p.get(key):match[key]=p[key]
        for field in ['Focus','Stage','Attributes']:
            match['metadata'][field]=sorted(set(match['metadata'][field]+p['metadata'][field]))
            if len(match['metadata'][field])>1:
                match['metadata'][field]=[v for v in match['metadata'][field] if v not in {'Not specified','Not verified'}]
        if p.get('kind')=='main' or (p['origin']=='review'):match['kind']='main'
        if match['metadata']['Evidence']==['Legacy unverified'] and p['origin']!='legacy':match['metadata']['Evidence']=['Reviewed source']
    return groups

def enrich(p):
    p=dict(p);p['metadata']={k:list(v) for k,v in p['metadata'].items()};p['verified']=False
    try:
        if p.get('doi'):
            data=json.loads(fetch('https://api.crossref.org/works/'+urllib.parse.quote(p['doi'],safe=''))).get('message',{})
            canonical=(data.get('title') or [''])[0]
            # Identifier matches still need a title check: a wrong legacy link must not rename a paper.
            tokens=lambda s:set(re.findall(r'[a-z0-9]+',s.lower()))
            a,b=tokens(canonical),tokens(p['title'])
            # The FAIMI short title abbreviates the publisher's expanded AI/CMR wording.
            known_expansion=p['doi']=='10.1093/ehjdh/ztaf008' and norm(canonical).startswith('aninvestigationintothecausesofracebias')
            if canonical and (len(a&b)/max(1,len(a|b))>=0.75 or known_expansion):
                p['title']=html.unescape(re.sub('<[^>]+>','',canonical))
                p['venue']=(data.get('container-title') or ['Paper'])[0]
                parts=(data.get('published') or {}).get('date-parts',[[]])[0]
                if parts:p['year']=str(parts[0])
                p['verified']=True;p['metadata']['Evidence']=['Primary metadata']
                if data.get('abstract'):p['abstract']=re.sub('<[^>]+>',' ',data['abstract']);p['metadata']['Evidence']=['Primary abstract']
            else:p['verification_warning']='DOI/title mismatch or unresolved title'
    except Exception as exc:p['verification_warning']=type(exc).__name__
    return p

def apply_primary_links(records):
    """Apply independently checked reference-to-DOI mappings without renaming seeds."""
    mappings=json.loads((ROOT/'data/primary-link-resolutions.json').read_text())
    by_reference={p['reference']:p for p in mappings}
    for p in records:
        for source in p['sources']:
            match=by_reference.get(source.get('reference'))
            if not match or norm(p['title'])!=norm(match['title']):continue
            p['doi']=match['doi'].lower()
            p['links']['Paper']='https://doi.org/'+p['doi']
            p['venue']=match['verified_venue']
            p['verified']=True
            if p['metadata']['Evidence']!=['Primary abstract']:
                p['metadata']['Evidence']=['Primary metadata']
    return records

def main():
    if not (CACHE/'review.xml').exists():
        CACHE.mkdir(parents=True,exist_ok=True)
        (CACHE/'review.xml').write_bytes(fetch('https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11487181/fullTextXML'))
    raw=legacy()+survey();f,foundations=faimi();raw+=f;workshop=workshops()
    raw.append(identity({'title':'FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models','year':'2024','venue':'NeurIPS Datasets and Benchmarks','links':{'Paper':'https://arxiv.org/abs/2407.00983','Code':'https://github.com/FairMedFM/FairMedFM'},'sources':[{'url':FAIMI_URL,'section':'Software toolkits: FairMedFM'}],'metadata':metadata('FairMedFM fairness benchmark medical imaging'),'origin':'faimi'}))
    records=merge(raw)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(enrich,records))
    from scripts.literature_pipeline.sources import _parse_arxiv
    identifiers=sorted({p['arxiv_id'] for p in records if p.get('arxiv_id')})
    for offset in range(0,len(identifiers),20):
        try:
            payload=fetch('https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':','.join(identifiers[offset:offset+20]),'max_results':20}))
            batch,_=_parse_arxiv(payload)
            indexed={p['arxiv_id']:p for p in batch}
            for p in records:
                actual=indexed.get(p.get('arxiv_id',''))
                if not actual:continue
                p['abstract']=actual['abstract'];p['verified']=True;p['metadata']['Evidence']=['Primary abstract']
                if actual.get('doi'):p['doi']=actual['doi'].lower()
                if not p.get('doi'):p['title']=actual['title']
            if offset+20<len(identifiers):time.sleep(3)
        except Exception as exc:
            print('arXiv backfill failed:',type(exc).__name__)
    # A workshop programme is a discovery lead, not evidence of implemented fairness evaluation.
    records=merge(records)
    for p in records:
        if norm(p['title']).startswith('howfairisyourgraph'):
            p['links']['Paper']='https://proceedings.mlr.press/v182/ribeiro22a.html';p['venue']='MLHC';p['verified']=True;p['metadata']['Evidence']=['Primary metadata']
        if p.get('arxiv_id')=='2311.02189':
            p['year']='2024';p['venue']='ICLR';p['links']['Code']='https://github.com/Harvard-Ophthalmology-AI-Lab/FairSeg'
        if re.search(r'\breview\b|\bsurvey\b|perspective|ethical|framework for operationalizing',p['title'],re.I):p['kind']='survey'
        if p.get('doi') and not p.get('verification_warning'):p['links']['Paper']='https://doi.org/'+p['doi']
        elif p.get('arxiv_id'):p['links']['Paper']='https://arxiv.org/abs/'+p['arxiv_id']
        elif p.get('pmid'):p['links']['Paper']='https://pubmed.ncbi.nlm.nih.gov/'+p['pmid']+'/'
    records=apply_primary_links(records)
    out={'sources':{'legacy':'7ecc995','review':SURVEY_URL,'faimi':FAIMI_URL},'records':records,'foundations':foundations,'workshop_candidates':workshop,
         'counts':{'legacy_rows':len(legacy()),'review_table_rows':len(survey()),'faimi_rows':len(f)+1,'unique_catalog_records':len(records),'primary_metadata_verified':sum(p['verified'] for p in records)}}
    (ROOT/'data').mkdir(exist_ok=True)
    (ROOT/'.local/inventory.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
    (ROOT/'data/source-index.json').write_text(json.dumps({k:v for k,v in out.items() if k!='records'},ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(out['counts']))

if __name__=='__main__':main()
