# Source and migration audit · 2026-11-04

This is a targeted, source-traceable catalog rebuild, not a new systematic review or reproduction.

Original lines parsed: 35. The review Table 2 yields 69 citation occurrences (63 unique reference identifiers); its article-wide search-count prose is not used as a current catalog count. Selected medical/review/toolkit references from FAIMI yielded 74 reference occurrences. Exact titles and DOI/arXiv/PMID links were merged before rendering.

Rendered: 90 unique main-list papers; 16 surveys/perspectives. Retrieved primary bibliographic metadata for 93 records; other entries explicitly retain source-list/legacy evidence. Abstract availability is recorded separately from independent scientific verification.

## Sources

- [Original catalog](legacy-catalog.md), commit `7ecc995`, preserved verbatim.
- [Xu et al. 2024, Table 2](https://www.nature.com/articles/s41746-024-01276-5/tables/2), extracted through its [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11487181/).
- [FAIMI resources](https://faimi-workshop.github.io/resources/), including its medical studies, reviews, toolkits and dataset pointers.
- Official 2023–2026 FAIMI programme pages; all extracted title leads are archived in [workshop-candidates.md](workshop-candidates.md).

## Decisions and limits

- Preserved original code/data links and original source categories; duplicate entries are consolidated in the annual view and repeated only in topic navigation.
- Corrected DOI parsing to preserve parentheses in Elsevier identifiers. Bibliographic metadata is checked against the cited title before replacement.
- Review articles found inside a reference table are moved to Survey Papers. Nonmedical general fairness works are retained as cross-references.
- Programme titles without an accessible primary record remain discovery leads, including the explicitly tentative 2026 poster programme.
- Inherited metadata can need correction: source classification is not an independent test of model freezing, subgroup definitions or fairness gains.
- Primary-method review is performed for new machine inclusion proposals, with exact evidence spans. No claim of exhaustive coverage, widespread unfairness, method superiority or first-benchmark novelty is made.

Sixteen review-reference entries now link directly to DOI records after independent title and author checks against Crossref. The reproducible mappings and metadata endpoints are in [primary-link-resolutions.json](../data/primary-link-resolutions.json). Original display titles are preserved to avoid creating duplicate historical seeds.

## Unresolved bibliographic checks


## Version-lineage hold

arXiv:2110.14755 and DOI 10.1016/j.ebiom.2023.104467 share the same four authors and closely related encoding questions. The [author publication page](https://wp.doc.ic.ac.uk/bglocker/publications/) lists the journal article, while retrieved arXiv metadata supplies no journal reference or DOI tying the versions together. They are retained as separately identified bibliographic records pending explicit lineage confirmation, not claimed as independent methods or replications.

## Methodology and presentation revision

The preceding README revision merged the 106 historical bibliographic records and three full-text-screened discoveries into 109 entries. Surveys retain a Survey badge and share the evaluation/mitigation methodology rather than a separate list. Primary placements are 69 evaluation, 14 pre-processing, 22 in-processing and four post-processing; secondary contributions remain in metadata. Every title has local colored badges, a separate metadata paragraph and three English TLDR sentences. Dates preserve source precision; the latest year has month subsections. Chinese editorial reasoning is in reports/catalog-review.md. The four remaining reference-only entries now use verified primary PMLR/arXiv records, including RFIB arXiv:2203.04950, with matching title and authors.

Thirty-seven annotations were completed through the configured Qoder DeepSeek endpoint before it reported usage exhaustion. The remaining entries were edited from inspected primary abstracts, original bibliographic records and review methodology; missing outcome evidence is disclosed in the TLDR rather than filled with invented gains. These annotations are summaries, not 109 full-text audits. The production publication target is now main; literature-data is a historical archive.

## Maintainer review applied

The submitted review packet approved seven papers, rejected 43, held two and left one pending. Approved records were checked against primary PubMed metadata/abstracts and added with honest evidence labels, bringing the catalog to 116. The editorial and educational-image representation audit are described as such. Decisions and source review hashes are in data/curation-decisions.json; the original submitted Markdown is archived under reports/review-approval-50b463591dfd.md. New methodology-first screening rules are in docs/screening-policy.md.
