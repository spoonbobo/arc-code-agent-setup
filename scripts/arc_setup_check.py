#!/usr/bin/env python3
"""Check ARC-AGI setup and configuration."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade, OperationMode


def main():
    dotenv.load_dotenv()

    print("ARC-AGI Setup Check")
    print("=" * 40)

    # Check API key
    api_key = os.getenv("ARC_API_KEY", "")
    if api_key:
        print(f"✓ ARC_API_KEY: {api_key[:10]}...{api_key[-4:]}")
    else:
        print("✗ ARC_API_KEY: Not set (using anonymous key)")

    # Check operation mode
    mode = os.getenv("ARC_OPERATION_MODE", "normal")
    print(f"  ARC_OPERATION_MODE: {mode}")

    # Check game ID override
    game_id = os.getenv("ARC_GAME_ID", "")
    if game_id:
        print(f"  ARC_GAME_ID: {game_id}")
    else:
        print(f"  ARC_GAME_ID: Not set (auto-discovers)")

    # Check cached games
    env_dir = ROOT / "environment_files"
    if env_dir.exists():
        games = [d.name for d in env_dir.iterdir() if d.is_dir()]
        print(f"\nCached games: {len(games)}")
        for game in games:
            print(f"  - {game}")
    else:
        print(f"\nCached games: 0")

    print("\n" + "=" * 40)
    print("Setup check complete")


if __name__ == "__main__":
    main()
