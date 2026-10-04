# Research log — Will 2027 be the warmest year on record, according to NASA?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

The shared evidence sweep (GISTEMP, ERA5, CPC, Carbon Brief, Berkeley, markets) is logged in the
2026 sibling's research.md: `../2026-10-04-mc21095-nasa-warmest-year-on-record-2026/research.md`.

## Question mechanics

- Resolution source: NASA GISTEMP v4 annual, announced around 2028-01-15. 2027 must beat max(2024 = 1.29, 2026 ≈ 1.29 ± 0.02).
- Release schedule / cutoff: monthly GISTEMP around the 10th–15th; annual mid-January 2028.
- Edge cases and ambiguities: NASA's "tied" language for margins ≤ 0.02 °C (2020 vs 2016; 2025 vs 2023). This only matters in the left tail here.
- Subquestion 45424 was added to the group on 2026-08-18. The Metaculus community has had little time on it.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Year after a strong El Niño onset year sets a GISTEMP record | 3 clean (1998, 2016, 2024) + 1983 (volcanic) | 1983–2024 | 3/3 clean | GISTEMP graph.txt | yes |
| Margin over the onset year | 3 | — | +0.14, +0.11, +0.12 °C | graph.txt | yes |
| GISTEMP record years, unconditional | 30 | 1996–2025 | ~30% | graph.txt | no |

## Decomposition

Annual model, `mc_future`; spec kept here because raw/ holds data only:
- T_y = A26 − β·0.12 + s·(y − 2026) + β·R_y + u_y + v_y + solar_y, where A26 ~ N(1.294, 0.019) from the 2026 nowcast.
- s ~ N(0.032, 0.007); β = 0.09; R_2027 ~ N(1.1, 0.35); R_2028 ~ N(−0.5, 0.6); R_2029, R_2030 = 0.2·R_prev + N(0, 0.75).
- u AR(1), ρ = 0.3, sd 0.055; volcano: 2%/yr, −U(0.1, 0.35) °C, halving each year; solar −0.012 °C/yr from 2026.
- Record mapping uses 2-dp differences vs the prior max: ≥ +0.03 → 0.97; +0.01/+0.02 → 0.80; 0 → 0.5; < 0 → 0.01.

| Variant | P(YES 2027) | strict | median 2027 |
|---|---|---|---|
| central | 0.897 | 0.924 | 1.400 |
| trend 0.022 | 0.876 | 0.902 | 1.390 |
| trend 0.040 | 0.910 | 0.938 | 1.408 |
| β 0.07 | 0.864 | 0.889 | 1.381 |
| β 0.12 | 0.924 | 0.952 | 1.430 |
| R_2027 = 0.7 | 0.801 | 0.821 | 1.364 |
| no solar | 0.916 | 0.944 | 1.412 |
| noise sd 0.075 | 0.853 | 0.877 | 1.400 |

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-04 | Carbon Brief 2026-07-24 | 2027 ~1.71 °C above pre-industrial (90%: 1.49–1.93); 92% record | anchor |
| 2026-10-04 | Hausfather 2026-08-03 | 91% | anchor |
| 2026-10-04 | WMO decadal 2026-05-28 | 86% any year 2026–30 > 2024; 2027 named as likely | consistent |
| 2026-10-04 | CPC 2026-09-10; Carbon Brief 2026-09-21 | very strong / historic El Niño; peak ~4.1 °C in Nov | up |
| 2026-10-04 | "El Niño 2027 forecast La Niña transition" | press: super El Niños often flip to La Niña by mid-following-year (FOX Weather video; Newsweek) | small down (H2 2027) |
| 2026-10-04 | Kalshi KXGTEMP-27 | mislabelled duplicate of the 2026 market | no 2027 market |

## Dead ends and ruled-out hypotheses

- No Kalshi / Polymarket market for 2027 as of 2026-10-04.
- Metaculus aggregations: 403 (see the 2026 sibling).

## Open questions to chase next time

- CPC Nov/Dec 2026 discussions: timing of the El Niño decay, La Niña odds for JAS 2027.
- NASA annual 2026 value (sets the bar).
- Any Metaculus CP once fetchable.
