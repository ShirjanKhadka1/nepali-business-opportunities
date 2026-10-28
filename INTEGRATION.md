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
