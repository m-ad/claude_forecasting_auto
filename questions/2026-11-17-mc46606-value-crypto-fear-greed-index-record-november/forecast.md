# What value will the Crypto Fear & Greed Index record for November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46606/ |
| **Tournament** | minibench — one shot, window 2026-11-17T05:12:21Z -> 2026-11-17T08:12:21Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-17 / 2026-11-17 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 15, IQR [11, 21] (v1, 2026-11-17) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-17

### What resolves YES

A discrete question. It resolves to the integer that Alternative.me's API (`api.alternative.me/fng/`) records for the 2026-11-27 00:00 UTC timestamp. Other publishers' fear-and-greed numbers do not count. The range is 3–80, with both bounds open. The question text says the index was 20 on 13 Nov, but that is stale. The API itself, fetched today, gives **12 on 17 Nov**, after 13 (14 Nov), 10 (15 Nov) and 10 (16 Nov). The horizon is 10 daily prints from today's reading to the target. A reading of 25 or more ends "Extreme Fear", which would take +13 points from today.

### Outside view

The reference class is the index's level 10 days after a reading in the low teens. Extreme-fear stretches tend to persist:

| Episode | Low | How it played out |
|---|---|---|
| Nov 2025 | 10 on 17 Nov | Left extreme fear after 18 days, at 28 |
| Feb 2026 | 5 | Single digits to low teens for weeks |
| Mar 2026 | 11 on 31 Mar | Had been in extreme fear for 12+ straight days |
| Apr 2026 | 8 on 2 Apr | — |

Over 10 days the index typically moves ±5–10 points, with some reversion toward its long-run mean in the 40s. My outside-view median is about 15–16. The tails are fat: in August 2026 it moved 36 → 81 in a week.

### Inside view

Things holding the index down:
- Bitcoin fell to about $69–71k by 12–13 Nov, its lowest since August.
- US spot bitcoin ETFs have had persistent outflows ($1.44B over five sessions to 11 Nov).
- A December Fed hike looks fully priced after the hot October CPI.
- MSCI will drop Strategy, the largest corporate bitcoin holder, from its indexes after 30 Nov.

The index has also stopped falling: it has held at 10–13 for four days, which suggests the price is consolidating rather than crashing. The index is a momentum and volatility composite. A sideways week usually drifts it up into the mid-to-high teens. A relief bounce to about $75k+ would take it into the 20s or low 30s. A break below about $65k would send it into single digits; the all-time low is 5. Upcoming catalysts are Nvidia earnings and the FOMC minutes (18 Nov). I put the median at 15, skewed upward because 10 is already close to the floor.

### Evidence

- Alternative.me API (fetched 2026-11-17): 17 Nov 12; 16 Nov 10; 15 Nov 10; 14 Nov 13; 13 Nov 20; 12 Nov 28; 5 Nov 50; 22 Oct 68 [1].
- BTC prices [2][3]:
  - 10 Nov: $74.3k
  - 11 Nov: $73.9k
  - 12 Nov: $71.3k intraday low, lowest since August, with $650M+ of liquidations
- ETF outflows: $1.28B in the week to 7 Nov, and five straight days of outflows through 11 Nov [3][4].
- Fed: a 25 bp hike on 8–9 Dec is priced after the October CPI (+0.4% month on month) [5]. This is a secondary source.
- 2026 lows of the index: 5 (Feb), 8 (2 Apr), 11 (31 Mar) [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-17 | — |
| Polymarket BTC November touch | 43% touch $70k, 26% touch $67.5k, 81% touch $77.5k | 2026-11-06 | stale; $70k has since been touched |
| Index-specific market | none found | 2026-11-17 | — |

### What would change my mind

The forecast is most sensitive to the BTC price path from here to 27 Nov:
- A rebound above about $76k would put the index in the high 20s to 30s, above my p90.
- A capitulation below $65k would put it at 5–8, my p5–p10.

### Sources

1. https://api.alternative.me/fng/?limit=60 (accessed 2026-11-17)
2. https://fortune.com/article/price-of-bitcoin-11-12-2026/ (accessed 2026-11-17)
3. https://news.bitcoin.com/market-updates/bitcoin-price-breaks-below-72k-656m-liquidation-bloodbath/ (accessed 2026-11-17)
4. https://theblock.co/news/markets/2026-11-07-bitcoin-etfs-flip-negative-for-2026-after-1-28-billion-outflow-week-worst-since-june-435984 (accessed 2026-11-17)
5. https://kalshi.com/fed-rate-odds (accessed 2026-11-17)
6. https://cointelegraph.com/news/crypto-fear-and-greed-index-stuck-on-extreme-fear-but-is-there-a-silver-lining (accessed 2026-11-17)
7. https://news.bitcoin.com/price-predictions/prediction-markets-favor-another-drop-as-year-end-bitcoin-price-forecasts-sour/ (accessed 2026-11-17)
8. https://pro.edgex.exchange/en-US/news/article/crypto-fear-greed-index-25-lowest-since-august (accessed 2026-11-17)

**Question**: [What value will the Crypto Fear & Greed Index record for November 27, 2026?](https://www.metaculus.com/questions/46606/)
**Date**: 2026-11-17
**Forecast**: Median 15, IQR [11, 21]
**Thesis**: Alternative.me's index reads 12 today (10–13 for four days) after bitcoin's slide to about $70k, and deep-fear stretches historically last weeks. So the base case is a modest drift up into the mid-teens, with fat tails: single digits if bitcoin breaks $65k, 25–35 if it rallies back above $76k.
