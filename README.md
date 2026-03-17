# ARC Code Agent Setup

A complete toolkit for running and improving ARC-AGI-3 game attempts in OpenCode.

## Overview

This toolkit provides OpenCode integration for the ARC-AGI-3 interactive reasoning benchmark, including:

- **11 Quick Commands** for common operations via `/` in TUI
- **12 Full Tools** with TypeScript definitions and Python implementations
- **3 Repo-local Skills** for ARC-AGI workflows
- **Environment management** via `.env` configuration

## What's Included

### Commands (Quick Access)
Type `/` in OpenCode TUI to access:

| Command | Description |
|---------|-------------|
| `/arc-setup` | Check configuration and cached games |
| `/arc-games` | List all available games |
| `/arc-inspect [game_id]` | Inspect game metadata without playing |
| `/arc-actions [game_id]` | Show available actions |
| `/arc-download [game_id]` | Download game for offline use |
| `/arc-download-all` | Download all games |
| `/arc-play [game_id]` | Quick play with default settings |
| `/arc-sweep [game_id]` | Run multi-seed sweep |
| `/arc-scorecard-create` | Create tracked scorecard |
| `/arc-scorecard-get [id]` | Get scorecard results |
| `/arc-scorecard-close [id]` | Close scorecard |

### Tools (Full Interface)
Access via `/` for detailed control:

- `/arc_list_games` - List games with mode filter
- `/arc_download_game` - Download specific game
- `/arc_download_all` - Download all games
- `/arc_inspect_game` - Inspect without playing
- `/arc_show_actions` - Display actions
- `/arc_play` - Play with full options
- `/arc_play_with_recording` - Play with recording
- `/arc_run_sweep` - Multi-seed runs
- `/arc_create_scorecard` - Create custom scorecard
- `/arc_get_scorecard` - Get results
- `/arc_close_scorecard` - Close scorecard
- `/arc_setup_check` - Verify configuration

### Skills (Workflow Guidance)

- `arcagi3-research-loop` - Study games and plan attempts
- `arcagi3-attempt-review` - Diagnose finished runs
- `arcagi3-runner-design` - Design/improve runners

## Installation

### Quick Install (One-liner)

```bash
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash
```

### Manual Install

```bash
git clone https://github.com/spoonbobo/arc-code-agent-setup.git /tmp/arcagi-setup
cp -r /tmp/arcagi-setup/commands /tmp/arcagi-setup/skills /tmp/arcagi-setup/tools /tmp/arcagi-setup/scripts ./.opencode/
cp /tmp/arcagi-setup/.env.example ./.env.example
```

See [INSTALL.md](INSTALL.md) for detailed instructions.

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

## Quick Start

```
/arc-setup       # Verify installation
/arc-games       # See available games
/arc-play        # Quick play
```

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for Python dependency management
- [OpenCode](https://opencode.ai) editor
- ARC_API_KEY (optional, for online mode)

## Documentation

- [OpenCode Install Guide](.opencode/INSTALL.md) - Detailed installation and usage
- [ARC-AGI Docs](https://docs.arcprize.org) - Official ARC-AGI documentation
- [OpenCode Docs](https://opencode.ai/docs) - OpenCode editor documentation

## License

MIT License

## Support

- Issues: [https://github.com/spoonbobo/arc-code-agent-setup/issues](https://github.com/spoonbobo/arc-code-agent-setup/issues)
