#!/usr/bin/env python3
"""List available ARC-AGI games."""

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade, OperationMode


def get_operation_mode(mode_str: str) -> OperationMode:
    mode = mode_str.lower()
    if mode == "online":
        return OperationMode.ONLINE
    if mode == "offline":
        return OperationMode.OFFLINE
    return OperationMode.NORMAL


def main():
    parser = argparse.ArgumentParser(description="List available ARC-AGI games")
    parser.add_argument(
        "--mode", choices=["normal", "online", "offline"], default="normal"
    )
    args = parser.parse_args()

    dotenv.load_dotenv()

    arc = Arcade(operation_mode=get_operation_mode(args.mode))
    games = arc.get_environments()

    if not games:
        print(f"No games found in {args.mode.upper()} mode")
        return

    print(f"Found {len(games)} game(s) in {args.mode.upper()} mode:\n")
    for game in games:
        print(f"  {game.game_id}: {game.title}")


if __name__ == "__main__":
    main()
