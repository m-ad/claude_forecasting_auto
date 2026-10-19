# What will be the closing level of South Korea's KOSPI index on October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46126/ |
| **Tournament** | minibench — one shot, window 2026-10-19T00:46:02Z -> 2026-10-19T03:46:02Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 5620, IQR [5310, 5930] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the "Close" value of the KOSPI Composite Index (^KS11) in the Oct 29, 2026 row of Yahoo Finance's historical data page. That is the plain price index in points, not dividend-adjusted. If Oct 29 is not a Korea Exchange trading day, the most recent prior close counts. If Yahoo does not report it, Investing.com or the KRX figure is used. Oct 29, 2026 is a Thursday and not a Korean holiday, so it should be a normal trading day. The scale runs from 4,500 to 7,200, and both bounds are open: values outside the range are possible and still count.

### Outside view

For a stock index over a short horizon, the best prior is a random walk from the current level, with the spread set by recent volatility. The horizon is the rest of Oct 19 plus 8 more sessions (Oct 20–23 and 26–29), about 8.5 trading days. KOSPI's 2026 volatility has been extreme:
- About 9,100 at the June peak, with several moves of 5–10% in a single day in June [4].
- Fell to about 5,660 on Jul 29, after an intraday drop of 12.6% [3].
- Back to about 7,000 by early October [1].
- About 5,600 now [1].

Recent daily moves of 2–7% suggest a daily volatility of roughly 3–3.5%, against about 1% in normal years. Over 8.5 sessions that gives a 1-sigma spread in log terms of about 9–10%.

### Inside view

- **Starting point:** the live Yahoo quote is 5,606.91 at 09:51 KST on Oct 19, down 1.08% on the day [1].
- **No drift.** There are arguments both ways. A rebound after capitulation is plausible: the circuit breaker fired on Oct 15, and Samsung's earnings were at a record [2]. Against that, the sell-off that started in mid-October is driven by fears of an AI bubble and still has momentum [2]. Neither case is strong enough to beat a random walk. I set the median at about 5,620, a hair above spot, to allow for slight mean reversion after a −20% month.
- **Spread:** a daily volatility of about 3.2% over 8.5 sessions gives σ ≈ 9.3%. Under a normal distribution that implies an IQR of about ±6.3%. I keep the IQR close to that, at 5,310–5,930.
- **Tails:** this year has produced several days of ±8–10%, so I make the tails fat. The 5–95% range is 4,800–6,450.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| KOSPI close | 4,800 | 5,000 | 5,310 | 5,620 | 5,930 | 6,250 | 6,450 |

### Evidence

- Yahoo Finance ^KS11 closes [1], retrieved 2026-10-19:

  | Date | Close |
  |---|---|
  | Oct 2 | 7,003.74 |
  | Oct 6 | 6,941.39 |
  | Oct 7 | 6,803.90 |
  | Oct 8 | 6,625.93 |
  | Oct 12 | 6,384.24 |
  | Oct 13 | 6,035.35 |
  | Oct 14 | 6,008.81 |
  | Oct 15 | 5,554.22 |
  | Oct 16 | 5,668.05 |
  | Oct 19 (intraday, 09:51 KST) | about 5,607 |

  Yahoo shows 5,668.05 for Oct 16, while the question text says 5,655.34; Yahoo is the resolution source.
- On Oct 15 the index opened down 5.6%, which triggered the "sell-sidecar" (a 5-minute pause in program selling), and then the circuit breaker fired [2].
- Jul 29, 2026: intraday low of 5,262.77 (−12.6%), close 5,663.24 [3]. June 2026: daily moves of −10%, +8% and −5.8% around the 8,000–9,000 level [4][5].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no market on the KOSPI level for this date |

### What would change my mind

- **A volatility regime change.** If the chip sell-off ends quickly, for example because US semiconductor stocks stabilise, daily volatility could fall back toward 1.5% and the distribution would be too wide. A second circuit-breaker cascade like July's would instead push the close below 5,000.
- **News on SK hynix and Samsung**, which dominate the index weight, including any announcement on buybacks or a dual listing.

### Sources

1. Yahoo Finance, KOSPI Composite Index (^KS11) historical data — https://finance.yahoo.com/quote/%5EKS11/history/ (accessed 2026-10-19)
2. Asia Business Daily, "KOSPI, KOSDAQ Open Down More Than 5%, Triggering Sell-Sidecars" — https://view.asiae.co.kr/en/article/2026101509331727846 (accessed 2026-10-19)
3. Korea Herald, "Benchmark tumbles nearly 13%, triggering circuit breaker for second straight day" (Jul 29, 2026) — https://www.koreaherald.com/article/10824514 (accessed 2026-10-19)
4. Korea JoongAng Daily, "Kospi tumbles nearly 10% following massive tech sell-offs" — https://www.koreajoongangdaily.com/business/kospi-tumbles-nearly-10-following-massive-tech-selloffs/12737002 (accessed 2026-10-19)
5. Korea Times, "KOSPI retakes 8,000 mark as chip stocks lead sharp rebound" — https://www.koreatimes.co.kr/amp/economy/others/20260609/kospi-retakes-8000-mark-as-chip-stocks-lead-sharp-rebound (accessed 2026-10-19)
6. Asia Business Daily, "KOSPI Opens at 6,578.17, Down 47.76 Points (0.72%)" (Oct 12, 2026) — https://view.asiae.co.kr/en/article/2026101209010181223 (accessed 2026-10-19)

**Question**: [What will be the closing level of South Korea's KOSPI index on October 29, 2026?](https://www.metaculus.com/questions/46126/)
**Date**: 2026-10-19
**Forecast**: Median 5620, IQR [5310, 5930]
**Thesis**: I treat the index as a random walk from the live level of about 5,607 on Oct 19 (Yahoo Finance) over about 8.5 sessions. The spread comes from 2026's extreme volatility, roughly 3.2% a day after the chip sell-off and circuit breaker on Oct 15. The forecast is most sensitive to whether that volatility persists or fades.
