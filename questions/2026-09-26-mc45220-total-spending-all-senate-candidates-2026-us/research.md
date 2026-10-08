# Research log — What will be the total spending by all Senate candidates in the 2026 US election cycle?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: **UNKNOWN at v1.** On 2026-09-26 the question was "upcoming" and opens
  2026-09-28T17:00Z. The API returned null for criteria, fine print and background. Unit
  `$`, range 1e9–3e9 (open bounds), 200 buckets.
- Release schedule / cutoff:
  - close = scheduled resolve = 2026-12-02T23:00Z; the Cup ends 2027-01-04.
  - FEC report calendar for the 2026 general:
    - Q3 report through 09-30, due 10-15.
    - Pre-general report 10-01→10-14, due 10-22.
    - Post-general report 10-15→11-23, due **12-03**.
    - Year-end report due 2027-01-31.
  - The FEC 21-month summary (through 09-30) is usually published Nov–Dec. The 24-month
    summary is published spring 2027, too late for the Cup.
- Edge cases and ambiguities:
  1. Snapshot timing: pre- vs post-general data, worth ≈ ×0.75 vs ×0.965 of final.
  2. Definition: FEC 2-yr "running in 2026" vs full 6-yr election period vs OpenSecrets vs
     all Senate committees active in 2025-26 (×1.00 / ×1.08–1.10 / ×~1.06–1.08 / ×1.13–1.15).
  3. Outside money misread (×~3).
  4. Georgia runoff 2026-12-01.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Final 2-yr disb., Senate candidates running in cycle | 4 | 2018–2024 | $1.02B / $1.96B / $1.67B / $1.55B | FEC 24-mo summaries + bulk weball/cn recomputation | yes (level anchor) |
| Final disb. ÷ 18-mo receipts | 4 | 2018–2024 | 1.76 / 2.79 (2.36 ex-GA-runoffs) / 1.77 / 1.81 | FEC 18-mo summaries, bulk | yes (main projector) |
| Final disb. ÷ 18-mo disb. | 4 | 2018–2024 | 2.88 / 4.74 / 2.34 / 2.27 | same | secondary (noisier: early-spending timing varies) |
| Share of final disb. reported by Sep 30 (21-mo) | 4 | 2018–2024 | 0.64 / ~0.51 (0.62 ex-runoff) / 0.66 / ~0.71 | FEC 21-mo summaries | yes (timing branch) |
| FEC full-period aggregate ÷ 2-yr class | 1 | 2024 | 1.698 / 1.548 = 1.097 | FEC API + bulk | yes (definition multiplier) |
| All S committees ÷ running class | 4 | 2018–2024 | 1.08 / 1.08 / 1.14 / 1.13 | bulk | yes (definition multiplier) |

## Decomposition

`value = F × m × f` (+ runoff).

- **F:** R18 ≈ 860 ± 15 ($M) × multiple ~ LN(median 1.90, σ 0.11), with 15% × U(1.1, 1.3)
  surge → F median $1.67B.
- **m:** one of {1.00, 1.08, 1.06, 1.15}, weights {.35, .35, .15, .15}.
- **f:**

  | Resolver uses | f | Weight |
  |---|---|---|
  | Pre-general data | N(0.75, 0.045) | 0.40 |
  | Post-general data | N(0.965, 0.015) | 0.52 |
  | Outside money (LN median $4.5B) | — | 0.03 |
  | Diffuse (×LN σ 0.25) | — | 0.05 |

- **Runoff:** 15% chance of +U(0, 60)M in the post-general branch.
- **MC result:** 25/50/75 = $1.35B / $1.57B / $1.80B. Script logic reproduced in the
  forecast; the scratch script is not committed.

2026 cycle-to-date (bulk weball26, FEC file dated 2026-09-26; most coverage ends 06-30, a
few pre-primary reports run to Jul–Sep):

| Slice | n | Receipts | Disbursements | COH | Other |
|---|---|---|---|---|---|
| Running in 2026 | 336 | $880.8M | $643.9M | $369.9M | cand. loans $50.2M |
| All S committees | 634 | $1,156M | $864M | — | — |

- The difference between the two slices includes senators up in 2028/2030: Kelly $20.9M,
  Sanders $12.8M, Cruz $9.1M, etc.
- FEC API aggregate, election_year 2026 (full period): disbursements **$711.3M**, COH
  $367.0M, debts $34.6M. Retrieved 2026-09-26 but only printed, not saved; the retry hit
  the DEMO_KEY rate limit. The 2024 aggregate is saved in `raw/`: $1,698.4M disbursements.
- Top 2026 spenders (2-yr) through ~06-30:
  - Talarico $47.0M (raised $68.6M)
  - Ossoff $39.7M (raised $77.3M, COH $42.6M)
  - Krishnamoorthi $31.5M (IL primary)
  - Brown $22.3M
  - Graham $20.1M
  - Platner $19.3M
  - Cooper $14.3M (COH $20.7M)
  - Peltola $13.9M
- State totals: TX $91M, GA $57M, IL $44M, ME $40M, MI $38M, SC $35M, LA $34M, OH $32M.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-26 | Metaculus aggregations script + API `/api/posts/45220/` | upcoming; opens 09-28; CP reveal 10-01; criteria null; 8 forecasters; Cup Fall 2026 | timing ambiguity becomes central |
| 2026-09-26 | Metaculus scraper | failed: Chromium ERR_CERT_AUTHORITY_INVALID through proxy | dead end |
| 2026-09-26 | Metaculus search for sibling/analogous questions (author DaAdCh; "Senate candidates spending", "OpenSecrets", "cost of election") | no precedent question with criteria; donor questions used OpenSecrets/WaPo | none |
| 2026-09-26 | FEC 24-mo summaries 2020/2022/2024 | Senate final disb $2B / $1.7B / $1.5B | base rate |
| 2026-09-26 | FEC 18-mo summaries 2018–2024 | receipts 579.7 / 702.6 / 943.1 / 857.5; disb 353.2 / 413.7 / 710.6 / 681.9 | multiples |
| 2026-09-26 | FEC 21-mo summaries 2018–2024 | disb 649.7M / >1B / 1.1B / 1.1B | timing fractions |
| 2026-09-26 | FEC 15-mo 2025-26 & 2023-24 | 2026: rec 654, disb 400.8, COH 382.7; 2024: 611.2 / 426.4 / 313.6 | 2026 ≈ 2024 pace |
| 2026-09-26 | FEC 18-mo 2025-26 summary URL | 404, not yet published at the guessed URL | used bulk instead |
| 2026-09-26 | FEC bulk weball/cn 2018–2026 | reproduces FEC summaries; 2026 mid-year numbers above | main data |
| 2026-09-26 | FEC API DEMO_KEY | mostly OVER_RATE_LIMIT (shared IP); two calls succeeded | 2024 full-period aggregate $1.698B |
| 2026-09-26 | AdImpact 2026-06-11 | Senate ads $3.4B projected (+27% vs 2024, +48% vs 2022), all sponsors | small up-nudge to multiple |
| 2026-09-26 | Wesleyan 2026-09-17 | Senate ads so far: candidates $426M, groups $945M, coordinated $58M; broadcast volume below 2020 | candidate share low; limits up-nudge |
| 2026-09-26 | Wesleyan 2026-03-05 | groups 61% of Senate ad spending early in cycle | same |
| 2026-09-26 | WSHU 2026-09-21 | $4B spent on ads across congress + gov by 09-13; Ohio Senate $100M since 08-10 | context |
| 2026-09-26 | Carolina Public Press | NC race projected $600–800M total (all sponsors) | context |
| 2026-09-26 | Roll Call 04-16, 07-16; ABC Q2; Houston Public Media | Democratic records (Talarico $27.1M Q1, $28.3M Q2); GOP candidates weak; SLF > SMP | up for Dem, down for GOP; net small up |
| 2026-09-26 | GA polls (YouGov 51–41, Quantus 49–45) | runoff unlikely (~15%) | small |
| 2026-09-26 | OpenSecrets cost-of-election page | 403; archive.is not fetchable | definition multiplier for OpenSecrets inferred from Statista 2022 ($1.78B raised) |
| 2026-09-26 | Kalshi/Polymarket/Manifold | no spending market; Manifold TX-most-expensive 18% (M$323) | none |
| 2026-09-26 | Search for pre-general Senate totals (2024) | none directly; Dem candidates in 10 key races spent ~$76M in Oct 1–16 2024 (CNN via search) | pre-general adds ~0.08–0.11 of final |

## Dead ends and ruled-out hypotheses

- The Metaculus scraper can't get past the proxy CA; the page renders nothing.
- FEC 18-month 2025-26 summary: not found at the conventional URL (404) on 2026-09-26.
- FEC API with DEMO_KEY is rate-limited by a shared IP. Get a personal api.data.gov key if
  the operator can provide one.
- OpenSecrets pages return 403; archive.is is blocked for WebFetch.

## Open questions to chase next time

1. **Read the criteria once published (2026-09-28).** Source? Snapshot date? Definition?
   Everything hinges on it; see the sensitivity table.
2. CP / Pro / gold at 2026-10-01 reveal.
3. Q3 aggregate for 2026 Senate candidates (after 10-15, via bulk weball26 re-download):
   compare receipts through 09-30 with 2024's ≈$1.2B and 2022's ≈$1.3B.
4. If the criteria name OpenSecrets: find OpenSecrets' current 2026 Senate "spent" figure
   and its definition (6-yr incumbents?).
5. When was the FEC 21-month summary published in 2024 (the date matters if the resolver
   uses it)?

## 2026-09-26 (v2) — resolution criteria supplied by operator

- **Criteria (pasted by the operator; the API still null on 2026-09-26):** "total spending by
  all US Senate candidates running in 2026 according to the FEC". Fine print: "may wait until
  December 31, 2026". The background quotes FEC totals: 2024 $1,687,323,291; 2022
  $1,708,197,866; 2020 $2,007,613,859. Mid-August 2026 total $666,336,000 (D $393.9M, R
  $261.0M, other $11.4M).
- **Series identification:** the FEC API `candidates/totals/aggregates?office=S&election_full=true`
  gives 2020 $2,016.72M and 2024 $1,698.42M, i.e. ratios 0.995 and 0.993 to the stated values.
  So the series is the full-election-period "by the numbers" aggregate, not the 2-year
  statistical summary. 2026 today: disbursements $711.27M, receipts $993.27M (incl. $148.2M
  transfers from authorized committees), COH $367.0M, debts $34.6M. Snapshots are in `raw/`.
  - election_full=false calls: rate-limited, not obtained. Worth trying next time, to see
    whether the ~0.6% gap is a 2-yr/6-yr or active-candidate filter.
- **FEC 2026 calendar (verified):** Oct Quarterly 09-30/10-15; Pre-General 10-14/10-22;
  Post-General 11-23/12-03; Year-End 12-31/2027-01-31. So a 12-31 resolution sees data
  through 11-23 only (~96–97% of final).
- **v2 MC:** `resolved = ((F2 + U(60,110)) × 0.994) × f + runoff`, with f = 0.80
  post-general / 0.12 partial processing / 0.05 pre-general / 0.03 diffuse → $1.66B
  [$1.52B, $1.82B].
- **Open questions for the next update:**
  - How fast does the FEC process Senate post-general reports into the aggregate? Check
    2024: was the aggregate on 2024-12-31 already near final?
  - After 10-15, re-download weball26 and re-run the multiple check.

## 2026-10-02 (v3) — update

- **Metaculus (pre-fetched `raw/metaculus-2026-10-02.json`, 14:09Z).**
  - CP $1.694B [$1.497B, $1.950B], n=65.
  - Pro $1.816B [$1.591B, $2.088B], n=7.
  - Gold $1.709B [$1.530B, $1.927B], n=24.
  - Movement since opening (09-28): CP 1.686 → 1.754 (09-30) → 1.694; Pro flat at ~1.82;
    gold 1.766 → 1.709.
  - Reveal tripwire (> $200M gap) not fired.
- **Comments.**
  - Theomachado (09-28) asked whether the 12-02 page (data to 10-14) or a later page
    counts, and estimated a ~$220M timing gap.
  - The author, DaAdCh (09-28), replied that reporting lag "should and will be considered"
    by the admins, and that "we have almost a month to wait … and so will include
    post-general reports". The only limit is the tournament window.
  - DeRuina (09-30) made a disbursement-multiple argument: June disbursements were $711M in
    2022, $682M in 2024 and ~$670M in 2026, with finals at ~2.5×. They watch for Q3
    disbursements through 09-30 above ~$1.05B.
- **FEC bulk weball26/cn26** (file last-modified 2026-10-02 05:37Z) are unchanged versus
  09-26 for Senate candidates: running-2026 class 336 candidates, $880.8M receipts,
  $644.0M disbursements, $369.9M COH. 93 candidates have coverage past 06-30
  (pre-primary), carrying $173M of disbursements. No Q3 reports yet. Snapshot:
  `raw/fec-bulk-senate-totals-2026-10-02.csv`.
- **FEC API** `candidates/totals/aggregates` (election_full true and false): OVER_RATE_LIMIT
  on DEMO_KEY again. Still no full-period 2026 number newer than 09-26 ($711.3M).
- **Reporting calendar:** no FEC deadline has passed since 09-26.
  - October Quarterly (to 09-30) due 10-15. Expect bulk/API processing ~10-16 → 10-25.
  - Pre-General (to 10-14) due 10-22.
  - Post-General (to 11-23) due 12-03.
- **News searches** ("third quarter Senate fundraising 2026", "Talarico Paxton September
  2026", "Senate campaign spending 2026 most expensive"): no 2026 Q3 totals announced yet.
  - USAFacts snippet matches the bulk data (Talarico $47.0M, Ossoff $39.7M spent).
  - Washington Sun (09-20): after NRSC v. FEC, NRSC coordinated spending ~$46M (vs <$3M
    before); DSCC ~$1M. This party spending is not in candidate totals: small down.
- **OpenSecrets:** still 403.
- **MC** (`v2` model reproduced exactly: 1.658 [1.519, 1.813]). Timing weights 80/12/5/3 →
  87/8/2/3 give 1.671 [1.537, 1.824]. Hand adjustments: crowd +$10M (upper quartile +$15M),
  NRSC −$5M → **$1.675B [$1.540B, $1.835B]**.
- **Next:** re-download weball26 after ~10-16 (Q3) and ~10-24 (pre-general). Retry the FEC
  API in a fresh hour window.

## 2026-10-08 (v4) — update

- **Metaculus** (`raw/metaculus-2026-10-08.json`, 00:36Z):
  - CP $1.768B [$1.565B, $2.001B], n=86.
  - Pro $1.629B [$1.485B, $1.816B], n=7.
  - Gold $1.694B [$1.517B, $1.912B], n=28.
  - Pro trajectory: 1.816 (10-02) → 1.71 (10-03) → 1.624 (10-07).
  - The aggregations call returned an empty comment list. I re-fetched the comments once
    through the same `_Fetcher` and merged them into the snapshot.
- **New comment, nightsky81 (10-04):** the headline is $670,150,455. Their LLM-assisted
  audit claims:
  - Hovde was double counted in 2024 (+$32M).
  - Barrasso/Lee (2024) and Krishnamoorthi/Kelly (2026, −$35M) are missing from the
    aggregate because their district is null.
  - Year-end reports were ≈ $20M in each of 2022 and 2024.

  None of this is verified by me.
- **FEC page rendered (Playwright, /opt/pw-browsers/chromium)**, with network calls logged:
  - The headline query is `candidates/totals/aggregates?aggregate_by=office&election_full=true&election_year=YYYY&office=S&is_active_candidate=true`.
  - It reproduces the 2024, 2022 and 2020 values in the question to the dollar. 2018 is
    $1,056,300,414.
  - 2026: $670,150,904 (D 401.1 / R 257.5 / O 11.6).
  - **My v2/v3 add-on term was calibrated on the unfiltered aggregate ($711.3M on 09-26),
    which is $41M high.** I matched the 2020/2024 ratios but never checked the 2026 one
    (0.942). Lesson: verify the exact query behind a dashboard number, not just
    historical agreement.
  - The page's active top 10 includes Krishnamoorthi ($31.5M) and Cornyn, both primary
    losers. So the gap is not simply primary losers flagged inactive; the null-district
    hypothesis fits the size.
  - To render the year selector: `select#election-year` (the first `select` is
    `top-category`).
- **FEC bulk** 2026-10-07 05:41Z: unchanged ($880.8M receipts / $644.0M disbursements,
  class 2026). Headline − 2-year class = +$26.2M.
- **FEC API DEMO_KEY:** OVER_RATE_LIMIT. Not needed now: the page's own query gives the
  number.
- **News:** no Q3 toplines announced yet (Talarico, Ossoff, Brown, Cooper, Platner
  searched). GA: no October polls; the debate is on 10-08.
- **MC:**
  - The v3 model reproduces exactly: 1.671 [1.536, 1.824].
  - v4 replaces the add-on with D ~ N(+20, 15) → 1.619 [1.485, 1.773].
  - Hand adjustments (crowd +10, upper quartile +15; NRSC −5) → **$1.625B [$1.490B, $1.790B]**.
- **Next:** after 10-16, re-render the FEC page and re-download weball26 for Q3. Compare the
  2-year-class disbursements through 09-30 with ≈$1.0B (receipts view) vs ≈$0.9B
  (disbursement-multiple view).
