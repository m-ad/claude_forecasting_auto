# What will France's provisional year-on-year CPI inflation be for November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46598/ |
| **Tournament** | minibench — one shot, window 2026-11-16T20:07:30Z -> 2026-11-16T23:07:30Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 3.15, IQR [3.03, 3.27] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the headline year-on-year change in the French national CPI (IPC, all households, France) for November 2026. That is the figure in the title of INSEE's *provisional* release on 27 November 2026 at 08:45 CET, as first published. It is not the HICP (the EU-harmonised index), not the month-on-month figure, and not the definitive 11 December figure. The outcome is discrete in 0.1-point steps. The bounds are 2.95–4.55 and both are open. Arithmetic: the last print is October 2026 at +3.4% y/y. November is one month later. The y/y change from October to November is roughly November 2026 m/m minus November 2025 m/m. The base month, November 2025, was **−0.2% m/m** (definitive), with energy +1.3% and petroleum products +2.7%. If November 2026 m/m comes in at −0.2%, the rate stays at 3.4%. Each 0.1 pt of m/m below −0.2% takes about 0.1 pt off the y/y rate.

### Outside view

There is no clean reference class. The status quo is the last print, 3.4%. In 2026 the rate has moved by 0.0 to +0.7 pt a month during the energy shock. A typical month-to-month change in French y/y CPI is ±0.2–0.3 pt. Naive persistence gives 3.4 ± 0.3.

### Inside view

Decomposition by contribution, using INSEE's 2026 weights (energy 764/10,000, petroleum products 370):

| Component | Nov 2025 m/m contribution | Nov 2026 m/m contribution (est.) |
|---|---|---|
| Petroleum products | +2.7% × ~3.7% ≈ +0.10 pt | −5.5% (range −3.5 to −7) × ~4.8% effective weight* ≈ −0.26 pt |
| Gas / electricity | ≈ 0 | gas reference price +6.6% (indexed offers only) ≈ +0.07 pt; regulated electricity tariff unchanged |
| Ex-energy (seasonal fall in transport services, food) | ≈ −0.30 pt | assume similar, −0.30 ± 0.15 pt |
| **Total m/m** | **−0.2%** | **≈ −0.45%** |

*Weights are set at 2025 prices. Petroleum prices are about 35% above 2025 levels, which raises their effective share.

Diesel averaged 2.342 €/L in October [5] and about 2.18–2.21 €/L in 6–11 November [3][4], down ~6–7%. That followed the 23 October strategic-stock decree and a ~16% weekly drop in Brent to ~$92 [6]. E10 is down ~3–4%. Implied y/y: 3.4 + (−0.45 − (−0.2)) ≈ **3.15**. Uncertainty comes from the unrounded October rate (±0.05), the effective weights, late-November pump prices, transport services and fresh food. The combined standard deviation is about 0.18 pt. The lower bound is open, so values below 2.95 are allowed.

### Evidence

- INSEE, October 2026 provisional release: 3.4% y/y, +0.4% m/m, energy +24.1% y/y, 2026 weights [1][2].
- INSEE, November 2025 definitive release: −0.2% m/m, 0.9% y/y; energy +1.3% m/m, petroleum products +2.7%, services −0.5% (transport −5.4%) [8].
- Official weekly survey (DGEC, the energy directorate), 6 November 2026: diesel 2.178 €/L, against 2.371 a week earlier [4]. Over the month, prix-carburant.eu shows diesel −5.6% and E10 −3.3% [5].
- Brent settled at $92.57 on 9 November and was ~$92 on 11 November, after ~$107 at the start of the month [6].
- The gas reference price rose 6.6% on 1 November to 194.90 €/MWh. The next rise, +5.8% on 1 December, falls outside the reference period [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Kalshi (France CPI prelim series) | no November 2026 market found | 2026-11-16 | |
| Economist consensus | not found for November | 2026-11-16 | |

### What would change my mind

- **Pump prices in the second half of November.** If Brent rebounds to $105+ and diesel goes back above 2.30 €/L, the petroleum drag halves and the rate rises toward 3.3–3.4.
- **The effective weight of petroleum products.** If it is nearer 3.7% than 4.8%, add about 0.05 pt.
- **Transport services.** Airfares could fall less than their usual November seasonal drop.

### Sources

1. INSEE, IPC provisional October 2026 (EN), https://www.insee.fr/en/statistiques/9107975 (accessed 2026-11-16)
2. INSEE, IR266 IPC prov oct26 PDF, https://www.insee.fr/fr/statistiques/fichier/version-html/9107965/IR266_IPCprov_oct26.pdf (accessed 2026-11-16)
3. Connaissance des énergies / AFP, diesel fall early November 2026, https://www.connaissancedesenergies.org/afp/carburants-la-baisse-du-prix-du-gazole-debut-novembre-loin-de-compenser-la-hausse-depuis-fevrier-261110 (accessed 2026-11-16)
4. Selectra, official diesel survey 6 November, https://selectra.info/energie/actualites/marche/gazole-releve-officiel-6-novembre-prix-debut-aout (accessed 2026-11-16)
5. prix-carburant.eu, diesel after strategic-stock release, https://prix-carburant.eu/article/baisse-prix-gazole-liberation-stocks-strategiques (accessed 2026-11-16); October barometer https://prix-carburant.eu/barometre-mensuel-2026-10 (accessed 2026-11-16)
6. Nation Thailand, Brent after 9 November settlement, https://www.nationthailand.com/news/world/40073309 (accessed 2026-11-16)
7. JeChange, gas reference price +6.6% on 1 November 2026, https://www.jechange.fr/energie/gaz/news/prix-repere-gaz-troisieme-hausse-6-6-pourcent-1er-novembre-2026-record (accessed 2026-11-16)
8. INSEE, IPC definitive November 2025, https://www.insee.fr/fr/statistiques/8681584 (accessed 2026-11-16)

**Question**: [What will France's provisional year-on-year CPI inflation be for November 2026?](https://www.metaculus.com/questions/46598/)
**Date**: 2026-11-16
**Forecast**: Median 3.15%, IQR [3.03%, 3.27%]
**Thesis**: The last print is 3.4% (October). In November 2025, the base month, petroleum products rose 2.7% m/m. In November 2026, pump prices are down about 5–6% (diesel strategic-stock release, Brent ~$92), only partly offset by the +6.6% gas reference price, so the y/y rate should ease to about 3.1–3.2%. The forecast is most sensitive to late-November pump prices and to the effective weight of petroleum products.
