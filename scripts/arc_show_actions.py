#!/usr/bin/env python3
"""Show detailed actions for a game."""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade, OperationMode


def main():
    parser = argparse.ArgumentParser(description="Show ARC-AGI game actions")
    parser.add_argument("--game-id", required=True, help="Game ID")
    parser.add_argument(
        "--mode", choices=["normal", "online", "offline"], default="normal"
    )
    args = parser.parse_args()

    dotenv.load_dotenv()

    mode_map = {"online": OperationMode.ONLINE, "offline": OperationMode.OFFLINE}
    arc = Arcade(operation_mode=mode_map.get(args.mode, OperationMode.NORMAL))

    env = arc.make(args.game_id)
    if not env:
        print(f"Failed to create environment for {args.game_id}")
        sys.exit(1)

    actions = env.action_space
    print(f"Available actions for {args.game_id}:\n")

    for action in actions:
        print(f"  {action.name}")
        print(
            f"    Complex: {'Yes (requires x,y coordinates)' if action.is_complex() else 'No'}"
        )
        print()

    del env


if __name__ == "__main__":
    main()
