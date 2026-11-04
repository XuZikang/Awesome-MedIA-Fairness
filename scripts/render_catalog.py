"""Render annual and topic views from the reviewed, source-traceable inventory."""
from __future__ import annotations
import json
import re
from collections import Counter
from pathlib import Path
from scripts.build_catalog import ROOT, topics, norm, apply_primary_links
from scripts.catalog_schema import ALLOWED, TOPICS

REPO='https://github.com/XuZikang/Awesome-MedIA-Fairness'

def md(value):return str(value).replace('\n',' ').replace('<','&lt;').replace('>','&gt;').replace('[','\\[').replace(']','\\]')

def prepare(p):
    p=dict(p);p.setdefault('kind','main');m={k:list(v) for k,v in p['metadata'].items()}
    assets=[name for name in ['Code','Weights','Project','Data'] if name in p['links']]
    m['Assets']=assets or ['Paper only'];p['metadata']=m;p['topics']=topics(m)
    return p

def entry(p,full=True):
    venue=re.sub(r"[^\w .&/+-]",'',p.get('venue','Paper'))[:65].strip() or 'Paper'
    if venue.lower()=='faimi resource':venue='FAIMI-listed'
    if venue.lower()=='referenced study':venue='Review-listed'
    label={'Paper':'📝 Paper','Code':'💻 Code','Weights':'🌐 Weights','Project':'🌐 Project','Data':'📊 Data'}
    reference_only='nature.com/articles/s41746-024-01276-5#ref-' in p['links'].get('Paper','')
    if reference_only:label['Paper']='📚 Reference listing'
    lines=[f"- (*{venue}'{p['year'][-2:]}*) **{md(p['title'])}**",'  '+' '.join(f"[[{label[k]}]({v})]" for k,v in p['links'].items() if k in label)]
    if full:
        lines += ['  **Metadata:** '+' · '.join(f"`{k}: {' + '.join(p['metadata'][k])}`" for k in ALLOWED)]
        section=p['sources'][0].get('section','source list')
        lines += ['  > **Why it qualifies:** '+('Primary paper link pending; ' if reference_only else '')+'Reference-listed medical fairness work; source category: '+md(section)+'. Imported classifications are traceable to the listed sources; no independent reproduction or new fairness-gain claim is implied.']
        refs=[]
        for source in p['sources']:
            target=source['url']
            legacy=target.startswith('docs/')
            if legacy:target=REPO+'/blob/main/docs/legacy-catalog.md'
            label_source='Original catalog' if legacy else ('2024 review' if 'nature.com' in target else 'FAIMI')
            item=f'[{label_source}]({target})'
            if item not in refs:refs.append(item)
        lines+=['  > **Provenance:** '+' · '.join(refs)]
        if p.get('arxiv_id')=='2110.14755' or p.get('doi')=='10.1016/j.ebiom.2023.104467':
            lines+=['  > **Version note:** Possible preprint/journal lineage; see the [source audit]('+REPO+'/blob/main/docs/source-audit-2026-11-04.md). Not counted as independently evaluated methods.']
    elif p.get('kind')=='survey':
        refs=sorted({source['url'] if not source['url'].startswith('docs/') else REPO+'/blob/main/docs/legacy-catalog.md' for source in p['sources']})
        lines+=['  > **Provenance:** '+' · '.join(f'[Source {i+1}]({url})' for i,url in enumerate(refs))]
    return '\n'.join(lines)

def resources():
    result = '''## 🧰 Datasets, Benchmarks and Toolkits

### Datasets

| Resource | Fairness context | Access and limitations |
|---|---|---|
| [DDI](https://ddi-dataset.github.io/) | Dermatology and skin-tone evaluation | Follow the original dataset's access terms and annotations. |
| [Fitzpatrick17k](https://github.com/mattgroh/fitzpatrick17k) | Dermatology, skin-tone labels | Label reliability and skin-tone estimation are themselves audit questions. |
| [Harvard Glaucoma Fairness](https://github.com/luoyan407/Harvard-GF) | Ophthalmology and protected-group benchmarking | [Dataset landing page](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/A4XMO1). |
| [Harvard FairSeg](https://ophai.hms.harvard.edu/datasets/harvard-fairseg10k/) | Ophthalmic segmentation fairness | Check the authors' current data-access requirements. |
| [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) | Chest radiograph subgroup auditing | Demographic fields, patient splits and label uncertainty must be checked. |
| [MIMIC-CXR](https://physionet.org/content/mimic-cxr/) | Chest radiographs linked to clinical context | Credentialed access; do not redistribute patient records. |
| [ADNI](https://adni.loni.usc.edu/) | Neuroimaging, age/sex/race analyses | Application-based access and cohort selection constraints. |
| [UK Biobank](https://www.ukbiobank.ac.uk/) | Population imaging and demographic analyses | Approved research access; representativeness is not guaranteed. |

### Benchmarks

| Resource | Scope | Access |
|---|---|---|
| MEDFAIR | Multi-dataset fairness evaluation and mitigation | [Official code](https://github.com/ys-zong/MEDFAIR) |
| FairMedFM | Medical imaging foundation-model fairness | [Official code](https://github.com/FairMedFM/FairMedFM) |
| CXR-Fairness | Chest X-ray group metrics and mitigation | [Primary paper](https://proceedings.mlr.press/v174/zhang22a.html) |

### Toolkits

| Toolkit | Purpose | Access |
|---|---|---|
| Fairlearn | Group metrics and mitigation tooling | [Project](https://fairlearn.org/) |
| AI Fairness 360 | Fairness metrics and mitigation implementations | [Official code](https://github.com/Trusted-AI/AIF360) |
| Aequitas | Bias and fairness auditing | [Project](https://github.com/dssg/aequitas) |

These resources are entry points, not claims that one metric or mitigation method is clinically sufficient.
'''
    return re.sub(r'(?m)^\| (?!Resource \||Toolkit \||---)([^|]+) \|', r'| **\1** |', result)

def main():
    if (ROOT/'.local/inventory.json').exists():
        x=json.loads((ROOT/'.local/inventory.json').read_text())
    else:
        x=json.loads((ROOT/'data/source-index.json').read_text())
        x['records']=json.loads((ROOT/'data/catalog.json').read_text())
    records=[prepare(p) for p in apply_primary_links(x['records'])]
    main=[p for p in records if p.get('kind','main')!='survey'];surveys=[p for p in records if p.get('kind')=='survey']
    lines=['# Awesome-MedIA-Fairness','',
        'A curated, source-traceable collection on **medical algorithm fairness**, with medical imaging as its historical core and explicit coverage of EHR, clinical language/foundation models, physiological signals and healthcare algorithms.','',
        '[![Catalog validation]('+REPO+'/actions/workflows/validate-catalog.yml/badge.svg)]('+REPO+'/actions/workflows/validate-catalog.yml) '+
        '[![Link health]('+REPO+'/actions/workflows/check-links.yml/badge.svg)]('+REPO+'/actions/workflows/check-links.yml)','',
        f"**Catalog:** {len(main)} main-list papers and {len(surveys)} surveys/perspectives. **Evidence is recorded per entry:** importing a cited study is not an independent methods audit or reproduction.",'',
        'Built from the [original catalog](docs/legacy-catalog.md), [Xu et al., npj Digital Medicine 2024](https://doi.org/10.1038/s41746-024-01276-5), and [FAIMI resources](https://faimi-workshop.github.io/resources/). See the [source and migration audit](docs/source-audit-2026-11-04.md).','',
        'Weekly Qoder DeepSeek updates: [Chinese digest]('+REPO+'/blob/literature-data/reports/latest.md) · [weekly topic index]('+REPO+'/blob/literature-data/reports/weekly.md) · [screening proposals]('+REPO+'/blob/literature-data/reports/catalog-proposals.md). [Automation guide](docs/literature-automation.md).','',
        '## 🎯 Scope','',
        'We collect studies that examine **algorithmic fairness, protected-group disparities, bias mechanisms, mitigation, or fairness measurement** in an explicit medical/biomedical task. Null findings and unsuccessful mitigation are relevant; a positive fairness gain is not required.','',
        '### Inclusion and evidence','',
        'New machine inclusion proposals require all five: (1) a medical task, (2) an identifiable algorithm or model, (3) an explicit fairness/bias question, (4) defined groups/attributes, a subgroup-discovery protocol, or an explicit individual/counterfactual fairness definition, and (5) implemented evaluation with source-grounded evidence. Full-text verification is required before a machine inclusion proposal.','',
        'Static accuracy differences between disease classes, generic domain adaptation, ordinary imbalance, and health inequality without an algorithmic fairness question are insufficient. Protected-attribute predictability is evidence of encoding, not by itself proof of downstream discrimination. Reviews, perspectives, broad ethical frameworks and generic fairness theory are separated below.','',
        'Historical and reference-list imports remain visible with provenance and evidence labels. **Primary metadata/abstract means that source was retrieved, not that all classifications or findings have been independently re-audited.** Inherited mitigation-stage labels can require correction; post-processing is not assumed to freeze a predictor unless the primary protocol establishes it.','',
        '## 📌 Contents','',
        '- [Taxonomy](#-taxonomy)\n- [Survey Papers](#-survey-papers)\n- [Fairness Papers](#-fairness-papers)\n- [By Topic](#-by-topic)\n- [Datasets, Benchmarks and Toolkits](#-datasets-benchmarks-and-toolkits)\n- [Related Repositories](#-related-repositories)\n- [Cross-References](#-cross-references)\n- [Community and Calls](#-community-and-calls)\n- [Contributing](#-contributing)','',
        '## 🧬 Taxonomy','',
        '| Field | Controlled values |\n|---|---|']
    for field,values in ALLOWED.items():lines.append('| **'+field+'** | '+', '.join('`'+v+'`' for v in sorted(values))+' |')
    lines+=['','Use the smallest directly supported set. `Sex and gender` is a navigation label, not an assertion that the constructs or measurements are interchangeable. `Intersectional` requires joint-group analysis; multiple separate attributes alone are insufficient.','', '## 📚 Survey Papers','']
    for p in sorted(surveys,key=lambda p:(-int(p['year']),p['title'])):lines += [entry(p,False),'']
    lines+=['## 📝 Fairness Papers','', '> Annual entries are bibliographic records after exact-title/identifier deduplication, not independent experiments. Possible preprint/journal lineage is documented in the source audit; records are not merged solely from similar titles or shared authors. Source year and eventual publication year may differ.','']
    for year in sorted({p['year'] for p in main},reverse=True):
        lines+=['### '+year,'']
        for p in sorted((p for p in main if p['year']==year),key=lambda p:p['title'].lower()):lines += [entry(p),'']
    lines+=['## 🧭 By Topic','', '> A complementary index; a paper may appear in multiple topics.','']
    for topic in TOPICS:
        lines+=['### '+topic,'']
        for p in sorted((p for p in main if topic in p['topics']),key=lambda p:(-int(p['year']),p['title'])):lines += [entry(p,False),'']
    lines += [resources(),'## 🔗 Related Repositories','',
        '- [MEDFAIR](https://github.com/ys-zong/MEDFAIR)\n- [FairMedFM](https://github.com/FairMedFM/FairMedFM)\n- [AI Fairness 360](https://github.com/Trusted-AI/AIF360)','',
        '## 🔀 Cross-References','',
        'General fairness theory supports the medical literature but is not counted as medical empirical evidence:','']
    for p in x['foundations']:lines+=[f"- [{md(p['title'])}]({p['links']['Paper']}) · source: [FAIMI]({p['sources'][0]['url']})"]
    lines+=['','## 📣 Community and Calls','',
        '- [FAIMI](https://faimi-workshop.github.io/) · [Resources](https://faimi-workshop.github.io/resources/)\n- [FAIMI 2023–2026 programme leads](docs/workshop-candidates.md): official listings are discovery leads, not independent publication or scope verification.','',
        '## ⚖️ License','',
        'New catalog annotations and documentation: [CC BY 4.0](LICENSE-CONTENT). Automation code: [MIT](LICENSE). Referenced papers, source-site annotations and original illustrations retain their own rights; the legacy list is preserved with attribution.','',
        '## 📖 Citation','',
        'Please cite the [2024 systematic review](https://doi.org/10.1038/s41746-024-01276-5) when using its taxonomy or literature analysis, and use [CITATION.cff](CITATION.cff) for this maintained catalog.','',
        '## 🤝 Contributing','',
        'Read [CONTRIBUTING.md](CONTRIBUTING.md). Provide a primary source, medical task, algorithm, fairness question, group definition and evaluated evidence. Source-list membership alone is not a scientific quality guarantee.','',
        '## ✉️ Contact','', 'Zikang Xu · zikangxu@mail.ustc.edu.cn','']
    (ROOT/'README.md').write_text('\n'.join(lines))
    # Public inventory has provenance and source verification, never full abstracts.
    public=[]
    for p in records:
        q={k:v for k,v in p.items() if k!='abstract'};public.append(q)
    (ROOT/'data/catalog.json').write_text(json.dumps(public,ensure_ascii=False,indent=2)+'\n')
    leads=['# FAIMI programme discovery leads','', 'Fetched 2026-11-04. These titles come from official programme pages; unlinked papers and the tentative 2026 programme are not treated as verified publications or automatically promoted.','']
    existing={norm(p['title']) for p in records}
    for year in ['2026','2025','2024','2023']:
        leads += ['## '+year,'']
        for p in x['workshop_candidates']:
            if p['year']==year:leads += [f"- {md(p['title'])} · [official listing]({p['sources'][0]['url']})"+(' · already represented in catalog' if norm(p['title']) in existing else ' · publication/scope verification pending')]
        leads += ['']
    (ROOT/'docs/workshop-candidates.md').write_text('\n'.join(leads))
    audit=['# Source and migration audit · 2026-11-04','',
        'This is a targeted, source-traceable catalog rebuild, not a new systematic review or reproduction.','',
        f"Original lines parsed: {x['counts']['legacy_rows']}. The review Table 2 yields {x['counts']['review_table_rows']} citation occurrences (63 unique reference identifiers); its article-wide search-count prose is not used as a current catalog count. Selected medical/review/toolkit references from FAIMI yielded {x['counts']['faimi_rows']} reference occurrences. Exact titles and DOI/arXiv/PMID links were merged before rendering.",'',
        f"Rendered: {len(main)} unique main-list papers; {len(surveys)} surveys/perspectives. Retrieved primary bibliographic metadata for {sum(p.get('verified',False) for p in records)} records; other entries explicitly retain source-list/legacy evidence. Abstract availability is recorded separately from independent scientific verification.",'',
        '## Sources','',
        '- [Original catalog](legacy-catalog.md), commit `7ecc995`, preserved verbatim.\n- [Xu et al. 2024, Table 2](https://www.nature.com/articles/s41746-024-01276-5/tables/2), extracted through its [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11487181/).\n- [FAIMI resources](https://faimi-workshop.github.io/resources/), including its medical studies, reviews, toolkits and dataset pointers.\n- Official 2023–2026 FAIMI programme pages; all extracted title leads are archived in [workshop-candidates.md](workshop-candidates.md).','',
        '## Decisions and limits','',
        '- Preserved original code/data links and original source categories; duplicate entries are consolidated in the annual view and repeated only in topic navigation.\n- Corrected DOI parsing to preserve parentheses in Elsevier identifiers. Bibliographic metadata is checked against the cited title before replacement.\n- Review articles found inside a reference table are moved to Survey Papers. Nonmedical general fairness works are retained as cross-references.\n- Programme titles without an accessible primary record remain discovery leads, including the explicitly tentative 2026 poster programme.\n- Inherited metadata can need correction: source classification is not an independent test of model freezing, subgroup definitions or fairness gains.\n- Primary-method review is performed for new machine inclusion proposals, with exact evidence spans. No claim of exhaustive coverage, widespread unfairness, method superiority or first-benchmark novelty is made.','',
        'Sixteen review-reference entries now link directly to DOI records after independent title and author checks against Crossref. The reproducible mappings and metadata endpoints are in [primary-link-resolutions.json](../data/primary-link-resolutions.json). Original display titles are preserved to avoid creating duplicate historical seeds.','',
        '## Unresolved bibliographic checks','']
    for p in records:
        if p.get('verification_warning'):audit += ['- '+md(p['title'])+' · '+p['verification_warning']+'; source-listed metadata retained.']
    audit+=['','## Version-lineage hold','',
        'arXiv:2110.14755 and DOI 10.1016/j.ebiom.2023.104467 share the same four authors and closely related encoding questions. The [author publication page](https://wp.doc.ic.ac.uk/bglocker/publications/) lists the journal article, while retrieved arXiv metadata supplies no journal reference or DOI tying the versions together. They are retained as separately identified bibliographic records pending explicit lineage confirmation, not claimed as independent methods or replications.','']
    (ROOT/'docs/source-audit-2026-11-04.md').write_text('\n'.join(audit).rstrip()+'\n')
    print(f'Rendered {len(main)} main papers, {len(surveys)} surveys, {len(x["workshop_candidates"])} programme leads')

if __name__=='__main__':main()
