#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "🔧 Setting up CI/CD environment..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 required but not installed"
    exit 1
fi

if [ ! -d "$REPO_ROOT/.venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv "$REPO_ROOT/.venv"
fi

source "$REPO_ROOT/.venv/bin/activate"
echo "📥 Installing dependencies..."
pip install -q requests pyyaml
chmod +x "$SCRIPT_DIR"/*.py

echo "✅ Setup complete!"
echo "   Next: Add COPR secrets in GitHub, then run: python3 $SCRIPT_DIR/check_updates.py"
