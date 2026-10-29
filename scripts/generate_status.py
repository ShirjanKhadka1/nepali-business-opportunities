#!/usr/bin/env python3
"""Round 3 status generator for nepali-business-opportunities.

Counts real files, never a typed constant:
- sectors = sectors/*.md
- criteria = numbered criterion rows in framework/scorecard.md
  (total /40 = criteria x 5, checked, not assumed)
Writes status.json.
"""
import argparse
import json
import re
from datetime import date
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    root = Path(ap.parse_args().root)
    sectors = len(list((root / "sectors").glob("*.md")))
    scorecard = (root / "framework" / "scorecard.md").read_text(encoding="utf-8")
    criteria = len(re.findall(r"^\| \d+ \|", scorecard, flags=re.M))
    status = {
        "repo": "nepali-business-opportunities",
        "sectors": sectors,
        "criteria": criteria,
        "score_total": criteria * 5,
        "tests_passed": None,
        "tests_total": None,
        "tests_note": "No code tests (Markdown/framework repo)",
        "generated_by": "scripts/generate_status.py (Round 3: file counts from disk)",
        "generated_at": date.today().isoformat(),
        "method": "sectors/*.md counted from disk; criterion rows counted from "
                  "framework/scorecard.md; score total = criteria x 5",
    }
    (root / "status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
