# What will Serbia's year-on-year consumer price inflation be in October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46379/ |
| **Tournament** | minibench — one shot, window 2026-11-02T04:52:04Z -> 2026-11-02T07:52:04Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-12 |
| **Status** | open |
| **Current forecast** | Median 3.95, IQR [3.75, 4.2] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The answer is the annual CPI rate for October 2026 (October 2026 vs October 2025 = 100, in %, one decimal) in the first RZS (Statistical Office of the Republic of Serbia) release CN 11, due 12 November 2026. Later revisions don't count. The question has 21 outcomes from 3.2 to 5.2 in 0.1 steps, and both bounds are open. The arithmetic is one month: y/y(Oct 26) ≈ (1 + y/y Sep 26) × (1 + m/m Oct 26) / (1 + m/m Oct 25) − 1. The last print is September 2026 at 4.1% y/y and +0.2% m/m [1][2]. The month dropping out is October 2025 at +0.49% m/m, which included a 6.6% household electricity hike effective 1 Oct 2025 [3][4]. If October 2026 m/m equals +0.49%, the rate stays at about 4.1%. Every 0.1 pp of m/m above or below that moves y/y by about 0.1 pp. An October m/m of +0.35% gives about 3.95%.

### Outside view

The reference class is one-month changes in Serbian annual CPI outside base-effect months. These typically move ±0.1–0.4 pp. October m/m prints were about +0.26% in 2023 and +0.49% in 2025 (the latter with an electricity hike); 2022 was a +1.9% outlier during the energy shock [3][5]. In 2026 the m/m prints were Jun +0.2, Jul −0.2, Aug +0.5 and Sep +0.2 [1]. The prior is the last value, 4.1%, ±0.3 pp.

### Inside view

- **Base month.** Most of the big base effect (Sept 2025 −1.59% m/m when the 20% margin-cap decree started) has already passed into the September print. October 2025 (+0.49%) is a normal-to-high base month because of the electricity hike. There was no household electricity hike in October 2026. Serbia committed to the IMF to raise tariffs "no later than 1 Oct 2026" or "by year-end" [4][6]. On 31 Aug 2026, however, Danas reported that EPS (the state power utility) had not filed with AERS (the Energy Agency). It called a 1 Oct start "procedurally impossible" and expected the hike to come after the 25 Oct election [11]. I put about 5% on some hike still being recorded in October. That roughly 0.2–0.3 pp electricity contribution in the October 2025 base therefore drops out, which is the main downward force.
- **Momentum.** Upward. Food rose 0.6% m/m in September and is still −1.8% y/y, so the gap is closing. Transport rose 1.2% m/m. PPI (producer prices) was up 10.5% y/y in September [2][7]. Fuel prices were flat through October at 236/207 RSD [8]. The margin-cap decree expired on 1 Mar 2026 [9], so no new price-freezing effect applies.
- **Model** (`model.py`, Monte Carlo). Sept unrounded is uniform on 4.05–4.15. October m/m is drawn from N(0.33, 0.28) %, plus 0.15–0.35 pp with 5% probability for a tariff hike. Output: p5 3.5, p25 3.7, p50 3.9, p75 4.1, p95 4.4. I shifted the distribution up by about 0.05 and widened the upper tail. My reasons: core inflation is 4.5%, September m/m was well below the 0.5% consensus (a catch-up is possible), food is rebounding and PPI is high. The NBS (National Bank of Serbia) also expects inflation to "fluctuate around 4%" from September onward [10]. Final distribution: p5 3.4, p10 3.55, p25 3.75, p50 3.95, p75 4.2, p90 4.4, p95 4.6.

### Evidence

- Sep 2026: 4.1% y/y, +0.2% m/m, +3.3% vs Dec 2025. Food −1.8% y/y and +0.6% m/m. Water +21.8% y/y, rents +10.6% y/y (RZS via [2], retrieved 2026-11-02).
- Aug 2026: 2.2% y/y (+0.5% m/m). Jul 2026: 1.9%. Jun 2026: 2.7% [1].
- Oct 2025: +0.49% m/m and 2.8% y/y. Sep 2025: −1.59% m/m [3].
- Electricity: +6.6% from 1 Oct 2025. For 2026 there is an IMF commitment but no decision found [4][6].
- Fuel was unchanged at 236 RSD diesel and 207 RSD BMB95 on 16 and 23 Oct 2026 [8]. PPI was 10.5% y/y in Sep 2026 [7].
- Trading Economics models 3.5% by end-Q4. The NBS says inflation will stay around 4% [1][10].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | |
| NBS | "around 4%" from Sep 2026 through 2027 | Sep 2026 statement | central bank |
| Trading Economics | 3.5% end-Q4 2026 | 2026-11-02 | model, not consensus |

### What would change my mind

- **Electricity tariff hike in October 2026.** If an EPS hike took effect in October after all, the median moves to about 4.2.
- **Food prices.** Food is 31% of the basket. A sharp October rise (+1% m/m or more) pushes the outcome toward 4.4–4.6. A seasonal fall in fruit and vegetables pushes it toward 3.7.

### Sources

1. Trading Economics, Serbia inflation rate — https://tradingeconomics.com/serbia/inflation-cpi (accessed 2026-11-02)
2. Srpske novine, September 2026 inflation 4.1% — https://srpske.rs/en/news/ekonomija/2026/10/12/serbia-september-inflation-4-1-percent-water-rents (accessed 2026-11-02); also biznis.rs https://biznis.rs/vesti/srbija/medjugodisnja-inflacija-u-srbiji-u-septembru-bila-41-odsto-a-mesecna-02-odsto/
3. Focus Economics, Serbia consumer prices Oct 2025 — https://www.focus-economics.com/countries/serbia/news/inflation/serbia-consumer-prices-12-11-2025-inflation-slows-in-october-from-the-prior-month/ (accessed 2026-11-02, search snippet)
4. Balkan Green Energy News, electricity +6.6% Oct 2025 — https://balkangreenenergynews.com/rs/struja-poskupljuje-66-odsto-u-srbiji/ (accessed 2026-11-02)
5. Focus Economics, Oct 2023 CPI — https://www.focus-economics.com/countries/serbia/news/inflation/inflation-falls-to-lowest-level-since-january-2022-in-october/ (accessed 2026-11-02)
6. Beta Briefing, electricity may go up by year-end — https://betabriefing.com/see-business/serbia/35353-price-of-electricity-for-households-in-serbia-may-go-up-by-years-end (accessed 2026-11-02)
7. Trading Economics, Serbia PPI Sep 2026 — https://tradingeconomics.com/serbia/producer-prices-change/news/589540 (accessed 2026-11-02)
8. Nafta.hr, official Serbian fuel prices from 23 Oct 2026 — https://nafta.hr/?p=14351 (accessed 2026-11-02)
9. Vreme, margin-cap decree expiry — https://vreme.com/ekonomija/hoce-li-cene-podivljati-kada-istekne-uredba-o-marzama/ (accessed 2026-11-02)
10. Focus Economics, NBS Aug 2026 meeting — https://www.focus-economics.com/countries/serbia/news/monetary-policy/serbia-central-bank-meeting-13-08-2026-nbs-leaves-rates-unchanged-again-in-august/ (accessed 2026-11-02)
11. Danas, electricity hike and elections — https://www.danas.rs/vesti/ekonomija/poskupljenje-struje-izbori/ (accessed 2026-11-02)

**Question**: [What will Serbia's year-on-year consumer price inflation be in October 2026?](https://www.metaculus.com/questions/46379/)
**Date**: 2026-11-02
**Forecast**: Median 3.95%, IQR [3.75%, 4.2%]
**Thesis**: This is a one-month step from September's 4.1%. October 2025 (+0.49% m/m, including a 6.6% electricity hike) drops out of the base. With no electricity hike in October 2026 (delayed past the election [11]) and a typical October m/m of about 0.3–0.4%, the rate edges down to about 3.9–4.0%, against upward food, core and PPI momentum (RZS via [1][2], [3], [7]). The forecast is most sensitive to October food and administered prices.
