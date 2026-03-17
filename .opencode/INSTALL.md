# OpenCode Installation Guide

This guide explains how to use the ARC-AGI Toolkit with OpenCode.

## Overview

The ARC-AGI Toolkit provides Python scripts in the `.opencode/scripts/` directory that work with any coding agent, including OpenCode. These are generic CLI tools for running ARC-AGI-3 games, managing scorecards, and exploring game environments.

## Installation

Run these commands in your project root to set up the toolkit:

```bash
# Clone the toolkit
git clone --depth 1 https://github.com/spoonbobo/arc-code-agent-setup.git /tmp/arcagi-setup

# Create .opencode directory for OpenCode
mkdir -p .opencode

# Copy scripts, skills, and commands to .opencode/
cp -r /tmp/arcagi-setup/scripts .opencode/
cp -r /tmp/arcagi-setup/skills .opencode/
cp -r /tmp/arcagi-setup/commands .opencode/

# Copy configuration files
cp /tmp/arcagi-setup/.env.example ./.env.example
cp /tmp/arcagi-setup/launch.py.template ./launch.py
cp /tmp/arcagi-setup/AGENTS.md ./AGENTS.md

# Clean up
rm -rf /tmp/arcagi-setup

# Install dependencies
uv sync
```

Note: The `.opencode/INSTALL.md` file is NOT copied - it should be read directly from the remote repository URL.

## Using with OpenCode

OpenCode can directly invoke the Python scripts in the `.opencode/scripts/` directory. Use the following patterns:

### Quick Commands

OpenCode has quick commands available via the TUI (press `/`):

- `/arc-setup` - Check configuration
- `/arc-games` - List available games
- `/arc-play` - Quick play a game
- `/arc-inspect [game_id]` - Inspect game without playing
- `/arc-sweep [game_id]` - Run multi-seed sweep

### Direct Script Usage

You can also tell OpenCode to run scripts directly:

```
Run python .opencode/scripts/arc_setup_check.py to verify the setup
```

```
List available games with python .opencode/scripts/arc_list_games.py
```

```
Play game ls20-cb3b57cc with python .opencode/scripts/arc_play.py --game-id ls20-cb3b57cc --steps 20
```

## Available Scripts

All scripts are located in `.opencode/scripts/` and can be run with `python .opencode/scripts/<name>.py`:

**Game Execution:**
- `arc_play.py` - Quick play
- `arc_play_with_recording.py` - Play with recording
- `arc_run_sweep.py` - Multi-seed runs

**Game Discovery:**
- `arc_list_games.py` - List games
- `arc_setup_check.py` - Verify setup
- `arc_inspect_game.py` - Inspect game
- `arc_show_actions.py` - Show actions

**Game Management:**
- `arc_download_game.py` - Download specific game
- `arc_download_all.py` - Download all games

**Scorecard Management:**
- `arc_create_scorecard.py` - Create scorecard
- `arc_get_scorecard.py` - Get scorecard
- `arc_close_scorecard.py` - Close scorecard

## Skills

The toolkit includes skills in the `skills/` directory (also copied to `.opencode/skills/` for OpenCode):

- `arcagi3-research-loop` - Planning experiments
- `arcagi3-attempt-review` - Reviewing runs
- `arcagi3-runner-design` - Designing runners
- `arc-toolkit-usage` - Comprehensive script reference

OpenCode will automatically detect and use these skills from `.opencode/skills/`.

## Environment Variables

Set these in your `.env` file:

- `ARC_API_KEY` - Your ARC-AGI API key
- `ARC_OPERATION_MODE` - normal/online/offline (default: normal)
- `ARC_GAME_ID` - Default game ID

## Example Workflow

```bash
# Check setup
python .opencode/scripts/arc_setup_check.py

# List games
python .opencode/scripts/arc_list_games.py

# Inspect a game
python .opencode/scripts/arc_inspect_game.py --game-id ls20-cb3b57cc

# Quick play
python .opencode/scripts/arc_play.py --game-id ls20-cb3b57cc --steps 10

# Create scorecard for tracked run
python .opencode/scripts/arc_create_scorecard.py --game-id ls20-cb3b57cc --tags "baseline"

# Play with recording
python .opencode/scripts/arc_play_with_recording.py --game-id ls20-cb3b57cc

# Get results
python .opencode/scripts/arc_get_scorecard.py --scorecard-id <id>
```

## Troubleshooting

**Script not found:**
- Make sure you're in the project root
- Run `ls .opencode/scripts/` to verify scripts exist

**Import errors:**
- Run `uv sync` to install dependencies
- Verify Python 3.12+ is installed

**API errors:**
- Check `ARC_API_KEY` is set in `.env`
- Run `python .opencode/scripts/arc_setup_check.py` to diagnose

**Skills not loading in OpenCode:**
- Verify `.opencode/skills/` exists with skill directories

## Support

For detailed script documentation, see the `arc-toolkit-usage` skill or run any script with `--help`.
