#!/usr/bin/env python3
"""Close an ARC-AGI scorecard and get final results."""

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
    parser = argparse.ArgumentParser(description="Close ARC-AGI scorecard")
    parser.add_argument(
        "--scorecard-id", default="", help="Scorecard ID (default: current)"
    )
    parser.add_argument("--json", action="store_true", help="Output full JSON")
    args = parser.parse_args()

    dotenv.load_dotenv()

    arc = Arcade()
    scorecard = arc.close_scorecard(
        scorecard_id=args.scorecard_id if args.scorecard_id else None
    )

    if not scorecard:
        print("No scorecard found or already closed")
        sys.exit(1)

    if args.json:
        print(scorecard.model_dump_json(indent=2))
    else:
        print(f"Final Score: {scorecard.score}")
        scorecard_id = getattr(scorecard, "scorecard_id", "N/A")
        print(f"Scorecard ID: {scorecard_id}")


if __name__ == "__main__":
    main()
