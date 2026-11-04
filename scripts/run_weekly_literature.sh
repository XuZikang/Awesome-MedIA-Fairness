#!/usr/bin/env bash
# Run with existing Magpie/gh credentials; publish English catalog and Chinese evidence to main.
set -euo pipefail
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
mkdir -p .local
exec 9>.local/weekly.lock
flock -n 9 || { echo "Another literature update is running"; exit 1; }
test -z "$(git status --porcelain --untracked-files=no)"
python3 -m unittest discover -s tests -q
python3 scripts/validate_catalog.py

git fetch origin refs/heads/main:refs/remotes/origin/main
# The service updates source code before opening this shell script.
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
PUBLICATION_TREE="$(mktemp -d "$REPO_ROOT/.local/publication.XXXXXX")"
rmdir "$PUBLICATION_TREE"
git worktree prune --expire now
git worktree add --detach "$PUBLICATION_TREE" origin/main
rm -f "$PUBLICATION_TREE/reports/run-status.json"
set +e
python3 -u -m scripts.literature_pipeline.cli --require-model \
  --catalog "$PUBLICATION_TREE/README.md" \
  --state "$PUBLICATION_TREE/data/literature-state.json" \
  --output "$PUBLICATION_TREE/reports" \
  --publish-root "$PUBLICATION_TREE"
PIPELINE_STATUS=$?
set -e
# No stale marker can authorize publication after a fatal error.
test -f "$PUBLICATION_TREE/reports/run-status.json"
python3 - "$PUBLICATION_TREE" <<'PY'
import json,sys
from pathlib import Path
from scripts.validate_catalog import CatalogValidator,IssueFormValidator
root=Path(sys.argv[1]);text=(root/'README.md').read_text()
errors=CatalogValidator(text).validate()+IssueFormValidator(text,(root/'.github/ISSUE_TEMPLATE/01-paper-suggestion.yml').read_text()).validate()
if errors:raise SystemExit('\n'.join(errors))
status=json.loads((root/'reports/run-status.json').read_text())
if 'catalog_publication' not in status:raise SystemExit('Catalog publication did not complete')
PY
git -C "$PUBLICATION_TREE" config user.name "Medical Fairness Literature Bot"
git -C "$PUBLICATION_TREE" config user.email "medical-fairness-literature@users.noreply.github.com"
git -C "$PUBLICATION_TREE" add README.md assets/badges data/catalog.json data/literature-state.json reports
if ! git -C "$PUBLICATION_TREE" diff --cached --quiet; then
  git -C "$PUBLICATION_TREE" diff --cached --check
  git -C "$PUBLICATION_TREE" commit -m "docs: update English fairness catalog and Chinese screening evidence"
fi
git -C "$PUBLICATION_TREE" -c 'credential.helper=!gh auth git-credential' push origin HEAD:refs/heads/main
# Remove only this clean, successfully published transient worktree.
git worktree remove "$PUBLICATION_TREE"
exit "$PIPELINE_STATUS"
