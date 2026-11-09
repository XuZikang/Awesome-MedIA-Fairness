"""Versioned screening preferences supplied by the repository maintainer."""
import hashlib
import json
import re

POLICY_VERSION = '2-methodology-first'
POLICY_PROMPT = '''Prioritize original methodological contributions to medical algorithm fairness: evaluation designs, metrics, benchmarks, bias mechanisms and pre/in/post-processing mitigation. Original task-specific fairness audits are eligible, including negative findings; novelty or positive gains are not mandatory.
Give reviews, perspectives and editorial commentaries lower priority. A review/commentary is eligible ONLY if it names a specific medical disease or task AND provides substantive, detailed algorithmic-fairness analysis for that setting (for example subgroup metrics, mechanisms, a concrete evaluation framework, or compared mitigation methods). Both conditions need separate exact evidence spans. Mentioning fairness/bias once, listing ethics or governance challenges, or making generic equitable-AI recommendations is insufficient: exclude these incidental-mention papers, rather than recommending them as related. Generic nonmedical fairness methods are out of scope unless evaluated in an explicit medical task. Generic clinical robustness, class imbalance and site shift alone do not establish fairness.
For reviews, detailed task-specific synthesis may count as the evaluation criterion; do not demand experiments conducted by the review authors, and never portray synthesis as a new empirical result. If access is too limited to decide whether the required detailed analysis exists, use hold and explain the missing evidence. Distinguish review evidence from original methodology/evaluation. A maintainer's explicit inclusion exception is a human curation choice, not a reason to relax automatic rules for all future articles.'''


def paper_version(paper):
    """Article-content identity independent of model/provider/prompt changes."""
    fields={k:paper.get(k,'') for k in ('title','abstract_hash','updated','version','doi','pmcid')}
    return hashlib.sha256(json.dumps(fields,sort_keys=True).encode()).hexdigest()


def current_human_decision(paper, ledger):
    value=ledger.get(paper.get('id'),{})
    if value.get('content_version'):
        return value if value['content_version']==content_version(paper) else {}
    return value if value.get('paper_version')==paper_version(paper) else {}


def content_version(paper):
    """Database refresh timestamps alone do not invalidate human decisions."""
    fields={k:paper.get(k,'') for k in ('title','abstract_hash','version')}
    return hashlib.sha256(json.dumps(fields,sort_keys=True).encode()).hexdigest()


def priority_adjustment(paper):
    text=(paper.get('title','')+' '+paper.get('abstract','')).lower()
    review=bool(re.search(r'\breview\b|\bperspective\b|editorial commentary|scoping synthesis',paper.get('title','').lower()) or
                re.search(r'\b(?:this|our|narrative|scoping|systematic) review\b',text))
    methodology=bool(re.search(r'propos|novel|benchmark|fairness.metric|calibrat|mitigat|debias|audit|causal|framework',text))
    return (4 if methodology else 0)-(8 if review else 0)
