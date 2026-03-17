#!/usr/bin/env python3
"""Download a specific ARC-AGI game for offline use."""

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
    parser = argparse.ArgumentParser(description="Download ARC-AGI game")
    parser.add_argument(
        "--game-id", required=True, help="Game ID (e.g., ls20-cb3b57cc)"
    )
    parser.add_argument("--mode", choices=["normal", "online"], default="normal")
    args = parser.parse_args()

    dotenv.load_dotenv()

    print(f"Downloading {args.game_id}...")
    arc = Arcade(operation_mode=get_operation_mode(args.mode))

    try:
        env = arc.make(args.game_id)
        if env:
            print(f"✓ Successfully downloaded {args.game_id}")
        else:
            print(f"✗ Failed to download {args.game_id}")
            sys.exit(1)
    except Exception as e:
        print(f"✗ Error downloading {args.game_id}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
