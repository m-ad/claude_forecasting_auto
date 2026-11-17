# What will Nvidia's (NVDA) closing share price be on Friday, November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46602/ |
| **Tournament** | minibench — one shot, window 2026-11-17T00:45:59Z -> 2026-11-17T03:45:59Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-17 / 2026-11-17 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 157, IQR [144, 171] (v1, 2026-11-17) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-17

### What resolves YES

The question resolves to the NVDA "Close" from the regular session of Friday 27 Nov 2026, a half day that ends at 13:00 ET. The source is the Yahoo Finance history page, with stockanalysis.com as the fallback. The latest known close is **$156.14 on Mon 16 Nov 2026** (stockanalysis.com, fetched 2026-11-17) [1]. From there to the target close there are 7 sessions: Nov 17, 18, 19, 20, 23, 24 and 25, then the half day on the 27th (the market is shut on the 26th). The 7 sessions include the Q3 FY2027 earnings reaction: results come out after the close on 17 Nov, so the move shows up in the 18 Nov session. The range is $100–260 with both bounds open. A 10% move from $156 is about ±$16.

### Outside view

Treat the price as a random walk from $156.14. A normal NVDA week with an earnings print carries a log standard deviation of about 8–9%. That is roughly 2.5%/day over 7 sessions, plus an earnings-day move that has averaged about 5–8% [5]. This is no normal regime. The stock went from $206.69 on 3 Nov to $156.14 on 16 Nov, with daily moves of 4–9%. The SOX (Philadelphia Semiconductor Index) fell 12.25% on 5 Nov [6]. The CEO resigned on 12 Nov. Options were pricing an earnings move of about ±10.6% [2].

### Inside view

- Volatility: I assume roughly 3%/day of diffusion over 7 sessions (about 8% in total) and an earnings shock with a standard deviation of about 11%. Together that gives a log standard deviation of about 14%, with fat tails.
- Centre: I keep the median at the last close, nudged to $157. Two things argue for a rebound. The stock is oversold, the first time since April 2025 [7]. It trades at about 23x forward earnings with a consensus target of $314 [3][4]. Two things argue the other way. A leadership vacuum and AI-capex skepticism are behind a six-week losing streak, and momentum carries forward. Historically NVDA has been up after one week in 60% of post-earnings weeks [5]. That is weak evidence, so I add only a small upward drift.
- Percentiles: p5 121, p10 131, p25 144, p50 157, p75 171, p90 187, p95 199.

### Evidence

- Closes [1]: Nov 3 $206.69; Nov 5 $181.60; Nov 6 $186.64; Nov 9 $178.67; Nov 10 $168.89; Nov 11 $173.73; Nov 12 $166.19; Nov 13 $162.85; Nov 16 $156.14. The question text gives about $159.2 for Nov 13, but the source shows $162.85.
- Guidance is $108B ±2%. Consensus is about $108.8B revenue and $2.47 EPS. The options-implied earnings move is about ±10.6%, against a 10-year average of 7.8% [2].
- Baird cut its target from $500 to $200 and moved to neutral. Mizuho cut from $315 to $250. Reuters reports 59 of 64 brokers at buy, with a median target of $314 [3].
- House committee chairs requested a closed-door briefing from Huang on 18 Nov [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-17 | |
| Polymarket NVDA end-of-November ladder | no usable current price | 2026-11-02 | thin, ~$100 volume |
| Options-implied earnings move | ±10.6% | mid-Nov 2026 | MarketPulse [2] |

### What would change my mind

The earnings print and guidance on 17 Nov. A Q4 guide well above $120B, or a beat with reassurance about the CEO search, could add 10–15%. A guide that disappoints, or new China or legal revelations, could take another 15–20% off. A sudden permanent CEO appointment (Haas, Malachowsky) would also move the stock.

### Sources

1. https://stockanalysis.com/stocks/nvda/history/ (accessed 2026-11-17)
2. https://www.marketpulse.com/markets/nvidia-nvda-q3-earnings-preview-ai-spending-risks-and-governance-concerns-threaten-major-uptrend/ (accessed 2026-11-17)
3. https://www.indmoney.com/blog/us-stocks/nvidia-stock-price-target-cuts-goldman-sachs-300-jensen-huang-investigation (accessed 2026-11-17)
4. https://www.mitrade.com/insights/news/live-news/article-8-2221002-20261102 (accessed 2026-11-17)
5. https://www.regardsofwallstreet.com/tools/earnings-history/nvda (accessed 2026-11-17)
6. https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/ (accessed 2026-11-17)
7. https://www.stonex.com/en-gb/news-and-analysis/nasdaq-nvda-go-oversold-for-the-first-time-since-april-2025-lows-2026-11-09/ (accessed 2026-11-17)
8. https://thenextweb.com/news/house-chairs-jensen-huang-briefing-megaspeed (accessed 2026-11-17)
9. https://stockanalysis.com/news/nvidia-board-prepares-to-oust-jensen-huang/ (accessed 2026-11-17)

**Question**: [What will Nvidia's (NVDA) closing share price be on Friday, November 27, 2026?](https://www.metaculus.com/questions/46602/)
**Date**: 2026-11-17
**Forecast**: Median $157, IQR [$144, $171]
**Thesis**: The forecast is a random walk from the 16 Nov close of $156.14, over 7 sessions that include the 17 Nov earnings reaction (options imply ±10.6%) during a CEO-succession crisis. That gives a log standard deviation of about 14% and fat tails, with only a slight lean toward an oversold rebound. The earnings guide is the single biggest swing factor.
