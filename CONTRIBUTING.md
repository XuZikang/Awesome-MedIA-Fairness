# Contributing

Use the [paper-suggestion form](https://github.com/XuZikang/Awesome-MedIA-Fairness/issues/new?template=01-paper-suggestion.yml) or open a pull request. Main-list additions need a medical task, an identifiable algorithm, an explicit fairness/bias question, group definitions, a subgroup-discovery protocol or an individual/counterfactual fairness definition, and evaluated evidence.

Read the primary abstract and relevant methods. State what was evaluated, rather than assuming a positive fairness gain, causality or clinical benefit. Sensitive-attribute encoding is not by itself proof of downstream discrimination. Generic class imbalance, domain shift and health inequality do not qualify without an algorithmic fairness question. Reviews and perspectives belong in Survey Papers, and general nonmedical fairness theory in Cross-References.

Use the controlled labels in `scripts/catalog_schema.py`. Add one full entry under the correct publication year and concise copies under all applicable By Topic sections. Preserve provenance and official code/data links. Search titles, DOI, arXiv and PMID before submitting; preprint and journal versions may share a work, but genuine extensions are not automatically merged.

```markdown
- (*Venue'26*) **Paper title**
  [[📝 Paper](https://example.org/paper)] [[💻 Code](https://github.com/org/repo)]
  **Metadata:** `Domain: Medical imaging` · `Focus: Evaluation + Mitigation` · `Stage: In-processing` · `Attributes: Sex and gender` · `Assets: Code` · `Evidence: Primary full text`
  > **Why it qualifies:** Names the medical algorithm, protected-group question, intervention and evaluated evidence, including negative or limited results.
```

The sample URLs are placeholders, never valid catalog links. Evidence labels describe retrieved sources: primary bibliographic metadata is not a methods audit. Only mark Primary full text after inspecting the paper. A reviewer must check that mitigation-stage labels match the actual procedure, especially whether post-processing freezes the base predictor. Do not infer intersectional evaluation from the presence of several separately evaluated attributes.

Run:

```bash
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -v
git diff --check
```

Dataset/toolkit descriptions must link to the authors' official resources and describe access restrictions honestly. Do not upload patient data, private documents, API credentials or third-party full papers. New annotations/docs are CC BY 4.0; automation is MIT. Source works retain their own rights.
