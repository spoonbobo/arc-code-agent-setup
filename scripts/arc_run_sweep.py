#!/usr/bin/env python3
"""Run sweep of same game with different seeds."""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade, OperationMode
from arcengine import GameAction


def main():
    parser = argparse.ArgumentParser(description="Run ARC-AGI game sweep")
    parser.add_argument("--game-id", required=True, help="Game ID")
    parser.add_argument(
        "--mode", choices=["normal", "online", "offline"], default="normal"
    )
    parser.add_argument("--runs", type=int, default=5, help="Number of runs")
    parser.add_argument("--steps", type=int, default=10, help="Steps per run")
    args = parser.parse_args()

    dotenv.load_dotenv()

    mode_map = {"online": OperationMode.ONLINE, "offline": OperationMode.OFFLINE}
    arc = Arcade(operation_mode=mode_map.get(args.mode, OperationMode.NORMAL))

    print(
        f"Running sweep: {args.game_id} ({args.runs} runs, {args.steps} steps each)\n"
    )

    results = []

    for run_idx in range(args.runs):
        env = arc.make(args.game_id, seed=run_idx)
        if not env:
            print(f"Run {run_idx + 1}: Failed to create environment")
            results.append(None)
            continue

        actions = env.action_space
        if not actions:
            print(f"Run {run_idx + 1}: No actions available")
            results.append(None)
            continue

        obs = None
        for step in range(args.steps):
            obs = env.step(actions[0])

        results.append(obs.state.name if obs else "FAILED")
        print(f"Run {run_idx + 1} (seed={run_idx}): {results[-1]}")

    print(f"\nSweep complete: {sum(1 for r in results if r == 'WIN')}/{args.runs} wins")


if __name__ == "__main__":
    main()
