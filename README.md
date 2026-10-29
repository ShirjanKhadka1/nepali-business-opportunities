# 🇳🇵 Nepali Business Opportunities — scored, not asserted

**What this repo is, honestly:** a framework for finding the best business
opportunities *inside Nepal*, by scoring sectors on the same criteria,
with evidence gaps labelled — not a list that pretends "everything inside
Nepal" has already been analysed. No one has analysed everything. A repo
that claims it has is lying to you, and this repo will not do that.

**What it gives you instead:** a repeatable method, a sector shortlist
built from Nepal's known structural strengths, and a scoring worksheet
you (or anyone) can re-run with better data — so the "best" answer improves
as the evidence improves, instead of freezing on a guess.

> Research only, not investment advice. Starting a business or investing
> in one needs legal, tax, market, and financing advice specific to that
> venture. This repo does not replace any of that.

## The scoring framework (use it on every sector, every time)

Score each opportunity 1–5 on each criterion, with evidence cited for
every score. An opportunity with any criterion scored 1 on "evidence"
is not rankable yet — it is a research task, not a candidate.

| # | Criterion | What to evidence |
|---|---|---|
| 1 | Real demand, in Nepal | Who pays, how often, in NPR, from what source (not "huge market") |
| 2 | Nepal advantage | What does Nepal do better/cheaper/closer than the alternative? (labour, location, resource, language, diaspora, regulation) |
| 3 | Unit economics | Price, cost, margin, working capital — even rough, with sources |
| 4 | Barriers & moat | What stops the next entrant copying it in 6 months? |
| 5 | Capital & payback | Start-up capital, time to first revenue, time to payback |
| 6 | Regulation & risk | Licences, policy change risk, FX, power, logistics, political risk |
| 7 | Jobs & spillover | Does it build skills / suppliers / exports, or just extract? |
| 8 | Evidence quality | Primary data / filings / official stats = 5; news anecdote = 2; guess = 1 |

**Total out of 40. Rank only opportunities with evidence quality ≥ 3.**
Anything below that goes to the "research first" list, not the ranking.

## Sector shortlist — starting points, NOT a ranking

These sectors appear because Nepal has a structural reason to look at
them — a resource, a diaspora, a cost base, or an unmet local need.
Their order below is alphabetical, not ranked. Ranking them without
scored evidence would be exactly the dishonesty this repo refuses.

See `sectors/` for one file per sector, each with: why Nepal, who pays,
main barriers, what to verify first, and a blank scorecard.

- **Agriculture & food processing** — value addition to what Nepal already grows
- **Education & skills** — vocational, English, and professional training with employer linkage
- **Health & wellness services** — diagnostics, clinics, and care where access is the gap
- **Hydropower-linked services** — engineering, maintenance, local supply chains (not just generation)
- **IT & digital services for export** — software, design, data, support, in English, from Nepal
- **Local manufacturing & import substitution** — goods Nepal imports that it could make at competitive quality
- **Remittance-linked services** — savings, insurance, investment products for migrant families
- **Tourism, done properly** — trekking, culture, wellness, and the services around them (not just hotels)

## Evidence dossiers — 2026-10-29

Three sectors now have dated evidence dossiers in `evidence/`, each citing
only public sources actually opened and read on 2026-10-29, with gaps labelled
UNKNOWN. Their scores are sector-level indicative scores only: per
`framework/scorecard-use-note.md`, only a specific opportunity ("X service
for Y customer at Z price") can be ranked, so these totals must NOT be used
to reorder the alphabetical shortlist above, and no sector is described here
as "leading" or "top".

- **Hydropower-linked services** — dossier `evidence/2026-10-29-hydropower-linked-services.md` — scored 24/40, evidence quality 3 (Economic Survey 2082/83 figures and NEA export data via secondary reporting; no primary filing directly read).
- **Remittance-linked services** — dossier `evidence/2026-10-29-remittance-linked-services.md` — scored 25/40, evidence quality 3 (NRB statistics via Radio Nepal and a World Bank remittance series; no NRB primary PDF directly read). Note: the Fiscal Nepal page used for the licensed-company count headlines monetary totals 10x the NRB billion figures for the same period — this repo uses the NRB billion figures and does not quote those headlines.
- **Tourism, done properly** — dossier `evidence/2026-10-29-tourism-done-properly.md` — scored 24/40, evidence quality 3 (NTB 2024 arrival statistics and a World Bank feature; the World Bank jobs/GDP/spend figures are a dated 2019 baseline, not current figures).

No dossier yet for the other five shortlisted sectors — Agriculture & food
processing, Education & skills, Health & wellness services, IT & digital
services for export, and Local manufacturing & import substitution. They
remain unscored and unranked, not "researched and found wanting": their
evidence simply has not been compiled in this repo yet.

## How to find "the best one" — the honest procedure

1. Score all 8 sectors with the framework above, citing evidence per score.
2. Take the top 2 by total (evidence ≥ 3 only).
3. For each top sector, list 3 specific business models inside it (not
   "tourism" — "X service for Y customer at Z price").
4. Score those 6 models again, with unit economics this time.
5. The highest-scoring model, with its evidence attached, is your current
   best candidate — until better evidence changes the ranking. Say so, in
   those words, when you share it.

## What to verify before acting on any candidate

- [ ] Real customers interviewed (not just "people would buy this")
- [ ] Real prices and costs from suppliers, not from articles
- [ ] Licence / registration requirements, in writing, from the regulator
- [ ] Power, logistics, and payment realities for that exact location
- [ ] A competitor list with their prices — if you cannot name 3, you have
      not researched the market yet

## Quick start

1. Read the scoring framework in `README.md` above.
2. Pick one sector file in `sectors/` and read its "what to verify first"
   list before treating any part of it as evidence.
3. Score it on `framework/scorecard.md`, citing evidence for every score.

## Limitations

- The 8 sectors are starting points in alphabetical order, NOT a ranking.
  Ranking them without scored evidence would be exactly what this repo
  refuses to do.
- No sector has been fully analysed here, and no opportunity in this repo
  is a verified business case: real customers, prices, costs, and licence
  requirements must still be verified (see "What to verify" above).
- Scores are only as good as the evidence cited for them.

> Research only, not investment advice; never a buy/sell recommendation

See `CONTRIBUTING.md` for how to contribute and `SECURITY.md` for how to
report a security issue privately.

## License

MIT. If you re-run the scoring with better data, contribute your scorecard
back — that is how this repo gets more accurate over time.
