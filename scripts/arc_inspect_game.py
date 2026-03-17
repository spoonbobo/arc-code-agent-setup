#!/usr/bin/env python3
"""Inspect a game without playing (show metadata and actions)."""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade


def main():
    parser = argparse.ArgumentParser(description="Inspect ARC-AGI game")
    parser.add_argument("--game-id", required=True, help="Game ID to inspect")
    parser.add_argument(
        "--mode", choices=["normal", "online", "offline"], default="normal"
    )
    args = parser.parse_args()

    dotenv.load_dotenv()

    from arc_agi import OperationMode

    mode_map = {"online": OperationMode.ONLINE, "offline": OperationMode.OFFLINE}
    arc = Arcade(operation_mode=mode_map.get(args.mode, OperationMode.NORMAL))

    # Create environment without rendering
    env = arc.make(args.game_id)
    if not env:
        print(f"Failed to create environment for {args.game_id}")
        sys.exit(1)

    info = env.info
    print(f"Game ID: {info.game_id}")
    print(f"Title: {info.title}")
    print(f"Tags: {', '.join(info.tags) if info.tags else 'None'}")

    actions = env.action_space
    print(f"\nAvailable Actions: {len(actions)}")
    for action in actions:
        complex_str = " (complex, needs x,y)" if action.is_complex() else ""
        print(f"  - {action.name}{complex_str}")

    # Cleanup
    del env


if __name__ == "__main__":
    main()
