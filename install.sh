#!/bin/bash
set -e

echo "🎮 Installing ARC-AGI Toolkit..."

# Check if we're in a project directory
if [ ! -f "pyproject.toml" ] && [ ! -d ".git" ]; then
    echo "⚠️  Warning: No pyproject.toml or .git found. Are you in a project root?"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

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

# Copy directories to root (generic components)
echo "📁 Copying generic components..."
cp -r "$TMP_DIR/scripts" . 2>/dev/null || echo "  - scripts/ already exists or copy failed"
cp -r "$TMP_DIR/skills" . 2>/dev/null || echo "  - skills/ already exists or copy failed"
cp -r "$TMP_DIR/commands" . 2>/dev/null || echo "  - commands/ already exists or copy failed"

# Copy .opencode directory (OpenCode-specific)
if [ -d "$TMP_DIR/.opencode" ]; then
    mkdir -p .opencode
    cp -r "$TMP_DIR/.opencode/"* .opencode/ 2>/dev/null || echo "  - .opencode/ copy completed"
fi

# Copy root-level files if they don't exist
echo "📄 Copying configuration files..."

if [ ! -f ".env.example" ]; then
    cp "$TMP_DIR/.env.example" .env.example 2>/dev/null || true
    echo "✅ Created .env.example"
fi

if [ ! -f "AGENTS.md" ]; then
    cp "$TMP_DIR/AGENTS.md" AGENTS.md 2>/dev/null || true
    echo "✅ Created AGENTS.md"
fi

if [ ! -f "launch.py" ]; then
    cp "$TMP_DIR/launch.py.template" launch.py 2>/dev/null || true
    echo "✅ Created launch.py from template"
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
echo "📁 Installed components:"
echo "  - scripts/      : Python CLI tools (12 scripts)"
echo "  - skills/       : Workflow guidance (4 skills)"
echo "  - commands/     : Quick reference docs"
echo "  - .opencode/    : OpenCode-specific setup"
echo ""
echo "Next steps:"
echo "  1. Copy .env.example to .env and configure:"
echo "     cp .env.example .env"
echo ""
echo "  2. Install dependencies (if not already done):"
echo "     uv sync"
echo ""
echo "  3. Verify setup:"
echo "     python scripts/arc_setup_check.py"
echo ""
echo "  4. List available games:"
echo "     python scripts/arc_list_games.py"
echo ""
echo "For agent-specific instructions, see:"
echo "  - OpenCode: .opencode/INSTALL.md"
echo "  - Generic: README.md"
echo ""
