# Will Bitcoin be at or above $85,000 at the start of October 31, 2026 (UTC)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46170/ |
| **Tournament** | minibench — one shot, window 2026-10-20T09:17:04Z -> 2026-10-20T12:17:04Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-20 / 2026-10-31 |
| **Status** | closed |
| **Current forecast** | Median 22.0%, IQR [17.0%, 28.0%] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

YES if CoinGecko's Bitcoin historical-data table, in its row dated 2026-10-31 (the 00:00:00 UTC snapshot), shows a BTC/USD price of $85,000.00 or more; any lower value resolves NO. Only that single snapshot counts — not an intraday high, not a touch earlier in the month. If CoinGecko stops publishing, a credible BTC/USD price at 00:00 UTC on 31 Oct is used. In practice this is a European-style binary option: BTC above $85,000 at one instant, about 10.6 days after this forecast.

### Outside view

Reference class: a ~10.6-day log return of BTC, roughly driftless at this horizon. Spot is $81,324 (CoinGecko API, 2026-10-20 ~09:42 UTC [2]), so YES needs a gain of about +4.5% (ln ratio 0.044). Deribit's 30-day implied-volatility index (DVOL) has been 37.3–39.1 from Oct 14–20, 2026, with 38.1 on Oct 20 [11]. Allowing 35–50% annualised volatility for model risk (DVOL was 46 in June 2026 [6]; realized volatility was in the 20s in August [7]), the 10.6-day standard deviation is 6–8.5%. At the implied 38%, it is ~6.5%, which puts $85k about 0.68 sigma above spot. A lognormal model then gives a 23–30% probability. A fat-tailed Student-t with the same standard deviation gives 18–25%, because fat tails move mass toward the centre for moderate moves (`model.py`). Base rate: **~24%**.

### Inside view

- **Momentum and flows are mildly negative.** BTC is down 2.0% over 24h and 2.9% over 7 days [2]. Spot ETFs had net outflows of −$617M from 1–16 October [5]. BTC briefly fell below $80k last week, liquidating about $950M of positions, mostly longs [3][4]. The rebound to $82.8k on Oct 19 has faded [3]. The 2026 trend is down from the $126k all-time high.
- **Event risk is the FOMC (Federal Open Market Committee) meeting on Oct 27–28,** three days before resolution. Prediction markets give about 86% for a hold and about 14% for a 25bp hike (DeFi Rate averaging Kalshi and Polymarket, Oct 20 [8]). A hold is mostly priced in, so this adds modest volatility in both directions. A dovish surprise could plausibly push BTC through $85k; a hike would likely push it lower.
- **$85k is the top of the recent range,** last held around Oct 2–7 ($85.5–86.5k [1]). Getting back there needs a move out of the range, not just drift.
- I make no material adjustment for direction: weak momentum is not reliably predictive at a 10-day horizon. I shade slightly below the lognormal midpoint because of the outflows and the fat-tail effect.

Result: **22%**, IQR 17–28%. The width reflects uncertainty about volatility (30% vs 55% annualised moves the answer by ±6pp).

### Evidence

- CoinGecko historical table (fetched 2026-10-20): closes of $81,875 (Oct 19), $82,020 (Oct 18), $81,408 (Oct 17), $81,524 (Oct 16), $82,156 (Oct 15), $81,604 (Oct 14), $83,115 (Oct 13) [1].
- CoinGecko API: $81,324, −1.99% in 24h, 2026-10-20 ~09:42 UTC [2].
- BGeometrics daily report: $81,970 on 19 Oct 2026, −0.1% day on day [9].
- Investing.com (Oct 17): BTC was holding above $81k as ETF outflows weighed. It briefly dipped below $80k during the week and had a weekly high above $84k [4].
- coin-turk (Oct 19): BTC near $82,800, a five-day high, as Fed hike expectations eased. Glassnode sees support at $77.5k [3].
- TFTC: spot BTC ETF net flows for 1–16 Oct total −$617.2M [5].
- DeFi Rate (Oct 20): Oct 28 FOMC hold ~86%, 25bp hike ~14% [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-20 | |
| Polymarket "BTC above $85k on Oct 31" | none found | 2026-10-20 | The October $85k *touch* market already resolved YES on Oct 2 (bitcoin.com) [10]; that is a different contract |
| Kalshi / Manifold | none found | 2026-10-20 | |
| Deribit implied vol (DVOL) | 38.1 (Oct 14–20 range 37.3–39.1) | 2026-10-20 | Options-implied ~0.68σ to $85k gives ~25% under lognormal, ~19–20% with fat tails [11] |
| Polymarket/Kalshi "hit in 2026" | $85k 73% (touch, any time in 2026) | 2026-09-07 | Touch market, not an Oct 31 close; context only [12] |

### What would change my mind

The most sensitive input is the volatility assumption. If BTC options were pricing 55%+ vol going into FOMC, the probability would be near 30%; at 30% vol it would be near 15–19%. Second, any sharp move before Oct 31: a reclaim of $84k in the next few days would put this near 40–45%, and a break below $80k would put it under 10%.

### Sources

1. CoinGecko, Bitcoin historical data — https://www.coingecko.com/en/coins/bitcoin/historical_data (accessed 2026-10-20)
2. CoinGecko API simple price — https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd (accessed 2026-10-20)
3. coin-turk, "Bitcoin trades near $82,800 as ETF outflows and Fed policy shape 2026 outlook" — https://en.coin-turk.com/bitcoin-trades-near-82800-as-etf-outflows-and-fed-policy-shape-2026-outlook/ (accessed 2026-10-20)
4. Investing.com, "Bitcoin price holds above $81,000 as ETF outflows weigh on sentiment" — https://www.investing.com/news/cryptocurrency-news/bitcoin-price-holds-above-81000-as-etf-outflows-weigh-on-sentiment-4955253 (accessed 2026-10-20)
5. TFTC, Bitcoin ETF flows October 2026 — https://www.tftc.io/bitcoin-etf-flows/october-2026 (accessed 2026-10-20)
6. Glassnode Studio, BTC DVOL — https://studio.glassnode.com/charts/derivatives.DvolOhlc?a=BTC (search snippet, accessed 2026-10-20)
7. VanEck, mid-August 2026 Bitcoin ChainCheck — https://www.vaneck.com/us/en/blogs/digital-assets/matthew-sigel-vaneck-mid-august-2026-bitcoin-chaincheck/ (search snippet, accessed 2026-10-20)
8. DeFi Rate, Fed decision odds — https://defirate.com/odds/fed-decision/ (accessed 2026-10-20)
9. BGeometrics daily report 2026-10-19 — https://bgeometrics.com/reports/daily/2026-10-19.html (accessed 2026-10-20)
10. Bitcoin.com News, Polymarket October price markets — https://news.bitcoin.com/price-predictions/bitcoin-price-prediction-polymarket-90k-october/ (search snippet, accessed 2026-10-20)
11. Deribit API, BTC volatility index data — https://www.deribit.com/api/v2/public/get_volatility_index_data?currency=BTC&resolution=86400 (accessed 2026-10-20)
12. Bitcoin.com News, year-end bitcoin price predictions — https://news.bitcoin.com/year-end-bitcoin-price-predictions-grow-cautious-as-bettors-eye-81k/ (accessed 2026-10-20)

**Question**: [Will Bitcoin be at or above $85,000 at the start of October 31, 2026 (UTC)?](https://www.metaculus.com/questions/46170/)
**Date**: 2026-10-20
**Forecast**: Median 22.0%, IQR [17.0%, 28.0%]
**Thesis**: BTC is at ~$81.3k (CoinGecko, Oct 20) and needs about +4.5% by the single 00:00 UTC Oct 31 snapshot. A 10.6-day lognormal/fat-tailed volatility model at 35–50% annualised gives 18–30%. Mild negative momentum and ETF outflows (−$617M in October) shade it to ~22%, with the Oct 28 FOMC (Federal Open Market Committee) meeting, ~86% priced as a hold, the main event risk. The forecast is most sensitive to the volatility assumption and to any break out of the $79–84k range before month-end.
