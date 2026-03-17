---
name: arcagi3-attempt-review
description: Use when a remote ARC-AGI-3 run has finished and you need to diagnose what happened from scorecards, reasoning logs, and replay evidence
---

# ARC-AGI-3 Attempt Review

## Overview

Use this skill to review a completed run and decide the next most informative change.

Core principle: do not explain a bad score with one vague story when the artifacts can separate runner failures from reasoning failures.

## When to Use

- After a weak or surprising remote run
- When comparing two attempts
- When deciding whether to change prompts, policy, or runner code
- When scorecards and replays exist but the failure mode is unclear

Do not use this skill before the run artifacts are available.

## Review Order

1. Confirm the run provenance: game, scorecard ID, tags, config, and major hypothesis.
2. Inspect scorecard outcomes and any structured logs.
3. Inspect replay-worthy reasoning and notable action sequences.
4. Classify the failure.
5. Recommend one next change with a clear expected signal.

## Failure Buckets

- `exploration failure` - the agent never learned the key mechanic
- `planning failure` - the agent learned pieces but did not sequence them well
- `execution failure` - the chosen actions were poor despite having enough information
- `runner failure` - resets, scorecards, action formatting, API handling, or orchestration were wrong

## What Evidence To Use

- scorecard fields and score deltas
- replay links or recorded trajectories
- reasoning metadata on important actions
- available-action changes over time
- whether actions were hypothesis-driven or blind

## Recommendation Rules

- Recommend the next most informative change, not the largest rewrite.
- Distinguish between "needs better game understanding" and "needs better implementation."
- Call out wasted actions explicitly.
- If the run lacked enough metadata to diagnose well, say so and fix observability first.

## Common Mistakes

- blaming the policy when the runner was broken
- using only final score instead of trajectory evidence
- not separating exploration waste from necessary exploration
- changing multiple variables before the next attempt
