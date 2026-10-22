#!/usr/bin/env bash
# Commit and push the current state of the LO-CARB prototype.
# Usage: ./push.sh "Commit message"
set -e
cd "$(dirname "$0")"
git add -A
if git diff --cached --quiet; then echo "Nothing to commit."; exit 0; fi
git commit -m "${1:-Update LO-CARB website prototype}"
git push
