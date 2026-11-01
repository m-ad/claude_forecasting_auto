# Post-mortem procedure — how to learn from resolved questions

A repeatable recipe for the analysis behind [`postmortem-2026-11.md`](postmortem-2026-11.md):
pick the worst resolved forecasts and matched controls, analyse each one in a subagent, integrate,
replay candidate distribution rules, rank changes by utility against risk. Run it from an
interactive session (`/postmortem`); nothing here runs in CI except the report in step 1.

When: after each tournament round, or once ~20 new questions have resolved since the last
post-mortem. Fewer than that and the outliers dominate.

## 1. Aggregate first (deterministic, seconds)

```bash
uv run scripts/postmortem.py report                      # scores by type, PIT, replay
uv run scripts/postmortem.py report --since 2026-11-02   # only what was forecast after the last change
uv run scripts/postmortem.py pit                         # PIT per question, sorted
uv run scripts/postmortem.py replay --detail             # per-question deltas per rule
```

The daily sync appends the same report to its run summary, so the trend is visible without
running anything. Read it before looking at single questions:

- **Peer score by type** — where the losses are. Round 1: numeric −8.3 mean vs binary +10.5.
- **PIT coverage** — calibrated is ~half inside the IQR and ~a tenth outside 5–95 %, spread evenly
  over both sides. Middle right but tails missed ⇒ shape problem (floor, interpolation); one side
  only ⇒ directional bias.
- **Replay** — the effect of every rule variant against what was submitted. `--since` the last
  rule change is the out-of-sample test of that change.

Also split by research regime when the process changed during the round (`ledger/usage.jsonl`
holds searches, scouts and duration per session).

## 2. Draw the sample

```bash
uv run scripts/postmortem.py sample --worst 6 --controls 6 --seed <YYYYMMDD of today>
```

- **Worst N** by official peer score. If two of them are the same underlying event (the NZ pair in
  round 1), give them one analyst and **pull in the next worst** until N events are covered.
- **Controls**: N random positive-score questions, **type-matched** to the worst set (the script
  does this). Their job is to stop you over-learning from outliers: a feature present in the
  controls too is not the cause of the failures.
- Note natural pairs (sister questions on one source, one scored well and one badly) and tell
  both analysts to contrast them.
- Record the seed and the slugs in the write-up.

## 3. One analyst per question, in parallel

Spawn one `general-purpose` subagent per question (per event for duplicates), **all in one
message**, in the background. Each gets the [analyst brief](#analyst-brief) plus a per-question
paragraph: the slug, role (failure/control), peer score, forecast (median, IQR, p5/p95 or p),
outcome and PIT (from `postmortem.py pit`), searches/scouts/duration, and 2–4 pointed extra
questions (e.g. "what was the historical distribution of this weekly series?", "compare with
the sister question X"). Do not hand them your hypothesis about the aggregate pattern — let them
find it.

Save each returned report to the scratchpad as it arrives; they are long.

## 4. Integrate (yourself — never delegate this)

- One table: question, peer, role, error codes, ex-ante : luck split.
- **Verify the one or two findings that carry the most weight** against repository files yourself
  (round 1: the Japan horizon error, from the cached report and `model.py`).
- **Resolve analyst disagreements empirically**, not by vote (round 1: implied-vol scaling, settled
  by a 2,027-window historical test).
- Contrast failures with controls: what do only the failures have?
- Look for shocks shared across questions (round 1: Brazil's run-off hit two Argentine questions).

## 5. Replay candidate rules before proposing them

Any proposal that changes how distributions are built is replayed on everything resolved:

- add the variant to `VARIANTS` in `scripts/postmortem.py` (or a keyword to
  `submit_metaculus.continuous_cdf`) and run `replay --detail`;
- accept only if the total gain survives dropping the three best questions, the median does not
  turn clearly negative, and the worst single-question cost is small;
- a test (`test_every_submitted_cdf_is_reproduced_by_a_known_rule_set`) guarantees the baseline is
  what was actually submitted. When the submitter's rules change, add the new rule set to
  `RULE_SETS`, keep the old one.

## 6. Write up and implement

- `docs/postmortem-<YYYY-MM>.md`: data and sample, aggregate diagnostics, replay table, the
  per-question table and answers, failures vs controls, a **ranked suggestion list with a status
  column**, a do-not list, what to check next round, caveats. Carry the open items from the
  previous post-mortem forward.
- Rank by expected utility against risk: deterministic script changes with replay evidence first,
  near-zero-risk skill text next, anything that can propagate errors (sibling reuse, new refusals)
  last.
- Implement red/green: a failing test that encodes the lesson, then the change. New refusals in
  `log_forecast.py` go under the research floor, so the deadline waiver still protects the forecast.

## Pitfalls

- **Hindsight**: a forecast can be good and lose. Every analyst splits ex-ante error from luck.
- **Outliers**: three questions carried most of round 1's replay gain; always report the total
  without the top three.
- **In-sample tuning**: choose rule parameters conservatively and judge them on the next round.
- **Correlated questions**: MiniBench writes clusters from one source on one day; count events, not
  questions.
- **The peer score's continuous scaling** *c* (0.5–1) was unverified in round 1; keep results in
  nats.
- **Web evidence** gathered by analysts is mostly WebFetch summaries — verify what a conclusion
  rests on.

## Analyst brief

Paste this, then the per-question paragraph.

```text
# Post-mortem brief

## Context
- Repo: <repo root> — an autonomous Metaculus bot in a bot tournament (MiniBench). Each question is
  forecast exactly once, unattended in CI, following .claude/skills/tournament-forecast/SKILL.md
  (read it: it is the process under review; also docs/postmortem-<last>.md if one exists).
- Scoring: Metaculus spot peer score — roughly 100 × (ln p_ours(outcome) − mean over other bots of
  ln p_other(outcome)); for numeric/discrete questions p is the density of the submitted CDF at the
  outcome (a scaling constant may apply; do not rely on it). Positive = better than the average
  bot. Other bots' forecasts are not available.
- Process changes during the round: <dates and what changed, e.g. research floor, CDF rules>.
- Today is <date>. The question(s) below have resolved.

## Files (read-only)
- questions/<slug>/meta.yaml, forecast.md, model.py (if present), raw/* (metaculus-question-*.json
  holds resolution_criteria, fine_print, description, scaling; research-log-*.json the searches).
- ledger/forecasts.jsonl — grep the slug: forecast record (median, IQR, percentiles, timestamp),
  submission record (submitted CDF), resolution record (outcome).
- ledger/usage.jsonl — grep the slug: duration, turns, web_searches, subagents.

## Task
1. Facts: exactly what resolves; our forecast; the outcome; where it fell in our distribution.
2. Reconstruct what happened in the world (targeted web research, ≤ ~15 searches/fetches): what
   drove the outcome, and when the decisive information became public relative to the forecast
   timestamp. Was the resolution consistent with the written criteria (the resolver is an LLM)?
3. Separate ex-ante error (knowable at forecast time within the session budget) from luck. Guard
   against hindsight bias: a good forecast can lose.
4. Answer: (1) What was good? (2) What was bad? (3) How could it have been better calibrated? —
   a concrete alternative (percentiles or probability) justifiable from information available at
   forecast time; whether it would have scored better, and what it would cost had the outcome
   landed near our original median.
5. Classify the error with the codes below (primary + secondary); give an ex-ante vs luck split.
6. Lesson: one or two process changes (skill text, a script check, a research category, a
   distribution rule) that would have caught this without hurting questions the bot got right.
   Say explicitly if the lesson is question-specific and should NOT be generalised.

Codes: RES misread criteria / resolver mismatch · SRC latest source value not fetched, stale or
snippet-only · BASE missing or wrong base rate · TAIL dispersion too narrow · DIR anchored on the
last value / status quo against the trend · MIX interpretation hedge putting mass where neither
reading lands · EVID found evidence misweighted · LUCK reasonable ex ante, outcome in a tail · OTHER

## Constraints
- Read-only: do not create, edit or delete any file in the repository; do not run git. Scratch
  work goes to <scratchpad>.
- Python: `uv run python -c "..."` from the repo root if you need to compute.
- Cite URLs for factual claims about what happened. Say when unsure. Never invent numbers.

## Return format (markdown, ≤ 700 words)
## <slug> — peer score X (failure | control)
- Facts table: type, forecast (median, IQR, p5, p95 or p), outcome, PIT, searches/scouts/duration,
  forecast time vs resolution date
- What happened (2–4 dated bullets with sources)
- 1) Good  2) Bad  3) Better calibration (concrete numbers)
- Error codes: primary / secondary; ex-ante vs luck split
- Lesson & proposed repo change (and whether it generalises)
Controls additionally: what did this forecast do right that a failure would not have, and was it
lucky (would the same process have lost under a plausible alternative outcome)?
```
