# Which band will Rosstat's October 2026 annual CPI inflation figure fall into?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46383/ |
| **Tournament** | minibench — one shot, window 2026-11-02T05:59:35Z -> 2026-11-02T08:59:35Z |
| **Type** | multiple_choice |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 26.5%, IQR [20.0%, 33.0%] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves on the October 2026 index as a percentage of October 2025, from Rosstat's monthly release "Об индексе потребительских цен в октябре 2026 года" (due 13 Nov 2026). The bands are: below 6.90; 6.90–6.99; 7.00–7.09; 7.10–7.19; 7.20–7.29; 7.30 or more. Weekly-based estimates do not count. The arithmetic is mechanical once October's month-on-month (m/m) figure is known, because September's year-on-year (y/y) figure is fixed at 6.35% and October 2025 was +0.50% m/m:

y/y(Oct) = 1.0635 × (1 + m_Oct26) / 1.0050 − 1

Each 0.1 pp of October m/m moves the annual figure by about 0.106 pp. One band therefore equals about 0.095 pp of m/m.

| October 2026 m/m | Implied y/y | Band |
|---|---|---|
| 0.95% | 6.83% | Below 6.90% |
| 1.05% | 6.93% | 6.90–6.99 |
| 1.15% | 7.04% | 7.00–7.09 |
| 1.25% | 7.15% | 7.10–7.19 |
| 1.35% | 7.25% | 7.20–7.29 |
| 1.45% | 7.36% | 7.30 or above |

Rosstat's weekly data put October-to-date at +1.14% by 26 Oct [1]. The 27 Oct–2 Nov week has not been published yet; at the recent ~0.08%/week pace, 27–31 Oct adds about 0.06. The weekly-implied October m/m is therefore about 1.20%, which maps to **7.09% y/y, right on the 7.00/7.10 boundary**. The Economy Ministry's 7.11% for 26 Oct [1] uses this same method: it interpolates the October 2025 *monthly* figure (check: 1.0635 × 1.0114 / 1.0042 = 7.11%). By month-end it converges on the formula above.

### Outside view

The reference class is how far Rosstat's monthly m/m CPI lands from the cumulative weekly estimate for the same month (monthly minus weekly):

| Month | Weekly cumulative (approx.) | Monthly | Gap |
|---|---|---|---|
| Oct 2024 | 0.73 to 28 Oct + ~0.08 ≈ 0.81 | 0.75 | −0.06 [6] |
| Jul 2025 (tariff month) | 0.65 | 0.57 | −0.08 [5] |
| Oct 2025 | 0.79 to 27 Oct + ~0.07 ≈ 0.86 | 0.50 | ≈ −0.36 [4] |
| Aug 2026 | −0.08 | −0.08 | 0.00 [7] |
| Sep 2026 | ~0.30 | 0.35 | +0.05 [8] |

The mean is about −0.09 pp and the spread about 0.17 pp. The monthly figure covers about 500 items against the weekly basket's 110, and in October it tends to pick up seasonal falls in fruit and vegetables and in services such as travel. Two Octobers in a row came in below the weeklies.

### Inside view

Model (`model.py`): weekly-implied m/m ~ N(1.20, 0.03) plus a monthly−weekly gap drawn from a t-distribution with 5 degrees of freedom, centred at −0.06 to −0.10 with scale 0.15–0.16, mapped through the formula above and rounded to two decimals. I blended the two runs. Median 7.01% y/y; IQR roughly [6.88%, 7.13%].

- The tariff indexation of 1 Oct (+0.96% in the week of 29 Sep–5 Oct) is fully inside October in both baskets. It is not a source of gap in itself, but July 2025, also a tariff month, came in 0.08 below the weeklies.
- Late October was soft: petrol fell 0.7% in the week of 13–19 Oct and 1.63% in the week of 20–26 Oct; non-food fell 0.21% in the week of 20–26 Oct [1][9]. That softness supports a negative gap. Services were running at about 11% y/y, which supports a positive one [1].
- I give extra weight to the October 2025 gap (−0.36). The Central Bank's 6.8% "as of 19 October" [3] matches a calculation against the October 2025 *weekly* base (1.0635 × 1.0106 / 1.0063 = 6.81%). That match confirms the 2025 weeklies overstated the 2025 monthly by roughly 0.3 pp.

### Evidence

- 20–26 Oct 2026: weekly CPI +0.08%, October-to-date 1.14%, year-to-date 6.24%; Economy Ministry annual estimate 7.11% (7.15% a week earlier, 7.22% on 12 Oct) [1].
- 29 Sep–5 Oct 2026: +0.96% on the utility tariff indexation; Economy Ministry annual estimate 7.17% before the September revision [2].
- September 2026: 0.35% m/m (analysts' consensus 0.27%, weeklies ~0.30%), 6.35% y/y; August −0.08% m/m, 6.33% y/y [7][8].
- October 2025: 0.50% m/m, 7.71% y/y [4]; October 2025 weeklies summed to 0.79% by 27 Oct [4].
- On 23 Oct 2026 the Central Bank held its key rate at 14% and raised its 2026 forecast to 7.1–7.6% [3]. Its 32-analyst October survey has 7.1% for 2026 [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-02 | Kalshi lists Russian unemployment only |
| Economy Ministry weekly-based y/y | 7.11% | 26 Oct 2026 | same arithmetic as the resolution figure, but uses weekly prices for 2026 |
| Central Bank y/y (weekly 2025 base) | 6.8% | 19 Oct 2026 | not comparable: uses 2025 weeklies as the base |

### What would change my mind

- **The 27 Oct–2 Nov weekly print (6 Nov).** A reading of 0.15% or more would add about 0.05 pp and shift the mass up about half a band. A reading of zero or less would shift it down.
- **Evidence of why October 2025's monthly figure fell 0.36 below the weeklies.** If it was a one-off, such as a statistical artefact or a specific services item, the gap centre should be nearer 0 and the 7.00–7.19 bands gain.

### Sources

1. AK&M, "Inflation in the Russian Federation since the beginning of October has been 1.14%", https://www.akm.ru/eng/news/inflation-in-the-russian-federation-since-the-beginning-of-october-has-been-1-14-/ (accessed 2026-11-02)
2. TASS, weekly CPI 29 Sep–5 Oct 2026, https://tass.com/economy/2198963 (accessed 2026-11-02)
3. Ukrainska Pravda, "Russia raises inflation forecast for 2026", https://www.pravda.com.ua/eng/news/2026/10/23/8059419/ (accessed 2026-11-02)
4. Ruinformer / finance.mail.ru, October 2025 CPI 0.50% m/m, 7.71% y/y, https://ruinformer.com/page/v-centrobanke-rf-nazvali-glavnye-prichiny-zamedlenija-infljacii-v-nojabre ; https://finance.mail.ru/article/inflyaciya-v-rf-s-14-po-20-oktyabrya-sostavila-0-22-68419967/ ; https://investfuture.ru/articles/analiziruem-inflyatsiyu-i-kolebaniya-tsen-v-rossii-za-nedelyu-s-21-po-27-oktyabrya-2025-goda-1169282141 (accessed 2026-11-02)
5. Moscow Times / investfunds, July 2025 CPI 0.57% vs weekly 0.65%, https://ru.themoscowtimes.com/2025/08/13/rost-potrebitelskikh-tsen-v-rf-v-iyule-uskorilsya-do-057-na-fone-indeksatsii-tarifov-a171551 (accessed 2026-11-02)
6. Interfax, weekly CPI 22–28 Oct 2024 and October 2024 0.75%, https://www.interfax.ru/business/989419 ; https://www.interfax.ru/business/992542 (accessed 2026-11-02)
7. investfuture, August 2026 deflation −0.08%, https://investfuture.ru/articles/rosstat-zafiksiroval-deflyatsiyu-v-rossii-v-avguste-na-urovne-0-08-1186106669 (accessed 2026-11-02)
8. Moscow Times, September 2026 CPI 0.35%, https://ru.themoscowtimes.com/2026/10/09/rosstat-otsenil-inflyatsiyu-v-rf-v-sentyabre-v-035-a208261 ; Interfax, https://interfax.com/newsroom/top-stories/119479/ (accessed 2026-11-02)
9. Moscow Times, petrol −0.7% in 13–19 Oct 2026, https://ru.themoscowtimes.com/2026/10/21/roznichnye-tseny-na-benzin-v-rf-snizilis-na-07-za-13-19-okt-rosstat-a209211 (accessed 2026-11-02)

**Question**: [Which band will Rosstat's October 2026 annual CPI inflation figure fall into?](https://www.metaculus.com/questions/46383/)
**Date**: 2026-11-02
**Forecast**: Median 26.5% (Below 6.90%), IQR [20.0%, 33.0%]
**Thesis**: The weekly data (October-to-date +1.14% by 26 Oct) imply about 1.20% m/m for October, which maps to ~7.09% y/y against October 2025's +0.50%. Rosstat's monthly figure has tended to land below the weeklies (−0.06 to −0.36 pp; two Octobers in a row), so the distribution centres near 7.0% with roughly 0.2 pp of spread: Below 6.90 26.5%, 6.90–6.99 20.5%, 7.00–7.09 21.5%, 7.10–7.19 15.5%, 7.20–7.29 9%, ≥7.30 7%. The result is most sensitive to the monthly−weekly gap.
