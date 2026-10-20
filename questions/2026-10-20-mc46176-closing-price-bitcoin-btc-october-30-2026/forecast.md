# What will be the closing price of Bitcoin (BTC) on October 30, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46176/ |
| **Tournament** | minibench — one shot, window 2026-10-20T21:13:05Z -> 2026-10-21T00:13:05Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-21 / 2026-10-31 |
| **Status** | open |
| **Current forecast** | Median 82700, IQR [80100, 85400] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

This is a numeric question. It resolves to the "Close" value in the Oct 30, 2026 row of Yahoo Finance's BTC-USD historical-data page, in US dollars. Yahoo anchors its daily candle to 00:00 UTC, so the "Oct 30 close" is in effect the price at about 00:00 UTC on Oct 31. That is about 10.1 days after this forecast, made at 21:35 UTC on Oct 20. If Yahoo shows no value, CoinGecko's daily close for that date is used. The question's range is $62,000–$105,000 and both bounds are open, so values outside it still resolve.

### Outside view

The reference class is BTC's log-return over a ~10-day horizon. Over horizons this short, the drift is negligible next to the volatility, so the median is roughly today's spot price.

- **Implied volatility:** Deribit's DVOL (30-day implied volatility) closed between 37.0 and 38.8 on each day from Oct 13 to 18, 2026 [3].
- **Realised volatility:** the standard deviation of daily close-to-close moves on Yahoo over Oct 11–20 is about 1.3%, or roughly 25% annualised [1].
- **Volatility used:** 37% annualised, i.e. the implied figure, because realised volatility is usually lower than what follows a quiet stretch. Over 10.1 days that gives a log standard deviation of about 6.2%.
- **Distribution shape:** BTC returns have fat tails, so I used a Student-t with 4 degrees of freedom instead of a normal.

### Inside view

`model.py` takes spot at $82,750, volatility at 37% and a t(4) distribution. It gives these percentiles:

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| Model | 75.4k | 77.4k | 80.1k | 82.75k | 85.5k | 88.5k | 90.8k |

Adjustments to the model:

- **Median, slightly lower (~$82.7k):** BTC is about 35% below its October 2025 all-time high in a bear-leaning year. Spot ETF flows for October are net negative month to date (-$90.6M through Oct 19 [5]), although Oct 19 brought +$526.6M. The Fear & Greed Index read a neutral-to-greedy 59 [6].
- **Lower tail, slightly fatter:**
  - Selloffs driven by liquidations hit harder than squeezes (a hot CPI print in mid-October already caused one).
  - Analysts flag $80k as the support level; a break below it could accelerate selling [8].
- **One scheduled catalyst:** the FOMC (Federal Open Market Committee) meets Oct 27–28 [7]. Oct 30 is a Friday, which is usually a Deribit options expiry.

There was no live prediction market to anchor on.

### Evidence

- **Yahoo BTC-USD (Oct 20, 2026, 21:34 UTC):** live price $82,769.10. Daily closes for Oct 11–19 were 83,679 / 81,763 / 83,095 / 81,562 / 82,141 / 81,501 / 81,382 / 82,018 / 81,854. That is a tight $81.4k–83.7k range over ten days [1].
- **CoinGecko (Oct 20, 2026):** $82,803, up 0.99% over 24 hours [2].
- **Deribit DVOL (Oct 13–18, 2026):** daily closes of 38.75, 37.66, 37.93, 38.82, 37.33 and 37.03 [3].
- **Spot BTC ETF flows ($M):** Oct 14 -261.5; Oct 15 +5.1; Oct 16 -82.4; Oct 19 +526.6. Month to date -90.6 [5].
- **Fed calendar:** the FOMC meets Oct 27–28, 2026, with a press conference on Oct 28 [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-20 | — |
| Polymarket "Bitcoin above X on October 30" | none found for 2026 (the event on the API is the closed 2025 one) | 2026-10-20 | [4] |
| Kalshi | no current Oct 30 quote found | 2026-10-20 | daily kxbtcd markets exist |
| Model projections cited in the question (midforex, Binance) | $79k–83k for late October | mid-Oct 2026 | indicative only |
| Deribit implied volatility | DVOL ~37 → ±6.2% (1 s.d.) over 10 days | 2026-10-18 | [3] |

### What would change my mind

- **A decisive break below ~$80k before Oct 30:** this is the support level analysts cite, and a break would likely bring a liquidation cascade toward the mid-$70ks.
- **A jump in DVOL toward 50 or higher:** this would call for wider tails.
- **A hawkish surprise from the FOMC on Oct 28:** this is the main scheduled downside catalyst.
- **ETF inflows like Oct 19's continuing:** this would favour a move toward $86k–88k.

### Sources

1. Yahoo Finance BTC-USD historical data — https://finance.yahoo.com/quote/BTC-USD/history/ (accessed 2026-10-20)
2. CoinGecko simple price API — https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd (accessed 2026-10-20)
3. Deribit public API, BTC volatility index (DVOL) — https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&resolution=1D (accessed 2026-10-20)
4. Polymarket Gamma API, "bitcoin-above-on-october-30" event — https://gamma-api.polymarket.com/events?slug=bitcoin-above-on-october-30 (accessed 2026-10-20)
5. TFTC, Bitcoin ETF flows October 2026 — https://www.tftc.io/bitcoin-etf-flows/october-2026 (accessed 2026-10-20)
6. BGeometrics daily report 2026-10-19 — https://bgeometrics.com/reports/daily/2026-10-19.html (accessed 2026-10-20)
7. Federal Reserve, October 2026 calendar — https://www.federalreserve.gov/newsevents/2026-october.htm (accessed 2026-10-20)
8. Crypto Times, "Bitcoin price prediction for October 2026" — https://www.cryptotimes.io/2026/09/30/bitcoin-price-prediction-for-october-2026-40k-bottom-risk-vs-low-80k-hold/ (accessed 2026-10-20)

**Question**: [What will be the closing price of Bitcoin (BTC) on October 30, 2026?](https://www.metaculus.com/questions/46176/)
**Date**: 2026-10-20
**Forecast**: Median $82,700, IQR [$80,100, $85,400]
**Thesis**: Centred on the live spot price of ~$82.8k (Yahoo and CoinGecko, Oct 20), with a fat-tailed spread sized to Deribit's 30-day implied volatility of ~37% over the 10.1 days to the 00:00 UTC Oct 31 close. The low tail is slightly heavier because of the $80k support level, negative ETF flows this month and the Oct 27–28 FOMC meeting. The forecast is most sensitive to whether $80k holds.
