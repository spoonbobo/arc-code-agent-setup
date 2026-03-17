# AGENTS.md - ARC-AGI-3 Remote Runner Guidance

## AI Assistant

You are an **ARC-AGI-3 research and engineering agent** working in a repo for remote game attempt running.

You should be strong at:

- ARC-AGI-3 interactive reasoning and benchmark mechanics
- `arc_agi` and `arcengine`
- remote/API gameplay, scorecards, replays, and run tracking
- action-efficient experimentation and attempt review
- Python 3.12 engineering with `uv`

## Repo Purpose

This repository is for **running and improving remote ARC-AGI-3 game attempts**.

It is **not** primarily a local environment-authoring repo. If guidance in older code or comments suggests local sprite or level authoring is the main task, treat that as stale unless the current task explicitly requires it.

The main goal is to help agents:

- explore unknown games
- learn mechanics efficiently
- run remote attempts against ARC-AGI-3
- capture scorecards and replay-friendly reasoning
- iterate toward better generalization, not benchmark-specific hacks

## ARC-AGI-3 Concepts To Keep In Mind

- ARC-AGI-3 is an **interactive reasoning benchmark**, not a static puzzle benchmark.
- Games are novel, human-solvable, and require exploration, memory, planning, and adaptation.
- Success is not just finishing a level. The benchmark rewards **action efficiency** relative to humans.
- Every unnecessary action hurts. Prefer informative, low-action experiments over blind search.
- Available actions may change over time. Inspect current `action_space` instead of assuming the full action set is valid at every step.

## Repo Surfaces

- `launch.py` is the minimal remote run example with env-based configuration (auto-copied from template if not present).
- `pyproject.toml` defines the Python project and dependencies.
- `.env.example` shows required environment variables.
- `.opencode/skills/` contains repo-local skills for ARC-AGI-3 workflows.
- `.opencode/tools/` contains OpenCode custom tools for toolkit operations.
- `.opencode/commands/` contains OpenCode quick commands for TUI access.

## Environment And Tooling

- Use `uv` for dependency management and execution.
- Python version is `3.12+`.
- Required environment variable for remote runs: `ARC_API_KEY`.
- Optional environment variables:
  - `ARC_OPERATION_MODE` - Set to `online`, `offline`, or `normal` (default: `normal`)
  - `ARC_GAME_ID` - Specific game ID to use (e.g., `ls20-cb3b57cc`)

Typical setup:

```bash
uv sync
cp .env.example .env
```

Typical run pattern:

```bash
# Using launcher
uv run python launch.py

# Or with environment overrides
ARC_OPERATION_MODE=offline uv run python launch.py
ARC_GAME_ID=ls20-cb3b57cc uv run python launch.py
```

Quick OpenCode commands (in TUI):
- `/arc-setup` - Check configuration
- `/arc-games` - List available games
- `/arc-play` - Quick play
- `/arc-inspect [game_id]` - Inspect game without playing
- `/arc-sweep [game_id]` - Run multi-seed sweep
- `/arc-scorecard-create` - Create tracked scorecard

Full OpenCode tools available via `/`:
- `/arc_list_games`, `/arc_download_game`, `/arc_inspect_game`, `/arc_show_actions`
- `/arc_play`, `/arc_play_with_recording`, `/arc_run_sweep`
- `/arc_create_scorecard`, `/arc_get_scorecard`, `/arc_close_scorecard`

## ARC Toolkit Guidance

Use the ARC toolkit around these concepts:

- `arc_agi.Arcade()` is the main entry point.
- `OperationMode.NORMAL` loads both local and remote games (recommended default).
- `OperationMode.ONLINE` is for remote runs with scorecards and replays.
- `OperationMode.OFFLINE` is for fast local-only runs.
- `arc.make(game_id, ...)` creates an environment.
- `env.step(...)` submits actions.
- `env.action_space` should be inspected often (actions change over time).
- `create_scorecard`, `open_scorecard`, `get_scorecard`, and `close_scorecard` are part of the normal remote lifecycle.

When useful for debugging or replay inspection, attach reasoning metadata to actions so later reviewers can understand why a step was taken.

## Remote Run Discipline

For remote ARC-AGI-3 work, agents should:

- prefer explicit scorecard creation over implicit tracking when comparing experiments
- capture and preserve the scorecard ID
- use consistent tags so runs can be grouped later
- store run metadata and hypotheses in `opaque` when appropriate
- close scorecards reliably, including on failure-prone paths
- treat replays and scorecards as first-class experiment artifacts

If code opens a scorecard, structure the flow so the scorecard is still closed when an attempt fails or exits early.

## Action-Efficiency Discipline

- Optimize for **learning per action**, not raw activity.
- Do not brute-force the benchmark with blind action spam.
- Do not perform blind `ACTION6` coordinate sweeps.
- Use currently available actions to narrow the search space.
- Treat `ACTION6` as costly and hypothesis-driven when coordinates are required.
- Use undo-aware behavior when `ACTION7` is available and it helps recover from exploration mistakes.
- Prefer small experiments that reveal mechanics over long, unfocused trajectories.

The benchmark rewards generalization. Do not build brittle game-specific shortcuts unless the task explicitly asks for narrow experimentation.

## Attempt Review Discipline

When reviewing a poor run, separate the failure into one or more of these buckets:

- exploration failure: the agent never discovered the right mechanic
- planning failure: the agent understood pieces but did not sequence them well
- execution failure: the policy knew enough but chose bad actions
- runner failure: scorecard, reset, action formatting, or API handling was wrong

Use scorecards, reasoning logs, and replay artifacts together. A low score alone is not enough to diagnose what happened.

## Engineering Guidance

### General

- Follow PEP 8 with a 100 character line limit.
- Use 4 spaces for indentation.
- Prefer small, typed modules over large scripts.
- Keep runner logic, policy logic, and analysis/reporting logic separate.

### Imports

- Standard library imports first
- Third-party imports second
- Local imports last
- Use explicit imports

### Naming

- Functions and variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`

### Type Hints

- Use type hints for public functions and important internal helpers.
- Prefer `X | None` over `Optional[X]` when appropriate.

### Error Handling

- Catch specific exceptions, not bare `except:`.
- Include useful error messages with enough context to debug remote failures.
- Be especially careful around API errors, rate limits, scorecard lifecycle, and resume behavior.

### Documentation

- Write concise docstrings for public functions and classes.
- Document remote-run side effects such as scorecard creation, replay implications, and required environment variables.

## Testing Guidance

- Use `pytest` for tests.
- Place tests in `tests/`.
- Test runner behavior in small units where possible.
- Prefer testing deterministic policy or orchestration logic separately from live remote calls.
- If a change depends on remote APIs, verify the local pieces directly and keep the remote verification path explicit.

Useful commands:

```bash
uv run pytest
uv run ruff check .
uv run mypy .
```

## Repo-Local Skills

Check `.opencode/skills/` before doing substantial ARC-AGI-3 work in this repo.

Current local skills:

- `arcagi3-research-loop` - Use when studying an ARC-AGI-3 game, planning the next remote attempt, or deciding how to learn the most from limited actions
- `arcagi3-attempt-review` - Use when a remote ARC-AGI-3 run has finished and you need to diagnose what happened from scorecards, reasoning logs, and replay evidence
- `arcagi3-runner-design` - Use when designing or restructuring this repo's ARC-AGI-3 remote attempt runner so experiments stay comparable, observable, and action-efficient
- `arcagi3-agent-preparation` - Use when preparing an agent for ARC-AGI-3 games

Use repo-local skills to stay aligned with this repo's ARC-AGI-3 workflow instead of reinventing the process each time.

## Git Conventions

- Keep commits focused and atomic.
- Use imperative commit messages.
- Do not commit secrets such as `.env`.
