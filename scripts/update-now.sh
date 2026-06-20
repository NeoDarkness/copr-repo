#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$REPO_ROOT"
echo "🚀 Checking for updates..."

[ -d ".venv" ] && source ".venv/bin/activate"
python3 "$SCRIPT_DIR/check_updates.py"

if git diff --quiet; then
    echo "✅ No changes"
else
    echo "✅ Changes detected. Review: git diff"
fi
