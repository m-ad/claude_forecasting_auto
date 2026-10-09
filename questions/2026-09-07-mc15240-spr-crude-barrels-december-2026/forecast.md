# How many barrels of crude oil will the Strategic Petroleum Reserve hold in December 2026?

| | |
|---|---|
| **Source** | Metaculus #15240 (question group), subquestion id **31308** — https://www.metaculus.com/questions/15240/how-many-barrels-of-crude-oil-will-the-strategic-petroleum-reserve-hold-on-the-following-dates/ |
| **Type** | numeric (barrels) |
| **Opened / Closes / Resolves** | 2025-01-20 / 2026-12-30 / ~2027-02-26 (EIA *Petroleum Supply Monthly* print) |
| **Status** | open |
| **Current forecast** | **Median 271,700,000 barrels, IQR [260,500,000, 280,100,000]** (v3, 2026-10-09) |
| **Community** | Last cached (2026-09-30 04:55 UTC, fetched 2026-10-02): CP 287,770,298 IQR [274.0 Mb, 333.3 Mb] (5 forecasters) · gold 292,861,812 (4) · Pro 400,242,449 (1). Fresh CP unavailable 2026-10-09 (Cloudflare block) |
| **Next review** | 2026-10-21 (after the expected award notice for the 2026-09-29 RFP) |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v3 — Re-analysis — 2026-10-09

Mode: **re-analysis**. The question's structure changed. v2's "final tranche" was a 10% hypothetical. DOE then issued an actual RFP for it on 2026-09-29, with deliveries **scheduled for November–December 2026**, inside this question's window. The December model is rebuilt around the size of that award.

### Revision

| Driver | Direction | Effect |
|---|---|---|
| Prior (v2, 2026-09-24) | — | Median 283.1 Mb, IQR [281.3, 286.4] |
| **Starting level is now observed, not projected**: WCSSTUS1 for the week ending 10-02 = **282.983 Mb** (draws 0.785 and 0.784 Mb in the last two weeks) [1]. v2 started from the sibling's v4 end-September (284.2 monthly). The leftover trickle after 10-02 is U(0.2, 2.5) Mb (award tally ~1.04 Mb left, plus the uncertainty in DOE's "more than 133 Mb" figure) | ↓ | **−0.9 Mb** |
| **DOE RFP of 2026-09-29: up to 40 Mb from Big Hill and Bryan Mound, bids closed 2026-10-06, deliveries Nov–Dec 2026** [2][3]. Award size is the dominant unknown. Against a large take-up: the identical June offer placed **0.5 Mb** (one award, Vitol) [4][5]. For it: the front of the Brent curve is steeply backwardated again (Dec-26 $102.6 vs Jan-27 $99.0 on 2026-10-01 [6], with the long end in the $60s), and diesel is at a record, which makes borrowing now against ~2028 returns at a ~25% premium roughly break-even to attractive. EIA's October STEO assumes **all 40 Mb** lifts (Nov 262.5, Dec 242.5) [7]. Mixture: 22% ≈ nothing (< 1 Mb), 20% 1–8, 30% 8–25, 28% 25–40 Mb. Median award ~12.6 Mb, and 65–100% of the award is lifted by 31 Dec | ↓ | **−10.1 Mb** |
| **Exchange returns in Nov–Dec: 38% → 18%.** The October STEO holds the SPR flat from December to June and starts returns in **July 2027** (+17.2 Mb/month) [7]. DOE is scheduling 40 Mb *out* of Big Hill in Nov–Dec, the same site that secondary sources said would receive returns from 1 November. Reporting on the RFP says returns of all exchange barrels run to late 2028 [5]. Manifold's thin "SPR starts increasing before Dec 2026" market is at 41% (7 traders) [8], discounted | ↓ | **−1.4 Mb** |
| Escalation 8% → 5%, mandated sale 10% → 7%, refill 8% → 7%. The live 40 Mb RFP is now the policy response, so an extra release beyond 172 Mb is less likely before 31 Dec. Polymarket "Venezuelan oil added to SPR by Dec 31" is at 7.5% ($5.0k volume) [9] | ↑ | **+0.6 Mb** |
| Bridge: N(+0.18, 0.38) kept for quiet Decembers. **N(+0.4, 0.6) when Nov–Dec carries > 5 Mb of lifts**, because the heavy-draw months (Mar–May 2026) had residuals of +0.5 to +1.1 Mb | → | ~0 on the median, widens tails |
| **New forecast** | | **Median 271.7 Mb, IQR [260.5, 280.1]** |

Effects are one-at-a-time switches of each input back to its v2 value in `raw/scenario-model-2026-10-09.py`. They sum to −11.8 against the actual −11.4 move, the gap being interaction.

### Tripwire check (against v2)

| Tripwire from v2 | Fired? | Note |
|---|---|---|
| WPSR weeks 09-25 to 10-09 show 0.3–0.5 Mb/week draws → down ~300,000 barrels; two flat/build weeks → up ~600,000 | **Partial (stronger)** | 0.785 and 0.784 Mb, above the band. Captured in the starting level (−0.9 Mb). The week ending 10-09 is not yet out (release slipped by the Columbus Day holiday) |
| October STEO shows COSQPUS rising in Nov–Dec 2026 → up ~2 Mb; flat to mid-2027 → down ~300,000 | **Fired: down branch, in a stronger form** | The STEO falls by 40 Mb in Nov–Dec, stays flat to June 2027, and rises from July 2027 [7] |
| **DOE issues an RFP for the remaining ~38 Mb by 2026-11-15 → down ~7 Mb** | **FIRED (2026-09-29)** | 40 Mb, deliveries Nov–Dec [2]. Applied as a full re-model: −10.1 Mb on the median |
| Such an RFP awarded at > 15 Mb by 2026-11-30 → down ~15 Mb | Pending | Bids closed 10-06. No award notice by 2026-10-09: the DOE listing's latest item is the 09-29 RFP [10]. The June award took 12 days (06-10 → 06-22) |
| First WCSSTUS1 build by week ending 11-13 → up ~4 Mb | Not yet due | — |
| No build through week ending 12-04 → down ~1 Mb | Not yet due | — |
| Hormuz re-closed or new IEA collective action by 12-15 → down ~10 Mb | Not fired | — |
| Refill appropriations or Venezuela swap with 2026 delivery by 12-01 → up ~2 Mb | Not fired | Polymarket 7.5% [9] |

The v2 review was due 2026-10-08 and was done one day late. The RFP fired on 09-29, ten days before this review. The September sibling had already logged it on 10-02.

### What resolves YES

Unchanged from v1: EIA *Petroleum Supply Monthly*, series MCSSTUS1, end-December 2026, thousand barrels × 1,000, printing around 2027-02-26. Metaculus schedules resolution for 2027-03-30 [11]. Sub-question 31308 is open and closes 2026-12-30.

**Consistency constraint with the September sibling (v6).** December is computed as
Dec = Sep_weekly − D(1–2 Oct) − trickle(after 10-02) − tranche lifted − escalation − mandated + returns + refill + bridge_Dec.
Sep_weekly is the sibling's own v6 sampler, imported from its model file, and D is the part of the observed week-ending-10-02 draw that fell after 30 September. Sep_weekly − D is identically the observed 282.983 Mb, so the two forecasts share the same 2 October anchor and cannot disagree about it. On the monthly basis, December's median is 11.7 Mb below September's (283.4). P(Dec > Sept) = 5.5%, which requires exchange returns or refill barrels to outrun the new tranche and the trickle.

### Outside view

There are two reference classes. (1) The unconditional 3-month MCSSTUS1 change (median 0, IQR [−2.5, +3.9] Mb) is no longer the right prior, because a release with a scheduled delivery window falls inside the horizon. (2) **SPR exchange offers versus barrels placed** in 2026: six solicitations so far, about 133.5 Mb placed against about 212 Mb offered. That is ~63% overall, but bimodal: ~100% of what was offered in March–May, ~1% in June. The October offer is closer in market conditions to the spring rounds (Brent above $100, a steep prompt backwardation) than to June. The June failure is recent, and the design is the same. So I put the mass on "partial" and allow both modes.

### Inside view

Monte Carlo, 1,000,000 draws (`raw/scenario-model-2026-10-09.py`):

Output: **median 271.69**, IQR **[260.46, 280.14]**, p5 249.6, p10 253.3, p90 282.1, p95 283.8. Mean 269.6. P(Dec < 275) = 57.5%; **P(Dec < 252.4 Mb, the statutory floor cited in coverage) = 8.6%**; P(Dec > Sept) = 5.5%.

Posted as **median 271,700,000, IQR [260,500,000, 280,100,000]**. The distribution is wide and bimodal-ish: one mode near 281 (the award fails) and a broad shoulder from 245 to 270.

### Evidence

- **The RFP is real and specific.** DOE's own release: "up to 40 million barrels", Big Hill and Bryan Mound, bids due 11:00 CT on 2026-10-06, "deliveries under awarded exchanges are scheduled for November and December 2026", a 25% premium achieved on earlier exchanges [2]. Rigzone's 10-05 write-up gives the same terms [3].
- **The June precedent is the strongest disconfirming fact.** The DOE award notice for RFP DE-RP96-26PO00005 lists a single 500,000-barrel award to Vitol (as of 2026-06-22) [4]. I found no explanation for the failure. My inference, flagged as **speculation**, is that the premium was too high relative to the curve at the time.
- **The STEO's full-40-Mb path is a modelling convention, not a forecast of take-up.** EIA normally models announced volumes as executed. Weight it as an upper bound, not as a central estimate.
- **The market is pricing tightness.** Brent December 2026 closed at $102.63 on 2026-10-01 and the January contract at $99.02 [6]. Diesel was about $6.50/gal in late September [5].
- **Absent, and looked for:** any report of bid volumes received on 10-06, and any award notice (DOE listing and searches as of 2026-10-09 [10]). An award will likely post 10-13 to 10-20, which is the most important update for this question.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP, q31308 | **287,770,298**, IQR [274.0, 333.3 Mb], 5 forecasters | **2026-09-30 04:55 UTC** (cached 2026-10-02 in the September sibling's `raw/metaculus-2026-10-02.json`) | **Fresh CP unavailable 2026-10-09 (Cloudflare block).** Stale: it predates the RFP's salience. The lower quartile (274) sits close to my median |
| Metaculus gold medalists | 292,861,812, IQR [274.1, 378.1 Mb], 4 | same | same |
| Metaculus Pros | 400,242,449 (1) | same | one stale forecast, ignored |
| EIA STEO Oct-2026 `COSQPUS` Dec | **242.547 Mb** | modelling 2026-10-01 (downloaded 2026-10-09) | Full 40 Mb lifted; near my p2.5. An upper bound on the draw, not a central estimate |
| Manifold — "SPR lowest value in 2026" | P(< 250 Mb) 34.7%; hi-res sibling P(> 275) 34.7%, P(> 250) 43.4% | 2026-10-09 | 12 and 8 traders, mutually inconsistent. Directionally agrees that a large draw is likely. Discounted |
| Manifold — "US announces another SPR drawdown before Nov 1" | 81% | 2026-10-09 | 10 traders; the RFP arguably already qualifies |
| Polymarket — "Venezuelan oil added to SPR by Dec 31" | 7.5% | 2026-10-09 | $5.0k volume; refill branch |
| Kalshi `KXSPR` | no open markets | 2026-10-09 | — |

The cohorts disagree with each other (CP 288 vs gold 293 vs Pro 400). All three are stale relative to the RFP, so no fact I might have missed explains the gap.

### Scenarios

| # | Scenario | Weight | Implies (Mb, monthly print) |
|---|---|---|---|
| 1 | RFP fails or nearly fails (< 1 Mb), trickle ends | 22% | 279–283 |
| 2 | Small award (1–8 Mb) | 20% | 274–281 |
| 3 | Medium award (8–25 Mb) | 30% | 258–275 |
| 4 | Large award (25–40 Mb) lifted mostly by 31 Dec | 28% | 242–263 |
| overlay | Returns in Nov–Dec (18%), escalation (5%), refill (7%), mandated sale (7%) | — | ± a few Mb |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Award mixture (median 12.6 Mb) | the June outcome repeats (award < 1 Mb certain) | median ≈ 281.6, IQR [280.7, 282.6] |
| Award mixture | full 40 Mb awarded (STEO) | median ≈ 249.5, IQR [245.6, 253.2] |
| Lifted share 65–100% | 100% | median ≈ 269.3 |
| Returns 18% | 38% (v2) | median ≈ +1.4 Mb |

### What would change my mind (tripwires)

The award announcement partitions the outcome. The bands below cover the whole range.

- [ ] **By 2026-10-23:** DOE award notice for the 2026-09-29 RFP (DOE news listing / spr.doe.gov award PDF), total awarded **A**:
  - **A < 2 Mb** → **up ~9,000,000 barrels** (median → ~281), tighten IQR to ~±1.5 Mb.
  - **2 ≤ A < 15 Mb** → median → ≈ 281.8 − 0.80·A (A = 8 → ~275.7). IQR ~±1.5 Mb plus the lift-share spread.
  - **15 ≤ A ≤ 40 Mb** → same formula (A = 30 → ~257.8). IQR ~±3 Mb.
  - **No notice by 2026-10-23** → nothing awarded yet, or a delay → **up ~2,000,000 barrels**.
- [ ] **By 2026-11-25:** WCSSTUS1 weekly draws in November above 2 Mb/week → the award is lifting on schedule → confirm. Under 0.5 Mb/week despite a > 10 Mb award → slippage into 2027 → **up ~0.3 × A**.
- [ ] **By 2026-12-05:** any week-on-week build through the week ending 12-04 → returns started → **up ~3,000,000 barrels**.
- [ ] **By 2026-12-15:** Hormuz re-closed or a new IEA collective action → **down ~10,000,000 barrels**.
- [ ] **By 2026-12-01:** refill appropriations enacted, or a Venezuela swap contract with 2026 delivery dates → **up ~2,000,000 barrels**.
- [ ] **By 2026-10-31:** August PSM bridge test (shared with the September sibling): ≤ 285.70 → bridge negative → **down ~400,000 barrels**.

### Sources

1. EIA — *Weekly U.S. Ending Stocks of Crude Oil in the SPR* (WCSSTUS1) — https://www.eia.gov/dnav/pet/hist_xls/WCSSTUS1w.xls — 10-02 = 282,983 kb; 09-25 = 283,767. Snapshot `raw/eia-weekly-wcsstus1-2026-10-09.xls` (accessed 2026-10-09)
2. DOE — *The United States Energy Department Continues Execution of Strategic Reserve Release Commitments* (2026-09-29) — https://www.energy.gov/articles/united-states-energy-department-continues-execution-strategic-reserve-release-commitments (accessed 2026-10-09)
3. Rigzone — *USA Continues Strategic Petroleum Reserve Release* (2026-10-05) — https://www.rigzone.com/news/usa_continues_strategic_petroleum_reserve_release-05-oct-2026-184770-article/ (accessed 2026-10-09)
4. DOE SPR — *FY26 SPR Oil Release No. 3 Award Information* — https://www.spr.doe.gov/posting/EXCHANGE/FY26%20SPR%20Oil%20Release%20No.%203/1-Request%20for%20Proposal/FY26%20SPR%20Oil%20Release%20No.%203%20Award%20Information.pdf — Vitol 500,000 barrels as of 2026-06-22; cited from search-result text, because a direct fetch on 2026-10-09 redirected to a 404 (accessed 2026-10-09)
5. OilMonster (Reuters-sourced) — *US to loan up to 40 million barrels of oil from SPR, last batch from global deal* — https://www.oilmonster.com/article/us-to-loan-up-to-40-million-barrels-of-oil-from-spr-last-batch-from-global-deal/8642 — June take-up ~0.5 Mb; repayment of the exchange barrels not expected until late 2028; diesel ~$6.50 (accessed 2026-10-09)
6. Commodity-Board (CMB) — *Crude oil rally steepens backwardation as Brent-WTI spread widens* — https://commodity-board.com/crude-oil-rally-steepens-backwardation-as-brent-wti-spread-widens — Brent Dec-26 $102.63, Jan-27 $99.02 (2026-10-01); cited from search-result text (accessed 2026-10-09)
7. EIA — *Short-Term Energy Outlook*, October 2026, table 4a `COSQPUS` — https://www.eia.gov/outlooks/steo/xls/STEO_m.xlsx — modelling completed 2026-10-01; Sep 283.347, Oct 282.547, Nov 262.547, Dec 242.547, flat to Jun-27, Jul-27 259.747. Snapshot `raw/eia-steo-oct2026-base.xlsx` (accessed 2026-10-09)
8. Manifold search API — https://api.manifold.markets/v0/search-markets?term=strategic%20petroleum%20reserve — snapshot `raw/manifold-spr-markets-2026-10-09.json`; market detail via https://api.manifold.markets/v0/market/<id> (accessed 2026-10-09)
9. Polymarket gamma API — https://gamma-api.polymarket.com/public-search?q=strategic%20petroleum%20reserve — "Venezuelan oil added to SPR by December 31?" 7.5% / 92.5%, volume $5,046 (accessed 2026-10-09)
10. DOE — *Petroleum Reserves News* listing — https://www.energy.gov/hgeo/opr/listings/petroleum-reserves-news — latest item 2026-09-29 RFP; no award (accessed 2026-10-09)
11. Metaculus API, post 15240 (bot key; aggregations hidden) — `raw/metaculus-api-2026-10-09.json` — 31308 open, closes 2026-12-30, scheduled resolve 2027-03-30 (fetched by the parent session 2026-10-09)
12. September sibling, v6 — `questions/2026-09-07-mc15240-spr-crude-barrels-september-2026/forecast.md` and its `raw/scenario-model-2026-10-09.py` (imported for the September leg)
13. Kalshi trade API `KXSPR` — https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXSPR — no open markets (accessed 2026-10-09)

**Date**: 2026-10-09
**Forecast**: Median 271,700,000, IQR [260,500,000, 280,100,000]
**Thesis**: DOE's 2026-09-29 RFP for up to 40 Mb from Big Hill and Bryan Mound, with deliveries scheduled for November–December 2026 [2], turns December into a question about award size. The identical June offer placed only 0.5 Mb [4]. Today's steep backwardation with Brent above $100 [6] argues for a larger take-up, and the October STEO assumes all 40 Mb (Dec 242.5) [7]. The forecast is a 22/20/30/28 mixture over ~0, 1–8, 8–25 and 25–40 Mb awards. It starts from the observed 282.98 Mb level at 10-02 [1], which is the same anchor the September sibling uses. Exchange returns before year-end are cut to 18% because the STEO starts them in July 2027.

---

## v2 — Update — 2026-09-24

### Revision

| Driver | Direction | Effect |
|---|---|---|
| Prior (v1, 2026-09-07) | — | Median 281.9 Mb, IQR [278.3, 285.2] |
| **Starting level: the September sibling's path, re-derived.** v1 started from the sibling's v1 end-September of 282.3 Mb with ~4.7 Mb of award balance still to land. Three weekly prints later (1.244, 0.403, 0.405 Mb draws) the sibling's v4 puts end-September at **284.2 Mb, IQR [283.8, 284.5]**, and the residual balance is **2.61 Mb**. This model now reuses the sibling's September sampler verbatim, then drains most of the residual in October–November in the trickle regime [1][2] | ↑ | **+1.95 Mb** (incl. −1.4 Mb mean Oct–Dec residual trickle) |
| **Exchange returns from 1 Nov: 45% → 38%.** No DOE document yet confirms the 1 Nov Big Hill date; it still traces to secondary sources [9]. Against it: GAO (May 2026) put Big Hill LE2 completion in early 2028; EIA's STEO models no returns before mid-2027; the June-RFP write-up says returns fall "primarily throughout 2027, stretching into Q1 2028" [9][10]. DOE's 2026-09-23 line, returns of ~200 Mb "within the next year", fits either timing [5] | ↓ | **−0.7 Mb** |
| **Final ~38 Mb tranche before 31 Dec: 13% → 10%, centre 18 → 16 Mb.** Seventeen more days of DOE silence (nothing since 2026-07-09 [4]), *including* Brent at $104.82 on 09-17 and record diesel, i.e. through the kind of price spike that should have triggered it. Less runway: RFP → award → lift now has to fit in ~14 weeks | ↑ | **+0.35 Mb** |
| **Fresh escalation beyond the programme: 7% → 8%.** Hormuz traffic still restricted, Brent back above $103 on 09-23 after Iran's UN address, diesel $6.53/gal record on 09-22 [6][7][8]. No new IEA collective action; Europe was floated as the lead contributor to any second round, focused on products [11] | ↓ | **−0.1 Mb** |
| **Refill / Venezuela swap barrels delivered in 2026: 12% → 8%.** Still a proposal (Wright, 2026-09-03); no signed swap contract with delivery dates. Polymarket prices "Venezuelan oil added to SPR by Dec 31" at 7.5% ($1.6k volume) [12] | ↓ | **−0.3 Mb** |
| **New forecast** | | **Median 283.1 Mb, IQR [281.3, 286.4]** |

The prior-to-new move (+1.2 Mb) is the sum of the rows (+1.95 − 0.7 + 0.35 − 0.1 − 0.3), each
measured by switching that one input back to its v1 value in `raw/scenario-model-2026-09-24.py`.

### Tripwire check (against v1)

| Tripwire from v1 | Fired? | Note |
|---|---|---|
| DOE issues an RFP for the remaining ~38 Mb by 2026-11-15 → down ~8 Mb | **Not fired to date** | DOE listing still ends 2026-07-09 (re-read 2026-09-24) [4] |
| Such an RFP awarded at > 15 Mb by 2026-11-30 → down ~15 Mb | Not fired to date | No RFP |
| First WCSSTUS1 build by wk. ending 2026-11-13 → up ~4 Mb | Not yet due | Still drawing (0.405 Mb, wk. ending 09-18) [1] |
| No build through wk. ending 2026-12-04 → up ~1.5 Mb | Not yet due | |
| Hormuz re-closed or new IEA collective action by 2026-12-15 → down ~10 Mb | **Not fired** | Strait restricted throughout, not newly re-closed; no new IEA action [7][11]. Pressure is higher than at v1 (Brent $95 → $103), reflected as +1 pp in the escalation branch |
| Refill appropriations enacted or Venezuela swap signed with 2026 delivery by 2026-12-01 → up ~3 Mb | Not fired to date | Proposal only [12][13] |

Review was due 2026-09-21; done three days late. Nothing in the gap fired.

### What resolves YES

Unchanged from v1: EIA *Petroleum Supply Monthly*, series MCSSTUS1, end-December 2026,
thousand barrels × 1,000, printing around 2027-02-26. One refinement: the weekly→monthly
bridge is now the September sibling's calibrated N(+0.18, 0.28) Mb (36 months of data), widened
to SD 0.38 for the longer horizon, replacing v1's assumed N(0, 0.9).

### Outside view

Unchanged from v1 (unconditional 3-month MCSSTUS1 change median 0, IQR [−2.5, +3.9] Mb;
"announced ≠ delivered" for the remaining ~38 Mb).

### Inside view

December = end-September level − remaining award trickle − (final tranche) − (escalation) −
(mandated sale) + (exchange returns) + (refill). Monte Carlo, 1,000,000 draws
(`raw/scenario-model-2026-09-24.py`), September leg identical to the sibling's v4:

- End-September (monthly basis): median 284.16, IQR [283.84, 284.49], the sibling's number.
- Oct–Dec residual trickle: mean 1.4 Mb (most of the 2.61 Mb balance lands in the trickle
  regime, plus U(0, 1.5) Mb of award-tally uncertainty in that regime).
- Returns 38% × U(2, 10) Mb; final tranche 10% × ~16 Mb; escalation 8% × ~16 Mb;
  mandated sale 10% × U(1, 4); refill 8% × U(0.5, 4).

Output: **median 283.09**, IQR **[281.25, 286.37]**, p5 263.8, p10 270.1, p90 290.2, p95 291.6.
P(Dec < 275 Mb) = 13.6%; P(Dec < 252.4 Mb) = 0.7%; P(Dec > Sept) = 38.3%.

Posted as **median 283,100,000, IQR [281,300,000, 286,400,000]**. Still left-skewed
(mean 282.0 < median).

### Evidence

- **The September leg is now nearly known**, and the December question has become mostly a
  question about two binary events: do returns start on 1 November, and does DOE re-offer the
  last ~38 Mb. Everything else is ±1.5 Mb.
- **The returns date is still the weakest link and got weaker.** I looked for a DOE document
  confirming the 1 November Big Hill start and did not find one; I did find the June-RFP
  write-up putting that tranche's returns in 2027–Q1 2028 [10] and a GAO timeline for Big Hill
  LE2 in early 2028 [9]. Neither directly contradicts earlier tranches' contractual dates, so this
  is a trim, not a collapse (LR ≈ 0.75).
- **DOE's silence through a price spike is evidence of absence** for a new tranche (LR ≈ 0.75),
  but the spike itself raises the chance of an *escalation* response. Those two push opposite
  ways and roughly cancel on the median; the escalation one fattens the left tail slightly.
- **Disconfirming evidence I hunted for:** a DOE statement that returns have been deferred to
  2027 (none — which is why returns stay at 38%, not 20%); a new RFP or loan (none); a signed
  Venezuela swap (none).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold, q31308 | **no community snapshot taken for this version** | 2026-09-24 | Post 15240 refused with HTTP 403 twice today (default TLS and forced TLS 1.2). Last good values (2026-08-27 vintage, fetched 2026-09-07): CP 399.8 Mb, Pro 400.2 Mb, gold 399.8 Mb, n = 4 — physically unreachable, stale, not used |
| EIA STEO Sept-2026, `COSQPUS` end-Dec | flat after September (~282.05 Mb) | 2026-09-09 vintage | Carried forward from the sibling's v3 read; the STEO holds the SPR flat and models no 2026 returns |
| Polymarket — "Venezuelan oil added to SPR by Dec 31?" | 7.5% | 2026-09-24 | $1.6k volume; informs the refill branch [12] |
| Manifold — "US announces another drawdown of SPR before Oct 1 / Nov 1" | 65% / 46% | 2026-09-24 | 12 / 6 bettors, mutually incoherent (a later deadline cannot be less likely); discounted to zero weight |
| Kalshi | no SPR-level market | 2026-09-24 | `KXSPR` empty |

### Scenarios

| # | Scenario | Weight | Implies (Mb, p10–p90) |
|---|---|---|---|
| 1 | Plateau: residual trickles out, no returns, no new tranche (incl. ~5% small mandated sale, ~4% small refill) | 51% | 280.9–284.8 (median 282.3) |
| 2 | Exchange returns begin Nov, no big draw | 31% | 284.8–292.4 (median 288.6) |
| 3 | Final tranche and/or escalation release | 17% | 257.5–278.6 (median 268.4) |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Returns start 1 Nov with 38% | 45% (v1) | median ≈ 283.8, IQR [281.3, 287.3] |
| Returns 38% | certain from 1 Nov | median ≈ 287.8, IQR [284.9, 290.3] |
| Final tranche 10% | 13% at 18 Mb (v1) | median ≈ 282.8 |
| End-Sept 284.2 | end-Sept 282.3 (v1's start) | whole distribution ≈ −1.9 Mb |
| Oct–Dec trickle drains the 2.61 Mb residual | trickle stops at 30 Sept | median ≈ 284.4 (+1.3 Mb) |

### What would change my mind (tripwires)

- [ ] **By 2026-10-14:** WPSR prints for weeks ending 09-25 to 10-09 still show ~0.3–0.5 Mb/week
      draws → trickle confirmed → **down ~300,000 barrels**; if two consecutive builds or flat
      weeks → **up ~600,000 barrels**.
- [ ] **By 2026-10-14:** October STEO (due ~10-06) shows `COSQPUS` rising in Nov–Dec 2026
      (returns modelled in 2026) → **up ~2,000,000 barrels**; if still flat through mid-2027 →
      **down ~300,000 barrels**.
- [ ] **By 2026-11-15:** DOE issues an RFP for the remaining ~38 Mb → **down ~7,000,000 barrels**.
- [ ] **By 2026-11-30:** such an RFP awarded at > 15 Mb → **down ~15,000,000 barrels**.
- [ ] **By 2026-11-20:** first week-on-week build in WCSSTUS1 on or before week ending 11-13
      (returns started) → **up ~4,000,000 barrels**.
- [ ] **By 2026-12-05:** no build through week ending 12-04 → returns slipped to 2027 →
      **down ~1,000,000 barrels** (returns branch collapses onto the plateau).
- [ ] **By 2026-12-15:** Hormuz re-closed or a new IEA collective action announced →
      **down ~10,000,000 barrels**.
- [ ] **By 2026-12-01:** refill appropriations enacted, or a Venezuela swap contract signed with
      2026 delivery dates → **up ~2,000,000 barrels**.

### Sources

Sources 1–24 from v1 carry forward; the ones load-bearing for v2 are listed here with access dates.

1. EIA — *Weekly U.S. Ending Stocks of Crude Oil in the SPR* (WCSSTUS1) — https://www.eia.gov/dnav/pet/hist_xls/WCSSTUS1w.xls — 2026-09-18 = 284,552 thousand barrels. Snapshot in the September sibling's `raw/eia-weekly-wcsstus1-2026-09-24.xls` (accessed 2026-09-24)
2. September sibling, v4 — `questions/2026-09-07-mc15240-spr-crude-barrels-september-2026/forecast.md` — end-September 284.2 Mb, IQR [283.8, 284.5] (2026-09-24)
3. EIA — *U.S. Crude Oil Stocks in the SPR, Monthly* (MCSSTUS1) — https://www.eia.gov/dnav/pet/hist_xls/MCSSTUS1m.xls — ends June 2026 (accessed 2026-09-24)
4. DOE — *Petroleum Reserves News* listing — https://www.energy.gov/hgeo/opr/listings/petroleum-reserves-news — nothing after 2026-07-09 (accessed 2026-09-24)
5. The Daily Caller — *America's Emergency Oil Stockpile Is Running Low As Winter Nears* (2026-09-23) — https://dailycaller.com/2026/09/23/strategic-petroleum-reserve-drawdown-diesel-heating-oil-winter/ (accessed 2026-09-24)
6. CNBC — *Oil prices rise, snap five day losing streak as Iran vows it will not surrender* (2026-09-23) — https://www.cnbc.com/2026/09/23/iran-us-talks-crude-oil-un-wti.html — cited from search-result text; page returned 403 (accessed 2026-09-24)
7. Wikipedia — *2026–2028 world oil market chronology* — https://en.wikipedia.org/wiki/2026%E2%80%932028_world_oil_market_chronology (accessed 2026-09-24)
8. Scripps News — *Diesel prices hit record $6.51 as White House says no export ban planned* — https://www.scrippsnews.com/us-news/diesel-prices-hit-record-high-as-fuel-costs-continue-to-climb (accessed 2026-09-24)
9. GAO-26-106918 — https://files.gao.gov/reports/GAO-26-106918/index.html — Big Hill LE2 completion expected early 2028 as of May 2026 (per search summary, accessed 2026-09-24; report itself accessed 2026-09-07); Plainview Energy Part I — https://www.plainview-energy.com/p/us-strategic-petroleum-reserve-deep — source of the 1 Nov 2026 returns claim (accessed 2026-09-24)
10. Plainview Energy — *SPR Infrastructure: Big Hill, West Hackberry RFP* (2026-06-12) — https://www.plainview-energy.com/p/us-strategic-petroleum-reserve-deep-b24 — June-RFP returns "primarily throughout 2027, stretching into the first quarter of 2028" (accessed 2026-09-24)
11. Yahoo Finance / Investing.com — *Will IEA/OECD countries release more strategic oil stocks?* — https://finance.yahoo.com/energy/articles/iea-oecd-countries-release-more-015434097.html (accessed 2026-09-24; search-summary level)
12. Polymarket — *Venezuelan oil added to Strategic Petroleum Reserve by...?* via gamma API — https://gamma-api.polymarket.com/public-search?q=Venezuelan%20oil%20Strategic%20Petroleum%20Reserve — Dec-31 leg 7.5%. Snapshot `raw/polymarket-venezuela-spr-2026-09-24.json` (accessed 2026-09-24)
13. BOE Report / Reuters — *Venezuela's heavy crude could be swapped for American oil to fill emergency reserve, Wright says* (2026-09-03) — https://boereport.com/2026/09/03/venezuelas-heavy-crude-could-be-swapped-for-american-oil-to-fill-emergency-reserve-wright-says/ (accessed 2026-09-07, re-surfaced 2026-09-24 with no follow-up contract)
14. Manifold search API — https://api.manifold.markets/v0/search-markets?term=strategic%20petroleum%20reserve — snapshot `raw/manifold-spr-markets-2026-09-24.json` (accessed 2026-09-24)
15. Metaculus — question group 15240, subquestion 31308 — https://www.metaculus.com/questions/15240/ — attempted 2026-09-24, HTTP 403 (accessed 2026-09-24, no data returned); no snapshot

**Date**: 2026-09-24
**Forecast**: Median 283,100,000, IQR [281,300,000, 286,400,000]
**Thesis**: December now starts from the September sibling's re-derived end-September level (284.2 Mb, up from v1's 282.3) with only 2.61 Mb of award balance left, which a ~0.4 Mb/week trickle mostly drains by November [1][2]. That +1.95 Mb is partly offset by trimming the 1 November Big Hill returns branch from 45% to 38% (still no DOE confirmation; GAO and the June-RFP write-up point to 2027) and the refill branch from 12% to 8% (Polymarket 7.5%) [9][10][12]. DOE's continued silence through Brent above $100 cuts the final-tranche branch from 13% to 10%, while the Hormuz pressure behind that price nudges the escalation branch up to 8% [4][7]. Net +1.2 Mb to 283.1, still left-skewed; no Metaculus community snapshot was taken for this version.

---

## v1 — Initial forecast — 2026-09-07

### What resolves YES

The question resolves to the **EIA monthly series MCSSTUS1** — "U.S. Crude Oil Stocks in
the Strategic Petroleum Reserve", thousand barrels, **end of month** — for December 2026,
multiplied by 1,000. The only stated ambiguity clause ("if the EIA stops updating this
tracker, the question will resolve as ambiguous") is not live. The December figure prints
in the *Petroleum Supply Monthly* around **2027-02-26**, roughly two months after the
question closes on 2026-12-30. Two mechanics to keep straight:

1. **The weekly series (WCSSTUS1) is not the resolution source**, but it is the only live
   read. MCSSTUS1 is the stock at the last *calendar* day of the month; interpolating the
   weekly path to that date reproduced the three published 2026 drawdown months to within
   1.1 Mb (residual SD ≈ 0.6 Mb) — see `research.md`.
2. **DOE's "SPR Quick Facts" inventory is a different number** (294.1 Mb at 2026-08-20 vs
   EIA's 289.7 Mb for the same week). Only EIA resolves this.

Mb = million barrels throughout. IQR = interquartile range, the middle 50% of the belief
distribution.

### Outside view

Unconditional MCSSTUS1 base rates (n = 315 three-month windows since 2000): median change
**0**, IQR **[−2,498, +3,924] thousand barrels**, p10 −14,592, p90 +10,896. Only 28.9% of
months since 1977 move more than 3 Mb. So the status-quo prior for a ~4-month-ahead SPR
question is a near-flat level with fat tails on both sides — and, unlike the September
sibling, that prior is close to right here, because the drawdown programme is exhausted
before the window even opens.

The second reference class is **announced SPR programmes versus delivered volume**, and it
governs the left tail: 2022's 180 Mb release executed in full, 140 Mb of FY24–FY27
congressionally mandated sales were cancelled, and the 2026 exchange has awarded only
133.5 of 172 Mb (78%). Announced volume is an intention with roughly a coin-flip
completion rate — which is exactly the status of the remaining ~38.5 Mb.

### Inside view

The Q4 level is the September level plus four discrete policy terms, not a trend.

**Starting point.** From the 415.442 Mb plateau to 286.604 Mb on 2026-08-28, DOE delivered
128.838 Mb against 133.5 Mb awarded across five exchange tranches — a residual of ~4.7 Mb.
The sibling forecast puts 30 September at **282.3 Mb (IQR 280.6–283.8)**.

**Term 1 — exchange returns (up).** The programme is an *exchange*: barrels come back with
an 18–24% in-kind premium, with returns reported to begin **1 November 2026** at Big Hill
and running to September 2028. That start date depends on the Big Hill LE2 life-extension
build finishing (GAO-26-106918 had the site offline with zero fill/drawdown capability as
of ~May 2026), and EIA's own STEO models **no returns before July 2027**. DOE-wide fill
capability of 0.44 Mb/d caps November plus December at ~26 Mb. → **45% × ~+6 Mb**.

**Term 2 — the final ~38.5 Mb tranche (down).** DOE offered 40 Mb on 2026-06-10 and
awarded 0.5 Mb — a 1.25% take-up, after a 17–18 June US–Iran ceasefire removed the
prompt-scarcity value that made a ~26% in-kind premium worth paying. Reporting says Trump
still plans "a final 39 million barrel release" that would take the reserve to ~243 Mb.
No solicitation has appeared in the three months since, including through the July–August
re-escalation when WTI crossed $100 on 2026-07-23. → P(RFP by mid-November) ≈ 35% ×
P(clears materially) ≈ 45% × P(delivers before 31 Dec) ≈ 85% ≈ **13%, centre −18 Mb**.

**Term 3 — fresh escalation (down).** The war is ongoing; Brent ~$95 and WTI ~$90.5 in
early September with elevated Hormuz risk. But the IEA has spent most of its collective
ammunition, US drawdown capability is 61% of design, and the reserve is at a 43-year low.
→ **7% × ~−18 Mb**.

**Term 4 — mandated sale and refill (small, both signs).** ~7 Mb of congressionally
mandated sales remain scheduled across FY2026–27 (10% × ~−3 Mb); refill purchases or
Venezuela heavy-for-light swap barrels actually delivered in 2026 (12% × ~+2.5 Mb). The
$20 bn refill request is not appropriated and the SPR Petroleum Account is depleted.

![December scenarios](charts/december-scenarios.png)

![SPR trajectory and the two open subquestions](charts/spr-trajectory.png)

Monte Carlo, 500k draws, in `raw/scenario-model-2026-09-07.py`:
median 281.9, IQR [278.3, 285.2], p5 259.1, p95 292.4. P(Dec > Sep) = 47.4%;
P(Dec < 275 Mb) = 17.4%; P(Dec < 252.4 Mb) = 1.8%.

The distribution is deliberately **left-skewed**. The upside is capped by physical fill
capability and by the fact that returns can only start once; the downside carries a 38 Mb
policy option DOE says it still intends to exercise. Median ≈ mean − 1.8 Mb.

### Evidence

- **The June tranche failure is the load-bearing fact** (LR strongly toward "flat"). It
  converts "172 Mb will be released" into "133.5 Mb was released" and leaves the remaining
  38.5 Mb contingent on a market that has already refused it once at these premiums.
- **Absence of expected evidence.** If DOE meant to finish the programme, the July–August
  re-escalation was the window, and DOE's petroleum-reserves news feed carries no SPR item
  after 2026-07-09. Three months of silence is informative.
- **EIA's STEO holds `COSQPUS` flat at 284.803 Mb from August 2026 through June 2027**,
  with returns only from July 2027 at 0.555 Mb/d. That is a bookkeeping convention rather
  than a modelled schedule, so I do not treat it as a hard forecast — but it is the
  resolution agency's working assumption and it says both "no more drawdown" and "no 2026
  returns".
- **Physical constraints bound both tails.** GAO-26-106918: drawdown 2.7 of 4.415 Mb/d,
  fill 0.44 of 0.785 Mb/d, infrastructure held together "with Band-Aids". Fortune
  (2026-08-25) details upconing, salt creep and thermal shock. The SPR cannot move ±40 Mb
  in a quarter in the *upward* direction under any scenario.
- **A misconception worth correcting, including in the popular coverage.** Fortune and
  Hydrocarbon Processing describe 252.4 Mb as a hard statutory floor. CRS IN12542 is
  explicit that there is **no statutory minimum inventory level**; 252.4 Mb is the floor
  below which EPCA §161(h) *limited* drawdown authority may not be used, and the current
  programme runs on a severe-supply-interruption finding plus an IEP collective action —
  which is why DOE's own stated end-point of ~243 Mb sits below it. The US is also a net
  petroleum exporter, so the IEA 90-day reserve obligation does not bind. Do not model
  252.4 as a stop.
- **Disconfirming evidence I hunted for.** A hidden July/August tranche (none — and the
  observed cumulative draw leaves no room for one); an appropriated refill that would push
  the level up (the $20 bn request dates to March 2025 and is not enacted); a scheduled
  large return in Q4 (the 1 November date comes from a secondary source, not a DOE
  document, and EIA disagrees with it — this is the single weakest link in the forecast).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted), q31308 | 399,811,115 (IQR 364.8–429.3 Mb) | 2026-08-27 | n = 4; no update in 11 days |
| Metaculus Pro, q31308 | 400,242,449 | 2026-08-27 | **n = 1** |
| Metaculus gold medalists, q31308 | 399,811,115 | 2026-08-27 | n = 4; identical to the CP, i.e. the CP *is* the gold cohort here |
| EIA STEO `COSQPUS` (Aug-2026 vintage) | 284,803,000 | 2026-08-11 | the resolution agency's own baseline |
| Kalshi | no market | 2026-09-07 | `KXSPRMIN`/`KXSPR` return empty via the trade API |
| Polymarket | no live market | 2026-09-07 | only an expired "reserves fall to __ by June 5" event |
| Manifold — "SPR lowest value in 2026" | P(<250 Mb) 34.7%, P(<200 Mb) 18.3%, P(<150 Mb) 8.3% | 2026-09-07 | 12 bettors; the hi-res sibling violates monotonicity (P(>275) 53.6% vs P(>250) 50.9%) — heavily discounted |
| Manifold — "when will the SPR start increasing again" | 41% before Oct, 48% before Nov, 50% before Dec 2026 | 2026-09-07 | 6 bettors; agrees with a flat-to-slightly-up Q4 |
| Sentinel Team / Mantic / GJOpen / INFER | no matching question | 2026-09-07 | |

**Material disagreement, stated plainly.** I sit ~118 Mb below the community prediction
and ~118 Mb below the single Pro forecaster. Note that the CP and the gold cohort are the
*same number* here — four forecasters, all gold medalists, so there is no independent
cohort to triangulate against, and the last movement was 2026-08-27. A gap this size
against a Pro cohort normally means I have missed something; here it is checkable in one
click: **the SPR was already at 286.604 Mb on 2026-08-28**, and a return to 400 Mb by
December would require +114 Mb in four months against a maximum fill capability of
0.44 Mb/d (~53 Mb in four months, and that only if every site could receive
simultaneously). The cohorts' number is physically impossible, not merely optimistic.
These are pre-war forecasts on a low-traffic subquestion of a 13-part group. I am not
deferring.

My real disagreement is with **Manifold's 34.7% on the SPR dipping below 250 Mb at some
point in 2026** versus my 1.8% for December (and roughly 5% for any point in Q4). That is
play money, 12 bettors, and a contract shape with severe longshot bias — but it is the
only forecaster source that materially disagrees on the *tail*, so it is the one to watch
if the final tranche is re-offered.

### Scenarios

| # | Scenario | Weight | Implies (Mb) |
|---|---|---|---|
| 1 | Programme done, returns have not started, no new tranche (EIA STEO path) | 42% | 280–284 |
| 2 | Exchange returns begin on schedule from 1 Nov (Big Hill LE2 complete) | 25% | 285–294 |
| 3 | Final ~38 Mb tranche re-offered and partly executed before 31 Dec | 13% | 258–277 |
| 4 | FY27 mandated sale or other small net draw, returns still absent | 8% | 277–280 |
| 5 | Fresh escalation → releases beyond the 172 Mb programme | 7% | 250–270 |
| 6 | Material refill purchases, Venezuela swap barrels, or fast returns | 5% | 290–300 |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Returns begin 1 Nov with only 45% probability (Big Hill LE2 risk; EIA says July 2027) | Returns are contractually certain from 1 Nov at ~5 Mb/month | median ≈ 289 Mb, IQR [285, 293] |
| 13% chance the final ~38 Mb tranche delivers before 31 Dec | DOE re-offers in October and it clears like tranches 1–4 (~55% take-up) | median ≈ 268 Mb, IQR [258, 280] |
| No further escalation beyond the current war (7%) | Hormuz re-closes and a second IEA collective action is agreed | median ≈ 265 Mb, with a tail to 245 |
| September lands at 282.3 Mb | September lands at 278 Mb (award tally understated) | median ≈ 277.6 Mb, whole distribution shifts down ~4 Mb |

### What would change my mind (tripwires)

- [ ] **2026-11-15** DOE issues an RFP for the remaining ~38 Mb →
      **down ~8,000,000 barrels**
- [ ] **2026-11-30** such an RFP is awarded at **more than 15 Mb** →
      **down ~15,000,000 barrels**
- [ ] **2026-11-20** first week-on-week **build** in WCSSTUS1 on or before the week ending
      2026-11-13 (Big Hill returns started on schedule) → **up ~4,000,000 barrels**
- [ ] **2026-12-05** still no week-on-week build through the week ending 2026-12-04 →
      returns have slipped to 2027 → **up ~1,500,000 barrels** (mass onto the flat scenario)
- [ ] **2026-12-15** Strait of Hormuz re-closed, or a new IEA collective action announced →
      **down ~10,000,000 barrels**
- [ ] **2026-12-01** SPR refill appropriations enacted, or a Venezuela-swap contract signed
      with 2026 delivery dates → **up ~3,000,000 barrels**

### Sources

1. EIA, *Weekly U.S. Ending Stocks of Crude Oil in the SPR* (WCSSTUS1) — https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=WCSSTUS1&f=W (via api.eia.gov v2; accessed 2026-09-07; snapshot in `raw/`)
2. EIA, *U.S. Crude Oil Stocks in the SPR, Monthly* (MCSSTUS1) — https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCSSTUS1&f=M (accessed 2026-09-07; snapshot in `raw/`)
3. EIA, *Short-Term Energy Outlook*, series `COSQPUS` and `COSQ_DRAW` — https://www.eia.gov/outlooks/steo/ (accessed 2026-09-07; snapshot in `raw/`)
4. EIA, *Weekly Petroleum Status Report* schedule — https://www.eia.gov/petroleum/supply/weekly/ (accessed 2026-09-07)
5. Metaculus, question group 15240, aggregations for question ids 31307 and 31308 — https://www.metaculus.com/questions/15240/ (accessed 2026-09-07; snapshot in `raw/`)
6. DOE, *United States to Release 172 Million Barrels of Oil From the Strategic Petroleum Reserve* — https://www.energy.gov/articles/united-states-release-172-million-barrels-oil-strategic-petroleum-reserve (accessed 2026-09-07)
7. DOE, *Energy Department Initiates Additional SPR Emergency Exchange* (2026-04-01, 10 Mb, Bryan Mound) — https://www.energy.gov/hgeo/articles/energy-department-initiates-additional-strategic-petroleum-reserve-emergency-exchange (accessed 2026-09-07)
8. DOE, *Energy Department Awards Contracts for 8.5 Million Barrels from SPR in Second Phase of Emergency Exchange* — https://www.energy.gov/hgeo/opr/articles/energy-department-awards-contracts-85-million-barrels-spr-second-phase-emergency (accessed 2026-09-07)
9. DOE, *Energy Department Continues Initiating SPR Emergency Exchanges* (2026-04-09, 30 Mb, West Hackberry) — https://www.energy.gov/hgeo/opr/articles/energy-department-continues-initiating-strategic-petroleum-reserve-emergency (accessed 2026-09-07)
10. DOE, *Petroleum Reserves News* listing (most recent item 2026-07-09) — https://www.energy.gov/hgeo/opr/listings/petroleum-reserves-news (accessed 2026-09-07)
11. DOE, *SPR Quick Facts* (294.1 Mb as of 2026-08-20) — https://www.energy.gov/hgeo/opr/spr-quick-facts (accessed 2026-09-07)
12. S. A. Perera, *The Forty Million Barrels That Did Not Clear* — https://shanakaanslemperera.substack.com/p/the-forty-million-barrels-that-did (accessed 2026-09-07). Secondary analysis; source of the per-tranche take-up rates (53/85/87/58/1.25%).
13. Hydrocarbon Processing, *Depleted U.S. SPR loses potency as Iran war grinds on* (Aug 2026) — https://www.hydrocarbonprocessing.com/news/2026/08/depleted-us-spr-loses-potency-as-iran-war-grinds-on/ (accessed 2026-09-07). Source of the "final 39 Mb release → ~243 Mb" plan.
14. Fortune, *Less than 300 million barrels left: the engineering limits threatening the American SPR* (2026-08-25) — https://fortune.com/2026/08/25/strategic-petroleum-reserve-oil-energy-gas-hormuz/ (accessed 2026-09-07)
15. Congressional Research Service, IN12542, *Strategic Petroleum Reserve: Inventory Outlook and Policy Considerations* — https://www.congress.gov/crs-product/IN12542 (read via https://www.everycrsreport.com/reports/IN12542.html; accessed 2026-09-07)
16. GAO-26-106918, *Energy Security: Congress and DOE Need a Unified Plan to Align Priorities and Investments for the SPR* — https://files.gao.gov/reports/GAO-26-106918/index.html (accessed 2026-09-07)
17. Plainview Energy, *US Strategic Petroleum Reserve Deep Dive: Drawdowns and the 2026 Exchange Program* — https://www.plainview-energy.com/p/us-strategic-petroleum-reserve-deep (accessed 2026-09-07). Secondary; source of the "returns from 1 November 2026 at Big Hill" claim, **not independently verified against a DOE document**.
18. Al Jazeera, *IEA agrees to release 400 million barrels of oil from strategic reserves* (2026-03-11) — https://www.aljazeera.com/news/2026/3/11/iea-proposes-release-of-400m-barrels-of-oil-from-strategic-reserves (accessed 2026-09-07)
19. EnergyNow, *Oil Holds Near Five-Week Highs as U.S.-Iran Fighting Keeps Hormuz Risk Elevated* (Sept 2026) — https://energynow.com/2026/09/oil-holds-near-five-week-highs-as-u-s-iran-fighting-keeps-hormuz-risk-elevated/ (accessed 2026-09-07)
20. BOE Report / Reuters, *Venezuela's heavy crude could be swapped for American oil to fill emergency reserve, Wright says* (2026-09-03) — https://boereport.com/2026/09/03/venezuelas-heavy-crude-could-be-swapped-for-american-oil-to-fill-emergency-reserve-wright-says/ (accessed 2026-09-07)
21. Seeking Alpha, *Energy secretary to seek $20B to refill depleted U.S. strategic oil reserve* — https://seekingalpha.com/news/4418711-energy-secretary-to-seek-20b-to-refill-depleted-u_s_-strategic-oil-reserve (accessed 2026-09-07)
22. Manifold Markets, SPR markets (`us-strategic-petroleum-reserve-lowe`, `us-announces-another-drawdown-of-st`, `when-will-the-us-strategic-petroleu`) — https://manifold.markets/ (accessed 2026-09-07; snapshot in `raw/`)
23. Kalshi trade API, series `KXSPRMIN` / `KXSPR` / `SPR` — https://api.elections.kalshi.com/trade-api/v2/markets (accessed 2026-09-07; empty, no SPR-level market)
24. Wikipedia, *2026–2028 world oil market chronology* — https://en.wikipedia.org/wiki/2026%E2%80%932028_world_oil_market_chronology (accessed 2026-09-07; used only for the dated price/event skeleton)

**Date**: 2026-09-07
**Forecast**: Median 281,900,000 barrels, IQR [278,300,000, 285,200,000]
**Thesis**: The 172-Mb IEA-coordinated exchange has awarded only 133.5 Mb and delivered 128.8 Mb of it by 2026-08-28, so the drawdown exhausts itself in September at ~282 Mb and Q4 is a plateau, not a trend — which is also EIA's own STEO assumption (flat 284.8 Mb through June 2027). The forecast is really about two tails: a 45% chance exchange returns start at Big Hill on the contractual 1 November date (+6 Mb) against a 13% chance DOE finally places the un-awarded ~38.5 Mb after its 2026-06-10 tranche drew a single 0.5 Mb bid. The Metaculus cohorts near 400 Mb are pre-war forecasts and are physically unreachable at DOE's 0.44 Mb/d fill capability.
