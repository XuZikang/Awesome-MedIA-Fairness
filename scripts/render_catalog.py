"""Render the English methodology catalog from public structured records only."""
from __future__ import annotations
import html
import json
import re
from pathlib import Path
from scripts.build_catalog import norm
from scripts.catalog_schema import ALLOWED, MAIN_HEADING
from scripts.catalog_editorial import METHODS, validate_annotation

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/XuZikang/Awesome-MedIA-Fairness'
COLORS = {'Fairness Evaluation':'2563eb','Pre-processing':'b45309','In-processing':'9333ea','Post-processing':'15803d','Stage pending':'64748b',
          'Domain':'0369a1','Focus':'0e7490','Attributes':'be185d','Assets':'0f766e','Evidence':'475569','Survey':'92400e'}


def md(value):
    return str(value).replace('\n',' ').replace('<','&lt;').replace('>','&gt;').replace('[','\\[').replace(']','\\]')


def badge(label, family):
    slug = re.sub('[^a-z0-9]+','-', (family+'-'+label).lower()).strip('-')
    path = ROOT/'assets/badges'/f'{slug}.svg'
    path.parent.mkdir(parents=True, exist_ok=True)
    width = max(40, int(len(label)*6.4+16))
    color = COLORS.get(family, '64748b')
    path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" role="img" aria-label="{html.escape(label, quote=True)}"><title>{html.escape(label)}</title><rect width="{width}" height="20" rx="4" fill="#{color}"/><text x="{width/2}" y="14" text-anchor="middle" fill="white" font-family="Verdana,Arial,sans-serif" font-size="11">{html.escape(label)}</text></svg>\n')
    return f'![{md(label)}](assets/badges/{slug}.svg)'


def entry(p):
    method=p['method'];m=p['metadata']
    venue=re.sub(r"[^\w .&/+-]",'',p.get('venue','Paper'))[:65].strip() or 'Paper'
    tags=[badge(method,method)]
    if p.get('kind')=='survey':tags.append(badge('Survey','Survey'))
    for field in ('Domain','Focus','Attributes','Assets','Evidence'):
        tags.append(badge(' + '.join(m[field]),field))
    labels={'Paper':'Paper','Code':'Code','Weights':'Weights','Project':'Project','Data':'Data'}
    links=' '.join(f'[[{labels[k]}]({v})]' for k,v in p['links'].items() if k in labels)
    lines=[f"- (*{venue}'{p['year'][-2:]}*) **{md(p['title'])}** "+' '.join(tags), '', '  '+links, '',
           '  **Metadata:** '+' · '.join(f"`{k}: {' + '.join(m[k])}`" for k in ALLOWED), '',
           '  **TLDR:** '+' '.join(md(sentence) for sentence in p['tldr_en']), '',
           '  **Date:** '+p['publication_date'], '']
    return '\n'.join(lines)


def sort_key(p):
    # Unknown month/day sorts after known dates in the same year, never invented.
    return p['publication_date'].ljust(10,'0'), p['title'].casefold()


def validate_records(records):
    seen=set()
    for p in records:
        key=norm(p['title'])
        if key in seen:raise ValueError('Duplicate paper title: '+p['title'])
        seen.add(key)
        if p.get('method') not in METHODS:raise ValueError('Missing primary methodology: '+p['title'])
        validate_annotation({'tldr_en':p.get('tldr_en'),'method':p['method'],'reason_zh':'分类验证','evidence_quotes':[]},'')
        if not re.fullmatch(r'\d{4}(?:-\d{2}(?:-\d{2})?)?',p.get('publication_date','')) or p['publication_date'][:4]!=p['year']:
            raise ValueError('Invalid publication date: '+p['title'])
        if len(p['publication_date'])>=7 and not 1<=int(p['publication_date'][5:7])<=12:raise ValueError('Invalid month')
        for field,allowed in ALLOWED.items():
            if not p['metadata'].get(field) or not set(p['metadata'][field])<=allowed:raise ValueError('Invalid '+field+': '+p['title'])
        if not p['links']['Paper'].startswith('https://'):raise ValueError('Missing primary record')


def main(root=None):
    global ROOT
    if root is not None:ROOT=Path(root)
    records=json.loads((ROOT/'data/catalog.json').read_text())
    validate_records(records)
    latest=max(p['year'] for p in records)
    lines=['# Awesome-MedIA-Fairness','',
        'A collection of research on **medical algorithm fairness**, covering medical imaging, clinical prediction, physiological signals and clinical foundation models.','',
        '[![Catalog validation]('+REPO+'/actions/workflows/validate-catalog.yml/badge.svg)]('+REPO+'/actions/workflows/validate-catalog.yml) '+
        '[![Link health]('+REPO+'/actions/workflows/check-links.yml/badge.svg)]('+REPO+'/actions/workflows/check-links.yml)','',
        f"**{len(records)} papers**, including surveys and perspectives, organized by methodology. Each paper has one primary placement; secondary contributions remain in its metadata and TLDR.",'',
        '## 🎯 Scope','',
        'Studies must address algorithmic fairness, subgroup disparities, bias mechanisms, fairness measurement or mitigation in a medical task. Negative findings are eligible. Predicting a protected attribute does not by itself establish downstream discrimination. General fairness foundations are listed separately.','',
        '## 📌 Contents','',
        '- [Taxonomy](#-taxonomy)\n- [Papers](#-papers)\n  - [Fairness Evaluation](#fairness-evaluation)\n  - [Pre-processing](#unfairness-mitigation-pre-processing)\n  - [In-processing](#unfairness-mitigation-in-processing)\n  - [Post-processing](#unfairness-mitigation-post-processing)\n- [Datasets, Benchmarks and Toolkits](#-datasets-benchmarks-and-toolkits)\n- [Contributing](#-contributing)','',
        '## 🧬 Taxonomy','',
        'The methodology follows [Addressing fairness issues in deep learning-based medical image analysis: a systematic review](https://doi.org/10.1038/s41746-024-01276-5). Surveys and empirical studies share the same taxonomy; surveys carry an additional badge.','',
        '| Method | Definition |\n|---|---|',
        '| '+badge('Fairness Evaluation','Fairness Evaluation')+' | Benchmarking, subgroup comparisons, bias source tracing, mechanism discovery and fairness measurement. |',
        '| '+badge('Pre-processing','Pre-processing')+' | Interventions on training data, sampling, augmentation or data transformation. |',
        '| '+badge('In-processing','In-processing')+' | Interventions on learning objectives, representations, model training or optimization. |',
        '| '+badge('Post-processing','Post-processing')+' | Interventions after model training, such as output adjustment, calibration or reviewed model adaptation; predictor freezing must be established from the specific protocol. |','',
        '`Stage pending` is an evidence-status bucket for mitigation records whose intervention stage is not yet established, not an additional methodology. Within each category, records run newest to oldest. The latest catalog year is divided by month; missing months remain explicitly unverified. Dates retain the precision supplied by the original record, rather than the discovery date.','',
        '| Field | Controlled values |\n|---|---|']
    for field,values in ALLOWED.items():
        lines.append('| **'+field+'** | '+', '.join(badge(v,v if v in METHODS else field)+' `'+v+'`' for v in sorted(values))+' |')
    lines+=['','Title badges use distinct colors for methodology, domain, focus, attributes, available assets and evidence level. Metadata and evidence labels describe the available record; a metadata or abstract check is not a full-methods audit.','',MAIN_HEADING,'']
    for method in METHODS:
        group=[p for p in records if p['method']==method]
        if not group and method=='Stage pending':continue
        heading=method if method=='Fairness Evaluation' else 'Unfairness Mitigation: '+method
        lines+=['### '+heading,'']
        for year in sorted({p['year'] for p in group},reverse=True):
            lines+=['#### '+year,'']
            month=None
            for p in sorted((p for p in group if p['year']==year),key=sort_key,reverse=True):
                current=p['publication_date'][:7] if len(p['publication_date'])>=7 else 'Month unverified'
                if year==latest and current!=month:
                    lines+=['##### '+current,''];month=current
                lines+=[entry(p),'']
    lines += [resources(),'## 🔗 Related Repositories','',
        '- [MEDFAIR](https://github.com/ys-zong/MEDFAIR)\n- [FairMedFM](https://github.com/FairMedFM/FairMedFM)\n- [AI Fairness 360](https://github.com/Trusted-AI/AIF360)','',
        '## 🔀 Cross-References','', 'General fairness foundations, outside the medical catalog:','']
    index=json.loads((ROOT/'data/source-index.json').read_text())
    for p in index['foundations']:lines += [f"- [{md(p['title'])}]({p['links']['Paper']})"]
    lines+=['','## 📣 Community and Updates','',
        '- [FAIMI](https://faimi-workshop.github.io/) · [Resources](https://faimi-workshop.github.io/resources/)\n- [FAIMI programme discovery leads](docs/workshop-candidates.md)\n- [Weekly review packet](reports/review-latest.md) · [review instructions](docs/review-workflow.md) · [Chinese screening evidence](reports/latest.md)\n- [Source audit](docs/source-audit-2026-11-04.md) · [original catalog archive](docs/legacy-catalog.md)\n- [Weekly automation guide](docs/literature-automation.md): candidate review packets update every Sunday at 10:07 Asia/Shanghai; new papers enter this README only after explicit maintainer approval.','',
        '## ⚖️ License','', 'New catalog annotations: [CC BY 4.0](LICENSE-CONTENT). Automation code: [MIT](LICENSE). Referenced papers and original materials retain their own rights.','',
        '## 📖 Citation','', 'Please cite the [systematic review](https://doi.org/10.1038/s41746-024-01276-5) when using its taxonomy, and [CITATION.cff](CITATION.cff) for this catalog.','',
        '## 🤝 Contributing','', 'Read [CONTRIBUTING.md](CONTRIBUTING.md). Supply an original paper record, publication date, three English TLDR sentences and evidence for the methodology label. Chinese screening notes belong in reports.','',
        '## ✉️ Contact','', 'Zikang Xu · zikangxu@mail.ustc.edu.cn','']
    (ROOT/'README.md').write_text('\n'.join(lines))
    print(f'Rendered {len(records)} papers using the review methodology')

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


if __name__=='__main__':main()
