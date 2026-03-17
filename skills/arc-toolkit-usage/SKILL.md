---
name: arc-toolkit-usage
description: Comprehensive guide to using the ARC-AGI Toolkit Python scripts for running remote game attempts, managing scorecards, and exploring games
---

# ARC-AGI Toolkit Usage Guide

## Overview

This skill provides a comprehensive reference for all scripts in the `scripts/` directory. These are generic Python CLI tools that work with any coding agent.

## Quick Start

All scripts are located in the `scripts/` directory and can be run directly:

```bash
python scripts/<script_name>.py [options]
```

## Script Reference

### Game Execution

#### arc_play.py
Quick play an ARC-AGI game with default settings.

**Usage:**
```bash
python scripts/arc_play.py
python scripts/arc_play.py --game-id ls20-cb3b57cc
python scripts/arc_play.py --mode offline --steps 20
```

**Options:**
- `--game-id`: Specific game ID (auto-discovers if not provided)
- `--mode`: Operation mode - normal/online/offline (default: normal)
- `--steps`: Number of steps to run (default: 10)
- `--render`: Enable terminal rendering

**When to use:** Quick testing, development, or running a single game session.

---

#### arc_play_with_recording.py
Play a game with full recording enabled for later analysis.

**Usage:**
```bash
python scripts/arc_play_with_recording.py --game-id ls20-cb3b57cc
python scripts/arc_play_with_recording.py --steps 50 --tags "experiment-1"
```

**Options:**
- `--game-id`: Game ID to play
- `--steps`: Number of steps
- `--tags`: Comma-separated tags for the run
- `--note`: Optional note about the attempt

**When to use:** When you need to capture full replay data for analysis or debugging.

---

#### arc_run_sweep.py
Run multiple attempts with different random seeds.

**Usage:**
```bash
python scripts/arc_run_sweep.py --game-id ls20-cb3b57cc --runs 10
python scripts/arc_run_sweep.py --runs 20 --steps 15
```

**Options:**
- `--game-id`: Game ID (auto-discovers if not provided)
- `--runs`: Number of runs with different seeds (default: 5)
- `--steps`: Steps per run (default: 10)
- `--mode`: Operation mode (default: normal)

**When to use:** Statistical analysis, testing policy robustness, or gathering performance metrics across multiple runs.

---

### Game Discovery & Setup

#### arc_list_games.py
List all available ARC-AGI games.

**Usage:**
```bash
python scripts/arc_list_games.py
python scripts/arc_list_games.py --mode online
python scripts/arc_list_games.py --mode offline
```

**Options:**
- `--mode`: Filter by operation mode - normal/online/offline (default: normal)

**When to use:** To see what games are available before starting work.

---

#### arc_setup_check.py
Verify ARC-AGI setup and configuration.

**Usage:**
```bash
python scripts/arc_setup_check.py
```

**Checks:**
- API key configuration
- Operation mode settings
- Cached games count
- Environment status

**When to use:** First-time setup verification or troubleshooting connection issues.

---

#### arc_inspect_game.py
Inspect a game without playing it.

**Usage:**
```bash
python scripts/arc_inspect_game.py --game-id ls20-cb3b57cc
```

**Options:**
- `--game-id`: Game ID to inspect (required)
- `--mode`: Operation mode (default: normal)

**When to use:** Understanding game mechanics, available actions, or initial state before attempting.

---

#### arc_show_actions.py
Show available actions for a specific game.

**Usage:**
```bash
python scripts/arc_show_actions.py --game-id ls20-cb3b57cc
```

**Options:**
- `--game-id`: Game ID (auto-discovers if not provided)

**When to use:** Planning your action strategy or debugging action space issues.

---

### Game Management

#### arc_download_game.py
Download a specific game for offline use.

**Usage:**
```bash
python scripts/arc_download_game.py --game-id ls20-cb3b57cc
```

**Options:**
- `--game-id`: Game ID to download (required)

**When to use:** Preparing for offline development or caching games for faster access.

---

#### arc_download_all.py
Download all available games for offline use.

**Usage:**
```bash
python scripts/arc_download_all.py
python scripts/arc_download_all.py --mode online
```

**Options:**
- `--mode`: Which games to download - normal/online/offline (default: normal)

**When to use:** Setting up a complete offline environment or batch caching.

---

### Scorecard Management

#### arc_create_scorecard.py
Create a new tracked scorecard for a game.

**Usage:**
```bash
python scripts/arc_create_scorecard.py --game-id ls20-cb3b57cc
python scripts/arc_create_scorecard.py --game-id ls20-cb3b57cc --tags "baseline,v1"
```

**Options:**
- `--game-id`: Game ID (required)
- `--tags`: Comma-separated tags
- `--note`: Optional note
- `--opaque`: JSON string for custom metadata

**When to use:** Starting a tracked experiment or formal evaluation run.

---

#### arc_get_scorecard.py
Retrieve and display a scorecard.

**Usage:**
```bash
python scripts/arc_get_scorecard.py --scorecard-id <id>
```

**Options:**
- `--scorecard-id`: Scorecard ID (required)
- `--json`: Output as JSON

**When to use:** Reviewing results from a previous run.

---

#### arc_close_scorecard.py
Close a scorecard and finalize results.

**Usage:**
```bash
python scripts/arc_close_scorecard.py --scorecard-id <id>
```

**Options:**
- `--scorecard-id`: Scorecard ID (required)

**When to use:** Completing an experiment and finalizing the scorecard.

---

## Common Workflows

### Quick Development Test
```bash
# Check setup
python scripts/arc_setup_check.py

# List available games
python scripts/arc_list_games.py

# Quick play
python scripts/arc_play.py --steps 5
```

### Formal Experiment
```bash
# Create scorecard
python scripts/arc_create_scorecard.py --game-id ls20-cb3b57cc --tags "experiment-1"

# Run with recording
python scripts/arc_play_with_recording.py --game-id ls20-cb3b57cc --steps 50

# Get results
python scripts/arc_get_scorecard.py --scorecard-id <id>

# Close scorecard
python scripts/arc_close_scorecard.py --scorecard-id <id>
```

### Multi-Seed Analysis
```bash
# Run sweep
python scripts/arc_run_sweep.py --game-id ls20-cb3b57cc --runs 20 --steps 15

# Analyze results (output will show aggregate stats)
```

### Offline Development
```bash
# Download all games
python scripts/arc_download_all.py

# Work offline
python scripts/arc_play.py --mode offline --game-id ls20-cb3b57cc
```

## Environment Variables

All scripts respect these environment variables:

- `ARC_API_KEY`: Your ARC-AGI API key
- `ARC_OPERATION_MODE`: Default operation mode (normal/online/offline)
- `ARC_GAME_ID`: Default game ID

Set these in your `.env` file or export them in your shell.

## Best Practices

1. **Always check setup first** when starting a new session
2. **Use tags** for scorecards to organize experiments
3. **Close scorecards** reliably, even on failures
4. **Prefer offline mode** for rapid iteration
5. **Use sweeps** for statistical validation
6. **Record important runs** for later analysis

## Troubleshooting

**"No games available"**
- Check `ARC_API_KEY` is set
- Try different operation mode
- Run `arc_setup_check.py` to diagnose

**"launch.py not found"**
- Ensure you're in the project root directory
- Run `install.sh` to set up the project

**"Permission denied"**
- Make sure scripts are executable or use `python scripts/...`

---

For more details on specific scripts, run them with `--help` flag.
