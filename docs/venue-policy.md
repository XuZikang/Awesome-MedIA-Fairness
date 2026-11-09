# Venue eligibility policy

This policy is an evidence gate for future medical-AI fairness candidates. It
does not remove or reclassify the existing catalog. Human approval remains a
separate requirement after this venue assessment.

## Verified source editions

The runtime registry is `config/venue-policy.json`. The downloaded source
artifacts and the one-off parsers are retained under
`.local/venue-policy-sources/`.

| Registry | Edition and authority | Rows | Source SHA-256 |
| --- | --- | ---: | --- |
| CAS | 2025 Chinese Academy of Sciences partition table, published by Hebei Normal University as an institutional copy | 21,772 | `c3b8d16839317f0d46115216e70808d2ed5bd9b194377a76ffcfec55ca632238` |
| CCF | Seventh edition, China Computer Federation; published 2026-03-31 and corrected 2026-04-09 | 679 | `271b630b576bf8a4f802e767f5694caded93680e22b3a19bef7902591c45c1d3` |

CAS source page: <https://huaxue.hebtu.edu.cn/a/2025/09/23/A5A5BBD96F6B4410B87B6D4C43BDFD63.html>

CCF source page: <https://www.ccf.org.cn/Academic_Evaluation/By_category/2026-03-31/870181.shtml>

The CCF PDF explicitly says that only Full paper/Regular paper conference
papers are considered; Short paper, Demo, Technical Brief, Summary, Findings
and accompanying Workshops are outside the directory. The extracted CCF rows
are 294 journals and 385 conferences (A/B/C combined); the source PDF is the
authoritative row list used here, not a secondary ranking site.

## Decisions

- A journal is eligible only when its exact normalized title or registered ISSN
  matches a 2025 CAS zone 1/2 record.
- A main conference is eligible only when its exact normalized name/alias
  matches a CCF A/B conference record. CCF journal A/B records do not qualify
  a journal under this policy; they remain pending unless another supported
  CAS record qualifies it.
- CAS zone 3/4 journal matches and CCF C conference matches are explicitly `ineligible`. CCF journal grades do not establish a CAS partition.
- Missing or unsupported venues, unverified ranks, ambiguous aliases, and
  title/ISSN conflicts are `pending`. Matching is exact after Unicode
  normalization, case folding, punctuation/whitespace normalization and ISSN
  hyphen removal; no fuzzy similarity or publisher inference is used.
- A conference marked Workshop, Short paper, Demo, Technical Brief, Summary or
  Findings is not allowed to inherit its parent conference's rank. A journal
  short communication is not treated as a conference non-regular paper.
- A plain preprint returns `status: "preprint"` and
  `eligible_for_human_review: true`, while `automatic_inclusion` is always
  false. An arXiv/preprint record with an external DOI, unresolved publication
  tracking state, or unknown/conflicting confidence is `pending` until its
  formal identity is explicit.
- When `formal_publications` are supplied, each formal version is assessed
  first. Any failed formal venue makes the preprint `ineligible`; an unresolved
  formal assessment makes it `pending`; all confirmed formal assessments must
  qualify before the preprint can return `eligible`.

## Python interface

```python
from scripts.venue_policy import assess_venue, load_policy, validate_policy

policy = load_policy(repo_root)
errors = validate_policy(policy)
result = assess_venue(
    {
        "journal_title": "Medical Image Analysis",
        "journal_issns": [],
        "conference": "",
    },
    policy,
)
```

`assess_venue()` returns at least `status`, `reason_zh`, `evidence`,
`eligible_for_human_review` and `automatic_inclusion`. Formal-version checks
are included in `formal_assessments`; no rank is fabricated for a preprint.

The module accepts `journal_title`, `journal_issns`/`issns`, `conference`,
`publication_type`/`paper_type`, `formal_publications`, `publication_tracking`,
`confidence`, `source`, `arxiv_id` and DOI fields. `load_policy(root)` accepts
the repository path explicitly so callers do not depend on their working
directory.

## Scope and maintenance limits

The CAS table is an institutional copy rather than a direct CAS-hosted API,
and the table itself contains a small number of duplicate/case-variant or
ambiguous rows. Such exact conflicts are retained as evidence and produce a
pending result rather than an inferred rank. CCF entries do not supply ISSNs in
the official PDF; title/alias matching therefore remains the exact fallback
for CCF, while an ISSN/title conflict is pending when both are supplied.

The policy is intentionally not a JCR/SCIE gate and does not infer a venue from
DOI prefixes, publishers or conference families. Existing catalog grandfather
handling is owned by the catalog integration layer and is not performed here.
