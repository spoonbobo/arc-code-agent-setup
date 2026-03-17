# Installing ARC-AGI Toolkit

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Python 3.12+
- `uv` for Python dependency management
- ARC_API_KEY (optional, for online mode)

## Quick Install

From your project root:

```bash
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash
```

## Manual Installation

```bash
# Clone this repository
git clone https://github.com/spoonbobo/arc-code-agent-setup.git /tmp/arcagi-setup

# Copy files to your project
cp -r /tmp/arcagi-setup/commands /tmp/arcagi-setup/skills /tmp/arcagi-setup/tools /tmp/arcagi-setup/scripts ./.opencode/

# Optional: copy example environment file
cp /tmp/arcagi-setup/.env.example ./.env.example
```

## Configuration

1. Copy `.env.example` to `.env` and edit:
   ```bash
   cp .env.example .env
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Verification

Run these commands in OpenCode TUI:

- `/arc-setup` - Check configuration
- `/arc-games` - List available games
- `/arc-play` - Quick play

For detailed instructions, see `.opencode/INSTALL.md`

## What's Included

- **11 Commands** - Quick access via `/` in TUI
- **12 Tools** - Full TypeScript tool interface
- **13 Python Scripts** - Implementation backing
- **3 Skills** - ARC-AGI specific guidance

## License

MIT
