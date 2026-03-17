#!/usr/bin/env python3
"""Play game with recording enabled."""

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
    parser = argparse.ArgumentParser(description="Play ARC-AGI game with recording")
    parser.add_argument("--game-id", required=True, help="Game ID")
    parser.add_argument(
        "--mode", choices=["normal", "online", "offline"], default="normal"
    )
    parser.add_argument("--steps", type=int, default=10, help="Number of steps")
    parser.add_argument(
        "--render", action="store_true", help="Enable terminal rendering"
    )
    args = parser.parse_args()

    dotenv.load_dotenv()

    mode_map = {"online": OperationMode.ONLINE, "offline": OperationMode.OFFLINE}
    arc = Arcade(operation_mode=mode_map.get(args.mode, OperationMode.NORMAL))

    render_mode = "terminal" if args.render else None

    env = arc.make(args.game_id, render_mode=render_mode, save_recording=True)
    if not env:
        print(f"Failed to create environment for {args.game_id}")
        sys.exit(1)

    print(f"Playing {args.game_id} with recording enabled...")

    actions = env.action_space
    if not actions:
        print("No actions available")
        sys.exit(1)

    for step in range(args.steps):
        action = actions[0]  # Use first available action
        obs = env.step(action)
        if obs:
            print(f"Step {step + 1}: {obs.state.name}")

    print(f"\nRecording saved to recordings/ directory")


if __name__ == "__main__":
    main()
