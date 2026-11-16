# What will SpaceX's (SPCX) closing share price be on Friday, November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46595/ |
| **Tournament** | minibench — one shot, window 2026-11-16T17:42:04Z -> 2026-11-16T20:42:04Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | open |
| **Current forecast** | Median 137, IQR [128, 146.5] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the official regular-session close of SPCX (Nasdaq) on Friday, 2026-11-27, as shown in the "Close" column of Yahoo Finance's SPCX history page. That day is a half session: the market closes at 1:00 p.m. ET, and after-hours trades do not count. If no close is reported that day, the most recent prior close is used. The scale runs from $95 to $190 with both bounds open. **Arithmetic:** the latest value is $138.28 intraday at 2:09 p.m. ET on Mon 2026-11-16 [1]; Fri Nov 13 closed at $139.11 [1]. The question text says $136.99, but Yahoo shows $139.11 and Yahoo is the resolution source. From today's close to the target there are **8 trading sessions**: Nov 17, 18, 19, 20, 23, 24, 25 and 27 (Nov 26 is Thanksgiving), plus the rest of today, about 9 sessions of risk in all. The Dec 8 lock-up expiry falls after the resolution date.

### Outside view

The reference class is a random walk from spot with this stock's own volatility. Over its last 9 sessions [1] the daily log returns had a standard deviation of about 5%. That window includes the −9.5% day on Nov 5 and the +8.3% day on Nov 6. Option implied volatility in October was about 55–62% a year (≈3.5–3.9% a day) [5]. I use about 3.9% a day, which over ~8.5 sessions gives a σ of about 11.5% in log terms, with fat tails (Student-t-like). Centred on $138, that gives an IQR of about ±7% and a 5–95% range of about −19% to +20%.

### Inside view

- **Drift.** I cut the median by about 1%, to $137, for the Dec 8 unlock overhang. That tranche is 342–798M shares, against a float that rises to about 40% [3][4], and the academic literature finds a small negative abnormal return before lock-up expiry (≈−1%) [6]. I keep the cut small because the August unlock was followed by a +26–35% squeeze [8].
- **Starship Flight 15.** I could not find its outcome. Today's session is flat (−0.6%), so whatever happened is already in the price.
- **Upper tail.** I keep it a little fatter than the lower one, because the float is small, short interest has run high and past squeezes have been violent [8]. Analyst targets average $220–$245 [7], but they carry little weight over 8 sessions.
- **Half session.** The Nov 27 session is shortened and thin. It adds a little variance, which is already inside the fat tails.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| $ | 112 | 118.5 | 128 | 137 | 146.5 | 158 | 166 |

### Evidence

- Yahoo SPCX history (accessed 2026-11-16) [1]:

  | Date | Close ($) |
  |---|---|
  | Nov 3 | 141.31 |
  | Nov 4 | 135.92 |
  | Nov 5 | 123.62 |
  | Nov 6 | 134.27 |
  | Nov 9 | 142.07 |
  | Nov 10 | 143.09 |
  | Nov 11 | 139.75 |
  | Nov 12 | 139.94 |
  | Nov 13 | 139.11 |
  | Nov 16 (intraday) | 138.28 |

  Daily volume ran 67–171M shares.
- **Lock-up.** The Dec 8 unlock is 342–798M shares, depending on whether a price-test tranche rolls in [3][4]. A 1.3bn-share unlock on Oct 22 coincided with the slide to $134.72 on Oct 30 [9].
- **S&P 500.** S&P denied SpaceX fast-track entry, and inclusion is not expected before mid-2027 [10].
- **Analysts.** Citi initiated at Buy with a $200 target and Stifel reiterated $190 in November [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket, SpaceX market cap at end of November | $1.75–2.00T bucket leads at 33% | 2026-11-16 | Only about $1.8K traded, so thin. The bucket is roughly $127–145/share at ~$1.9T ≈ $137. |
| Manifold, "SPCX < $100 by Dec 31" | 82% | undated | Play money, low volume, and the snapshot looks stale. Discounted heavily. |
| Options implied volatility | ~55–62% annualised | Oct 2026 | 8-session 1σ ≈ ±10–11% |

### What would change my mind

- Evidence of heavy pre-unlock selling, such as a block trade or a secondary offering announced before Nov 27, would pull the median down 5–10%.
- A big Starship result or a squeeze that pushes the stock decisively above $150 would move the median up. Neither is visible in today's flat tape.

### Sources

1. https://finance.yahoo.com/quote/SPCX/history/ (accessed 2026-11-16)
2. https://www.nasdaqtrader.com/trader.aspx?id=calendar (accessed 2026-11-16; cited from the question text, not fetched)
3. https://www.nasdaq.com/articles/spacex-stock-3-things-watch-december-lock-cliff (accessed 2026-11-16; search snippet)
4. https://protos.com/spacexs-biggest-stock-unlocks-are-still-ahead/ (accessed 2026-11-16; search snippet)
5. https://marketchameleon.com/Overview/SPCX/OptionChain (accessed 2026-11-16; search snippet)
6. https://thesis.eur.nl/pub/60187/Bachelor-Thesis-Final-Version-498076ll.pdf (accessed 2026-11-16; search snippet)
7. https://www.marketbeat.com/stocks/NASDAQ/SPCX/forecast/ (accessed 2026-11-16; search snippet)
8. https://247wallst.com/investing/2026/08/10/up-26-spacex-briefly-breaks-above-ipo-price-fundamental-turnaround-or-short-squeeze/ (accessed 2026-11-16; search snippet)
9. https://www.fool.com/investing/2026/06/27/why-spacex-stock-plummeted-this-week/ (accessed 2026-11-16; search snippet)
10. https://www.streetinsider.com/Reuters/Why+SpaceX+faces+a+longer+wait+to+join+S%26P+500/26609997.html (accessed 2026-11-16; search snippet)
11. https://polymarkets.co.il/en/market/spacexs-market-cap-end-of-november-2026/ (accessed 2026-11-16; search snippet)

**Question**: [What will SpaceX's (SPCX) closing share price be on Friday, November 27, 2026?](https://www.metaculus.com/questions/46595/)
**Date**: 2026-11-16
**Forecast**: Median 137.0 $, IQR [128.0 $, 146.5 $]
**Thesis**: This is a random walk from the Nov 16 intraday price of $138.3 (Yahoo) over 8 sessions, at about 4% daily volatility, which matches realized volatility and the ~55–60% implied volatility. The median is shaded down about 1% for the Dec 8 lock-up overhang, and both tails are fat because single-day moves of 6–10% recur in this stock.
