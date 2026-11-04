#!/usr/bin/env bash
# This script runs on the user's existing server. Credentials stay in Magpie/gh.
set -euo pipefail
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
mkdir -p .local
exec 9>.local/weekly.lock
flock -n 9 || { echo "Another literature update is running"; exit 1; }

# Refuse to overwrite a locally modified code checkout. Generated outputs use
# a different worktree, so the production source checkout stays clean.
test -z "$(git status --porcelain --untracked-files=no)"
# The service refreshes main with ExecStartPre, before Bash opens this script.
# This avoids replacing a running shell script during a code update.
python3 -m unittest discover -s tests -q
python3 scripts/validate_catalog.py

OUTPUT_TREE="${LITERATURE_OUTPUT_TREE:-$REPO_ROOT/../output}"
git ls-remote --heads origin refs/heads/literature-data > .local/output-ref
if [ -d "$OUTPUT_TREE" ]; then
  test -z "$(git -C "$OUTPUT_TREE" status --porcelain)"
  if [ -s .local/output-ref ]; then
    git fetch origin refs/heads/literature-data:refs/remotes/origin/literature-data
    git -C "$OUTPUT_TREE" merge --ff-only refs/remotes/origin/literature-data
  fi
elif [ -s .local/output-ref ]; then
  git fetch origin refs/heads/literature-data:refs/remotes/origin/literature-data
  git worktree prune --expire now
  git worktree add --detach "$OUTPUT_TREE" refs/remotes/origin/literature-data
else
  git worktree prune --expire now
  git worktree add --detach "$OUTPUT_TREE" HEAD
fi

# Build in a staging directory. A failed model/source run must not leave the
# persistent output worktree dirty or mistake an old marker for a fresh run.
RUN_OUTPUT="$(mktemp -d "$REPO_ROOT/.local/weekly-run.XXXXXX")"
mkdir -p "$RUN_OUTPUT/data"
if [ -f "$OUTPUT_TREE/data/literature-state.json" ]; then
  cp "$OUTPUT_TREE/data/literature-state.json" "$RUN_OUTPUT/data/"
fi
if [ -d "$OUTPUT_TREE/reports" ]; then
  cp -R "$OUTPUT_TREE/reports" "$RUN_OUTPUT/reports"
fi
python3 - "$RUN_OUTPUT" <<'PY'
from pathlib import Path
import sys
marker = Path(sys.argv[1]) / 'reports/run-status.json'
if marker.exists():
    marker.unlink()
PY
set +e
python3 -u -m scripts.literature_pipeline.cli --require-model \
  --state "$RUN_OUTPUT/data/literature-state.json" \
  --output "$RUN_OUTPUT/reports"
PIPELINE_STATUS=$?
set -e
test -f "$RUN_OUTPUT/reports/run-status.json"
test -f "$RUN_OUTPUT/data/literature-state.json"
mkdir -p "$OUTPUT_TREE/data" "$OUTPUT_TREE/reports"
cp "$RUN_OUTPUT/data/literature-state.json" "$OUTPUT_TREE/data/"
cp -R "$RUN_OUTPUT/reports/." "$OUTPUT_TREE/reports/"
git -C "$OUTPUT_TREE" config user.name "Medical Fairness Literature Bot"
git -C "$OUTPUT_TREE" config user.email "medical-fairness-literature@users.noreply.github.com"
git -C "$OUTPUT_TREE" add data/literature-state.json reports
if ! git -C "$OUTPUT_TREE" diff --cached --quiet; then
  git -C "$OUTPUT_TREE" commit -m "docs: update Chinese literature digest and screening"
fi
git -C "$OUTPUT_TREE" -c 'credential.helper=!gh auth git-credential' push origin HEAD:refs/heads/literature-data
if [ "$PIPELINE_STATUS" -eq 0 ]; then
  python3 - "$RUN_OUTPUT" <<'PY'
from pathlib import Path
import shutil
import sys
directory = Path(sys.argv[1]).resolve()
if directory.parent == Path('.local').resolve() and directory.name.startswith('weekly-run.'):
    shutil.rmtree(directory)
else:
    raise SystemExit('Unexpected staging directory; refusing cleanup')
PY
fi
exit "$PIPELINE_STATUS"
