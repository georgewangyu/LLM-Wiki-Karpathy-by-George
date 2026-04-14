#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = REPO_ROOT / "wiki" / "log.md"


def append_entry(date_text: str, topic: str, summary: str, sources: list[str]) -> None:
    lines = [
        "",
        f"## [{date_text}] {topic}",
        "",
        f"- Summary: {summary.strip()}",
    ]
    if sources:
        for src in sources:
            lines.append(f"- Source: `{src}`")
    text = LOG_PATH.read_text(encoding="utf-8")
    LOG_PATH.write_text(text.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Append a structured entry to wiki/log.md")
    parser.add_argument("--date", default=date.today().isoformat(), help="Entry date (YYYY-MM-DD)")
    parser.add_argument("--topic", required=True, help="Topic/title segment for the entry")
    parser.add_argument("--summary", required=True, help="Concise summary sentence")
    parser.add_argument("--source", action="append", default=[], help="Optional source reference (repeatable)")
    args = parser.parse_args()

    if not LOG_PATH.exists():
        raise FileNotFoundError(f"Missing log file: {LOG_PATH}")

    append_entry(args.date, args.topic, args.summary, args.source)
    print(f"Appended entry to {LOG_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
