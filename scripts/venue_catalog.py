"""Prospective venue gate; preserve the explicitly approved existing catalog."""
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def title_key(title):
    normalized=re.sub(r'[^a-z0-9]','',title.casefold())
    return hashlib.sha256(normalized.encode()).hexdigest()


def validate_catalog_venues(records):
    from scripts.venue_policy import assess_venue,load_policy
    baseline=json.loads((ROOT/'config/catalog-venue-baseline.json').read_text())
    protected=set(baseline['approved_title_sha256'])
    new=[p for p in records if title_key(p['title']) not in protected]
    if not new:return
    policy=load_policy()
    for p in new:
        paper={**p,'journal_title':p.get('journal_title') or (p.get('venue','') if not p.get('arxiv_id') else '')}
        result=assess_venue(paper,policy)
        if result['status'] not in {'eligible','preprint'}:
            raise ValueError('Publication venue not eligible or verified: '+p['title']+'; '+result['reason_zh'])
