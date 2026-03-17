#!/usr/bin/env python3
"""Download all available ARC-AGI games for offline use."""

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
    parser = argparse.ArgumentParser(description="Download all ARC-AGI games")
    parser.add_argument("--mode", choices=["normal", "online"], default="normal")
    args = parser.parse_args()

    dotenv.load_dotenv()

    print(f"Discovering games in {args.mode.upper()} mode...")
    arc = Arcade(operation_mode=get_operation_mode(args.mode))
    games = arc.get_environments()

    if not games:
        print("No games found")
        return

    print(f"Found {len(games)} game(s)\n")

    downloaded = 0
    failed = 0

    for game in games:
        print(f"Downloading {game.game_id}...", end=" ")
        try:
            env = arc.make(game.game_id)
            if env:
                print("✓")
                downloaded += 1
            else:
                print("✗")
                failed += 1
        except Exception as e:
            print(f"✗ ({e})")
            failed += 1

    print(f"\nDownloaded: {downloaded}, Failed: {failed}")


if __name__ == "__main__":
    main()
