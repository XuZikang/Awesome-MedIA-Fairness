#!/usr/bin/env bash
# Publish only an explicitly reviewed Markdown packet using the configured model.
set -euo pipefail
if [[ $# != 1 || ! -f "$1" ]]; then
  echo "Usage: $0 /path/to/reviewed.md" >&2
  exit 1
fi
APPROVAL_FILE="$(cd -- "$(dirname -- "$1")" && pwd)/$(basename -- "$1")"
REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"
mkdir -p .local
exec 9>.local/weekly.lock
flock -n 9 || { echo "Another literature update is running" >&2; exit 1; }
test -z "$(git status --porcelain --untracked-files=no)"
git fetch origin refs/heads/main:refs/remotes/origin/main
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
PUBLICATION_TREE="$(mktemp -d "$REPO_ROOT/.local/editorial.XXXXXX")"
rmdir "$PUBLICATION_TREE"
git worktree add --detach "$PUBLICATION_TREE" origin/main
set +e
(
  cd "$PUBLICATION_TREE"
  python3 -m scripts.publish_catalog --approval-file "$APPROVAL_FILE"
)
EDITORIAL_STATUS=$?
set -e
# Status 2 retains decisions when evidence or model access is still pending.
if [[ "$EDITORIAL_STATUS" != 0 && "$EDITORIAL_STATUS" != 2 ]]; then
  echo "Publication stopped. Worktree retained at $PUBLICATION_TREE" >&2
  exit "$EDITORIAL_STATUS"
fi
(
  cd "$PUBLICATION_TREE"
  python3 scripts/validate_catalog.py
  git add README.md assets/badges data/catalog.json data/curation-decisions.json reports
  git diff --cached --check
  if ! git diff --cached --quiet; then
    git -c user.name="Medical Fairness Literature Bot" \
        -c user.email="medical-fairness-literature@users.noreply.github.com" \
        commit -m "Curate explicitly reviewed medical fairness literature"
    git -c 'credential.helper=!gh auth git-credential' push origin HEAD:refs/heads/main
  fi
)
git worktree remove "$PUBLICATION_TREE"
exit "$EDITORIAL_STATUS"
