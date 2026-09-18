# Research log — SPR crude barrels, September 2026 (Metaculus 15240 / subquestion 31307)

Shared research base with the December 2026 sibling
(`2026-09-07-mc15240-spr-crude-barrels-december-2026`). Both were built in the same
session from the same evidence; the December file carries the same log with the
Oct–Dec-specific material expanded.

## Question mechanics

- **Resolution source**: EIA monthly series **MCSSTUS1** — "U.S. Crude Oil Stocks in the
  Strategic Petroleum Reserve", thousand barrels, end of month. Resolves as the printed
  value × 1,000 (e.g. Sep-2022 = 416,393 → 416,393,000).
- **Release schedule**: MCSSTUS1 comes from the *Petroleum Supply Monthly*, roughly a
  two-month lag (Jun-2026 was already published on 2026-09-07). September 2026 will
  therefore not print until ~2026-11-30. Historically the admin resolved later still:
  Mar-2026 resolved on 2026-07-19, Sep-2025 on 2026-01-27.
- **Question group**: post 15240 has 13 subquestions; only 31307 (September 2026,
  closes 2026-09-30) and 31308 (December 2026, closes 2026-12-30) are open.
  The aggregation endpoint returns HTTP 400 for the *group post* without an explicit
  `question_id`; the bundled skill script does not expose that flag, so the cohorts were
  pulled with a scratch helper hitting
  `aggregation_explorer/?post_id=15240&question_id=<qid>&aggregation_methods=<m>`.
- **Edge cases**: (a) "If the EIA stops updating this tracker, the question will resolve
  as ambiguous" — the only ambiguity clause, and not live. (b) MCSSTUS1 is revisable;
  the resolver uses the value visible at resolution time. (c) The **weekly** series
  (WCSSTUS1) is *not* the resolution source, but is the best available proxy — see below.
- **Fine print**: empty. Comments (37 on the post) contain no resolution dispute; every
  past resolution was a straight read of the EIA table.

## Weekly → monthly bridge (the key mechanical step)

MCSSTUS1 is the stock at the last calendar day of the month. Linearly interpolating the
weekly WCSSTUS1 series to that date reproduces the published monthly values closely,
including during the fast 2026 drawdown:

| Month | Weekly before | Weekly after | Interpolated | Published MCSSTUS1 | Error (kb) |
|---|---|---|---|---|---|
| 2025-08 | 404,710 (8/29) | 405,224 (9/5) | 404,857 | 404,941 | +84 |
| 2026-04 | 397,924 (4/24) | 392,700 (5/1) | 393,447 | 394,524 | +1,077 |
| 2026-05 | 357,119 (5/29) | 349,192 (6/5) | 354,853 | 355,381 | +528 |
| 2026-06 | 325,655 (6/26) | 319,489 (7/3) | 322,133 | 322,186 | +53 |

Residual SD ≈ 0.6 Mb (million barrels) — small next to the policy uncertainty. Modelled
as N(0, 0.6).

## Live data pulled 2026-09-07

- **WCSSTUS1, week ending 2026-08-28 = 286,604 thousand barrels** (published 2026-09-02).
  Next WPSR: **Thursday 2026-09-10** (shifted from Wednesday by the 2026-09-07 federal
  holiday). Snapshot: `raw/eia-weekly-wcsstus1-2026-09-07.json`.
- **MCSSTUS1 through 2026-06 = 322,186**. Snapshot: `raw/eia-monthly-mcsstus1-2026-09-07.json`.
- **EIA STEO** (August-2026 vintage) series `COSQPUS`: end-Aug 284.803 Mb, then **flat at
  284.803 through June 2027**, with returns modelled only from July 2027 at 0.555 Mb/d
  (`COSQ_DRAW`). Snapshot: `raw/eia-steo-spr-outlook-2026-09-07.json`.
- **DOE SPR Quick Facts**: 294.1 Mb as of 2026-08-20 — ~4.4 Mb above the EIA weekly for
  the same week (289.726 at 8/21). DOE's own inventory count is not the resolution
  source; noted so a future update does not confuse the two.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Monthly Δ MCSSTUS1, full history | 584 | 1977-10 → 2026-06 | median +198 kb, IQR [−3, +2,370], p5 −6,267, p95 +6,498 | EIA | partly — unconditional, dominated by quiet regime |
| Monthly Δ MCSSTUS1, 2000+ | 317 | 2000-01 → 2026-06 | median 0, IQR [−5, +1,438], p5 −9,375 | EIA | yes, for the "programme over" branch |
| 3-month Δ MCSSTUS1, 2000+ | 315 | same | median 0, IQR [−2,498, +3,924], p10 −14,592, p90 +10,896 | EIA | yes, for December |
| Months with abs(Δ) > 3,000 kb ("active programme") | 169 (28.9%) | 1977–2026 | median +4,051, p5 −19,459, min −39,143 | EIA | yes, sets the left tail |
| Announced SPR programmes delivered in full | 3 | 2022, 2023-24 mandated sales, 2026 | 2022: 180/180 Mb delivered; 2023-24: 140 Mb of mandated sales **cancelled**; 2026: 133.5/172 Mb awarded so far | DOE, Argus, CRS | yes — announced ≠ delivered |

The dominant lesson from the last class: **an announced SPR volume is an intention, not a
schedule.** Roughly half the announced volume of the last decade never moved.

## Decomposition — the September number

The drawdown is a contracted-delivery process, not a free variable. Three estimators:

**A. Contract balance (weight 55%).** Volumes *awarded* under the 172 Mb exchange:

| Tranche | RFP | Offered (Mb) | Awarded (Mb) |
|---|---|---|---|
| 1 | 2026-03-10, three sites | 86 | 45.2 |
| 2 | 2026-04-01, Bryan Mound | 10 | 8.5 |
| 3 | 2026-04-09, West Hackberry | 30 | 26.0 |
| 4 | end-April, multisite | 92.5 | 53.3 |
| 5 | 2026-06-10, 40 Mb | 40 | **0.5** (Vitol only) |
| | | **258.5 offered** | **133.5 awarded** |

Drawn from the 415.442 Mb plateau (weeks 2026-02-13 → 2026-03-20) to 286.604 on
2026-08-28 = **128.838 Mb delivered**. Residual ≈ **4.7 Mb**, essentially all of which
should land in September. → ~282.0 Mb.

**B. Weekly-taper extrapolation (weight 20%).** Recent weekly draws: −6.115, −5.268,
−3.700, −3.122 Mb; decay ratios 0.87 / 0.70 / 0.84, mean ≈ 0.80. Continuing that decay
to 2026-09-30 implies −8.0 Mb → ~278.6 Mb. Note this estimator **exceeds the contract
balance**, so it is only right if the award tally is understated — which is why it gets
less weight than A.

**C. EIA STEO (weight 25%).** 284.8 Mb. But the August STEO was built on data through
2026-08-07 (298.694) and its "flat from end-August" path is a bookkeeping convention, not
a modelled schedule: it implies a 1.8 Mb draw in the final three days of August, faster
than the 3.1 Mb/week actually observed in the week ending 8/28, and then an instant stop.
Treated as a real but stale upper anchor.

Plus a 9% chance a re-offered final tranche starts lifting barrels inside September
(−1 to −7 Mb) and a 6% chance of a token refill delivery (+0.3 to +1.5 Mb).

Monte Carlo (500k draws) in `raw/scenario-model-2026-09-07.py`.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-07 | Metaculus aggregation_explorer, post 15240 | HTTP 400 without `question_id`; group posts need it | tooling note |
| 2026-09-07 | Metaculus cohorts, q31307 | CP 317.1 Mb (n=6 in window), Pro 403.9 (n=1), gold 379.1 (n=5) | all three impossible given published data — see below |
| 2026-09-07 | Metaculus comments (20 most recent) | pure resolution bookkeeping, no dispute | confirms clean resolution |
| 2026-09-07 | EIA API v2, WCSSTUS1 | 286,604 kb at 2026-08-28; drawdown decelerating | the anchor |
| 2026-09-07 | EIA API v2, MCSSTUS1 | monthly published through 2026-06 | bridge calibration |
| 2026-09-07 | EIA API v2, STEO COSQPUS/COSQ_DRAW | flat 284.8 Sep-26 → Jun-27; returns only from Jul-27 | upper anchor; also says EIA does not expect 2026 returns |
| 2026-09-07 | "SPR emergency release 2026 DOE drawdown" | 172 Mb US share of a 400 Mb IEA action, from 2026-03; Hormuz closed 2026-02-28 | regime identification |
| 2026-09-07 | DOE petroleum-reserves news listing | **nothing after 2026-07-09**; last SPR item is the 2026-06-10 RFP | strong evidence of absence for a new tranche |
| 2026-09-07 | "The Forty Million Barrels That Did Not Clear" (Substack) | June RFP: 40 Mb offered, 0.5 Mb awarded (1.25%); prior take-ups 53/85/87/58% | the single most load-bearing find |
| 2026-09-07 | DOE award releases (45.2 Mb, 8.5 Mb, 26 Mb, 53.3 Mb) | corroborates the award tally | contract balance ≈ 4.7 Mb |
| 2026-09-07 | Hydrocarbon Processing, Aug-2026 | "Trump plans a final 39 Mb release … would reduce inventory to ~243 Mb" | left tail for December |
| 2026-09-07 | Fortune 2026-08-25 (engineering limits) | upconing, salt creep, thermal shock; drawdown at 61% of design | caps the speed of any further release |
| 2026-09-07 | GAO-26-106918 | drawdown 2.7 of 4.415 Mb/d; **fill 0.44 of 0.785 Mb/d**; Big Hill offline for LE2 | caps December returns at ~26 Mb over two months |
| 2026-09-07 | CRS IN12542 | **no statutory minimum inventory level**; US is a net exporter so the IEP 90-day rule does not bind; 92.6–99.6 Mb of mandated sales remain through 2031 | corrects the "252.4 Mb hard floor" story |
| 2026-09-07 | "SPR mandated sale FY2026 FY2027" | 140 Mb of FY24–27 mandated sales cancelled; ~7 Mb still scheduled across FY26–27 | small December downside |
| 2026-09-07 | Oil price, early Sept 2026 | WTI ~$90.5–90.8 (9/2–9/3), Brent ~$95; Hormuz risk elevated, transit recovering | keeps a re-offer plausible but not compelling |
| 2026-09-07 | Kalshi trade API, KXSPRMIN / KXSPR / SPR | **no open SPR-level market** | no real-money anchor |
| 2026-09-07 | Manifold search "Strategic Petroleum Reserve" | see market table in `forecast.md` | thin play money, discounted |
| 2026-09-07 | Polymarket | only an expired "reserves fall to __ by June 5" event; nothing live on SPR level | no anchor |
| 2026-09-07 | Sentinel Team / Mantic / GJOpen / INFER | no matching SPR-level question found | none |

## Dead ends and ruled-out hypotheses

- **`curl`/WebFetch on `energy.gov/hgeo/opr/...` sometimes 403s** while `energy.gov/hgeo/articles/...`
  works. Not a data problem, just retry a sibling URL.
- **archive.is is blocked from this sandbox** ("unable to fetch"), so the CNBC paywall
  workaround in `AGENTS.md` §5 did not work here; CNBC pieces are cited by headline only.
- **Kalshi has no SPR-inventory series** despite a `kxsprmin` slug appearing in search
  results — the API returns an empty market list for it, open or closed.
- **The "252.4 Mb statutory floor" reported by Fortune and Hydrocarbon Processing is not an
  absolute floor.** It is the minimum below which EPCA §161(h) *limited* drawdown authority
  may not be used. The current programme runs on a severe-supply-interruption finding plus
  an IEP collective action, which carries no such limit — and DOE's own stated target of
  ~243 Mb is below 252.4. Do not treat 252.4 as a hard stop in the model.
- **DOE SPR Quick Facts inventory ≠ EIA WCSSTUS1** (294.1 vs 289.7 for the same week).
  Only the EIA series resolves this question.

## Open questions to chase next time

1. Has DOE re-offered the un-awarded ~38.5 Mb? Watch `energy.gov/hgeo/opr/listings/petroleum-reserves-news`.
2. Is the Big Hill LE2 life-extension build complete, and did return deliveries actually
   start on 2026-11-01? The 1 Nov date is from a secondary source (Plainview Energy), not
   from a DOE document — **verify before relying on it**.
3. Does the September-2026 STEO (due ~2026-09-09) move `COSQPUS` off 284.803?
4. Was any part of the ~7 Mb FY26–27 mandated sale executed, or deferred again?
5. Did the Venezuela heavy-for-light swap (floated by Sec. Wright on 2026-09-03) reach a
   signed contract, and with what delivery dates?

---

# v3 working log — 2026-09-18

## The two data problems v1 and v2 worked around are both solved

**1. Direct EIA downloads work from this container.** v1 used `api.eia.gov`; v2 fell back to
WebSearch corroboration across five news outlets because "direct EIA API/dnav fetch unavailable
this session". Plain `curl` on the dnav XLS endpoints succeeds, needs no API key, and returns the
full history:

```bash
curl -sSL -o WCSSTUS1w.xls https://www.eia.gov/dnav/pet/hist_xls/WCSSTUS1w.xls   # weekly SPR
curl -sSL -o MCSSTUS1m.xls https://www.eia.gov/dnav/pet/hist_xls/MCSSTUS1m.xls   # monthly SPR
curl -sSL -o sep26_base.xlsx https://www.eia.gov/outlooks/steo/archives/sep26_base.xlsx
```

Parse with `pandas.read_excel(..., sheet_name='Data 1', skiprows=2)` (needs `xlrd` for the old
`.xls`, `openpyxl` for the STEO `.xlsx`). This is strictly better than news corroboration: it
carries **revisions** (the 09-04 value is now 285,360, not the 285,400 v2 used) and the whole
history needed for calibration.

**2. The STEO table value that defeated v2 is in `archives/<mon><yy>_base.xlsx`.** Sheet `4atab`,
row keyed `COSQPUS`, columns mapped by sheet `Dates` row 10 (`202201`…`202712`).

## The bridge calibration — the most reusable thing in this version

Three versions have forecast a *monthly* series (MCSSTUS1, the resolution source) while reasoning
about a *weekly* one (WCSSTUS1), with the gap handled by an assumed SD of 0.6 Mb and no bias.
Regressing the monthly print against a linear interpolation of the weekly series at month end:

| Window | n | Mean residual (kb) | SD (kb) |
|---|---|---|---|
| Last 36 months | 36 | **+134** | **234** |
| Last 12 months | 12 | +242 | 338 |

The monthly sits slightly **above** the weekly interpolation, and it holds through the steepest
drawdown months of 2026: Apr +1,078, May +527, Jun +54. Using N(+180, 280) instead of N(0, 600)
raises the median ~0.2 Mb and removes about a third of the IQR width on its own. Saved to
`raw/eia-bridge-calibration-2026-09-18.json`. **This calibration is reusable for the December-2026
sibling question** (`2026-09-07-mc15240-spr-crude-barrels-december-2026`), which is still running
on the v1 assumption.

## The STEO disconfirms itself

September-2026 STEO, modelling completed **2026-09-03**:

| Month | STEO `COSQPUS` | Weekly-implied | Gap |
|---|---|---|---|
| 202607 (Jul, "historical") | 303.935 | 304.809 | −0.87 |
| 202608 (Aug, "historical") | 284.152 | ~286.07 | **−1.92** |
| 202609 (Sep, forecast) | 282.052 | — | — |

EIA flags July and August as historical, but the *Petroleum Supply Monthly* only publishes through
June, so those are EIA estimates — and both sit below a weekly series that has run *above* the
monthly print in every recent month. The STEO's SPR block is a contract-schedule projection, and
the contract schedule is what the last two weekly prints falsified. Weight cut to 12%, not zero,
because EIA sees delivery paperwork I do not.

## Metaculus

Re-fetch failed twice with **HTTP 403** — a genuine Cloudflare/rate-limit response, distinct from
the TLS-handshake failure (`status 0`) that blocked v2 and that `METACULUS_FORCE_TLS12=1` fixes.
The other three questions updated this session all fetched cleanly with that flag immediately
before, so this is question-group rate limiting, not the environment. Not a binding limitation
here: the cohorts sit 32–119 Mb above a level the SPR has already fallen below.

## Open questions to chase next time

1. The 2026-09-23 and 2026-09-30 WPSR prints. Two numbers, then the question is essentially
   settled ahead of the November resolution.
2. Any DOE or trade-press word on what happens to the unlifted 3.055 Mb residual balance —
   rescheduled, deferred, cancelled, or re-offered. Still not findable either way.
3. The October STEO (due ~2026-10-07), specifically whether `COSQPUS` for September converges to
   the weekly series or holds near 282.
4. The *Petroleum Supply Monthly* July and August actuals (~2026-10-31). These are the direct
   test of the bridge calibration, before it decides the December sibling question too.

## Metaculus: three refusals, and one correction to my own bookkeeping

Post 15240 returned **HTTP 403** on all three aggregation attempts on 2026-09-18, including one
after a four-minute backoff — while posts 40966, 41172 and 45230 all fetched cleanly with
`METACULUS_FORCE_TLS12=1` immediately before and after. So this is not the TLS problem and not a
general rate limit: it is specific to a 30-plus-subquestion group whose aggregation request is
large enough to draw a challenge on its own.

The `metaculus-scraper` fallback *did* render the page (33 forecasters, 37 comments) but a
question group carries no headline community prediction and the scraper cannot reach
per-subquestion aggregations — so it returned no number. It was still worth running: it
re-verified the resolution rule verbatim ("based on the EIA monthly data — MCSSTUS1 ... 416,393
thousand barrels ... would resolve as 416,393,000").

I first logged v3 with the 2026-09-07 cohort values in `meta.current.community` and in the ledger
line. That was wrong: an 11-day-old snapshot is not this version's community anchor, rule 4 says
fresh data only, and the repo's own `test_community_snapshot_is_not_older_than_the_forecast_it_annotates`
caught it. Both are now null, meaning **no community snapshot was taken for v3**, which is the
truth. The stale values stay in `forecast.md`, explicitly dated, where they can be read for what
they are. Note for future sessions: `log_forecast.py add` stamps `community.as_of` with today's
date whatever the numbers' real vintage, so passing `--cp/--pro/--gold` from a cached snapshot
silently mislabels it.
