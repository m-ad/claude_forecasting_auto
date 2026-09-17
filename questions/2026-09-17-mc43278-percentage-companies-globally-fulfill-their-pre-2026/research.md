# Research log — What percentage of companies globally will fulfill their pre-2026 broiler commitments in 2026 and 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: [Chicken Watch progress tracker](https://chickenwatch.org/progress-tracker),
  run by The Humane League / Open Wing Alliance (OWA). Metaculus reads it on **2028-01-01**.
- **Exact filter (fine print)**: Issue = `Broiler`, Victory Date `1990–2025`, Timeline `2026 and after`
  → denominator. Add status `Reporting Fulfilled` → numerator.
- **Release schedule**: none. The tracker is a live Google Sheet, updated ad hoc by OWA staff.
  There is no scheduled refresh, which is itself a load-bearing fact (see below).
- **Annulment clause**: if Chicken Watch stops reporting or changes criteria incomparably.

### The tracker is machine-readable — how to re-pull it

The page embeds an Awesome Table view (`-NqYH6wXir1Ia4I27P6G`) backed by a public Google
Sheet. `raw/chickenwatch_pull.py` drives Chromium, records the `gviz/tq` response off the
wire and writes the broiler slice plus a summary; `raw/base_rates.py` reproduces every
reference class below offline from that snapshot; `raw/model.py` is the scenario mixture.

- Sheet: `docs.google.com/spreadsheets/d/1GcOfjaHy0xTPluZKUkxyNH8u0_qE7T6tdUpeUg7GEyI`, tab `Cleaned`.
- 2026-09-17 pull: 3566 rows total (2916 cage-free, 650 broiler).
- **Question's filter today: 4 / 405 = 0.988%.**

### The scaling decodes the creator's intent exactly

Metaculus `scaling` for this discrete question: `range_min 0.862068965645`,
`nominal_min 0.98522167…`, `nominal_max 14.77832512…`, `range_max 14.9014778321`,
`inbound_outcome_count 57`.

- `4/406  = 0.9852216749%` → **exactly** `nominal_min`
- `60/406 = 14.7783251232%` → **exactly** `nominal_max`
- `3.5/406` and `60.5/406` → **exactly** the range bounds; `60 − 4 + 1 = 57` buckets.

So the question is literally: **how many of ~406 commitments will read "Reporting Fulfilled"
on 2028-01-01?** Buckets are integer counts 4…60, closed below, open above. The denominator
was 406 at question creation (2026-06-20) and is 405 today — i.e. the numerator has not moved
in three months and the denominator has drifted by one row.

### Edge cases / counter-intuitive resolutions

- The filter keeps **only forward-looking pledges**: Victory Date ≤ 2025 with a deadline ≥ 2026
  means Victory Date < Timeline always. Chicken Watch's dataset also contains 15 broiler rows
  logged as *already met on the day they were recorded* (Victory Date ≥ Timeline, 14/15
  fulfilled, 93%). Those are excluded by construction — anyone quoting a raw "broiler
  fulfilment rate" that includes them is quoting a number this question cannot produce.
- Deadline **extensions do not shrink the denominator**: moving a company from 2026 to 2030
  keeps Timeline ≥ 2026. Only row *deletion* shrinks it.
- The denominator is whatever the tracker shows on 2028-01-01, not 406.
- A company can resolve into the numerator by **ceasing to sell chicken** — Bastard Burgers is
  marked fulfilled with the note "Chicken is no longer served."

## Reference classes considered

Rates are Chicken Watch's own `Reporting Fulfilled` share, pulled 2026-09-17, restricted to
**forward-looking** pledges (Victory Date < Timeline) whose deadline has already passed —
the only class that matches this question's construction.

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Broiler, global, deadline passed | 226 | TL ≤ 2025 | **3.10%** (7) | Chicken Watch pull | **yes — primary** |
| Broiler, North America, deadline passed | 205 | TL ≤ 2025 | 2.44% (5) | same | yes — floor case |
| Broiler, Europe, deadline passed | 21 | TL ≤ 2025 | 9.52% (2) | same | yes — but n=21, 2 events |
| Broiler, US BCC 2024 cohort | 193 | 21 months post-deadline | 2.59% (5) | same | yes — closest deadline analogue |
| Cage-free, global, deadline passed | 1285 | TL ≤ 2025 | 37.98% (488) | same | yes — upper bound / difficulty gap |
| Cage-free, Europe, deadline passed | 613 | TL ≤ 2025 | 44.86% (275) | same | yes |
| Broiler, "already met when logged" (VD ≥ TL) | 15 | — | 93.3% (14) | same | **no — excluded by the filter** |
| Founders Pledge broiler follow-through | — | — | 30% | Rethink Priorities [6] | no — measures *real* compliance, not Chicken Watch status |
| Rethink Priorities broiler follow-through | — | — | 1–94% | RP / EA Forum [7] | no — uninformative width |

**The cage-free / broiler gap is ~12×** and is the single most important structural fact:
cage-free egg switching is a procurement change with a functioning supply chain; ECC
compliance requires a breed change the European industry says is not available at scale.

## Decomposition

Composition of the 405-row denominator (2026-09-17):

| Cut | Detail |
|---|---|
| Deadline | 353 × 2026, 5 × 2027, 19 × 2028, 7 × 2029, 18 × 2030, 3 × 2032 |
| Policy version | 360 Europe/UK (ECC), 34 US/Canada v2, 7 NZ/Aus, 3 US/Canada v1, 1 Brazil |
| Status | 4 Reporting Fulfilled, 193 Reporting, 208 Not Reporting |
| Country (top) | France 78, UK 65, Sweden 54, Germany 52, US 29, Spain 10 |
| Industry | Restaurant 136, Foodservice 90, Retailer 82, Manufacturer 52, Hospitality 21 |
| Mean lead time | 5.57 years (Timeline − Victory Date) |

For the numerator to grow, each company needs three things in sequence:
`P(reaches 100% of its pledged scope) × P(publicly reports it) × P(Chicken Watch logs it)`.
Only the 353 + 5 rows due by end-2027 are even eligible; the 47 rows with 2028+ deadlines
contribute ~0.

The third factor is the one most forecasters will miss — see the disconfirming evidence below.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-17 | Metaculus aggregations API, post 43278 | discrete, 57 buckets; **status `upcoming`, 1 forecaster, no CP/Pro/gold, 0 comments** | no crowd anchor exists; verified twice (API + scraper) |
| 2026-09-17 | Chicken Watch tracker, full sheet pull | 4/405 = 0.988% today; scaling decodes to counts 4…60 / 406 | fixes the question to a count problem |
| 2026-09-17 | Same, forward-looking past-deadline cohorts | broiler 3.1% global / 2.4% NA / 9.5% EU; cage-free 38.0% / 44.9% EU | primary outside view |
| 2026-09-17 | Same, US BCC 2024 cohort | 5/193 at 21 months post-deadline; 27 still merely "Reporting" | deadlines do **not** trigger a fulfilment wave in this dataset |
| 2026-09-17 | OWA *ECC Progress Report 2025* (PDF) [1] | 394 signatories (Jul 2025); 1.3 bn chickens covered; "**few of the hundreds of ECC commitments have been completely fulfilled**" | confirms sparse numerator |
| 2026-09-17 | Same, p.4 | "Previously, the ECC had a **blanket deadline of 2026**. With the deadline approaching quickly, we made the decision to take a **more flexible approach — working with companies on a case-by-case basis** to set ambitious and achievable deadlines" | **largest single downward driver**: the campaigner has retired the deadline that would have forced the reporting event |
| 2026-09-17 | Same, p.8 | ECC requires third-party audit + public annual per-criterion reporting; Beter Leven 1★ (NL), Deutscher Tierschutzbund (DE), Red Tractor Enhanced Welfare (UK) accepted as equivalent | modest upward: a cheap documentable route to a fulfilment claim that the US 2024 cohort never had |
| 2026-09-17 | ChickenTrack 2025 (CIWF, pub. Mar 2026) [2] | 107 signatories tracked, 76 reported; **3 at 100% overall** (Waitrose, REMA 1000 Norge, Norsk Kylling); breed: 36 below 10%, 17 at 0% | real full compliance ≈ 3% of major signatories, one year out |
| 2026-09-17 | ChickenTrack 2024 (pub. Apr 2025) [3] | 93 tracked, 64 reported; 2 at 100% (M&S, Norsk Kylling); 1 at 100% on breed (Schiever) | 2 → 3 in a year among the majors |
| 2026-09-17 | Cross-check ChickenTrack vs Chicken Watch | **Norsk Kylling (100% ECC since Aug 2022), REMA 1000, Waitrose (100% from Sep 2025) are all marked `Not Reporting` on Chicken Watch** | **decisive**: the resolution source systematically lags/undercounts real fulfilment |
| 2026-09-17 | Sustainable Chicken Forum launch, Feb 2026 [4][5] | 8 businesses / 18 UK brands (Yum!/KFC, BKUK, Nando's, Wagamama/TRG, Big Table, Popeyes UK, Wingstop UK, Loungers) quit the BCC | downward on real compliance; mostly *already removed* from the tracker — Nando's, Big Table, TRG, Wagamama, Pizza Hut, Greene King, Whitbread, Mitchells are all absent from the whole 650-row broiler sheet |
| 2026-09-17 | Frontiers in Animal Science 2025 (peer-reviewed) [8] | UK slower-growing transition costs +25–32%/kg (EU) to +37.5%/kg (UK); consumer–citizen gap; 2026 deadline "highly unlikely" | confirms breed is the binding constraint |
| 2026-09-17 | BroilerNet / Zootecnica; WATTPoultry [9][10] | EU "premium concept" chicken ~8% (2019) → 15–20% expected by 2025; France 24% slower-growing | supply exists but is nowhere near 100% for ~400 companies |
| 2026-09-17 | Rethink Priorities [6] | Founders Pledge: 60% cage-free vs **30% broiler** follow-through; ACE 31–86% (mean 53%) general | these price *real* compliance over an open horizon, not Chicken Watch status by 2028 |
| 2026-09-17 | EA Forum / RP [7] | broiler follow-through 1–94%; cage-free 48–84%; 92% of ≤2024 cage-free deadlines fulfilled (Jul 2025) | corroborates the cage-free/broiler gap |
| 2026-09-17 | Metaculus tournament notebook + EA Forum announcement [11][12] | Animal Futures tournament (Metaculus × Sentient Futures × The Unjournal), 16 questions, $3,400 prizes | explains why the question exists; no creator estimate published |

## Dead ends and ruled-out hypotheses

- **Wayback Machine**: `web.archive.org` was returning "Temporarily Offline" on 2026-09-17 and
  the CDX index had **zero** captures of the backing `gviz` URL. So there is **no time series**
  of the tracker's fulfilled count. This is the biggest missing input; the only internal
  substitute is the cross-section by deadline year. *Next update: retry the CDX query, and in
  any case diff `raw/chickenwatch-broiler-2026-09-17.csv` against a fresh pull — that CSV is
  now the first point of a series we are building ourselves.*
- **Firebase / Awesome Table REST API**: `awesome-table.firebaseio.com` returns
  `Permission denied` (401) without anonymous auth. Use the Playwright wire-capture instead.
- **Direct Chicken Watch scraping via WebFetch**: the tracker page is a Next.js shell; the data
  is only in the embedded iframe's `gviz` call. WebFetch returns nothing useful.
- **Dutch head start does not apply.** Albert Heijn and Jumbo are absent from the whole broiler
  sheet — they never signed the ECC (they run Beter Leven instead). The 40 "Netherlands" rows
  are pan-European commitments (Aldi Nord, Subway, Domino's, McCain…), not Dutch retailers.
- **Danish convenience-sector wave does not apply either**: those ~40 commitments carry 2025
  deadlines, so they sit outside the Timeline ≥ 2026 filter.
- **Metaculus community prediction**: genuinely does not exist (1 forecaster, CP unrevealed,
  no comments). Confirmed via both the aggregations API and the page scraper. No Kalshi /
  Polymarket / Manifold / GJOpen / INFER market on corporate animal-welfare pledge fulfilment
  was found. Sentinel and Mantic do not cover this domain.

## Open questions to chase next time

1. Does Chicken Watch do a **post-deadline status pass** in H1 2027? Diff the CSV. This is
   ~70% of the variance in the answer.
2. Does the **ChickenTrack 2026 report** (expected ~March 2027, covering 2026) raise the
   "100% compliant" count above 3, and do those names then appear on Chicken Watch?
3. Do **Norsk Kylling, REMA 1000, Waitrose, M&S** ever flip to `Reporting Fulfilled`? If those
   four — the clearest real-world fulfilments in existence — stay `Not Reporting` through 2027,
   the low scenarios are basically confirmed.
4. Does OWA publish an **ECC Progress Report 2026/2027**, and does it name a fulfilled count?
5. Does the **denominator** stay near 400, or does OWA purge withdrawn commitments? A purge
   raises the percentage mechanically without any company doing anything.
