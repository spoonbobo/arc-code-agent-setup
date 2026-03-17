---
name: arcagi3-research-loop
description: Use when studying an ARC-AGI-3 game, planning the next remote attempt, or deciding how to learn the most from limited actions
---

# ARC-AGI-3 Research Loop

## Overview

Use this skill to turn vague curiosity about a game into a small, action-efficient experiment plan.

Core principle: every action should either advance the level or reduce uncertainty about the rules.

## When to Use

- Starting work on a new game
- Planning the next remote attempt
- Looking at a partially understood game and deciding what to test next
- Trying to avoid wasting actions on blind exploration

Do not use this skill for low-level code refactors that do not change research behavior.

## Loop

1. Restate the current game, known objective, and what remains uncertain.
2. Separate known mechanics from guessed mechanics.
3. Identify the single most valuable unknown.
4. Propose the smallest action sequence that could resolve that unknown.
5. Record what the attempt should teach, not just what it should do.
6. After the run, update the model of the game before planning another attempt.

## What To Inspect

- current `action_space`
- recent observations and state transitions
- scorecard and replay context
- reasoning attached to prior actions
- whether a failure was caused by misunderstanding or by poor execution

## Action-Efficiency Rules

- Prefer low-action probes over long uninformed sequences.
- Do not spam actions to "see what happens."
- Do not brute-force `ACTION6` with blind coordinate sweeps.
- If `ACTION7` is available, consider whether controlled undo-based exploration is cheaper than restart-heavy exploration.
- When taking a risky action, state what hypothesis it is testing.

## Good Output

A good result from this skill is a short experiment note with:

- current hypothesis
- evidence already observed
- next attempt plan
- expected learning from success or failure

## Common Mistakes

- confusing activity with progress
- mixing multiple hypotheses into one long attempt
- failing to record what was learned from a run
- ignoring changing `action_space`
- treating replay artifacts as optional
