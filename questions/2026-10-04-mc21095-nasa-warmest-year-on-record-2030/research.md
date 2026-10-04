# Research log — Will 2030 be the warmest year on record, according to NASA?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

The shared evidence sweep is logged in the 2026 sibling's research.md:
`../2026-10-04-mc21095-nasa-warmest-year-on-record-2026/research.md`. The annual Monte Carlo spec is in
the 2027 sibling's research.md.

## Question mechanics

- Resolution source: NASA GISTEMP v4 annual for 2030, announced around 2031-01-15. 2030 must beat every year through 2029, including the 2027 super-El-Niño year.
- Release schedule / cutoff: annual mid-January 2031.
- Edge cases and ambiguities: NASA's "tied" language at ≤ 0.02 °C; GISS institutional continuity over 4+ years (budget cuts proposed in 2025; a building eviction reported in 2025). Speculative risk that the series is discontinued or rebranded; if so, Metaculus might annul rather than resolve NO.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| GISTEMP record years, unconditional | 30 | 1996–2025 | ~30% | graph.txt | yes (upper anchor) |
| 3 years after a super-El-Niño peak year | 2 (2001, 2019) | 1998–2019 | 0/2 | graph.txt | yes (lower anchor) |
| Record-to-record gaps after a super El Niño | 2 | — | 7 yr (1998 → 2005); 4 yr to a tie, 7 to a clear record (2016 → 2020/2023) | graph.txt | context |

## Decomposition

Monte Carlo (spec in the 2027 sibling):

| Variant | P(YES 2030) | median 2030 |
|---|---|---|
| central | 0.260 | 1.355 |
| trend 0.022 | 0.190 | 1.316 |
| trend 0.040 | 0.324 | 1.388 |
| β 0.07 | 0.298 | 1.359 |
| β 0.12 | 0.218 | 1.351 |
| R_2027 = 0.7 | 0.328 | 1.356 |
| no solar | 0.356 | 1.404 |
| noise 0.075 | 0.267 | 1.356 |

ENSO-scenario cross-check: 0.25·0.60 + 0.45·0.22 + 0.30·0.08 ≈ 0.27.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-04 | Manifold search "warmest year record" | "Will 2030 be the warmest year on record?" 33%, 23 bettors | discounted comparison |
| 2026-10-04 | WMO decadal 2026–2030 | 86% any year > 2024; 2026–30 range 1.3–1.9 °C above pre-industrial | weak |
| 2026-10-04 | IGCC 2025 | 0.27 [0.2–0.4] °C/decade human-induced | trend prior |

## Dead ends and ruled-out hypotheses

- No real-money market on 2030 found.

## Open questions to chase next time

- 2026 and 2027 annual values (they set the bar).
- Literature on the solar-cycle-25 amplitude and its expected 2030 minimum effect on GMST (the size of the −0.012 °C/yr assumption).
- Post-2027 ENSO outlooks (beyond about 9 months these have little skill).
