# What will be the total spending by all Senate candidates in the 2026 US election cycle?

| | |
|---|---|
| **Source** | Metaculus #45220 — https://www.metaculus.com/questions/45220/what-will-be-the-total-spending-by-senate-candidates-in-2026-us-election-cycle/ |
| **Type** | numeric (USD; Metaculus range $1.0B–$3.0B, both bounds open) |
| **Opened / Closes / Resolves** | opens 2026-09-28 (upcoming at v1; criteria not yet published) / 2026-12-02 / 2026-12-02 (scheduled; Metaculus Cup Fall 2026 ends 2027-01-04) |
| **Status** | open |
| **Current forecast** | **Median $1.57B, IQR [$1.35B, $1.80B]** (v1, 2026-09-26) |
| **Community (as of 2026-09-26)** | hidden until `cp_reveal_time` 2026-10-01T17:00Z · 8 forecasters · no Pro or gold aggregation yet |
| **Next review** | 2026-10-01 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-09-26

![Forecast mixture by resolution timing](charts/distribution.png)

### What resolves YES

**The resolution criteria, fine print and background are not yet published.** The question
is in Metaculus's "upcoming" state and opens 2026-09-28T17:00Z; the API (queried with the
bot key on 2026-09-26) returns `resolution_criteria: null`, `fine_print: null`,
`description: null`, and there are no comments. What *is* fixed: unit `$`, range
$1.0B–$3.0B in 200 buckets of $10M with **open lower and upper bounds**, close **and**
scheduled resolution 2026-12-02T23:00Z, and membership in the Metaculus Cup Fall 2026,
which stops forecasting on 2027-01-01 and closes on 2027-01-04.

That last fact carries the most weight in this forecast. The question cannot wait for the
FEC's authoritative *24-month statistical summary*, which comes out in spring of the
following year. It must resolve on data visible in **December 2026**. Federal candidates
file a **pre-general report** (covering 2026-10-01 → 10-14, due 10-22) and a
**post-general report** (covering 10-15 → 11-23, due **2026-12-03**, one day *after* the
scheduled resolution). So the resolved number depends on when the resolver pulls the data:

- **On or before 2026-12-02:** the data stops at about 2026-10-14 (or 09-30 if the FEC's
  21-month summary is used). Historically that is only ~70–80% of final spending.
- **Any time 2026-12-03 → 2027-01-04:** the data runs through 2026-11-23, about 96–97% of
  final (Georgia runoff spending aside).

The second ambiguity is the **definition of "Senate candidates"**. The public series
differ by up to ~15%:

- the FEC statistical summary counts candidates *running in the cycle*, activity in the
  2-year window only;
- the FEC "by the numbers" page / API aggregate uses the *full 6-year Senate election
  period*;
- OpenSecrets;
- "every Senate candidate committee active in 2025–26", which includes senators up in 2028
  and 2030.

The title's "*all* Senate candidates" leans toward the broader readings. Counter-intuitive
paths to resolution: (a) the snapshot timing above; (b) a resolver that reads "spending in
Senate races" and adds outside money, which roughly triples the figure to $4B+; (c) a
2026-12-01 Georgia runoff, which adds spending the December data only partly captures.

### Outside view

Reference class: **Senate candidates running in the cycle, 24-month (2-year) disbursements,
last four cycles**. Recomputed from FEC bulk files, which reproduce the FEC's published
summaries to rounding:

| Cycle | Class | Receipts at 18 mo (Jun 30) | Disb. at 18 mo | Disb. at 21 mo (Sep 30) | **Final 2-yr disb.** | Final ÷ 18-mo receipts | Share of final spent by Sep 30 |
|---|---|---|---|---|---|---|---|
| 2018 | I, D-defence, D wave | $579.7M | $353.2M | $649.7M | **$1.018B** | 1.76 | 64% |
| 2020 | II, D-offence, GA runoffs | $702.6M | $413.7M | >$1.0B | **$1.962B** | 2.79 (≈2.36 ex-runoffs) | ~51% (~62% ex-runoffs) |
| 2022 | III, GA runoff | $943.1M | $710.6M | $1.1B | **$1.666B** | 1.77 | 66% |
| 2024 | I, pres. year, CA special | $857.5M | $681.9M | $1.1B | **$1.548B** | 1.81 | ~71% |
| **2026** | II, D-offence | **≈$860–881M** | **≈$644M** | (due Oct 15) | ? | — | — |

The raw base rate for the final 2-year figure is $1.0–2.0B, with a recent-cycle cluster
at **$1.55–1.67B**. The most stable predictor is final ÷ 18-month receipts, at 1.76–1.81
in three of four cycles. Applied to 2026's ≈$860M that gives **$1.51–1.56B**; the 2020
multiple (ex-runoffs 2.36) gives **$2.0B**.

Alternative definitions, 2024 finals:

- FEC API "by the numbers" full-period aggregate: **$1.698B** (×1.10).
- All Senate committees active in the 2-year window: **$1.749B** (×1.13).
- OpenSecrets: for 2022, Senate candidates *raised* $1.78B vs the FEC-class $1.65B
  (×~1.08).

### Inside view

Decomposition: `resolved value = F × m × f`

- **F** = final 2-year disbursements of 2026 Senate candidates, excluding any runoff
  - = 18-month receipts (≈$860M) × multiple.
  - Multiple: median **1.90**, σ(log) 0.11, plus a 15% chance of a 2020-style late surge
    (×1.1–1.3).
  - That sets it above the 1.78 norm, for three reasons:
    1. Democrats are on offence on a Class II map in TX, OH, NC, ME, IA, AK and NE (like
       2020).
    2. Individual Democrats are posting records: Talarico raised a record $27.1M in Q1 and
       $28.3M in Q2 (~$69M cycle), and Ossoff held ~$43M cash on hand on June 30.
    3. Mid-year cash on hand is high: $370M vs $305M (2024) and $383M (2022).
  - Against: Republican *candidates* are weak fundraisers this cycle and self-fund far
    less. Candidate loans are $50M so far vs $187M final in 2024, and 2024 had McCormick,
    Hovde, Sheehy and Scott. The GOP side is being carried by the Senate Leadership Fund,
    NRSC and MAGA Inc., which are outside money and don't count here.
  - → F median **$1.67B**, IQR [$1.54B, $1.82B].
- **m** = definition multiplier:

  | Definition | m | Weight |
  |---|---|---|
  | FEC 2-yr | 1.00 | 0.35 |
  | FEC full-period "by the numbers" | 1.08 | 0.35 |
  | OpenSecrets | 1.06 | 0.15 |
  | All Senate committees | 1.15 | 0.15 |

- **f** = timing share of final spending the resolver can see:

  | Resolver pulls data | f | Weight |
  |---|---|---|
  | On pre-general / Sep-30 data | N(0.75, 0.045) | 0.40 |
  | On post-general data | N(0.965, 0.015) | 0.52 |
  | Misreads to include outside money (≈$4.5B) | — | 0.03 |
  | Other / diffuse (×lognormal σ 0.25) | — | 0.05 |

  - Georgia runoff: Ossoff leads Collins 51–41 (YouGov, Sep 15–18) and 49–45 (Quantus).
    I give it a 15% chance, adding ≤$60M under the post-general branch.

The 0.40 weight on an early snapshot comes from `scheduled_resolve_time = close time =
2026-12-02`, one day before post-general reports are due. It is tempered because many
authors set resolve = close by default, and admins often resolve days later on the freshest
data.

### Evidence

- **2026 is not running ahead of 2022/2024 on candidate money at mid-year.**
  - 18-month disbursements: ≈$644M vs $682M (2024) and $711M (2022).
  - 18-month receipts: ≈$870M vs $858M (2024) and $943M (2022).
  - At 15 months, receipts were $654M vs $611M (2024), disbursements $401M vs $426M.
  - In real terms the 2026 18-month receipts equal 2020's.
  - LR ≈ 1 against "record candidate spending". This is the main anchor.
- **AdImpact (2026-06-11):** Senate ad spending of all sponsors is projected at $3.4B,
  +27% vs 2024 and +48% vs 2022.
  - It is a projection, and most of it is outside money. **Wesleyan Media Project
    (2026-09-17):** Senate ad spending so far is $426M candidate, $945M group, $58M
    coordinated; groups have 69%. Senate broadcast volume is "not record-breaking… higher
    than every cycle but for 2020".
  - Read-through to *candidate* spending: modestly positive. LR ~1.3 for the upper half of
    F, already reflected in the 1.90 multiple.
- **Race-level signals:**
  - NC is projected at $600–800M in total (Carolina Public Press), but that is all
    sponsors.
  - Ohio saw $97M of ads from 08-10 to 09-13; TX $59M, ME $51M, MI $48M, GA $44M.
  - Democrats outraised Republicans ~4:1 in battleground Q2.
- **Absent evidence:** I found no report of an aggregate Senate-candidate Q3 surge (Q3 ends
  09-30; reports are due 10-15). No such signal yet.
- **Disconfirming stream, checked:** Republican candidates' weak hauls and low
  self-funding pull F down relative to 2024. Paxton raised $2.2M in Q2 and Collins held
  $2.1M cash on hand. That is why I don't take AdImpact's +27% at face value.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | hidden (n=8) | 2026-09-26 | reveals 2026-10-01T17:00Z |
| Metaculus Pro | not available | 2026-09-26 | no Pro aggregation on upcoming question |
| Metaculus gold medalists | not available | 2026-09-26 | — |
| Kalshi / Polymarket | no market | 2026-09-26 | they list race-winner and control markets only |
| Manifold | "TX Senate race most expensive in history" 18% | 2026-09-26 | M$323 volume, tangential, discounted |
| Sentinel / Mantic / GJOpen / INFER | no matching question | 2026-09-26 | — |
| Question design | range $1.0–3.0B, centre $2.0B | — | the author's range centre is above my median |

There is nothing to reconcile yet: no cohort numbers exist. The range centre of $2.0B
matches 2020's final figure. If the CP comes in at ~$2B, I should check whether forecasters
assume 2020-style growth, outside money, or a 6-year definition. None of those follows from
the mid-year FEC data.

### Scenarios

| # | Scenario | Weight | Implies (median) |
|---|---|---|---|
| 1 | Resolved on data through ~Oct 14 (or the FEC 21-month summary) | 0.40 | ≈$1.32B |
| 2 | Resolved on post-general data (through Nov 23), normal late cycle | 0.44 | ≈$1.68B |
| 3 | Post-general data + 2020-style Democratic surge | 0.08 | ≈$2.0B |
| 4 | Resolver counts outside money / "Senate race spending" | 0.03 | ≈$4.5B (above range) |
| 5 | Other definitions / diffuse | 0.05 | ≈$1.7B, wide |

Monte Carlo mixture (400k draws): 5th $1.12B · 10th $1.19B · **25th $1.35B · 50th
$1.57B · 75th $1.80B** · 90th $2.05B · 95th $2.33B. P(<$1.0B) ≈ 1%; P(>$3.0B) ≈ 3%.
The distribution is bimodal, driven by timing (chart above).

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Timing mix 40/52 | criteria confirm post-general data are used | Median $1.72B, IQR [$1.56B, $1.91B] |
| Timing mix 40/52 | criteria fix a snapshot on/before 2026-12-02 | Median $1.34B, IQR [$1.21B, $1.51B] |
| Multiple 1.90, 15% surge | 2020-style surge certain | Median $1.84B, IQR [$1.58B, $2.10B] |
| Multiple 1.90, 15% surge | multiple = 2018/22/24 average 1.78, no surge | Median $1.44B, IQR [$1.24B, $1.63B] |
| Definition mix | FEC 2-year statistical-summary class only | Median $1.49B, IQR [$1.28B, $1.69B] |

### What would change my mind (tripwires)

- [ ] Criteria published 2026-09-28 name a source/date that includes post-general reports
  (resolution on/after 2026-12-03, or "final/complete" data) → **up ~$150M** (to ≈$1.72B)
- [ ] Criteria published 2026-09-28 fix a snapshot on/before 2026-12-02, or name pre-general
  / 21-month data → **down ~$230M** (to ≈$1.34B)
- [ ] Criteria define the quantity as outside + candidate spending ("spending in Senate
  races") → **either, re-analyse from scratch** (new level ≈ $4B+)
- [ ] Q3 filings (due 2026-10-15): cycle receipts of 2026 Senate candidates through 09-30
  above $1.30B (Q3 > ~$430M; 2024's Q3 ≈ $340M) → **up ~$100M**; below $1.15B → **down
  ~$80M**
- [ ] Cycle-to-date disbursements of 2026 Senate candidates through 09-30 (FEC 21-month
  summary or bulk file) above $1.20B → **up ~$80M**; below $1.00B → **down ~$80M**
- [ ] Georgia 2026-11-03 result forces a 2026-12-01 runoff → **up ~$20M** (only partly
  inside the December data)

### Sources

1. Metaculus API, post 45220 / question 45413 (metadata, scaling, dates; criteria null) — https://www.metaculus.com/api/posts/45220/ (accessed 2026-09-26); snapshot `raw/metaculus-2026-09-26.json`
2. FEC, Statistical Summary of 24-Month Campaign Activity of the 2023-2024 Election Cycle — https://www.fec.gov/updates/statistical-summary-of-24-month-campaign-activity-of-the-2023-2024-election-cycle/ (accessed 2026-09-26)
3. FEC, 24-Month Summary 2021-2022 — https://www.fec.gov/updates/statistical-summary-of-24-month-campaign-activity-of-the-2021-2022-election-cycle/ (accessed 2026-09-26)
4. FEC, 24-Month Summary 2019-2020 — https://www.fec.gov/updates/statistical-summary-24-month-campaign-activity-2019-2020-election-cycle/ (accessed 2026-09-26)
5. FEC, 18-Month Summary 2023-2024 (incl. 2018–2024 comparison table) — https://www.fec.gov/updates/statistical-summary-of-18-month-campaign-activity-of-the-2023-2024-election-cycle/ (accessed 2026-09-26)
6. FEC, 18-Month Summary 2021-2022 — https://www.fec.gov/updates/statistical-summary-of-18-month-campaign-activity-of-the-2021-2022-election-cycle/ (accessed 2026-09-26)
7. FEC, 18-Month Summary 2019-2020 — https://www.fec.gov/updates/statistical-summary-18-month-campaign-activity-2019-2020-election-cycle/ (accessed 2026-09-26)
8. FEC, 18-Month Summary 2017-2018 — https://www.fec.gov/updates/statistical-summary-18-month-campaign-activity-2017-2018-election-cycle/ (accessed 2026-09-26)
9. FEC, 21-Month Summaries 2017-18, 2019-20, 2021-22, 2023-24 — https://www.fec.gov/updates/statistical-summary-21-month-campaign-activity-2017-2018-election-cycle/ · https://www.fec.gov/updates/statistical-summary-21-month-campaign-activity-2019-2020-election-cycle/ · https://www.fec.gov/updates/statistical-summary-of-21-month-campaign-activity-of-the-2021-2022-election-cycle/ · https://www.fec.gov/updates/statistical-summary-of-21-month-campaign-activity-of-the-2023-2024-election-cycle/ (accessed 2026-09-26)
10. FEC, 15-Month Summaries 2025-26 and 2023-24 — https://www.fec.gov/updates/statistical-summary-of-15-month-campaign-activity-of-the-2025-2026-election-cycle/ · https://www.fec.gov/updates/statistical-summary-of-15-month-campaign-activity-of-the-2023-2024-election-cycle/ (accessed 2026-09-26)
11. FEC bulk data, "All candidates" (weball) and candidate master (cn) files, 2018–2026 — https://www.fec.gov/files/bulk-downloads/2026/weball26.zip etc. (accessed 2026-09-26); derived snapshot `raw/fec-bulk-senate-totals-2026-09-26.csv`
12. FEC API `candidates/totals/aggregates` (office=S) — https://api.open.fec.gov/v1/candidates/totals/aggregates/ (accessed 2026-09-26; 2024 snapshot in `raw/`)
13. AdImpact, "2026 Election Cycle to Reach Record $11.6 Billion in Ad Spending" (2026-06-11) — https://adimpact.com/blogs/adimpact-reveals-2026-election-cycle-to-reach-record-11.6-billion-in-ad-spending (accessed 2026-09-26)
14. Wesleyan Media Project, release 2026-09-17 — https://mediaproject.wesleyan.edu/releases-091726/ (accessed 2026-09-26)
15. Wesleyan Media Project, release 2026-03-05 — https://mediaproject.wesleyan.edu/releases-030526 (accessed 2026-09-26)
16. WSHU, "2026 midterm elections on track for record political ad spending" (2026-09-21) — https://www.wshu.org/connecticut-news/2026-09-21/2026-midterm-elections-political-ad-spending (accessed 2026-09-26)
17. Carolina Public Press, NC Senate race expected to be most expensive ever — https://carolinapublicpress.org/73700/get-ready-for-most-expensive-senate-race-ever/ (accessed 2026-09-26)
18. Roll Call, "Democratic candidates start 2026 with a fundraising bang" (2026-04-16) — https://rollcall.com/2026/04/16/democratic-candidates-start-2026-with-a-fundraising-bang/ (accessed 2026-09-26)
19. Roll Call, "Democratic candidates sustain fundraising pace as GOP strains to keep up" (2026-07-16) — https://rollcall.com/2026/07/16/democratic-candidates-sustain-fundraising-pace-as-gop-strains-to-keep-up/ (accessed 2026-09-26)
20. ABC News, "Democrats dominate fundraising in key Senate races, but Republicans still have ample resources" — https://abcnews.com/Politics/democrats-dominate-fundraising-key-senate-races-republicans-ample/story?id=134829415 (accessed 2026-09-26)
21. Houston Public Media, Talarico record $27M Q1 (2026-04-15) — https://www.houstonpublicmedia.org/articles/news/politics/election-2026/2026/04/15/549140/james-talarico-texas-senate-democrat-fundraising-27-million/ (accessed 2026-09-26)
22. Atlanta News First, YouGov poll Ossoff 51–41 (2026-09-23) — https://www.atlantanewsfirst.com/2026/09/23/new-poll-ossoff-holds-double-digit-lead-over-collins-governors-race-dead-heat/ ; Quantus 49–45 (2026-09-18) — https://www.atlantanewsfirst.com/2026/09/18/poll-ossoff-holds-4-point-lead-over-collins-tight-georgia-senate-race/ (accessed 2026-09-26)
23. Statista (OpenSecrets data), total funds raised by Senate candidates 2021/22 — https://www.statista.com/statistics/1317762/total-funds-raised-running-senate-election-cycle-party (accessed 2026-09-26, via search snippet)
24. CNN, "The 'first prediction-market election'…" (2026-09-24) — https://www.cnn.com/2026/09/24/politics/midterm-elections-prediction-markets-kalshi-polymarket (accessed 2026-09-26)
25. Manifold, "Will the 2026 Texas Senate race be the most expensive Senate race in history" — https://manifold.markets/AutopoieticErgodicity/will-the-2026-texas-senate-race-be (accessed 2026-09-26)

**Date**: 2026-09-26
**Forecast**: Median $1.57B, IQR [$1.35B, $1.80B]
**Thesis**: FEC data show 2026 Senate candidates at mid-year roughly level with 2022/2024 (≈$870M raised, ≈$644M spent by June 30). Historical final-to-midyear multiples, nudged up for a Democratic-offence Class II map, put final 2-year spending near $1.67B (Wesleyan and AdImpact show the ad boom is mostly outside money). The median is pulled lower by a 40% chance that the question, which must resolve before the Cup ends on 2027-01-04, is decided on pre-general data that captures only ~75% of spending; the still-unpublished resolution criteria are the dominant uncertainty.
