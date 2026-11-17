# Will front-month ICE Brent crude futures (January 2027 contract) settle above $100.00 per barrel on 27 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46601/ |
| **Tournament** | minibench — one shot, window 2026-11-17T00:14:21Z -> 2026-11-17T03:14:21Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-17 / 2026-11-17 / 2026-11-28 |
| **Status** | closed |
| **Current forecast** | Median 18.0%, IQR [13.0%, 24.0%] (v1, 2026-11-17) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-17

### What resolves YES

YES if ICE Futures Europe's official settlement for Brent January 2027 (BRN F27, Barchart CBF27) on Friday 27 November 2026 is **strictly above $100.00/bbl**. Barchart's historical-prices row is the display source and ICE's figure governs if they differ. A settle of exactly $100.00 is NO. Arithmetic: the front month traded at about $92.0 on 17 Nov 2026 (Asian session, Trading Economics). $100.00 is therefore +8.7% away (ln 0.083). The contract has about 9 trading sessions left (17–20 and 23–27 Nov; ICE trades on US Thanksgiving, 26 Nov). The 29 Nov OPEC+ meeting falls after the settlement date and cannot affect it.

### Outside view

The reference class is a lognormal price move over 9 sessions in the 2026 war-regime volatility. Daily moves of 3–6% have been common since August, which implies roughly 50–70% annualised volatility, or σ(9d) ≈ 9.5–11.5%. The needed move is about +0.73–0.88σ, which gives P(close > $100) ≈ 19–23% with no drift. Brent has re-crossed $100 on escalation four times in 2026 (Mar, May, Jul, Sep). Spikes recur, so the tails are fat on the upside.

### Inside view

The adjustments are downward. Brent has fallen from $103.60 (3 Nov) to ~$92 (17 Nov), including the sharpest weekly drop since 2020. The IEA projects a surplus of about 2 mb/d this quarter, Goldman warns of a 2027 glut, Saudi Arabia and the UAE cut official selling prices (OSPs), and Trump is signalling restraint on Iran. On the other side, incidents continue: Iran struck a US base in Bahrain and tankers hit mines in Hormuz on 16 Nov, and the market fell anyway. The market is discounting escalation, but one large incident or a collapse of talks could add 5–10% in a day, as it did on 5 Nov (+$3.67). Net effect: about −4 pp from the no-drift lognormal figure. **Forecast 18%.**

### Evidence

- Brent settled at $92.57 on 9 Nov, after a 16% weekly fall [1]. It settled at $91.49 on 10 Nov and $92.53 on 11 Nov (scout, snippet citing Reuters). The question text gives $95.82 on 12 Nov.
- 16 Nov: Brent fell ~2% to below $94, then ~$92, on the improving supply outlook. The same reports cover the Iran strike on the Bahrain base and mines in Hormuz [2].
- 17 Nov: ~$92.03, −0.44% [2].
- 5 Nov: Brent rose $3.67 to $98.29 on tanker attacks [3]. Single-headline moves of this size are routine.
- OPEC+ held December output unchanged; its ministerial meeting is on 29 Nov [4].
- Brent recrossed $100 in Sep 2026 on Iran and Houthi escalation [5].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-17 | |
| Polymarket / Kalshi | no live Brent late-Nov market found | 2026-11-17 | WTI snapshots found were stale |
| EIA STEO | Brent "near $100" for rest of 2026 | 2026-11-10 | per question text; written when price was ~$95 |
| Trading Economics model | Q4 ~$98 | 2026-11-17 | model forecast, not a market |

### What would change my mind

The main risk is an escalation shock: talks collapse, a major strike on Gulf export infrastructure, or a Hormuz closure. That would make $100 likely within days. A front month already back near $97 by 23–24 Nov would put this near 40%. A signed US–Iran deal would drop it below 5%.

### Sources

1. https://www.nst.com.my/amp/business/economy/2026/11/1574340/oil-falls-over-us7-trump-signals-restraint-iran (accessed 2026-11-17)
2. https://tradingeconomics.com/commodity/brent-crude-oil (accessed 2026-11-17)
3. https://www.nationthailand.com/news/40073162 (accessed 2026-11-17)
4. https://gvwire.com/2026/11/01/opec-keeps-december-oil-output-targets-steady-ahead-of-tougher-call-for-2027/ (accessed 2026-11-17)
5. https://www.businesstoday.com.my/2026/09/10/oil-hits-us100-as-iran-us-strikes-rattle-markets/ (accessed 2026-11-17)
6. https://www.khaleejtimes.com/business/oil-steadies-as-hormuz-attacks-blunt-hopes-for-iran-truce-2 (accessed 2026-11-17)
7. https://www.barchart.com/futures/quotes/CBF27/historical-prices (accessed 2026-11-17; fetch failed)

**Question**: [Will front-month ICE Brent crude futures (January 2027 contract) settle above $100.00 per barrel on 27 November 2026?](https://www.metaculus.com/questions/46601/)
**Date**: 2026-11-17
**Forecast**: Median 18.0%, IQR [13.0%, 24.0%]
**Thesis**: Brent January has slid to ~$92 (17 Nov, Trading Economics), so $100 needs a +8.7% move in 9 sessions. War-regime volatility gives that about a 20% chance; de-escalation momentum and an IEA-projected surplus shade it lower. The forecast is most sensitive to an escalation shock in the Gulf, which has pushed Brent back over $100 four times this year.
