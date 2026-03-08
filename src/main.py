from __future__ import annotations

import argparse
import json
from pathlib import Path

from .bot.workflow import DailyWorkflow


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.example.json")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    args = parse_args()
    config = load_config(args.config)
    if args.dry_run:
        config["dry_run"] = True

    artifacts = Path(config.get("artifacts_dir", "artifacts"))
    artifacts.mkdir(parents=True, exist_ok=True)

    workflow = DailyWorkflow(config=config)
    workflow.run()


if __name__ == "__main__":
    main()
