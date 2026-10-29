> **SUPERSEDED (Round 3) — do not use the numbers below as current.**
> The canonical programme map is
> [`finance-research-agents/ops/SYSTEM-MAP.md`](https://github.com/ShirjanKhadka1/finance-research-agents/blob/main/ops/SYSTEM-MAP.md),
> and current counts live in each repo's generated `status.json`
> (produced by `scripts/generate_status.py`, checked by `scripts/check_numbers.py`).
> This file is kept in place, unchanged except for this banner and for
> count claims replaced by pointers below, so its history is preserved.
> Any number still visible below is historical, not current.

# Integration — nepali-business-opportunities

## Role in the system
The opportunity layer for Nepal. It does not research companies or
markets — it ranks business ideas inside Nepal by scored evidence, so
the "best" answer is earned, not asserted.

## Connections
- Framework: `framework/scorecard.md` — 8 criteria, total /40, rankable
  only if evidence quality ≥ 3.
- Sectors: `sectors/` — 8 starting sectors, alphabetical, not ranked.
- Agents that can run it: investment-researcher (demand + advantage),
  financial-analyst (unit economics), world-market-researcher (global
  context: does this opportunity depend on a world theme?),
  reality-checker (evidence audit — the most important pass here).
- Sibling repos: nepali-capital-market-research (financing context),
  nepal-market-research (company examples, if any sector has one).
## How a candidate becomes "the best"
Score all 8 sectors → top 2 → 3 models each → score again with unit
economics → highest scorer with evidence attached = current best.
If better evidence arrives, the ranking changes — and the repo says so.
