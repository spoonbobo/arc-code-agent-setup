#!/usr/bin/env python3
"""
Quick play an ARC-AGI game.

Usage:
    python scripts/arc_play.py
    python scripts/arc_play.py --game-id ls20-cb3b57cc
    python scripts/arc_play.py --mode offline --steps 20
"""

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Quick play an ARC-AGI game")
    parser.add_argument("--game-id", help="Game ID (auto-discovers if not provided)")
    parser.add_argument(
        "--mode",
        choices=["normal", "online", "offline"],
        default="normal",
        help="Operation mode (default: normal)",
    )
    parser.add_argument(
        "--steps", type=int, default=10, help="Number of steps (default: 10)"
    )
    parser.add_argument(
        "--render", action="store_true", help="Enable terminal rendering"
    )
    args = parser.parse_args()

    # Build command
    cmd = ["python", "launch.py"]

    # Set environment variables
    env = os.environ.copy()
    env["ARC_OPERATION_MODE"] = args.mode
    if args.game_id:
        env["ARC_GAME_ID"] = args.game_id
    if args.render:
        env["ARC_RENDER_TERMINAL"] = "1"

    # Run launch.py
    try:
        result = subprocess.run(
            cmd,
            env=env,
            capture_output=True,
            text=True,
            check=True,
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running game: {e}", file=sys.stderr)
        print(e.stdout)
        print(e.stderr, file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(
            "Error: launch.py not found. Make sure you're in the project root.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
