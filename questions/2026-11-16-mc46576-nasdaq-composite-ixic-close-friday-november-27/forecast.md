# What will the Nasdaq Composite (^IXIC) close at on Friday, November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46576/ |
| **Tournament** | minibench — one shot, window 2026-11-16T07:02:53Z -> 2026-11-16T10:02:53Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 24950, IQR [24200, 25700] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the "Close" value that Yahoo Finance's ^IXIC history table shows for Nov 27, 2026. That day is the shortened post-Thanksgiving session, which ends at 1:00 p.m. ET. If Yahoo has no value, Nasdaq's COMP history page is used instead. If the session does not happen, the question is annulled. The bounds of 21,000 and 29,000 are both open. The last known close is 24,922.08 on Fri Nov 13, 2026, taken from the question text, which cites Nasdaq [1]. From that close to the target there are **9 trading sessions**: Nov 16–20 (5), Nov 23–25 (3) and Nov 27 (1). Nov 26 is the Thanksgiving closure. At 27% annualised volatility, one standard deviation over 9 sessions is about 27% × √(9/252) ≈ 5.1%, roughly ±1,270 points.

### Outside view

I treat the index as a random walk from the last close, 24,922, with roughly zero drift over two weeks. The Nasdaq Composite's long-run annualised volatility is about 20–25%. V-Lab's GARCH model gave about 27% in mid-2026 [6]. Volatility right now is above normal. On Nov 5 the index fell 5.52% to 24,315, which put it about 12% below its record close of 27,477 on Oct 5 [2][3]. The VIX (the S&P 500 implied-volatility index) closed at 28.2 on Nov 5 and has since eased to about 17.5–20 [4]. Two-week index returns have fat tails, so the outer percentiles should be wider than a normal distribution would give.

### Inside view

- **Events inside the window.** Nvidia's fiscal Q3 results are expected after the close on Nov 17 or 18 (the date is unconfirmed) [7]. Its CEO resigned on Nov 12. Anthropic's IPO is set to price on Nov 18 and start trading on Nov 19 as ANT, at about $70–78 a share and up to $64.4B raised [8]. Q3 GDP and October PCE inflation come out on Nov 25 [9]. Markets price a Fed hike in December. Each of these can move the index 1–3% in a day. They widen the distribution but do not tilt it in a known direction.
- **Drift.** Seasonality around Thanksgiving is mildly positive: the Wednesday before has averaged +0.54% [5]. After a correction there is some mean-reversion potential, and there is also momentum and rate pressure from a 10-year yield near 5.1%. I set the median at 24,950, about +0.1%.
- **Spread.** I use a 9-session standard deviation of about 5%, with fat tails, mild left skew and a slightly narrow middle. Percentiles: p25 and p75 at ∓3.0%, p10 and p90 at −6.0% and +5.9%, p5 and p95 at −8.4% and +7.7%. The left tail is a bit heavier because the market is in correction with a hawkish Fed.
- I found no information on weekend futures for Nov 16. That is a gap.

### Evidence

- Recent closes: Nov 3 at 25,365.67, Nov 4 at about 25,912, Nov 5 at 24,315 (−5.52%), Nov 11 at about 25,500, Nov 12 at 25,366.09 and Nov 13 at 24,922.08 [1][2][10].
- The VIX was 28.18 on Nov 5, 25.64 on Nov 6, 19.92 on Nov 9 and 17.49 on Nov 11 [4][1].
- The Fed funds target range is 3.75–4.00% after a September hike. Odds of a December hike were 68% on Nov 5 [3].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-16 | |
| Kalshi / Polymarket | no Nov 27 Composite contract found | 2026-11-16 | Kalshi has only year-end Nasdaq-100 markets |
| Options-implied | not retrieved | 2026-11-16 | I used the VIX as a proxy |

### What would change my mind

- How Nvidia's earnings land and how Anthropic trades on its debut, both in the window's first week. A move of ±5% in the mega-caps would shift the whole distribution.
- Any sign that the Fed will hike by 50bp (0.50 percentage points) instead of 25bp, which would push the left tail out further.

### Sources

1. Metaculus question text, citing Nasdaq COMP overview: https://indexes.nasdaq.com/Index/Overview/COMP (accessed 2026-11-16)
2. FourWeekMBA / IBTimes, Nov 5 2026 selloff: https://www.ibtimes.co.uk/nvidia-qualcomm-shares-nasdaq-ai-selloff-1830635 (accessed 2026-11-16)
3. BeInCrypto, Nasdaq correction and odds of a Fed hike: https://beincrypto.com/nasdaq-correction-rebound-fed-rate-hike/ (accessed 2026-11-16)
4. FRED VIXCLS: https://fred.stlouisfed.org/series/VIXCLS (accessed 2026-11-16)
5. FOREX.com/StoneX, Nasdaq 100 seasonality around Thanksgiving: https://www.forex.com/en-uk/news-and-analysis/nasdaq-100-outlook-thanksgiving-seasonality-and-volatility-trends/ (accessed 2026-11-16)
6. NYU V-Lab, Nasdaq Composite GJR-GARCH: https://vlab.stern.nyu.edu/volatility/VOL.CCMP:IND-R.GJR-GARCH (accessed 2026-11-16)
7. The Right Trader, NVDA earnings calendar: https://therighttrader.com/earnings-calendar/nvda (accessed 2026-11-16)
8. The Next Web, terms of the Anthropic IPO: https://thenextweb.com/news/anthropic-ipo-terms-1-4-trillion-valuation (accessed 2026-11-16)
9. Finance Calendar, BEA PCE/GDP release on Nov 25 2026: https://www.financecalendar.com/events/2026-11-25/ (accessed 2026-11-16)
10. Honolulu Star-Advertiser, record close on Oct 5 2026: https://www.staradvertiser.com/2026/10/05/breaking-news/nasdaq-notches-record-high-close-as-investors-focus-on-earnings/ (accessed 2026-11-16)

**Question**: [What will the Nasdaq Composite (^IXIC) close at on Friday, November 27, 2026?](https://www.metaculus.com/questions/46576/)
**Date**: 2026-11-16
**Forecast**: Median 24950, IQR [24200, 25700]
**Thesis**: The forecast is a random walk from the Nov 13 close of 24,922, nine sessions out, with a standard deviation of about 5% and fat tails. Volatility is high after the 5.5% drop on Nov 5, and Nvidia's earnings, Anthropic's IPO and the PCE release all fall inside the window. The width of the distribution matters more than its centre.
