# What will CoreWeave (CRWV) stock close at on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46127/ |
| **Tournament** | minibench — one shot, window 2026-10-19T01:52:09Z -> 2026-10-19T04:52:09Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 61, IQR [52.1, 71.5] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the regular-session (4:00 PM ET) closing price of CoreWeave Class A stock (Nasdaq: CRWV) on Thursday, October 29, 2026, in US dollars, as shown on Yahoo Finance's CRWV historical-data page. Credible other sources are used if Yahoo is unavailable. After-hours prices do not count. Both bounds are open: the $35–$105 range is only the plotting range, and a close outside it still resolves at its actual value. From the Friday, October 16 close, that leaves 9 trading sessions (Oct 19–23 and Oct 26–29).

### Outside view

For a liquid stock over a short horizon, the best prior is a random walk: the median equals the last close and the spread scales with volatility × √time. The last close is Friday, October 16. Yahoo's history page shows $61.39 [1], while the question text says $60.24. I anchor at about $61. CRWV has long traded at roughly 80–120% annualised realised volatility, and in the past week it moved −15.5%, +6% and −13.6% in a day [1][2]. That implies a current regime well above 100%. I assume about 120% annualised. Over 9 sessions that gives a log-sigma of 1.2 × √(9/252) ≈ 0.23. I widen it to about 0.24 with Student-t-like tails, because the stock is in a credit-stress episode.

### Inside view

- **Credit stress is the driver.** The 2032 unsecured notes touched a 15% yield and traded below 80 cents on the dollar after a venture capitalist's post on X on October 13. Five-year credit default swaps (CDS, insurance against default) hit a record of roughly 1,140–1,195 basis points [2][3]. The bonds rebounded partly on October 15, with the 2031s at 82.8 and the 2030s at 91.3 [3]. The stock still fell another ~12–14% on October 16.
- **The two sides roughly cancel.** Upward forces: short covering after an ~$806M short-seller paper profit [4], the CEO's memo pointing to the ~$104B backlog [2], and sell-side calls of an "overblown" move (Deutsche Bank target $150). Downward forces: momentum, a possible need for new financing, and contagion across AI infrastructure (Oracle −8.8%, Dell −11% on October 14) [2]. I do not tilt the median and keep it at the last close (~$61).
- **Catalysts in the window.** CoreWeave's own earnings come around November 11, after resolution. Big-tech earnings, where hyperscaler capital-spending guidance matters for AI-infrastructure sentiment, usually fall in the last week of October and may land just before or on October 29 (speculation: dates not verified this session). That keeps both tails fat.
- **Model.** A log-t-like distribution around $61 with sigma ≈ 0.24 gives p5 $40.1, p10 $44.3, p25 $52.1, p50 $61.0, p75 $71.5, p90 $83.9, p95 $92.8. It is right-skewed in dollars, as a log model implies.

### Evidence

- Yahoo Finance closes (accessed 2026-10-19): Oct 5 $87.39, Oct 6 $91.72, Oct 7 $88.45, Oct 8 $81.58, Oct 9 $82.08, Oct 12 $80.26, Oct 13 $77.81, Oct 14 $65.78, Oct 15 $69.69, Oct 16 $61.39 [1]. The question background gives $60.24 for October 16; the gap is unresolved, and I use about $61.
- October 14: CRWV −15.5%. The bonds briefly yielded more than 15% and traded below 80 cents on the dollar. CDS reached a record of roughly 1,194.5 basis points [2].
- October 15: the bonds rebounded sharply. The October 2031 notes rose to 82.8 and the June 2030 notes to 91.3 [3].
- October 16: short sellers held about $806M in paper profit as credit stress continued [4].
- Background: CoreWeave has raised about $20B of capital in 2026 [5], and a $1.5B refinancing bond sale was reported earlier [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Options-implied volatility | not retrieved | — | not checked within the time budget |
| Polymarket / Kalshi | none found | 2026-10-19 | no matching market searched successfully |

### What would change my mind

- A financing event (a new equity raise or convertible, or a distressed exchange) would shift the median down 10–20%. A strong refinancing or a backstop from a large customer or partner (e.g. Nvidia) would shift it up by a similar amount.
- Hyperscaler capital-spending guidance in late October: a cut would push the stock toward the lower tail.
- The October 16 close discrepancy ($60.24 vs $61.39) moves the centre by only about 2%. It is immaterial next to a sigma of about 24%.

### Sources

1. Yahoo Finance, CRWV historical data — https://finance.yahoo.com/quote/CRWV/history/ (accessed 2026-10-19)
2. Stock Alarm, "CoreWeave Shares Drop 15% Amid Concerns Over AI Borrowing Binge" — https://pro.stockalarm.io/news/coreweave-shares-drop-15-amid-concerns-over-ai-borrowing-binge-16848e1d (accessed 2026-10-19, via search summary)
3. ROIC.ai, "CoreWeave bonds rebound sharply after recent selloff" (2026-10-15) — https://www.roic.ai/news/coreweave-bonds-rebound-sharply-after-recent-selloff-10-15-2026 (accessed 2026-10-19, via search summary)
4. ROIC.ai, "CoreWeave short sellers score $806 million paper profit…" (2026-10-16) — https://www.roic.ai/news/coreweave-short-sellers-score-806-million-paper-profit-as-debt-fueled-ai-expansion-faces-credit-stress-10-16-2026 (accessed 2026-10-19, via search summary; page returned 403)
5. Yahoo Finance, "CoreWeave Has Raised $20 Billion in Capital This Year" — https://finance.yahoo.com/markets/stocks/articles/coreweave-raised-20-billion-capital-144406639.html (accessed 2026-10-19, via search summary)
6. DatacenterDynamics, "CoreWeave plans $1.5bn bond sale to refinance debt" — https://www.datacenterdynamics.com/en/news/coreweave-plans-15bn-bond-sale-to-refinance-debt/ (accessed 2026-10-19, via search summary)
7. Let's Data Science, "CoreWeave debt: 60 percent default odds, $104 billion backlog" — https://letsdatascience.com/blog/coreweave-debt-60-percent-default-odds-104-billion-backlog (accessed 2026-10-19, via search summary)

**Question**: [What will CoreWeave (CRWV) stock close at on October 29, 2026?](https://www.metaculus.com/questions/46127/)
**Date**: 2026-10-19
**Forecast**: Median $61.0, IQR [$52.1, $71.5]
**Thesis**: A random walk from the ~$61 October 16 close (Yahoo Finance), 9 sessions out, with about 120% annualised volatility and fat tails, because the stock is in a credit-stress episode (2032 bonds near a 15% yield, record CDS). Short-covering and "overblown" calls roughly offset financing and contagion risk, so the median is not tilted. The forecast is most sensitive to any new financing or distress news before October 29.
