from __future__ import annotations

import argparse
import json
from .pipeline import MockNeijingAtlasPipeline


def main() -> None:
    parser = argparse.ArgumentParser(prog="neijing-atlas")
    parser.add_argument("command", choices=["demo", "estimate"])
    parser.add_argument("--journal")
    args = parser.parse_args()

    pipe = MockNeijingAtlasPipeline()
    if args.command == "demo":
        journal = pipe.load_journal(args.journal)
        print(json.dumps(pipe.build_report(journal), ensure_ascii=False, indent=2))
    elif args.command == "estimate":
        print(json.dumps(pipe.estimate(), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
