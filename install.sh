#!/bin/bash
set -e

echo "🎮 Installing ARC-AGI Toolkit for OpenCode..."

# Check if we're in a project directory
if [ ! -f "pyproject.toml" ] && [ ! -d ".git" ]; then
    echo "⚠️  Warning: No pyproject.toml or .git found. Are you in a project root?"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Create .opencode directory if it doesn't exist
mkdir -p .opencode

# Temporary directory for download
TMP_DIR=$(mktemp -d)
trap "rm -rf $TMP_DIR" EXIT

echo "📦 Downloading ARC-AGI Toolkit..."

# Clone or download the repository
if command -v git &> /dev/null; then
    git clone --depth 1 https://github.com/spoonbobo/arc-code-agent-setup.git "$TMP_DIR" 2>/dev/null
else
    echo "❌ Git not found. Please install git or use manual installation."
    exit 1
fi

# Copy directories
echo "📁 Copying files..."
cp -r "$TMP_DIR/commands" .opencode/ 2>/dev/null || echo "  - commands/ already exists or copy failed"
cp -r "$TMP_DIR/skills" .opencode/ 2>/dev/null || echo "  - skills/ already exists or copy failed"
cp -r "$TMP_DIR/tools" .opencode/ 2>/dev/null || echo "  - tools/ already exists or copy failed"
cp -r "$TMP_DIR/scripts" .opencode/ 2>/dev/null || echo "  - scripts/ already exists or copy failed"

# Copy .env.example if it doesn't exist
if [ ! -f ".env.example" ]; then
    cp "$TMP_DIR/.env.example" .env.example 2>/dev/null || true
    echo "✅ Created .env.example"
fi

# Check for Python
echo "🐍 Checking Python dependencies..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.12+."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
if [ "${PYTHON_VERSION%%.*}" -lt 3 ] || ([ "${PYTHON_VERSION%%.*}" -eq 3 ] && [ "${PYTHON_VERSION#*.}" -lt 12 ]); then
    echo "⚠️  Python $PYTHON_VERSION found. Python 3.12+ recommended."
fi

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "⚠️  'uv' not found. Install with: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi

# Check for arc-agi package
echo "📋 Checking ARC-AGI package..."
if ! python3 -c "import arc_agi" 2>/dev/null; then
    echo "⚠️  arc-agi package not found."
    if [ -f "pyproject.toml" ]; then
        echo "   Run: uv sync"
    else
        echo "   Run: uv add arc-agi"
    fi
fi

echo ""
echo "✅ ARC-AGI Toolkit installed successfully!"
echo ""
echo "Next steps:"
echo "  1. Copy .env.example to .env and configure:"
echo "     cp .env.example .env"
echo ""
echo "  2. Install dependencies (if not already done):"
echo "     uv sync"
echo ""
echo "  3. Verify installation in OpenCode TUI:"
echo "     /arc-setup"
echo ""
echo "  4. List available games:"
echo "     /arc-games"
echo ""
echo "For detailed documentation, see:"
echo "  .opencode/INSTALL.md"
echo ""
