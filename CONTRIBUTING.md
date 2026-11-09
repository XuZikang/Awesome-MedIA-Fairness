# Contributing

Submit a paper suggestion or pull request with the original paper record and official resource links. Medical algorithm fairness studies require a medical task, an algorithm, an explicit fairness question, defined groups or a counterfactual/individual fairness protocol, and evaluated evidence. Null findings are welcome. Reviews and perspectives share the main methodology catalog and carry a Survey badge; general nonmedical fairness theory stays in Cross-References.

Edit `data/catalog.json`, then run `python3 -m scripts.render_catalog`. Do not edit generated README entries directly. Preserve original titles and identifiers, the available publication-date precision and original code/data links. Check DOI, arXiv, PMID and normalized title for duplicates. Version lineage needs explicit evidence; similar titles or matching authors alone are insufficient.

Choose one primary methodology from Fairness Evaluation, Pre-processing, In-processing or Post-processing, following the 2024 systematic review. Use Stage pending if a mitigation intervention is not established. Keep secondary contributions in metadata, with only the controlled labels from `scripts/catalog_schema.py`. Read the primary abstract and relevant methods; do not infer clinical benefit, positive gains, intersectionality or predictor freezing from a title.

Supply `tldr_en` as exactly three English sentences: the problem, the method/study design, and the supported result or interpretation. Explain evidence limitations honestly. The generated README is entirely English, has colored values in two rows below each title, without field-name prefixes or Assets/Evidence badges, and newest-first dates with month subheadings in the latest year. Chinese classification evidence and maintainer judgments belong in `reports/`.

Run:

```bash
python3 -m scripts.render_catalog
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -q
git diff --check
```

Do not upload patient data, private documents, credentials or third-party full papers. New catalog annotations are CC BY 4.0; automation code is MIT. Source works retain their own rights.

Screening prioritizes original methodology and task-specific fairness audits. Reviews and commentaries require a concrete medical disease/task and detailed fairness analysis; incidental fairness mentions are insufficient. See [screening-policy.md](docs/screening-policy.md).

For imaging records, use only explicitly supported modality values (for example MRI, CT, X-ray, OCT, dermoscopy or fundus photography). Multiple modalities may be selected when the study actually uses them. Use `Medical imaging (modality unspecified)` when the available source cannot establish the modality; do not label a study from incidental background mentions. Keep actual paper/code/data links in `links`; Assets remains internal bookkeeping.

Future additions must satisfy the [prospective venue policy](docs/venue-policy.md), as well as explicit maintainer approval and source-grounded topic screening. Run `python3 -m scripts.recall` before publication. Keep publication-identity candidates separate from confirmed relationships; do not merge on shared authors or a title search alone.
