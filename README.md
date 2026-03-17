# ARC Code Agent Setup

A complete toolkit for running and improving ARC-AGI-3 game attempts. Works with any coding agent.

## Overview

This toolkit provides generic Python CLI tools for the ARC-AGI-3 interactive reasoning benchmark:

- **12 Python Scripts** for game execution, discovery, and scorecard management
- **4 Skills** for ARC-AGI-3 workflows and toolkit usage
- **11 Quick Commands** for reference and guidance
- **Environment management** via `.env` configuration

All components are agent-agnostic and work with OpenCode, Claude Code, Cursor, or any coding agent.

## Installation

Installation differs by platform. Choose your agent:

### OpenCode

Tell OpenCode:
```
Fetch and follow instructions from https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/.opencode/INSTALL.md
```

Or run directly:
```bash
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash
```

**Detailed docs:** [.opencode/INSTALL.md](.opencode/INSTALL.md)

### Claude Code

Add to your CLAUDE.md or tell Claude:
```
This project uses the ARC-AGI Toolkit. Use Python scripts from the scripts/ directory.
See AGENTS.md for ARC-AGI-3 guidance and skills/ for workflow skills.
```

### Cursor

Tell Cursor:
```
Use the ARC-AGI Toolkit in this project. Run Python scripts from scripts/ directory.
Check skills/arc-toolkit-usage/SKILL.md for comprehensive script reference.
```

### Generic (Any Agent)

Use the Python scripts directly from `scripts/` directory. All scripts are standalone CLI tools.

```bash
# Install
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash

# Configure
cp .env.example .env
# Edit .env with your ARC_API_KEY

# Install dependencies
uv sync
```

## What's Included

### Scripts (CLI Tools)

Located in `scripts/` - use with any agent:

**Game Execution:**
- `arc_play.py` - Quick play a game
- `arc_play_with_recording.py` - Play with full recording
- `arc_run_sweep.py` - Multi-seed runs for analysis

**Game Discovery:**
- `arc_list_games.py` - List available games
- `arc_setup_check.py` - Verify setup
- `arc_inspect_game.py` - Inspect game without playing
- `arc_show_actions.py` - Show available actions

**Game Management:**
- `arc_download_game.py` - Download specific game
- `arc_download_all.py` - Download all games

**Scorecard Management:**
- `arc_create_scorecard.py` - Create tracked scorecard
- `arc_get_scorecard.py` - Get results
- `arc_close_scorecard.py` - Close scorecard

### Skills (Workflow Guidance)

Located in `skills/` - automatically detected by agents:

- `arcagi3-research-loop` - Study games and plan attempts
- `arcagi3-attempt-review` - Diagnose finished runs
- `arcagi3-runner-design` - Design/improve runners
- `arc-toolkit-usage` - Comprehensive script reference

### Commands (Quick Reference)

Located in `commands/` - reference documentation:

- `arc-setup.md` - Check configuration
- `arc-games.md` - List games
- `arc-play.md` - Quick play
- `arc-inspect.md` - Inspect game
- `arc-sweep.md` - Multi-seed sweep
- And 6 more...

## Quick Start

```bash
# Check setup
python scripts/arc_setup_check.py

# List games
python scripts/arc_list_games.py

# Quick play
python scripts/arc_play.py --game-id ls20-cb3b57cc --steps 10
```

## Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env`:
   ```
   ARC_API_KEY=your-api-key-here  # Optional
   ARC_OPERATION_MODE=normal      # online, offline, or normal
   ARC_GAME_ID=                   # Optional: specific game
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

## Project Structure

```
.
├── README.md              # This file
├── AGENTS.md             # Generic ARC-AGI-3 guidance
├── launch.py.template    # Generic launcher template
├── .env.example          # Environment template
├── install.sh            # Setup script
│
├── scripts/              # Generic Python CLI tools
│   ├── arc_play.py
│   ├── arc_list_games.py
│   └── ... (12 total)
│
├── skills/               # Agent-agnostic skills
│   ├── arcagi3-research-loop/
│   ├── arcagi3-attempt-review/
│   ├── arcagi3-runner-design/
│   └── arc-toolkit-usage/
│
├── commands/             # Quick reference
│   ├── arc-setup.md
│   ├── arc-play.md
│   └── ... (11 total)
│
├── .opencode/            # OpenCode-specific
│   └── INSTALL.md
│
├── .claude/              # Claude Code (future)
├── .cursor/              # Cursor (future)
└── .codex/               # Codex (future)
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for Python dependency management
- Any coding agent (OpenCode, Claude Code, Cursor, etc.)
- ARC_API_KEY (optional, for online mode)

## Documentation

- [OpenCode Guide](.opencode/INSTALL.md) - OpenCode-specific setup
- [AGENTS.md](AGENTS.md) - Generic ARC-AGI-3 guidance
- [ARC-AGI Docs](https://docs.arcprize.org) - Official ARC-AGI documentation

## Example Workflows

### Quick Development Test
```bash
python scripts/arc_setup_check.py
python scripts/arc_list_games.py
python scripts/arc_play.py --steps 5
```

### Formal Experiment
```bash
python scripts/arc_create_scorecard.py --game-id ls20-cb3b57cc --tags "baseline"
python scripts/arc_play_with_recording.py --game-id ls20-cb3b57cc
python scripts/arc_get_scorecard.py --scorecard-id <id>
```

### Multi-Seed Analysis
```bash
python scripts/arc_run_sweep.py --game-id ls20-cb3b57cc --runs 20 --steps 15
```

### Offline Development
```bash
python scripts/arc_download_all.py
python scripts/arc_play.py --mode offline --game-id ls20-cb3b57cc
```

## License

MIT License

## Support

- Issues: [https://github.com/spoonbobo/arc-code-agent-setup/issues](https://github.com/spoonbobo/arc-code-agent-setup/issues)
