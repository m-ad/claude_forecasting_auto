# Will Strategy (MSTR) close below $100 on Friday, November 27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46592/ |
| **Tournament** | minibench — one shot, window 2026-11-16T15:35:38Z -> 2026-11-16T18:35:38Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | resolved |
| **Current forecast** | Median 47.0%, IQR [39.0%, 55.0%] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

YES if the "Close" (not Adj Close) on Yahoo Finance's MSTR history page for Friday 27 Nov 2026 (half-day session, 1 p.m. ET close) is strictly below $100.00. Arithmetic: last full close Nov 13 = $111.62 (stockanalysis; the question text says $109.82); intraday Nov 16 at 11:11 ET = $102.93 (−7.8% on the day) [1]. The threshold is ~2.9% below today's price — well under one typical daily move (~5%). After today there are 8 sessions (Nov 17–20, 23–25, 27; Nov 26 closed). MSCI deletion takes effect after the close on Nov 30, i.e. after resolution [3].

### Outside view

Driftless lognormal: daily σ ≈ 5% (options implied vol ~75–82% annualised, early Nov [5]), ~8.5 sessions left including the rest of today → σ ≈ 14.5%. P(close < 100) = Φ(ln(100/102.93)/0.145) = Φ(−0.20) ≈ 42%. Reference class: a high-volatility stock sitting ~3% above a strike with ~9 sessions to go — close to a coin flip, slightly favouring "above".

### Inside view

Adjustments (+5 pp, one event cluster): the stock is in a sharp downtrend (−29% since Oct 28), bitcoin (~$68.6k on Nov 13, below Strategy's $75.5k cost basis) is at three-month lows [2], mNAV is ≈1 or below [6], so there is no premium to support it, and passive MSCI selling of ~$3B concentrates into the Nov 30 close, so pressure from front-running persists through resolution rather than reversing before it (deletion studies find reversal mostly *after* the effective date [7]). Against: index-deletion and crypto selloffs often overshoot and bounce; $4.75B USD reserve and STRC buybacks [1]; today's close is not yet known (could recover above $105 or finish below $100). Net ≈ 47%.

### Evidence

- Nov 16 2026, 11:11 ET: MSTR $102.93, −7.79%; headlines: Strategy bought only 485 BTC ($33.4M), $228.1M to STRC buybacks, USD reserve $4.75B [1].
- Daily closes Oct 28 $145.16 → Nov 13 $111.62 [1].
- Bitcoin ~$73.4k Nov 10 after hot CPI, three-month low Nov 11 [2]; ~$68.6k Nov 13 (question text).
- MSCI deletes MSTR from MSCI USA/World/ACWI effective close Nov 30; passive holders ~13M shares / ~$3B [3].
- Holdings 850,364 BTC at avg $75,456 (Nov 9 8-K) [4].
- 52-week low $81.81 (Jun 26 2026).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | no matching market found | 2026-11-16 | |
| MSTR options | ATM IV ~75–82% | early Nov 2026 | implies ~5% daily σ |

### What would change my mind

Today's close: below ~$100 would push this to ~55–60%; a rebound above $106 to ~35%. A bitcoin break below $65k (or a rally back above $75k) dominates everything else.

### Sources

1. https://stockanalysis.com/stocks/mstr/history/ and https://stockanalysis.com/stocks/mstr/ (accessed 2026-11-16)
2. https://theblock.co/news/markets/2026-11-10-bitcoin-price-cpi-inflation-73000-support-437301 (accessed 2026-11-16)
3. https://theblock.co/news/markets/2026-11-11-strategy-metaplanet-lose-msci-index-membership-november-reshuffle-438437 (accessed 2026-11-16)
4. https://theblock.co/news/business/2026-11-09-connecting-the-dots-michael-saylor-strategy-bitcoin-436094 (accessed 2026-11-16)
5. https://marketchameleon.com/Overview/MSTR/OptionChain/ (accessed 2026-11-16; via search snippet)
6. https://www.thebigwhale.io/article/strategy-when-the-premium-inverts-the-entire-dat-model-wobbles (accessed 2026-11-16)
7. https://www.cxoadvisory.com/?p=29115 (accessed 2026-11-16)

**Question**: [Will Strategy (MSTR) close below $100 on Friday, November 27, 2026?](https://www.metaculus.com/questions/46592/)
**Date**: 2026-11-16
**Forecast**: Median 47.0%, IQR [39.0%, 55.0%]
**Thesis**: MSTR traded at $102.93 intraday on Nov 16, only ~3% above the $100 strike with ~8.5 sessions left and ~5% daily volatility, so a driftless model gives ~42%. Bitcoin below Strategy's cost basis, no mNAV premium and MSCI deletion selling concentrated before the Nov 30 effective date tilt it up to ~47%. The forecast is most sensitive to bitcoin's path and to today's close.

## Resolution — 2026-11-28

Resolved **yes** (synced from the Metaculus API). The bot's forecast was 47.0% [39.0%, 55.0%]. Official spot peer score: -1.42.
