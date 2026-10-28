# Scorecard use note — how to score a sector honestly

> Research only, not investment advice. This note does not
> recommend starting, funding, or investing in any business.
> No market size, price, or cost is stated here, and none
> should be invented when using the scorecard — a figure
> without a source and a period is TO VERIFY, not a market.

## Why a separate note, not an edit to `scorecard.md`

`framework/scorecard.md` is the worksheet itself — "copy
this for every candidate". Editing it would change every
copy in circulation and blur the line between the blank
form and the instructions for using it. This note therefore
sits alongside it (and alongside
`framework/use-case-generation.md`), leaving the worksheet
exactly as it is. Read this note first; score second.

## The threshold, quoted from the framework (verified)

From `framework/scorecard.md`:

> Rank only if evidence quality ≥ 3.

And on the same worksheet:

> **Rankable?** Yes / No (No if evidence quality < 3)

The repo README states the same rule in words:

> **Total out of 40. Rank only opportunities with evidence
> quality ≥ 3.** Anything below that goes to the
> "research first" list, not the ranking.

That threshold is the whole honesty mechanism. It is not
a guideline to round up, and it is not averaged away:
evidence quality is criterion 8 of 8, scored 1–5 like the
others, and it gates the ranking on its own. A candidate
can total highly on demand, advantage, and unit economics
and still be unrankable if its evidence quality is below 3.

The evidence-quality scale, from the README:

- Primary data / filings / official stats = 5
- News anecdote = 2
- Guess = 1

Scores 3 and 4 are therefore the middle ground the scorer
must justify in the Evidence column: what source, dated
when, makes this better than anecdote but short of primary
data? If that sentence cannot be written, the score is not
a 3. A guess relabelled as a 3 is the exact dishonesty the
framework refuses.

## How to score, step by step

1. **Score an opportunity, not a sector.** The scorecard
   header says "Opportunity (specific, not a sector)".
   "Tourism" is not scorable; "X service for Y customer
   at Z price" is. Sector files are starting points for
   finding opportunities, not candidates themselves.
2. **One evidence citation per score.** Every row of the
   8-criterion table carries "source + date, or
   TO VERIFY" in its Evidence column. A score with a blank
   Evidence cell is an unscored row — leave it blank and
   say so, rather than filling it with a plausible number.
3. **Score evidence quality last, and honestly.** Read
   the other seven rows' Evidence cells first. If most of
   them rest on anecdote or guess, evidence quality is
   below 3, whatever the opportunity's promise sounds like.
4. **Apply the gate before reading the total.** If
   evidence quality < 3, stop: the candidate goes to the
   "research first" list, with its First verification step
   filled in (one concrete action, e.g. "interview 5
   customers in X"). Do not quote its total as a ranking,
   do not order it against scored candidates, and do not
   describe it as "leading" or "top".
5. **Only then compare totals.** Among rankable candidates
   (evidence quality ≥ 3), the total out of 40 may be
   compared — with the evidence attached, and with the
   standing caveat from the README's procedure: the
   highest scorer is the current best candidate "until
   better evidence changes the ranking. Say so, in those
   words, when you share it."
6. **Record what would change the score.** The worksheet's
   final row is not optional colour: name the evidence
   that would move the score up or down. A scorecard with
   no stated falsifier is a verdict, not research.

## Sectors stay alphabetical, not ranked

The sector files in `sectors/` are starting points, in
alphabetical order. This note does not rank them, and a
scorecard must not imply a ranking either: do not write
"the best sector", do not order a set of scorecards as if
the order were a verdict, and do not present the README's
sector list order as a ranking. Ranking happens only
through the scorecard, only for opportunities (not
sectors) with evidence quality ≥ 3, and only with the
evidence attached.

Two things that are NOT sector rankings, and must never be
copied into sector order:

- The order in which opportunities were investigated.
- The order in which proposals were generated (see below).

## How the Use-Case Generator links to the scorecard — without becoming a recommendation

The Use-Case Generator agent lives in the sibling repo
finance-research-agents (`agents/use-case-generator.md`,
runbook `runbooks/research-to-use-case.md`). Its job is
narrow, and the boundary matters:

**What it does.** It turns a completed research report into
a short list of research proposals — at most five per
report in the agent's own shape (evidenced problem, named
beneficiary, proposed study or build, data needed with
licence checked or marked UNKNOWN, feasibility verdict,
kill criterion, and a "What it is NOT" line). In this
repo's framework, the parallel cap is at most 3 proposals
per sector (`framework/use-case-generation.md`). The two
caps are different stages, not a contradiction: the agent
caps proposals per report; this repo caps proposals per
sector under consideration. Do not merge them into one
number.

**What it does not do.** It does not score, rank, or
recommend. A generated proposal is not a scorecard entry,
not a candidate, and not evidence of demand. Its internal
ordering — the agent ranks surviving use cases "by
evidenced problem size and data availability, and say[s]
so" — is a work-queue order for further research. It is
not a scorecard total, not a sector ranking, and must
never be presented as either.

**The gate between generator and scorecard.** A proposal
may be scored on `scorecard.md` only when it passes the
evidence gate in `framework/use-case-generation.md`:

- [ ] Its customer, payer, and price are named or
      explicitly TO VERIFY per line (no line left
      silently blank).
- [ ] Its kill criteria are written down before scoring.
- [ ] Its first verification step has been attempted, and
      the result recorded — including a negative result.
- [ ] No market size, price, or cost appears without a
      source and a period, or a TO VERIFY label.

Proposals that fail this gate stay in research. They are
not scored, not ranked, and not presented as candidates —
however promising they sound.

**A further input honesty rule.** The generator's own
inputs require a completed research report, with every
number sourced + period or labelled UNKNOWN; unsourced
research is sent back to the Reality Checker first, and
use cases are never generated from unsourced research.
An Inputs-only study (for example, the Bottlers Nepal
(Terai) study in nepal-market-research, which is Inputs
only and NOT a valuation) is therefore not a completed
report to generate from: its open questions are research
tasks, not findings to build proposals on, until the
study itself advances. If a proposal cites such a study,
it must carry the study's Inputs-only status with it —
not upgrade it by implication.

**Kill criteria travel with the proposal.** Every proposal
carries kill criteria agreed in advance (no payer found;
evidence quality stuck below 3; licence or regulatory
blocker in writing; unit economics failing on real
prices; no moat). If a criterion is met, the proposal is
killed or returned to research — it is not rescued by
enthusiasm, and a killed proposal is recorded as a result,
not hidden. A proposal that survives to scoring keeps its
kill criterion and its "What it is NOT" line attached to
its scorecard: the scorecard never outlives the proposal's
own limits.

**No recommendation, at either stage.** The generator
never recommends buying, selling, or holding any security,
never promises a return, and never presents a use case as
something that will be built, sold, or adopted. Scoring a
proposal does not change that: a high scorecard total is a
research finding ("this candidate currently scores
highest on the evidence attached"), not advice to start
or fund the business. Starting or investing in a business
needs legal, tax, market, and financing advice specific to
that venture; this repo does not replace any of that.

## Worked honesty checks (no new claims)

- A sector file says "Do not rank this sector until its
  scorecard is filled with cited evidence." That sentence
  is the rule, not a placeholder to delete once a draft
  exists. Delete it only when a cited, rankable scorecard
  exists — and then replace it with the scorecard's
  evidence, not with a ranking claim.
- A proposal whose only evidence is a news anecdote scores
  evidence quality 2. It is unrankable, however exciting.
  Its next step is its First verification step, not a
  total.
- A proposal ordered first by the generator because its
  problem is well evidenced is still unscored until it
  passes the gate above. Generation order ≠ score.
