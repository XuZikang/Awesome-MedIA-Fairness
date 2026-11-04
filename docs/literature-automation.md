# Automated literature discovery and catalog updates

The weekly pipeline searches arXiv, Europe PMC and PubMed, deduplicates identifiers and titles, and uses the existing Qoder DeepSeek endpoint for Chinese screening and English catalog annotations. **Weekly runs publish candidates and Chinese review packets only. New papers enter `README.md` only after explicit maintainer approval.** Chinese reasoning, exact evidence spans and run diagnostics remain in `reports/` on the same branch. The historical `literature-data` branch is retained as an archive and receives no new production updates.

## Catalog and methodology

`data/catalog.json` is the authoritative, public catalog. Each record preserves the original title, primary paper/resource links and available publication-date precision. The renderer `python3 -m scripts.render_catalog` is deterministic and requires no network, private cache or model. It produces colored local SVG badges and one complete entry per paper; surveys are integrated and marked with a Survey badge.

The methodology follows Xu et al. (2024): Fairness Evaluation, and Unfairness Mitigation through Pre-processing, In-processing or Post-processing. A separate Stage pending container avoids guessing an unknown mitigation stage. One primary placement reflects the paper's main contribution, while secondary contributions remain in metadata and three English TLDR sentences. Within each category, dates descend from newest to oldest; the latest catalog year has month subheadings. Missing month information is shown as unverified, never replaced by discovery time.

Historical labels and metadata are evidence-limited. Primary abstract/metadata retrieval does not imply a full-methods audit. The original inventory and source audit remain available in `docs/`; per-entry provenance markers are omitted from the README. Chinese classification rationales for the migration are in `reports/catalog-review.md`.

## Screening and human-approved inclusion

New machine additions require current full-text-supported screening with all five criteria: a medical task, an identifiable algorithm, an explicit fairness question, group definitions or an individual/counterfactual fairness protocol, and implemented evaluation. Null or unsuccessful results remain eligible. Encoding a sensitive attribute is not alone proof of unequal downstream performance. Abstract-only, unrelated and evidence-insufficient candidates stay in the Chinese screening reports.

After the maintainer submits a reviewed Markdown packet, `scripts/publish_catalog.py` requires an explicit approval file, accepts only approved paper IDs with matching evidence fingerprints, checks identifiers against the whole catalog, retrieves primary full text, and calls `scripts/catalog_editorial.py` for three English TLDR sentences and one primary methodology. Quotes are checked against supplied source spans; Chinese reasons are retained separately. The renderer validates structured records before publication. Model screening and summaries remain machine interpretations that the maintainer can correct by editing the JSON and rerendering.

Queries, overlap, per-query caps and the default 100-analysis budget are in `config/literature.json`. Failed query windows are retained and retried rather than marked complete. Failed English annotations are not promoted and cause a nonzero run status; other completed results are preserved. Full article bodies and abstracts stay out of public state.

## Production deployment

The independent IAI-61 systemd timer runs **Sunday 10:07 Asia/Shanghai** (02:07 UTC), with catch-up after downtime. Source checkout: `~/.local/share/medical-fairness-literature/repo`. Model environment: `~/.config/medical-fairness-literature.env`, mode 600. The existing Magpie user service exposes `http://127.0.0.1:3425/v1/chat/completions`, model `qoder-cn/dfmodel`, provider namespace `qoder-cn-medical-fairness`. Existing Qoder and GitHub credentials remain on the server.

The wrapper locks concurrent invocations, runs tests and catalog validation, and creates a temporary worktree from current `origin/main`. It searches/reviews against the persistent private SQLite database and writes public candidate state and Chinese review reports in that worktree. The wrapper verifies that README, catalog and badges have not changed and stages only candidate state and reports. It validates the completed output, creates a commit and pushes normally to `main`. It uses no force push. A concurrent remote change rejects the push and preserves the unpublished worktree for inspection; the next run starts from updated main. Successfully published worktrees are removed. Fatal runs without a fresh status marker cannot publish stale results.

```bash
systemctl --user status fairness-weekly.timer
systemctl --user start fairness-weekly.service
journalctl --user -u fairness-weekly.service -n 80 --no-pager
```

The GitHub workflow supports manual dispatch with an externally reachable model endpoint. Production uses the server's existing local sign-in. No extra weekly Codex automation or hosted schedule is required.

## Local operation

Python 3.9+, standard library only:

```bash
# Discovery and Chinese reports only; no model calls
python3 -m scripts.literature_pipeline.cli --metadata-only

# Model screening and Chinese human-review packets
python3 -m scripts.literature_pipeline.cli --require-model

# Explicit application after the maintainer submits approvals
python3 -m scripts.literature_pipeline.cli --require-model --publish-root . --approval-file /path/to/reviewed.md

# Deterministic render and validation
python3 -m scripts.render_catalog
python3 scripts/validate_catalog.py
python3 -m unittest discover -s tests -q
```

Set `LITERATURE_LLM_ENDPOINT`, `LITERATURE_LLM_MODEL`, optional `LITERATURE_LLM_API_KEY`, and a stable `LITERATURE_LLM_CACHE_NAMESPACE` in the local environment. `--require-model` refuses missing configuration or a zero analysis budget. HTTPS is required outside loopback. Article text is sent to the configured model provider. Official OA XML/arXiv HTML are used without paywall bypass.

Public files: `data/catalog.json`, `data/literature-state.json`, `reports/latest.md`, `reports/weekly.md`, `reports/catalog-proposals.md`, `reports/catalog-screening.md`, and `reports/run-status.json`. Private `.local/literature.sqlite3` retains fetched abstracts and review caches. Public JSON restores an empty database; copy private SQLite separately for full local continuity. Never run simultaneous processes against the same database.

## Maintainer review

See [the Chinese review guide](review-workflow.md). Open `reports/review-latest.md`; reply in chat with stable paper IDs and approve/reject/hold decisions, or edit the decision and comment lines in the Markdown file and provide it to the assistant. The weekly job never passes an approval file. Default pending and model suggestions are not approval.
