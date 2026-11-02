# What will the National Bank of Poland's EUR/PLN reference rate be on 13 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46400/ |
| **Tournament** | minibench — one shot, window 2026-11-02T13:55:28Z -> 2026-11-02T16:55:28Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | *not yet forecast* |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the EUR mid rate (PLN per EUR) in NBP Table A dated 2026-11-13 (a Friday, an ordinary business day). Only that fixing counts; 11 Nov is a holiday with no table. If no table is dated 13 Nov, the latest earlier table is used. Latest published fixing: **4.4185 on 2 Nov 2026** (Table 213/A/NBP/2026), up from 4.3955 on 30 Oct — the highest of 2026. Horizon: 2 Nov to 13 Nov = 9 business days, 8 fixings in between (11 Nov skipped). Bounds are open (4.2–4.6 is just the plotted range). No fallback arithmetic is needed beyond the status-quo rule.

### Outside view

A random walk from the last fixing. Using NBP's own series (api.nbp.pl, accessed 2026-11-02): daily moves recently ~0.25–0.3% (≈0.012 PLN); 9-business-day changes in 2025–26 had std ≈0.7–0.8% (≈0.03–0.035), recently ≈0.9–1.0% (≈0.04); 1M implied vol, only an undated MNI note, ~7–8% annualised, i.e. ≈0.05 PLN over 9 days. Largest recent 9-day moves: +3.0% (April 2025 tariff shock), +1.55% (Sep 2026), +1.07% (20 Oct–2 Nov 2026). Reference class: EUR/PLN 9-day changes, n≈450 windows 2025-26. I use sd ≈0.045 with fat tails.

### Inside view

Median 4.410, slightly below the last print 4.4185, for two reasons that I count as one: (a) recent spikes partly reverted (24 Sep 4.390 → 4.375; 28 Oct 4.409 → 4.395) and the last print came after a +0.5% one-day jump, and bank forecasts (Commerzbank 4.30 near term / 4.25 end-2026, ING expects 4.38–4.40) sit below spot. Offsetting: a persistent depreciation trend since August (4.30 → 4.42), a positive forward premium (≈+0.005–0.007 for 1M, speculation from rate differential), and event risk that is skewed to zloty weakness: the NBP board's legal quorum problem (Lipiński's term ends 4 Nov, Tusk not countersigning nominees), the MPC meeting 3–4 Nov with a new projection (85% hold nowcast; ING: hikes only from Q1 2027, so zloty exposed to dovishness), and the Sejm vote on Glapiński before the State Tribunal planned for 17–19 Nov, after the fixing. Net: median 4.410, skewed slightly to the upside in the tails. Percentiles: 5%: 4.335, 10%: 4.352, 25%: 4.382, 50%: 4.410, 75%: 4.438, 90%: 4.470, 95%: 4.492.

### Evidence

- NBP Table A EUR: 20 Oct 4.3716; 21 Oct 4.3641; 22 Oct 4.3685; 23 Oct 4.3917; 26 Oct 4.4026; 27 Oct 4.4056; 28 Oct 4.4090; 29 Oct 4.3951; 30 Oct 4.3955; 2 Nov 4.4185 [1]. Aug 2026 ~4.30–4.33, Sep ~4.32–4.39 [1].
- Commerzbank (Tatha Ghose, 19 and 27 Oct): zloty lags CE3 peers due to NBP institutional tensions; no clear near-term reversal catalyst [3]. Near-term forecast 4.30, end-2026 4.25 (7 Aug; stale vs spot) [4].
- ING (15 Oct): zloty exposed, EUR/PLN back to 4.38–4.40, hikes from Q1 2027 [5].
- MPC 4 Nov: reference rate 3.75%; nowcast 85% hold / 8% cut / 6% hike; September CPI 4.1% y/y [6].
- Glapiński: Sejm committee found 8 charges on 9 Oct; floor vote realistically 17–19 Nov (after our date); majority required disputed; Commerzbank (30 Jul) called the process low-impact for FX [6][7].
- Board: Lipiński's term ends 4 Nov; Tusk has not countersigned nominees; legal experts do not expect NBP decisions to be void [8].
- Disconfirmation (tests: "partial mean reversion, median below last print"): the evidence is mixed — the trend and institutional risk argue against reversion, so I kept only a 0.009 shave, not the 0.05–0.10 that bank forecasts would suggest.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found on EUR/PLN | 2026-11-02 | searches returned only ECB-rate markets |
| Commerzbank | 4.30 near term; 4.25 end-2026 | 2026-08-07 | stale vs spot 4.42 |
| ING | 4.38–4.40 | 2026-10-15 | |
| Forward (my estimate) | ≈4.424 | 2026-11-02 | speculation from rate differential |

### What would change my mind

A dovish MPC surprise (a cut) or a failure of the board to retain quorum on 4 Nov would push the median toward 4.45+; a clear legal resolution of the NBP board dispute, or a global risk-on move, would push it toward 4.36–4.38. The forecast is most sensitive to the 3–4 Nov MPC/board news.

### Sources

1. https://api.nbp.pl/api/exchangerates/rates/a/eur/last/30/?format=json (accessed 2026-11-02)
2. https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-01-01/2025-12-31/?format=json (accessed 2026-11-02)
3. https://www.fxstreet.com/news/polish-zloty-political-uncertainty-weighs-on-pln-against-euro-commerzbank-202610270831 (accessed 2026-11-02, via search summary)
4. https://www.fxstreet.com/news/polish-zloty-near-term-eur-pln-forecast-raised-to-430-commerzbank-202608070950 (accessed 2026-11-02)
5. https://www.tmgm.com/de/analysis/market-news/article/polish-zloty-exposed-as-nbp-delays-tightening-ing-202610150815 (accessed 2026-11-02)
6. https://finwire.pl/artykuly/decyzja-rpp-4-listopada-2026-prognoza (accessed 2026-11-02)
7. https://finwire.pl/artykuly/glapinski-trybunal-stanu-2026-osiem-zarzutow-kok-nbp-glosowanie-listopad (accessed 2026-11-02)
8. https://polandinsight.com/a-new-phase-in-the-power-struggle-over-the-national-bank-of-polands-management-board-18728/ (accessed 2026-11-02)
9. https://www.bluegamma.io/forex/eurpln-forward-rates-spot-and-curve (accessed 2026-11-02)

**Question**: [What will the National Bank of Poland's EUR/PLN reference rate be on 13 November 2026?](https://www.metaculus.com/questions/46400/)
**Date**: 2026-11-02
**Forecast**: Median 4.410 PLN, IQR [4.382 PLN, 4.438 PLN]
**Thesis**: Random-walk from the 2 Nov fixing of 4.4185 (9 business days, sd ≈0.045), shaved slightly for partial reversion of recent spikes and bank forecasts below spot, with fat upper tail for NBP board/MPC institutional risk on 3–4 Nov.
