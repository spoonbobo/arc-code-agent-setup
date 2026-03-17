---
name: arcagi3-runner-design
description: Use when designing or restructuring this repo's ARC-AGI-3 remote attempt runner so experiments stay comparable, observable, and action-efficient
---

# ARC-AGI-3 Runner Design

## Overview

Use this skill when shaping code for the remote attempt runner.

Core principle: a strong runner makes experiments comparable, failures diagnosable, and scorecard/replay artifacts easy to preserve.

## When to Use

- Adding new runner features
- Splitting a script into modules
- Introducing experiment tracking or policy abstractions
- Designing how remote attempts are configured and reviewed

Do not use this skill for one-line bug fixes that do not affect runner structure.

## Design Priorities

1. Keep orchestration separate from decision policy.
2. Preserve run provenance: tags, metadata, scorecard IDs, and config snapshots.
3. Make scorecards and replay/debug artifacts first-class outputs.
4. Handle remote constraints explicitly: API key use, rate limits, failures, retries, and safe closure.
5. Keep experiment comparison easy by avoiding hidden state and ad-hoc configuration.

## Preferred Boundaries

- `config` - run settings, game selection, environment setup
- `runner/orchestration` - scorecard lifecycle, retries, resets, attempt loop
- `policy/solver` - chooses actions from observations
- `analysis/reporting` - structured summaries, artifacts, attempt review support

## Remote Constraints

- Online runs need `ARC_API_KEY`.
- Rate limits matter.
- Scorecards should be closed even when runs fail.
- Remote behavior should be observable enough to support replay-based debugging.

## Anti-Patterns

- one giant script that mixes config, policy, API calls, and analysis
- hidden experiment parameters
- missing scorecard IDs in outputs
- no reasoning capture for important actions
- runner logic that encourages blind action spam instead of careful experimentation
