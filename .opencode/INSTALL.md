# Installing ARC-AGI Toolkit for OpenCode

## Prerequisites

- [OpenCode.ai](https://opencode.ai) installed
- Python 3.12+
- `uv` for Python dependency management
- ARC_API_KEY (optional, for online mode)

## Installation

### Option 1: One-liner Script (Recommended)

From your project root, run:

```bash
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash
```

This will:
- Copy `.opencode/` directory with all tools, commands, and skills
- Check Python dependencies
- Create `.env.example` if it doesn't exist

### Option 2: Manual Copy

```bash
# Clone the setup repository
git clone https://github.com/spoonbobo/arc-code-agent-setup.git /tmp/arcagi-setup

# Copy to your project
cp -r /tmp/arcagi-setup/commands ./.opencode/
cp -r /tmp/arcagi-setup/skills ./.opencode/
cp -r /tmp/arcagi-setup/tools ./.opencode/
cp -r /tmp/arcagi-setup/scripts ./.opencode/

# Optional: copy example files
cp /tmp/arcagi-setup/.env.example ./.env.example
```

## Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and set your configuration:
   ```
   ARC_API_KEY=your-api-key-here  # Optional, for online mode
   ARC_OPERATION_MODE=normal      # Options: online, offline, normal
   ARC_GAME_ID=                   # Optional: specific game ID
   ```

3. Install Python dependencies:
   ```bash
   uv sync
   ```

## Verification

After installation, verify everything works:

1. **Check setup:**
   ```
   /arc-setup
   ```

2. **List available games:**
   ```
   /arc-games
   ```

3. **Quick play:**
   ```
   /arc-play
   ```

## Available Commands

### Setup & Discovery
- `/arc-setup` - Check configuration and cached games
- `/arc-games` - List all available games
- `/arc-inspect [game_id]` - Inspect game metadata
- `/arc-actions [game_id]` - Show available actions

### Download & Cache
- `/arc-download [game_id]` - Download game for offline use
- `/arc-download-all` - Download all games

### Gameplay
- `/arc-play [game_id]` - Quick play
- `/arc-sweep [game_id]` - Run multi-seed sweep

### Scorecards
- `/arc-scorecard-create` - Create scorecard
- `/arc-scorecard-get [id]` - Get results
- `/arc-scorecard-close [id]` - Close scorecard

## Available Tools

Use `/` to access the full tool interface:

- `/arc_list_games` - List games with mode filter
- `/arc_download_game` - Download specific game
- `/arc_download_all` - Download all games
- `/arc_inspect_game` - Inspect without playing
- `/arc_show_actions` - Display actions
- `/arc_play` - Quick play with options
- `/arc_play_with_recording` - Play with recording
- `/arc_run_sweep` - Multi-seed runs
- `/arc_create_scorecard` - Create custom scorecard
- `/arc_get_scorecard` - Get results
- `/arc_close_scorecard` - Close scorecard
- `/arc_setup_check` - Verify configuration

## Troubleshooting

### Commands not showing in TUI
- Ensure `.opencode/commands/` exists with `.md` files
- Restart OpenCode

### Tools failing
- Check Python 3.12+ is installed: `python --version`
- Verify `uv` is installed: `uv --version`
- Run `uv sync` to install dependencies

### API errors
- Verify `ARC_API_KEY` is set in `.env`
- Check your internet connection for ONLINE mode

### Import errors
- Ensure you're running from project root
- Check `PYTHONPATH` includes the project directory

## Updating

To update to the latest version:

```bash
# Re-run the install script
curl -sL https://raw.githubusercontent.com/spoonbobo/arc-code-agent-setup/main/install.sh | bash
```

Or manually pull and copy:

```bash
cd /tmp/arcagi-setup && git pull
cp -r /tmp/arcagi-setup/.opencode/* ./.opencode/
```

## Getting Help

- **Issues:** [https://github.com/spoonbobo/arc-code-agent-setup/issues](https://github.com/spoonbobo/arc-code-agent-setup/issues)
- **ARC-AGI Docs:** [https://docs.arcprize.org](https://docs.arcprize.org)
- **OpenCode Docs:** [https://opencode.ai/docs](https://opencode.ai/docs)

## License

MIT License
