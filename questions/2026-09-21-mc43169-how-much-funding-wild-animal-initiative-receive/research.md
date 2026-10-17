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

---

## Addendum 2026-09-23 — correcting the "permanently" framing

Prompted by an operator challenge to the phrase "Good Ventures forced Open Philanthropy out
of wild animal welfare permanently". Went to the primary source, which I had only seen
second-hand through WAI's summaries [4][5]. **`forecast.md` v1 is left untouched (rule 8);
this note is the correction of record and the next update should carry it forward.**

Primary source: Alexander Berger & Emily Oehlsen (Open Philanthropy), "[Linkpost] An update
from Good Ventures", EA Forum, **2024-06-14** —
https://forum.effectivealtruism.org/posts/foQPogaBeNKdocYvF/linkpost-an-update-from-good-ventures
(accessed 2026-09-23).

**What was actually said** (verbatim): *"while we generally plan to continue increasing our
grantmaking in our existing focus areas via our partner Open Philanthropy, we have decided to
exit a handful of sub-causes (amounting to less than 5% of our annual grantmaking), and we
are no longer planning to expand into new causes in the near term by default."* The exited
sub-causes, named in the thread rather than the post: **wild animal welfare (including
averting human-caused harms), all invertebrate welfare (including farmed shrimp), digital
minds, gene editing**.

**What holds.** The direction of causation is right. Good Ventures is the funder; Open
Philanthropy is the advisor that recommends grants. OP cannot make Good Ventures money go
somewhere Good Ventures declines to send it, so "Good Ventures' decision, OP's consequence"
is the correct attribution, and WAI's own write-up uses "required". "Forced" is defensible
shorthand but it overstates: Good Ventures decided where *its own* money goes.

**What does not hold — "permanently" is wrong, and demonstrably so.** On **2025-10-01**
Berger added to the same thread: *"Good Ventures is now open to supporting work that Open
Phil recommends on digital minds/AI moral patienthood… Additionally, Good Ventures are now
open to considering a wider range of recommendations in right-of-center AI policy and a
couple other smaller areas."* So **one of the four exited sub-causes was reinstated ~16
months later**. Nobody ever said "permanent". The defensible claim is: *exited indefinitely,
with no announced route back, and — unlike digital minds — not named in the October 2025
partial reversal after 28 months.*

**A channel I wrongly wrote off.** My "dead ends" entry says Coefficient Giving re-entering
is "ruled out for 2026". That is too strong. The same 2024 post says OP *"expect[s] to be
able to direct funding to the most promising opportunities whether or not they are a fit for
Good Ventures"*, and invites donors interested in an exited sub-cause to reach out. CG's 2026
story is a sharp increase in money moved from non-Good-Ventures partners. So there are two
live routes, not zero: (a) Good Ventures reverses on wild animal welfare, as it did on
digital minds; (b) CG brokers a **non-GV** donor into the area without any reversal.

**Effect on the forecast: immaterial for 2026, and already mostly priced.** Either route has
to produce a *signed commitment by 2026-12-31* to touch this question. Route (a) has had 28
months without happening and WAW was passed over in the one reversal that did occur. Route
(b), if it happens, arrives as "a new institutional funder signs a multi-year commitment" —
which is exactly the `L` lump already carrying 42% weight; it changes who brokers the money,
not the size of the branch. I estimate the two routes together add **< +$0.1M** to the
median, inside rounding. The median stays **$3.72M**.

**The real lesson, which is Berger's own** (same post): *"such a high degree of reliance on
one funder… represents a structural risk."* That is the whole question. WAI's 990 line 8 was
a proxy for one funder's grant calendar from 2021 to 2024; from 2025 it is a proxy for
whether a *replacement* single funder signs a multi-year letter before 31 December. The
variance did not go away when Open Philanthropy left — it changed which desk it sits on.

**New tripwire for the next update** (not added to `meta.yaml`, which belongs to v1):
Coefficient Giving announces *any* wild-animal-welfare grant, from Good Ventures or a
non-GV partner, with a 2026 signature date, by 2026-12-31 → up, +1.0 USD millions.

---

## v2 working notes — 2026-10-17

### Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-10-17 | `metaculus_aggregations.py 43169` ×3 (11:14, ~11:20, ~11:26 UTC) + `metaculus_scrape.py` ×1 | All failed: 403 Cloudflare challenge; agent-proxy status shows `connect_rejected` for `brunhild.challenges.cloudflare.com:443` | CP/Pro/gold **not refreshed**; meta.yaml community set to null rather than carrying a stale snapshot |
| 2026-10-17 | EA Forum, TNF funding-landscape post (2024-10-02), full text | Verbatim: one ~$1M TNF grant for 2026-07-01..12-31; "won't be making any more grants in the WAW space at least until 2027"; 2027 decision "late 2026"; WAI: "more likely than not that they'll extend funding for WAI through 2027" | **Key driver**: the H2-2026 bridge is the 2025 TNF $1,075,000 |
| 2026-10-17 | WAI FY2024 audited statements (transparency page) | Grants receivable end-2024: $1.5M gross, all < 1 yr (OP tail); 1–5 yr: $0. Contributions w/o restriction $2,050,033; grants $275,294. Concentration: single donor $900,000 = 39% of 2024 support (2023: $5,622,192 = 82%) | No TNF promise outstanding at end-2024 → bridge booked 2025. 2024 also had a one-off ~$0.9M item |
| 2026-10-17 | WAI 2024 Form 990 public copy | Line 1f $2,325,327; Schedule B not in public copy | Confirms 2024 line 8 |
| 2026-10-17 | WAI 2025 annual report p.32 (re-read) | TNF $1,075,000; "draft, unaudited" | — |
| 2026-10-17 | EA Forum "Funding priorities for WAI in 2026" (re-read) | "$267,000 short" of $4.1M 2026 budget in Nov 2025, i.e. ~$3.83M already covered — only possible with the TNF bridge in hand | Consistent with driver |
| 2026-10-17 | ProPublica API, WAI | Latest filing FY2024 (no data fields; PDF processed 2026-01-20). No FY2025 | Tripwire 4 not fired |
| 2026-10-17 | WAI transparency page | Latest 990/audit: 2024. No FY2025 audit yet (FY2024 audit issued 2025-08-12) | — |
| 2026-10-17 | WAI blog index | Latest post 2026-08-12; nothing on funding since June grants round | Quiet |
| 2026-10-17 | EA Forum WAI tag | Latest: "Phase 3 of field-building" (2026-08-19), no revenue info; critical comment thread on cost-effectiveness | Neutral; weak negative for donor sentiment |
| 2026-10-17 | RP/ACE sheet CSV re-export | Byte-identical to 2026-09-21 | Projection not revised |
| 2026-10-17 | navigation.org/grants | Focus areas: climate, farm animal welfare, criminal justice, open science, nuclear (via Longview). No WAW | Weak negative on renewal |
| 2026-10-17 | ProPublica search "Navigation Fund" | Navigation Charitable Fund, EIN 92-1117448 (public charity). FY2024 990 PDF blocked by Cloudflare | Could not check whether the $900k 2024 donor was TNF; the audit books it as an unrestricted contribution, and TNF said only one bridge grant → probably not TNF |
| 2026-10-17 | ACE 2026 recommendations | Not out yet. WAI re-evaluated in 2025 and holds two-year status from 2025-11-04 | v1's ACE tripwire retired |
| 2026-10-17 | Coefficient Giving / AWF 2026 | No WAW grant to WAI found; no AWF 2026 payout report found | AWF 2026 uncertain, kept $0–0.3M |

### The accrual-timing finding, stated carefully

- **Claim:** TNF's 2025 contribution of $1,075,000 is the ~$1M bridge for July–Dec 2026, recognised
  in FY2025 when promised or paid. It therefore will not appear on the FY2026 990.
- **For:** TNF's stated plan is one bridge grant and no other WAW grants until 2027. The amount
  matches (~$1M). OP covered 2025 in full ($2M/yr through 2026-06-30), so WAI needed no TNF
  money for 2025 operations. No TNF receivable existed at end-2024. In Nov 2025 WAI said its 2026
  budget was ~93% covered.
- **Against / residual:** TNF could have given extra 2025 support and still made the bridge in
  2026; the $75k excess over "~$1M" is unexplained; the 2025 figures are draft. → P(claim) ≈ 0.8.
- **Decisive check:** FY2025 audit Note "Net assets with donor restrictions — time restricted"
  at 2025-12-31. ≈ $1M → claim confirmed.

### Monte Carlo (v2)

`B ~ LN(1.95, 0.15)`; `H ~ Bern(0.20)·LN(1.0, 0.1)`; `R ~ Bern(0.42)·LN(1.6, 0.4)`;
`L ~ Bern(0.30)·LN(1.1, 0.6)`; independent; 2M draws, seed 43169.
Quantiles p5..p95: 1.67, 1.81, 2.16, 3.09, 4.09, 5.10, 5.77.

### Open questions for v3

1. The WAI giving-season post (mid-Nov): does it mention TNF's 2027 decision?
2. The FY2025 audit: what is time-restricted at end-2025?
3. Re-fetch the Metaculus cohorts. If they have moved below ~3.6 without news, someone may have
   found the same accrual point.
