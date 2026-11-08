# What will net outlays by the US government be in millions of dollars in FY 2028?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46224/ |
| **Tournament** | bot-testing-area — one shot, window 2026-10-17T06:00:00Z -> 2028-10-01T03:59:00Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-17 / 2028-10-01 / 2028-10-20 |
| **Status** | open |
| **Current forecast** | Median 8,180,000, IQR [8,020,000, 8,350,000] (v1, 2026-11-08) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-08

### What resolves YES

The question resolves to the first FRED print of series FYONET (Federal Net Outlays, $ millions, annual fiscal year) for FY2028, i.e. 1 Oct 2027 – 30 Sep 2028. FRED's first print tracks the September Monthly Treasury Statement (MTS), released mid-October 2028. For example, FRED showed FY2025 as 7,009,974 in October 2025, revised to 7,011,105 in April 2026; that revision is ~0.02%, so it does not matter here. The latest actual is the September 2026 MTS: FY2026 = 7,395,800 (+5.5% on FY2025's 7,009,986) [2]. That leaves two fiscal years to project (FY2027, FY2028). Calendar check: 1 Oct 2028 is a Sunday, so roughly $118B of October-2028 mandatory payments is paid in late September and counted in FY2028 [4]. That inflates the resolving number. The bounds (4.0M–10.0M) are open and far from the plausible range.

### Outside view

Reference: the CBO February 2026 baseline. It projects 2026 = $7.45T and 2027 = $7.77T [1]. For 2028 it gives revenue of $6.1T (17.5% of GDP) and a deficit of 6.0% of GDP, which is just over $2T [1][5]. Together these imply outlays of about $8.15–8.2T, timing shift included. Historical CBO error on total outlays is about 2.3% mean absolute error (MAE) in the budget year, larger further out. Recent misses were −6% (FY2024) and −2% (FY2025), both underestimates [7]. At a 2-year horizon I take a standard deviation of about 3%, roughly ±$250B.

### Inside view

- FY2026 came in at $7.396T, about 0.7% below CBO's February projection [1][2]. I carry that small undershoot forward: about −$55B.
- Nominal growth in recent years has been 5.5–6% a year. Running FY2026 forward at 5% a year, plus the ~$118B shift, gives 7.396 × 1.05² + 0.12 ≈ 8.27T. Running it at 4% a year gives ≈ 8.12T. This brackets the CBO-implied figure.
- Upside skew comes from the President's FY2027 request: $1.5T for defense, including $350B through reconciliation. That would raise defense from 3.0% to about 3.7% of GDP by 2028 (CSIS) [6]. It was not enacted in the sources I found, and CBO notes that laws passed since February *reduced* discretionary projections [8].
- Also on the upside: a recession in 2027–28 (markets price about 35–41% for 2027 [9]), which would raise unemployment-insurance and safety-net spending, and higher interest rates.
- Downside: CBO's historical tendency to overestimate outlays, rescissions, and slower inflation.
- The IEEPA tariff refunds fall mainly on receipts in FY2026–27 and should not touch FY2028 [7].
- Median 8.18M; the right tail is wider than the left.

### Evidence

- FY2026 outlays were 7,395,800 $M (MTS, September 2026, released 16 October 2026) [2][3].
- CBO February 2026: outlays of 23.3% of GDP, holding near that level through 2028; $7.77T in 2027 [1].
- CBO: ~$118B of mandatory outlays shifts from FY2029 into FY2028 [4].
- FY2026 net interest was about $1.05–1.14T, up 8–11%, the fastest-growing component [10].
- The President's FY2027 budget proposes a $1.5T defense topline [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-08 | |
| CBO baseline (implied) | ~$8.15–8.2T | Feb 2026 | revenue + deficit for 2028, shift included |
| Kalshi / Polymarket | none on FY2028 outlay level | 2026-11-08 | Kalshi "spending cut before 2028" is a different question |

### What would change my mind

- A recession starting in 2027 would push the result toward 8.5M or more.
- Enacting the $350B defense reconciliation plus the $1.15T discretionary request would add about $100–200B to FY2028.
- A large rescissions package, or a sharp drop in interest rates, would pull toward 7.9M.
- A CBO re-baseline (expected around January–February 2027) would update the anchor.

### Sources

1. CBO, The Budget and Economic Outlook: 2026 to 2036, https://www.cbo.gov/publication/62105 and By the Numbers https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf (accessed 2026-11-08, via search summaries)
2. Treasury, Final Monthly Treasury Statement FY2026, https://fiscaldata.treasury.gov/static-data/published-reports/mts/MonthlyTreasuryStatement_202609.pdf (accessed 2026-11-08)
3. CBO Monthly Budget Review: September 2026, https://www.cbo.gov/system/files/2026-10/61985-MBR.pdf (accessed 2026-11-08)
4. CBO on timing shifts in the 2026–2036 outlook, https://www.cbo.gov/publication/62105 (accessed 2026-11-08)
5. CRFB, CBO's February 2026 Budget and Economic Outlook, https://www.crfb.org/papers/cbos-february-2026-budget-and-economic-outlook (accessed 2026-11-08)
6. CSIS, Unpacking the $1.5 Trillion FY 2027 Defense Budget Topline, https://www.csis.org/analysis/unpacking-15-trillion-fy-2027-defense-budget-topline (accessed 2026-11-08)
7. CBO evaluations of projections, https://www.cbo.gov/publication/59110 (snippets); tariff refunds, https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/ (accessed 2026-11-08)
8. CBO, President's 2027 budget analysis (June 2026), https://www.cbo.gov/system/files/2026-06/62385-presidents-budget.pdf (accessed 2026-11-08, snippet)
9. Yahoo Finance, Wall Street sees recession risk fading in 2026, but 2027 flashing warning signs, https://finance.yahoo.com/economy/articles/wall-street-sees-recession-risk-141240798.html (accessed 2026-11-08)
10. Fortune, US debt interest payments, fiscal 2026, https://fortune.com/2026/10/17/us-debt-interest-payments-fiscal-2026-1-trillion-federal-spending-revenue-gdp-growth-treasury-yields/ (accessed 2026-11-08)
11. FRED, FYONET, https://fred.stlouisfed.org/series/FYONET (accessed 2026-11-08)

**Question**: [What will net outlays by the US government be in millions of dollars in FY 2028?](https://www.metaculus.com/questions/46224/)
**Date**: 2026-11-08
**Forecast**: Median 8,180,000, IQR [8,020,000, 8,350,000]
**Thesis**: FY2026 outlays were $7.396T (Treasury MTS). CBO's February 2026 baseline implies about $8.15–8.2T for FY2028, which includes about $118B of payments pulled into FY2028 because 1 Oct 2028 is a Sunday. I trim slightly for FY2026's undershoot of CBO and skew the tails upward for a possible 2027–28 recession and the pending defense buildup.
