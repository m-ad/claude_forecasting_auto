# What will be Donald Trump's net approval on December 31, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/43323/ |
| **Tournament** | bot-testing-area — one shot, window 2026-04-27T15:03:00Z -> 2026-12-31T00:00:00Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-04-27 / 2026-12-31 / 2027-01-01 |
| **Status** | open |
| **Current forecast** | Median -22, IQR [-24.6, -19.4] (v1, 2026-10-18) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-18

### What resolves YES

The question resolves to Donald Trump's net approval (approve minus disapprove, in percentage points, so negative values) on 31 December 2026 per the Silver Bulletin average (natesilver.net). If that day is not published, the latest available December day is used; if Silver Bulletin stops publishing, the question is annulled. Bounds are open: range -35 to 0, with tail mass allowed outside.

### Outside view

Reference class: change in the Silver Bulletin net approval over a ~75-day horizon. In Trump's second term the average has drifted from about +12 (Jan 2025) to about -22 (Oct 2026), with typical 2.5-month moves of 2-5 points and rare moves above 7. In his first term it stayed within roughly ±4 points over similar spans. So the status quo (-22.3) with an SD of about 3.5-4 points is the base distribution. These volatility figures are my judgement; I did not compute them from the series.

### Inside view

The latest value is -22.3 (16 Oct 2026), just off an all-time low of -23.9 reached the weekend before. After a record low, mild mean reversion is plausible, but the 2026 trend has been downward (second-term low -20.6 on 31 Jul, -23.9 in Oct) and issue approval is poor (economy -32.9, inflation -48.9). The 3 Nov midterms fall in the window and could cut either way. I put the median at -22.0, essentially the status quo, with slightly more weight on a rebound than on a further decline, and a wide distribution (SD about 4) to cover unknown shocks. No quantitative model was run.

### Evidence

- Silver Bulletin: net approval -22.3 as of 16 Oct 2026; all-time low -23.9 days earlier; new polls TIPP (-13) and Noble Predictive (-12) pulled it up [1].
- Wikipedia polling table: Silver Bulletin 36.6% approve / 60.5% disapprove / net -23.9 on 8 Oct 2026 [2].
- Manifold market on the Silver Bulletin average cited -21.9 on 8 Oct and a low of -23.5 [3]. This is inconsistent with [2], probably because of capture time or revisions.
- Earlier second-term low -20.6 on 31 Jul 2026 [1]: the series fell about 2-3 points in 2.5 months.
- Kalshi VoteHub-based approval brackets (late June 2026 snapshot) cluster in the mid-30s, consistent with a stable low level [4].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-18 | |
| Kalshi (VoteHub approval year brackets) | approval mid-30s | June 2026 | different source, thin liquidity |
| Manifold (Election Day Silver Bulletin net) | about -22 | 2026-10-08 | play money, discounted |

### What would change my mind

A sustained move of the Silver Bulletin average away from -22 before year end (a rebound to -18 or a break below -26), or a major shock (war, recession, health event). The forecast is most sensitive to where the average sits in mid-December.

### Sources

1. https://www.natesilver.net/p/trump-approval-ratings-nate-silver-bulletin (accessed 2026-10-18)
2. https://en.wikipedia.org/wiki/Opinion_polling_on_the_second_Trump_presidency (accessed 2026-10-18, via search snippet)
3. https://manifold.markets/Terminator2/what-will-trumps-net-approval-be-in (accessed 2026-10-18, via search snippet)
4. https://simplefunctions.dev/odds/trumpapprovalyear (accessed 2026-10-18, via search snippet)
5. https://www.newsweek.com/trumps-pre-midterm-approval-rating-compared-to-biden-obama-and-bush-12304156 (accessed 2026-10-18, via search snippet)

**Question**: [What will be Donald Trump's net approval on December 31, 2026?](https://www.metaculus.com/questions/43323/)
**Date**: 2026-10-18
**Forecast**: Median -22.0%, IQR [-24.6%, -19.4%]
**Thesis**: Status-quo anchor on the Silver Bulletin net approval of -22.3 (16 Oct 2026), near a record low, with a ~4-point SD over 75 days for midterm and other shocks. Most sensitive to the level of the average in mid-December.
