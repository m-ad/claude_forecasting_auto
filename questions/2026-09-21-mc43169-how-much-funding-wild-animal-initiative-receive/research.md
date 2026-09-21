# Research log — How much funding will Wild Animal Initiative receive in 2026?

Working notes for v1 (2026-09-21). Rough is fine; completeness beats polish.

## Question mechanics

- **Resolution source**: Form 990 for Wild Animal Initiative Inc (EIN 82-2281466), fiscal
  year ending December 2026, **Part I line 8 "Contributions and grants"**, as it appears on
  ProPublica Nonprofit Explorer.
- **Units**: the Metaculus scale runs 1.0–7.0 with both bounds open. The resolution criteria
  say "financial amount (in US Dollars)" and the historical series runs $0.086M–$6.82M, so
  the scale is unambiguously **millions of USD**. (Attempted a scraper cross-check of the
  displayed unit string; Playwright failed on the sandbox proxy CA — `ERR_CERT_AUTHORITY_INVALID`.
  Not worth chasing: 1–7 cannot be anything but $M for this series.)
- **Release schedule**: filing lag has been 8–11 months after fiscal year end
  (FY2022 filed 2023-08-21, FY2023 filed 2024-11-11, FY2024 filed 2025-08-19). So the
  FY2026 990 lands roughly **2027-08 to 2027-11**. The question *closes* 2026-12-31 but
  cannot resolve until then.
- **Accounting basis — this is the whole question.** Verified from the ProPublica API that
  for every year `totrevenue − totcntrbgfts = invstmntinc` exactly, i.e. line 8 is
  everything except investment income. WAI reports on the **accrual** basis (stated in the
  ACE/RP financials sheet for 2025 and 2026). Under accrual/GAAP an *unconditional*
  multi-year promise is recognised in full in the year the promise is made, not when cash
  arrives. That is why the series oscillates so violently — see decomposition below.
- **Edge cases**:
  - If WAI ceases to exist or no FY2026 990 is filed → **annulled** (not NO). Low
    probability; WAI held $6.4M net assets at end-2025.
  - Audit adjustments: the 2025 figures used here are WAI's own *draft, unaudited* numbers
    ("will be updated once audited figures are available").
  - A late-December 2026 multi-year pledge letter lands in FY2026 revenue even if no cash
    moves until 2027. Conversely a pledge signed 2027-01-05 misses entirely. **The single
    largest source of variance in this question is the signature date on one grant letter.**

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| WAI's own 990 line 8 | 7 | 2018–2024 | geometric mean of 2021–24 = $3.43M; sd of log YoY = 1.42 (!) | ProPublica API [1] | Kept as volatility anchor only — the spikes are mechanical, not random |
| WAI 990 line 8, lump-years removed (2022, 2024, 2025) | 3 | 2022–2025 | $1.72M → $2.33M → $2.72M, +35%, +17% | [1], [3] | **Primary** — this is the recurring-revenue trend |
| Funder-by-funder build-up for 2026 | — | 2026 | ~$2.8–3.5M | [3], [8], [9] | **Primary** |
| Small EA-funded research nonprofits after losing their anchor funder | ~5 | 2024–26 | too few clean cases, and survivorship-biased | — | Dropped, noted |

The naive "every other year is a spike" pattern (2021 ↑, 2022 ↓, 2023 ↑, 2024 ↓ → 2025 ↑?)
**already failed in 2025** ($2.72M, a low year). That is important: the alternation was never
a cycle, it was Open Philanthropy's grant calendar, and OP is gone.

## Decomposition

### Why the series oscillates (mechanical, fully explained)

| Year | 990 line 8 | Of which: multi-year lump booked that year | Residual (recurring) |
|---|---|---|---|
| 2021 | $5.086M | OP $3.5M / 2 yrs, announced 2021 [6] | ~$1.59M |
| 2022 | $1.724M | none | $1.72M |
| 2023 | $6.818M | OP $6.0M, Jul 2023–Jun 2026 [5][7] | ~$0.8–1.3M |
| 2024 | $2.325M | none (possible small OP tail) | ~$1.85–2.33M |
| 2025 | **$2.716M** (draft) | none | $2.716M |

2025 is itemised to the dollar in WAI's 2025 Annual Report [3] and reconciles exactly with
the figure WAI gave Rethink Priorities/ACE ($2,716,044 contributions + $340,622 interest =
$3,056,666 ≈ the sheet's $3,056,665 total revenue [9]). That is a strong cross-validation of
both documents.

### 2025 funding sources (actual, [3] p.32)

| Source | 2025 |
|---|---|
| The Navigation Fund | $1,075,000 |
| Individual donations (~3,000 gifts) | $869,572 |
| ACE Recommended Charity Fund | $346,438 |
| EA Animal Welfare Fund | $300,000 |
| CAF Canada | $60,034 |
| Anonymous family foundation | $30,000 |
| Summerlee Foundation | $20,000 |
| Horne Family Foundation | $15,000 |
| **Total** | **$2,716,044** |

### 2026 build-up (mine)

| Source | 2026 estimate | Basis |
|---|---|---|
| ACE Recommended Charity Fund | **$0.44M (known)** | Feb 2026 $104,433 + Aug 2026 $339,295 [11][12]; WAI re-recommended Nov 2025 [13] |
| The Navigation Fund | $1.0–1.5M | 2025 $1.075M; "non-binding commitment to sustain funding through end of 2026" [4]; WAI says it cannot rely on TNF beyond that |
| Individual donations | $0.9–1.2M | 2025 $0.87M, growing, heavy post-OP appeals [8] |
| EA Animal Welfare Fund | $0–0.3M | last grant Apr–Jun 2025, $300k, explicitly "for activities in 2024 and 2025" [14] |
| CAF Canada + small foundations | $0.12–0.18M | 2025 $0.125M |
| New institutional funders | $0–0.4M | Foundation Relations Manager hired for 2026 [8] |
| **Recurring base** | **≈$2.8–3.5M, central $3.2M** | |

To reach WAI's own projection an additional ~$2M lump is needed.

### The $5,552,333 question

WAI told Rethink Priorities (report published 2026-08-14) that **2026 total revenue =
$5,552,333**, accrual basis, against 2026 total expenditure of $4,280,377 [9]. Net of
~$0.29M interest that is ~$5.26M of line-8 contributions — an 94% jump on 2025.

Confirmed the number is load-bearing, not a typo: the RFMF tabs compute 2027 room for more
funding as $6,975,333 − $5,552,333 = $1,423,000, and the first expansion line item
($125,000) sits at "annual total revenue needed $5,677,333" = $5,552,333 + $125,000. So
$5,552,333 is WAI's stated baseline annual revenue.

**For treating it as informative:**
- Same sheet's 2025 column is accurate to the dollar.
- Sheet explicitly states accrual for both years.
- Incentives run the *wrong* way for inflation: RFMF = capacity − revenue, so a higher
  reported revenue makes WAI look *less* fundable. They had no reason to overstate.
- Compiled mid-2026, so ~H1 actuals were in hand.
- WAI says its reserves gap is $0 against a $6.0M target while budgeting a $4.28M spend —
  i.e. they are planning *not* to draw down, which requires revenue ≈ or > spend.
- Nov 2025: WAI said it was only $267,000 short of fully funding the $4.1M 2026 budget [8].

**Against:**
- The 2026 column is a **budget** column (its expenditure figure is plainly a budget), so
  the revenue figure is a plan, not an actual.
- ACE's Nov 2025 review worked from a "projected 2025 revenue" of ~$3.8M [10]; the actual
  came in at $3.06M. Provenance of the $3.8M is ambiguous (it equals WAI's 2025 *budget* of
  $3,772,000), so this is weak evidence, but it points the right way: WAI's forward numbers
  have run high.
- No announcement anywhere — WAI blog (11 posts in 2026, none about funding received),
  EA Forum, Coefficient Giving, Navigation Fund — of any large 2026 commitment.
- 2026 operating behaviour looks like scarcity, not abundance: FTE cut 20 → 18 [9]; the
  June 2026 grants round awarded $727,658 across 13 projects [15] versus $1.4M across 17 in
  2024 [2].
- OP/Coefficient Giving is out permanently (Good Ventures board decision) [4][5]; nothing
  has replaced it at that scale.

**Reconciliation**: the scarcity signals are *not* decisive against the projection, because
accrual revenue is not spendable cash. A multi-year pledge signed in late 2026 for 2027–29
books entirely in FY2026 while WAI still runs lean during 2026. This is exactly what
happened in 2021 and 2023. So the scarcity evidence downweights the projection only mildly;
the "budget column" and "no announcement" points do most of the work.

Net: I put **~42% weight** on the projection being broadly right (contributions $3.7–6.2M)
and ~58% on 2026 tracking the recurring base.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-21 | Metaculus aggregations, post 43169, `--comments 12 --history` | CP 4.25 IQR[3.31,5.27] n=29; Pro 4.41 n=5; gold 4.23 n=15; 48 forecasters total. One comment, quoting RP's RFMF report | Anchor; cohorts agree |
| 2026-09-21 | CP history | All three cohorts stepped up on 2026-08-14/15 (CP 3.70→4.32, Pro 4.07→5.01→4.41, gold 3.72→4.27) — exactly when the RP report / the comment landed | The crowd's pre-RP view was ~3.7; they put ~35% weight on the projection. Mine is similar but from a lower base |
| 2026-09-21 | ProPublica Nonprofit Explorer + API v2, EIN 82-2281466 | Full 990 series; `totrevenue − totcntrbgfts = invstmntinc` exactly every year | Fixed the resolution metric precisely |
| 2026-09-21 | WAI 2025 Annual Report PDF (transparency page) | 2025: received funds $2,716,044, interest $340,622, expenses $3,908,154, net assets $6,851,041; full funder breakdown | **Highest-value find.** Sets the 2025 anchor and the funder structure |
| 2026-09-21 | WAI 2024 Annual Report PDF | 2024: functional expenses $3.4M, current assets $7.6M, $1.4M to 17 grantees, 23 donors >$5,000 | Context; grants-round size comparison |
| 2026-09-21 | ACE/RP "financials and future plans" Google Sheet (4 tabs, CSV export) | 2025/2026 revenue + expenditure, accrual, FTE 20→18, reserves target $6.0M, gap $0; RFMF arithmetic | The crux number and its provenance |
| 2026-09-21 | RP "Wild Animal Welfare Donation Opportunities & RFMF", 2026-08-14 | WAI 2026 budget $4.28M; 2027 RFMF $1.423M–$6.093M; movement-wide $3.16–8.23M | Confirms budget scale |
| 2026-09-21 | EA Forum "Funding priorities for WAI in 2026" (2025-11-18) | 2025 budget $3.772M; 2026 target $4.1M; "$267,000 short"; aspirational +$3.145M; "Open Philanthropy… no longer funds wild animal welfare" | Raised my base slightly |
| 2026-09-21 | EA Forum "WAI has urgent need for more funding" (2024-08-06) | OP grant = **$6M over three years, 2023-07-01 to 2026-06-30**, ~$2M/yr, ~half the budget | Explains the 2023 spike; confirms no OP money left to book |
| 2026-09-21 | EA Forum "Update on the wild animal welfare funding landscape" (2024-10-02) | Good Ventures required OP to exit; TNF non-binding commitment through end-2026, ~$1M grant to WAI covering H2 2026 | The TNF renewal risk |
| 2026-09-21 | ACE RCF updates Feb 2026 and Aug 2026 | WAI received $104,433 (Feb) + $339,295 (Aug) = **$443,728** | Hard 2026 actual; +$97k vs 2025, far less than I first guessed |
| 2026-09-21 | ACE charity review (2025 recommendation) | Funding capacity $6.9M/yr for 2026–27; ~50% of revenue recurring; reserves >230% of expenditure | Capacity ≠ revenue |
| 2026-09-21 | Coefficient Giving (ex-Open Philanthropy) grants search | 2021 $3.5M over two years; 2023 $6M. Site 403s to WebFetch; figures via search + WAI/EA Forum | Confirms the lump mechanism |
| 2026-09-21 | WAI blog index, all 11 posts of 2026 | No funding-received announcement; June 2026 grants round = $727,658 / 13 projects | Mild evidence against a 2026 windfall |
| 2026-09-21 | EA Funds Animal Welfare Fund payouts | Last WAI grant $300k, Apr–Jun 2025, "for activities in 2024 and 2025"; no 2026 payout report yet | AWF 2026 contribution uncertain, possibly $0 |

## Dead ends and ruled-out hypotheses

- **Coefficient Giving re-entering wild animal welfare in 2026** — searched; no evidence.
  The exit was a Good Ventures board decision, and CG's 2026 story is diversifying its
  *donor* base, not reopening this cause area. Ruled out for 2026.
- **A named 2026 mega-grant** (LJMU Centre of Excellence, endowed professorship,
  Conservation X Labs partnership) — all appear only as *aspirational* line items in the
  RFMF sheet and the ACE review, none as funded. Not ruled out, but unevidenced.
- **Playwright/metaculus-scraper cross-check** — blocked by the sandbox proxy CA. Not needed.
- **WAI 2025 audited financial statements / 2025 Form 990** — not yet published (transparency
  page lists 2017–2024 only; FY2025 990 due ~Nov 2026). This is the best single future
  check on the $2.716M draft figure.
- **Prediction markets** — no Kalshi, Polymarket or Manifold contract on WAI funding exists;
  searched. Metaculus is the only forecaster source.

## Open questions to chase next time

1. What does WAI's **2026 funding-priorities / Marginal Funding Week post** (expect
   mid-November 2026, by analogy with 2025-11-18) say about 2026 revenue to date? This is
   the single highest-value scheduled release before resolution.
2. Does the **FY2025 Form 990** (expect ~Aug–Nov 2026) confirm line 8 = $2,716,044? If the
   audited figure differs materially, my 2025 anchor moves.
3. Has **The Navigation Fund** committed anything for 2027+, and if so *when was the letter
   signed*? A 2026 signature is worth several million on this question; a 2027 signature is
   worth zero.
4. Does ACE's **November 2026** recommendation round keep WAI on the list (affects the
   Feb 2027 RCF disbursement, not 2026, but signals donor flow).
5. Did the ACE/RP sheet's 2026 revenue line get revised after 2026-08-14?
