#!/usr/bin/env python3
"""Create a custom ARC-AGI scorecard."""

import argparse
import os
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import dotenv
from arc_agi import Arcade


def main():
    parser = argparse.ArgumentParser(description="Create ARC-AGI scorecard")
    parser.add_argument("--tags", nargs="*", default=[], help="Tags for the scorecard")
    parser.add_argument("--source-url", default="", help="Source URL (e.g., git repo)")
    parser.add_argument("--opaque", default="", help="JSON string for opaque data")
    args = parser.parse_args()

    dotenv.load_dotenv()

    arc = Arcade()

    opaque_data = None
    if args.opaque:
        try:
            opaque_data = json.loads(args.opaque)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in --opaque: {args.opaque}")
            sys.exit(1)

    kwargs: dict[str, object] = {
        "tags": args.tags if args.tags else ["opencode-tool"],
    }
    if args.source_url:
        kwargs["source_url"] = args.source_url
    if opaque_data:
        kwargs["opaque"] = opaque_data

    scorecard_id = arc.create_scorecard(**kwargs)
    print(f"Created scorecard: {scorecard_id}")


if __name__ == "__main__":
    main()
