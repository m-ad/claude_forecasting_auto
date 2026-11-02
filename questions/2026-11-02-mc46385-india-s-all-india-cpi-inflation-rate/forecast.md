# What will India's All-India CPI inflation rate (year-on-year) for October 2026 be?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46385/ |
| **Tournament** | minibench — one shot, window 2026-11-02T06:37:51Z -> 2026-11-02T09:37:51Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | open |
| **Current forecast** | Median 6.02, IQR [5.77, 6.27] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the headline year-on-year (y/y) inflation rate for the All-India CPI (Consumer Price Index), General index, combined rural + urban, base 2024=100, for **October 2026**. The figure is the first provisional value in MoSPI's press release, due **12 Nov 2026, 16:00 IST**. The bounds of 4–8% are open on both sides.

The arithmetic runs as follows:
- The latest published month is September 2026: index 109.49 against 103.74 in September 2025, so y/y is 5.54%. August 2026 was 108.74, so September m/m (month-on-month) was +0.69% [1].
- The target is one month later, October 2026.
- ThePrint's mechanical path says a flat index from September would give October 5.54%, November 5.27% and December 5.18% [3]. That implies the October 2025 base index ≈ 103.7, essentially unchanged from September 2025. In the old series, October 2025 hit a record-low 0.25%, but that dip does **not** carry into this base. November 2025 is 104.01.
- Hence October 2026 y/y ≈ 5.54% + 1.055 × (October 2026 m/m).
- An m/m of +0.5% gives about 6.07%; 0% gives 5.54%; −0.3% gives about 5.2%; +1.0% gives about 6.6%.

### Outside view

The reference value is the flat-index figure of 5.54%. October m/m in India's CPI is usually positive. In the old food-heavy series it typically ran +0.5% to +1.1% (October 2024 about +1.1%). October 2025 was about 0% because of the GST (Goods and Services Tax) cut. The new series has a smaller food weight (36.75% vs 45.86%) [9], so seasonal swings are smaller. A typical new-series October m/m of +0.3% to +0.7% gives a prior centred near 5.9–6.1%. One-month uncertainty in Indian CPI m/m is about ±0.35 pp (1 sd), driven mainly by vegetables.

### Inside view

- **Upward:** Momentum is strong. September m/m was +0.69%, with onion +108% y/y, ginger, garlic and lemon, and restaurants +9.4% [1]. Onion arrivals fell and wholesale prices rebounded around 21 October [10]. Kharif onion output may be 5–7% lower [6]. The RBI (Reserve Bank of India) hiked on 7 October and puts Q3 FY27 at 6.0%, which means October–December average about 6% [4][5]. The festive season (Navratri/Dussehra) fell in October.
- **Downward:** Precious metals fell over October 2026: Delhi silver −17% and gold −5% from 1 to 30 October [8]. Silver jewellery has weight 0.31 and was at +88% y/y. Monthly averages fall less than the end-points, so I subtract about 0.05 pp. Tomato prices kept falling in mid-October [11]. SBI's >6.5% call was made before the September print and overshot September (5.65% forecast vs 5.54% actual) [6].
- **Combined:** Implied October m/m is about +0.45% (sd ~0.33), giving a median of **6.02%**. The tails are slightly widened for an onion reversal (downside) and a further vegetable spike (upside).

### Evidence

- MoSPI September 2026 release: 5.54% combined, rural 6.08%, urban 4.88%, CFPI (Consumer Food Price Index) 7.74%; index 109.49 (August 108.74); October release on 12 Nov [1] (retrieved 2026-11-02).
- ThePrint, 14 Oct 2026: at a flat index, October would be 5.54%; retail onion Rs 52.8/kg in September 2026 vs Rs 27.4 a year earlier [3].
- India Ratings (12 Oct 2026): October headline about 6.0%, food possibly 9.1% [4]. ICRA: October "set to cross 6%", food and beverages above 8% (search summary only) [2].
- RBI MPC (Monetary Policy Committee), 7 Oct 2026: repo rate 5.50%; Q3 FY27 CPI 6.0%; FY27 5.2% [5].
- SBI Research: above 6.5% in October–November; Ecowrap of 12 October has a November peak of 6.7–6.8% (secondary sources) [6][7].
- Delhi gold Rs 149,350 → 141,700 per 10 g; silver Rs 225,210 → 186,320 per kg, 1 → 30 Oct 2026 [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| India Ratings | ~6.0% | 2026-10-12 | after the September print |
| ICRA | >6% | ~2026-10-12 | search summary |
| SBI Research | >6.5% (Nov peak 6.7–6.8%) | early Oct 2026 | made before the September print, which it overshot |
| RBI | Q3 FY27 average 6.0% | 2026-10-07 | quarter average |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | |

### What would change my mind

- The October 2025 base index. If it is materially below 103.7 (that is, if the record-low old-series dip does carry into the new back series), every forecast shifts up one-for-one. My 103.7 is inferred from ThePrint's flat-index path, not read from a MoSPI table.
- Late-October vegetable prices. An onion collapse on kharif arrivals would push m/m to zero or below, giving 5.2–5.5%.

### Sources

1. MoSPI, Press Release CPI base 2024=100 for September 2026, https://www.mospi.gov.in/uploads/latestreleasesfiles/1791801549227-Press%20Release%20for%20the%20month%20of%20September,%202026.pdf (accessed 2026-11-02)
2. ICRA Insight / search summary, https://www.icra.in/ (accessed 2026-11-02)
3. ThePrint, "Decoding India's inflation: onions, silver key drivers", https://theprint.in/economy/decoding-indias-inflation-onions-silver-key-drivers-more-storage-capacity-will-make-rbis-task-easier/3071757/ (accessed 2026-11-02)
4. Business Today, 12 Oct 2026, https://www.businesstoday.in/latest/economy/story/retail-inflation-hits-21-month-high-set-to-squeeze-your-household-budget-further-561107-2026-10-12 (accessed 2026-11-02)
5. Angel One, September 2026 CPI and RBI projections, https://www.angelone.in/news/economy/india-s-retail-inflation-hits-23-month-high-of-5-54-in-september-2026 (accessed 2026-11-02)
6. ET/ANI via Digg, SBI Research, https://digg.com/world-business/1b976qw6 (accessed 2026-11-02)
7. Free Press Journal, SBI Research (20 Aug 2026), https://www.freepressjournal.in/business/retail-inflation-may-cross-6-in-october-november-before-easing-in-q4-fy27-report-says (accessed 2026-11-02)
8. Angel One gold/silver prices, 1 and 30 Oct 2026, https://www.angelone.in/news/commodities/check-gold-and-silver-prices-across-new-delhi-mumbai-and-chennai-on-october-30-2026 (accessed 2026-11-02)
9. Legacy IAS, new CPI series weights, https://www.legacyias.com/india-new-cpi-series-base-2024/ (accessed 2026-11-02)
10. Free Press Journal, Nashik/Lasalgaon onion market, https://www.freepressjournal.in/pune/nashik-onion-market-under-pressure-as-lasalgaon-rates-fall-to-49-per-kg (accessed 2026-11-02)
11. DT Next, Koyambedu vegetable rates 12 Oct 2026, https://www.dtnext.in/news/chennai/tomatoes-become-cheaper-by-rs-10-check-out-vegetable-rates-at-koyambedu-market-on-october-12-2026 (accessed 2026-11-02)

**Question**: [What will India's All-India CPI inflation rate (year-on-year) for October 2026 be?](https://www.metaculus.com/questions/46385/)
**Date**: 2026-11-02
**Forecast**: Median 6.02%, IQR [5.77%, 6.27%]
**Thesis**: The October 2025 base in the new series is roughly flat on September 2025, so October 2026 is about 5.54% plus that month's m/m change. Sticky onion and food momentum and the festive season suggest about +0.45% m/m, consistent with India Ratings (~6.0%), ICRA (>6%) and RBI's Q3 6.0%. Falling silver and gold and easing tomato prices temper it. The forecast is most sensitive to late-October vegetable prices and to the exact October 2025 base index.
