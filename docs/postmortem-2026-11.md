# Post-mortem: first MiniBench round (resolved by 2026-11-01)

The first systematic look at what the bot's resolved tournament forecasts got right and wrong,
and what changed because of it. How to repeat it: [`postmortem.md`](postmortem.md).

**Bottom line.** Most of the loss came from two fixable things: (1) how a numeric distribution
is turned into the CDF Metaculus receives — model-independent, fixed in one script, and clearly
positive on replay; (2) a handful of reasoning errors that more searching did not catch —
miscounted reporting periods, an unevaluated fallback formula, an unchecked cut away from the
reference class, one fact counted several times. Binaries are fine, and a higher search floor
would not have helped.

## Data and sample

- 47 MiniBench questions resolved with an official spot peer score (ledger + `meta.yaml`,
  2026-11-01). Peer score ≈ 100 × (ln p_ours − mean ln p_other) at the outcome; for continuous
  questions p is the density of the submitted CDF, possibly with a scaling constant *c* (0.5–1;
  the Metaculus scoring FAQ returned 403, so *c* is unverified).
- **Failures**: the 6 worst, plus the 7th and 8th (Bitcoin, Inovio) because two of the six are
  the same event (NZ advance votes) — 8 questions, 7 independent events.
- **Controls**: 6 random positive-score questions, **type-matched** to the worst six (4 numeric,
  1 binary, 1 discrete), seed 20261101 — `uv run scripts/postmortem.py sample` reproduces them
  while the resolved set is unchanged. Type matching because type is the strongest confounder
  (table below). Controls exist so the failures are not over-learned from.
- One analyst subagent per question (the NZ pair shared one), brief in
  [`postmortem.md`](postmortem.md#analyst-brief); integration and the replay done by the main
  session. World facts below come from the analysts' web research (often WebFetch summaries);
  the integrator verified only the Japan horizon finding against the repo.

## Aggregate diagnostics

**Peer score by type**

| Type | n | Sum | Mean | Negative |
|---|---|---|---|---|
| binary | 20 | +210.0 | +10.5 | 4 |
| discrete | 11 | +163.7 | +14.9 | 2 |
| **numeric** | **15** | **−124.0** | **−8.3** | **7** |
| multiple choice | 1 | +4.0 | +4.0 | 0 |
| all | 47 | +253.7 | +5.4 | 13 |

**Research floor (≥ 15 searches, from 2026-10-19 ~18:00 UTC) did not fix numerics**: numeric mean
−4.7 before (n = 10) and −15.3 after (n = 5); binaries +4.8 (n = 8) and +14.3 (n = 12). Small
and confounded by question mix — but the NZ advance-vote count was missed identically with 4
searches and with 21.

**PIT** (probability integral transform: the percentile of the submitted CDF at which the
outcome landed), 26 numeric/discrete questions; calibrated ≈ 2.6 per decile:

```
0.0-0.1
0.1-0.2  ### 3
0.2-0.3  ### 3
0.3-0.4  ## 2
0.4-0.5  ### 3
0.5-0.6  #### 4
0.6-0.7  # 1
0.7-0.8  # 1
0.8-0.9  #### 4
0.9-1.0  ##### 5   <- wheat 0.997, NZ 0.992, NZ 0.98
```

- 13/26 inside the IQR (expected 13): the middle of the distributions is calibrated.
- 4/26 outside 5–95 % (expected 2.6), **all high**; 3 at ≥ 0.98 (expected ≈ 1): the outer tails
  are too thin.
- 9 above p75 vs 4 below p25: a weak upward bias (one-sided binomial p ≈ 0.13).
- **The question's own range is informative**: 26/26 outcomes inside `range_min..range_max`,
  20/26 in its middle half. That is why a uniform floor over the range is cheap insurance.

**Binaries**: no evidence of miscalibration. Rescaling all 20 in logit space by 1.3 would have
gained +0.28 nats in total — noise. The ≤ 6 % bucket (6 questions) all resolved NO.

## Replay of distribution rules

Every resolved submission rebuilt from its ledger percentiles; change in log score at the outcome
against what was submitted, in nats (× ~100 *c* peer points). All 26 submitted CDFs are reproduced
exactly by the legacy rules (a test asserts it), so the deltas are real. `postmortem.py replay`
prints this table; the last three rows came from a scratch script and are kept for the record.

| Rule | Total | Median | Worse on | Worst | Total without top 3 |
|---|---|---|---|---|---|
| legacy: linear interpolation, 2 % floor (submitted) | 0 | 0 | 0 | 0 | 0 |
| **PCHIP + 5 % floor (adopted)** | **+1.45** | **+0.028** | 8/26 | −0.13 | **+0.35** |
| PCHIP, 2 % floor | +0.57 | +0.010 | 6/26 | −0.17 | +0.03 |
| PCHIP, 10 % floor | +2.29 | +0.009 | 10/26 | −0.14 | +0.25 |
| linear, 5 % floor | +0.88 | −0.013 | 18/26 | −0.03 | −0.11 |
| linear, tails beyond the IQR stretched ×1.5 | +1.26 | 0.000 | 14/26 | −0.40 | −1.65 |
| linear, everything stretched ×1.5 | +1.74 | −0.049 | 15/26 | −0.40 | −2.27 |
| linear, 10 % mixture of a ×3-wide copy | +0.95 | −0.038 | 16/26 | −0.07 | — |

- **PCHIP** (piecewise cubic Hermite, monotone; Fritsch–Carlson slopes) instead of straight
  lines between knots: a linear CDF has a flat density inside each segment and a cliff at each
  knot. Four analysts flagged it independently (Bitcoin −0.30 nats at its outcome, BCRA,
  Florida dengue, Argentina). It helps even on typical questions (positive median).
- **5 % floor rather than 10 %**: 10 % has the larger total, but it is in-sample; 5 % keeps more
  of its gain without the three outliers (+0.35 vs +0.25) and has the better median.
  Break-even for a floor is roughly one extreme miss per ~35 questions; the round had 3 in 26.
- **Blanket widening is a bet on outliers only**: it loses heavily once they are removed, and its
  worst single cost is three times the floor's.

## Per question

Error codes: **RES** criteria misread · **SRC** stale or missing source data · **BASE** missing or
wrong base rate · **TAIL** tails too thin · **DIR** anchored on status quo / last value against the
trend · **MIX** interpretation hedge with too much weight on the unlikely reading · **EVID** found
evidence misweighted · **LUCK** reasonable ex ante, outcome in a tail. Δ = change in ln density at
the outcome for the better forecast, and its cost had the outcome landed at our median.

| Question | Peer | Role | Codes | Ex-ante : luck | Searches |
|---|---|---|---|---|---|
| [NZ advance votes, day 4 (mc46142)](https://www.metaculus.com/questions/46142/) | −64.0 | fail | EVID / TAIL | 60:40 | 4 |
| [US wheat net export sales (mc46141)](https://www.metaculus.com/questions/46141/) | −63.2 | fail | TAIL / BASE | 30:70 | 3 |
| [NZ advance votes, days 1–4 (mc46164)](https://www.metaculus.com/questions/46164/) | −36.1 | fail | EVID / TAIL | 65:35 | 21 |
| [OpenAI math repo > 300 (mc46149)](https://www.metaculus.com/questions/46149/) | −32.7 | fail | DIR / RES | 55:45 | 4 |
| [Japan school closures (mc46152)](https://www.metaculus.com/questions/46152/) | −30.4 | fail | RES / DIR, MIX | 80:20 | 31 |
| [Hormuz AIS ship count (mc46161)](https://www.metaculus.com/questions/46161/) | −26.7 | fail | EVID / DIR | 80:20 | 17 |
| [Bitcoin close (mc46176)](https://www.metaculus.com/questions/46176/) | −24.2 | fail | LUCK / interpolation | 35:65 | 16 |
| [Inovio FDA approval (mc46168)](https://www.metaculus.com/questions/46168/) | −19.7 | fail | LUCK / EVID | 35:65 | 33 |
| [OpenAI repo withdrawals (mc46131)](https://www.metaculus.com/questions/46131/) | +21.9 | control | — / minor EVID | 70:30 skill | 5 |
| [Argentina country risk (mc46139)](https://www.metaculus.com/questions/46139/) | +15.9 | control | TAIL / EVID | 35:65, lucky | 4 |
| [US GDP advance (mc46124)](https://www.metaculus.com/questions/46124/) | +14.0 | control | — / minor SRC | 60:40 skill | 6 |
| [Florida dengue cumulative (mc46133)](https://www.metaculus.com/questions/46133/) | +4.5 | control | middle too wide / SRC | 80:20 | 2 |
| [CoreWeave close (mc46127)](https://www.metaculus.com/questions/46127/) | +4.3 | control | LUCK / SRC | 30:70 | 3 |
| [BCRA USD/ARS (mc46154)](https://www.metaculus.com/questions/46154/) | +3.0 | control | LUCK / SRC | 40:60 | 26 |

### Failures

**NZ advance votes — day 4 (mc46142) and days 1–4 (mc46164).** Forecasts 93k [84k, 103k] and
310k [278k, 342k]; outcomes 143,200 (PIT 0.98) and 452,600 (PIT 0.992).
1. *Good*: the right reference class (2017/2020/2023 aligned by days before election day: days
   1–4 cumulative 227k / 412k / 339k; day 4 73k / ~102k / 104k), careful criteria, spotted the
   enrolment law change.
2. *Bad*: both cut 13–15 % off the 2023 table on the premise that live counts were ordinary votes
   only — a premise its own analysis of the law change undermined. Both down-weighted 2020 as a
   COVID outlier: mc46164's p95 (398k) sat below 2020's 412k in its own table. The 850 vs ~400
   voting places upside clue was dismissed. 21 searches changed nothing (forecast / 2023 table:
   0.91 vs 0.90 with 4); the disconfirmation search looked at the downside already covered.
3. *Better*: anchor on the table basis, mix 2020 and 2023: mc46164 p5 270k / p50 370k / p95 475k
   (Δ +1.96, −0.67 at the old median); mc46142 p50 107k / p95 153k (Δ +1.4, −0.7).

**US wheat net export sales (mc46141).** 335k [260k, 420k], p95 590k; outcome 849,800 (PIT 0.997).
1. *Good*: exact reading (first Wheat figure, 2026/27, MT); centring on the 4-week average was
   defensible — the next release was 240k.
2. *Bad*: P(> 800k) = 0.5 % although an 850,418 t week happened 49 weeks earlier (2 of 28
   non-holiday Jun–Dec weeks ≥ 800k); "late October typically 200–600k" from memory (rule 4);
   the resolution PDF was never read (`pdftotext` denied, before `pdf_text.py`); 3 searches.
3. *Better*: same centre, p95 700k, p99 940k: Δ +1.44, −0.21 at the median.

**OpenAI math repository > 300 (mc46149).** 20 %; resolved YES.
1. *Good*: read history.md, the commit log and the README itself; state right (300/719, one short).
2. *Bad*: never computed the fine-print fallback — README % × total = 0.42 × 719 = 302, so any new
   history entry without a numerator resolved YES; discounted twice for the same evidence
   ("launch clean-up", "quiet for 11 days"); applied "most things don't happen" to an active
   publishing pipeline.
3. *Better*: P(batch in 10 days) ≈ 0.4 × P(YES | batch) ≈ 0.9 → ≈ 0.38: about +30 instead of −33,
   −25 if NO.

**Japan school closures (mc46152).** Mixture 65 % cumulative / 35 % weekly reading, median 8,915;
outcome 7,190 (cumulative, report for 19–25 Oct; PIT 0.363, density 0.24× uniform).
1. *Good*: caught the question text calling weekly figures cumulative; read the primary PDFs; a
   Monte Carlo model.
2. *Bad*: `model.py` projected **three** weeks past week 41 when two separate it from 19–25 Oct —
   the question's "第44週" label is wrong, its dates right, and the bot's own cached report dates
   week 41 as R8.10.5–10.11 (verified by the integrator). That one count is ~85–90 % of the
   loss; dropping the hedge alone recovers 0.15 nats. Also: holiday-week drop under-weighted
   (week 42 fell 42 %), side mode at 35 % where the criteria supported 10–20 %.
3. *Better*: two weeks, 85/15 mixture: p25 6,760 / p50 7,680 / p75 8,750: Δ +2.5, ≈ 0 at 8,915.

**Hormuz AIS ship count (mc46161).** Median 1.8 [0.21, 5.5]; outcome 11 (PIT 0.886).
1. *Good*: went to hormuz.now's archive, JSON and methodology; noticed the 19 Oct pipeline
   rebuild; kept a right tail (11 at p90).
2. *Bad*: read a cold-start zero (log one day old, 7d/30d windows mechanically zero, 6–12 a day
   the week before, Kpler 7–10) as a regime change; cited a 2.2-hour-old day's zero (P(0) ≈ 0.48 at
   8/day); anchored on PortWatch, which the question says runs lower; used 11 % of the clock.
3. *Better*: 12–15 % on zero, the rest a negative binomial with mean ≈ 7.5 (median 6, p90 13):
   P(11) 4.5 % vs 2.1 %, Δ ≈ +0.75.

**Bitcoin close (mc46176).** 82,700 [80,100, 85,400]; outcome 77,200 (PIT 0.103).
1. *Good*: live Deribit DVOL (37 %), correct 00:00 UTC anchoring, Student-t(4) shape — its core
   matched 2,027 historical 10-day windows normalised by DVOL; consistent with the sister binary
   mc46170 (+11.0).
2. *Bad*: straight-line interpolation flattened the p5–p10 segment where the outcome fell
   (−0.30 nats against its own model); no allowance for realised vol beating implied at low DVOL;
   90 % of the clock unused.
3. *Better*: a smooth CDF with σ ≈ 45 %: Δ +0.44, −0.09 at the median.

**Inovio FDA approval (mc46168).** 46 %; accelerated approval on the PDUFA date (YES).
1. *Good*: right criteria; found the one real risk (accelerated-approval eligibility next to an
   approved competitor); explicit 60 % prior; below the field in a direction the stock price
   supported (it fell into the decision).
2. *Bad*: one FDA filing-letter fact counted three or four times (letter, 10-Q, prospectus, press);
   late-cycle silence read as negative though mid-cycle found "no new significant issues"; no
   precedent research. Base rate: first-cycle approval ≈ 79 % for novel drugs (PDUFA V
   assessment), the bot used an unsourced 70–75 %.
3. *Better*: 0.55 [0.43, 0.66]: +18 on YES, −18 on NO — a coin flip; the fix is counting once,
   not hindsight.

### Controls

- **OpenAI withdrawals (+21.9).** *Good*: literal fine print; the structural fact (OpenAI repairs
  rather than withdraws: 14 revisions vs 1 withdrawal). *Bad*: "the repository is quiet" was
  false (it updated on 26 Oct); activity conflated with withdrawal. *Better*: P(update) ≈ 0.5 ×
  P(withdrawal | update) ≈ 0.2 ≈ 10 % — same number, robust. The same wrong P(update) fed
  mc46149, where it decided the outcome; the two forecasts (20 % vs 12 %) were incoherent.
- **Argentina riesgo país (+15.9, lucky).** *Good*: fresh Rava data, volatility from the series,
  named Brazil's run-off. *Bad*: never fetched the run-off odds (Bolsonaro 77 % on Polymarket: a
  ~23 % one-sided shock); median below the last close; 4 searches. The outcome sat exactly at
  p95; closes two days earlier (753–765) would have cost 41–82 more points. *Better*: a run-off
  branch: p50 645, p95 760, +23 points on average over the window's daily closes.
- **US GDP (+14.0) — the process to copy.** Centred on a GDPNow + market blend (3.3) rather than
  raw GDPNow (3.6) or stale nowcasts; width from GDPNow's published error (MAE 0.77, RMSE 1.15);
  fat tails. *Bad*: error figures from memory and snippets. Little to improve.
- **Florida dengue (+4.5).** *Good*: framing (week 40 + two increments) and 5–10 % on "report late,
  week 41 resolves" — the report did come out on the deadline day. *Bad*: middle too wide (two-week
  sums had been 100/106/116); the PDF was never opened; a flat linear plateau 450–510.
- **CoreWeave (+4.3).** *Good*: random walk centred on the fetched Yahoo close (the question's price
  was wrong). *Bad*: no options-implied vol: the IQR implied ~124 % annualised vs ~95 % implied.
  *Better*: IV-sized lognormal, Δ +0.27.
- **BCRA A3500 (+3.0).** *Good*: width matched historical 9-day moves; the deliberate upside skew
  kept it positive. *Bad*: anchored on 16 Oct although logged 1h45m after the 19 Oct close
  (already above our median); the downloadable resolution series was not fetched; two-thirds of
  the miss was the same Brazil run-off, never searched. *Better*: fresh close + skew, Δ ≈ +0.5.

### What separates failures from controls

- **Not effort.** Both groups ran 2–33 searches; all sessions used 2–4 of their 25 minutes.
- Failures let **one judgement override the question's own data** (the NZ basis cut, the Hormuz
  zero, the OpenAI status quo) or **skipped the question's arithmetic** (Japan's periods, OpenAI's
  fallback). Controls anchored on the resolution source's own series and carried its volatility.
- Controls shared weaknesses that luck covered: missed scheduled events (Brazil hit two of them),
  stale anchors, no implied vol. Two survived only because their upper tails reached far enough.
- **Analysts disagreed once**: the CoreWeave analyst proposed forcing fat-tailed distributions to
  the normal's IQR at implied vol; the Bitcoin analyst's test on 2,027 historical windows shows
  the t(4) core matched history. The empirical test wins; that proposal was dropped.

## Suggestions, ranked by expected utility against risk

| # | Change | Evidence | Risk | Status |
|---|---|---|---|---|
| 1 | Monotone cubic (PCHIP) between knots, tails continuing the end slope (`submit_metaculus.py`) | replay +0.57 alone, positive median | very low | **done** |
| 2 | Uniform floor 2 % → 5 % (`UNIFORM_MIX`) | +1.45 with 1; +0.35 without top 3; worst −0.13 | low (in-sample level) | **done** |
| 3 | Question arithmetic in the digest: periods from dates, fallbacks evaluated, gap to threshold (skill Step 1, methodology §0) | Japan Δ +2.5; OpenAI −33 → ~+30 | ~0 | **done** |
| 4 | Disconfirmation names the assumption it `tests`; one tail scout per question (skill §3a/3b; enforced by `log_forecast.py`) | NZ ×2, Hormuz, OpenAI | low | **done** |
| 5 | Reference-class bracket: p5/p95 outside the listed reference values unless excluded with a reason (optional `reference` check) | NZ mc46164 | low–medium | open |
| 6 | Decompose "source shows X by D": P(update) × P(satisfies \| update), rate from the source's history; status-quo prior only for one-off events | OpenAI pair | low | open |
| 7 | Count each underlying event once: `adjustments` list with event/date/effect, repeats refused (skill Step 4; `log_forecast.py`) | Inovio, OpenAI double discount | low | **done** |
| 8 | `upcoming_events` required for price/level questions, with market odds, modelled as a branch mixture | Brazil run-off in 2 controls | low | open |
| 9 | Sibling questions visible at scaffold time (same resolution URL/domain) — derive first, then reconcile | OpenAI 20 % vs 12 % | medium (error propagation) | open |
| 10 | Price-question recipe: today's close if after the close; σ from ATM IV/DVOL; quantiles from implied-vol-normalised h-day returns; dense percentiles | CoreWeave, Bitcoin, BCRA, Argentina (~10/47 questions) | medium | open |
| 11 | Series-fetch helper (xls/csv/json → `raw/`), `base_rate` computed from the resolution series' history | wheat, BCRA, Hormuz | low–medium (CI allowlist) | open |
| 12 | Source-health rule (break after a pipeline change ⇒ probable artefact) and partial-period scaling | Hormuz only | low | open |
| 13 | Width from a nowcast's published error (IQR half-width ≈ 0.7–0.85 × MAE, p5–p95 ≈ 1.6–1.8 × RMSE) | GDP control | low | open |
| 14 | PIT + replay script in the daily sync (`scripts/postmortem.py`) | this document | low | **done** |
| 15 | Width warnings in `log_forecast.py` ((p95−p5)/IQR) — would have flagged none of the failures | — | low value | open |

**Do not**: raise the search floor (no evidence quantity helps); widen distributions across the
board (see the replay); retune binaries (+0.28 nats over 20 is noise); generalise
question-specific priors (labs repair rather than withdraw, FDA review stages, a 1.2× DVOL
uplift, Brazil).

**Known gap**: a discrete forecast logged as a `pmf` goes through `discrete_cdf`, which has its
own minimum step and does not get the 5 % floor. No round-1 question used a pmf.

## What to check next round

Out of sample, with `uv run scripts/postmortem.py report --since 2026-11-02`:
- PIT: still 4+ of ~26 outside 5–95 %, all on one side? Then the floor is not enough, or there is
  a real directional bias to address.
- Replay: does the adopted rule still beat legacy on the new questions (median ≥ 0)?
- Research logs: do the `tests` entries name the biggest adjustment, or something trivial? Are
  `adjustments` lists empty everywhere (box-ticking)?

## Caveats

In-sample replay on 26 questions; *c* unverified; world facts from analysts' web research,
mostly WebFetch summaries; peer scores depend on the other bots, whose forecasts are unseen, so
"better forecast" rows are about our own log score, not a guaranteed sign change.
