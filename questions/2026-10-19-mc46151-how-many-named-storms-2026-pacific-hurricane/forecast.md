# How many named storms will the 2026 Pacific hurricane season have recorded as of October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46151/ |
| **Tournament** | minibench — one shot, window 2026-10-19T18:04:08Z -> 2026-10-19T21:04:08Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 23.1, IQR [22.7, 23.5] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the "Total storms" figure in the season-statistics infobox of the Wikipedia article "2026 Pacific hurricane season", as it stands at 23:59 UTC on 2026-10-29. That figure counts eastern *and* central Pacific named storms. It counts storms named at any point up to that time, whether or not they are still active. The answer can only be 22 or higher (closed lower bound at 22, open upper bound above 26). On 2026-10-19 the infobox reads **22** (19 East Pacific names through Trudy, plus 3 Central Pacific names: Lala, Moke, Nolo) [1]. So the question is really: how many *new* storms get named in the next ~10.2 days? A depression that never reaches tropical-storm strength does not count. Wikipedia usually updates within hours of an NHC advisory, so the risk of a lag only matters for a storm named in the last hours before the cutoff.

### Outside view

East Pacific activity drops off sharply after mid-October. The 1971–2009 cumulative climatology puts the 14th named storm around Oct 11 and the 15th around Nov 5. That works out to about 1 named storm per 3–4 weeks [3]. The recent record is busier. Across 2014–2025, the number of storms named Oct 17–29 was 0 in one year, 1 in seven years and 2 in four years: a mean of 1.25 per 13 days, with no year above 2 [8]. Scaled to the remaining ~10.2 days, that is about 1.0 expected new storm, and P(0) is roughly 0.3–0.35. A record, El Niño-boosted season (ACE ~343, the highest on record for the combined basins [1]) argues for at least that rate. The specific evidence is stronger still: a disturbance the NHC rates at 90% is already on the map.

### Inside view

- **EP94 (would be Vance).** The NHC rates EP94 at 60% for 48 hours and 90% for 7 days as of 11 AM PDT Oct 19. It expects a tropical depression around mid-week, moving W–WNW well south of Mexico in conducive conditions [2]. NHC high-probability genesis bins have historically verified at about the stated rate or better in the East Pacific; later verification found underprediction in the high bins [6]. Not every depression gets named, but this season 22 of 23 did. The system has open water and about 10 days to strengthen. I put P(EP94 becomes a tropical cyclone) ≈ 0.90 and P(it reaches tropical-storm strength | TC) ≈ 0.88, so **P(Vance by Oct 29) ≈ 0.80**. I add about 0.02 for a different, not-yet-flagged system becoming Vance if EP94 fails.
- **A further storm (would be Winnie).** No second area is flagged in the 7-day East Pacific or Central Pacific outlooks [2]. Any extra storm would therefore have to form in roughly Oct 24–29 from a disturbance that does not exist yet. Still, 7-day outlooks often miss systems that form 5–10 days out, and 4 of the last 12 seasons had two storms in this window [8]. I put P(≥1 more beyond Vance) ≈ 0.26 and P(≥2 more) ≈ 0.035.
- **Trudy** is already counted, so its fate does not matter. A downward revision of the count within 10 days is negligible.

Resulting probability mass: 22: 0.16, 23: 0.58, 24: 0.225, 25: 0.03, 26+: 0.005. Interpolated within the integer bins, this gives p5 21.8, p10 22.1, p25 22.7, p50 23.1, p75 23.5, p90 24.2, p95 24.4.

### Evidence

- Wikipedia infobox, accessed 2026-10-19: Total storms 22, total depressions 23. Trudy formed Oct 13 and is still active. Vance and Winnie are listed as unused [1].
- NHC East Pacific Tropical Weather Outlook, 1100 AM PDT Mon Oct 19 2026: EP94, several hundred miles SSW of Guatemala, 60% / 90%, with a "tropical depression expected to form around the middle of the week". The Central Pacific has no areas of interest; no formation is expected in 7 days [2].
- NHC home page, 8 AM MST Oct 19: TS Trudy at 60 mph, 999 mb, near 19.5N 108.5W [4].
- Trudy peaked at Category 3 on Oct 16 and was the 10th major hurricane of the season [5].
- 1971–2009 climatology: average dates of the 14th storm (~Oct 11) and 15th storm (~Nov 5) [3].
- Storms named Oct 17–29, 2014–2025, from Wikipedia season articles: 2014 1 (Trudy), 2015 2 (Olaf, Patricia), 2016 1 (Seymour), 2017 1 (Selma), 2018 2 (Vicente, Willa), 2019 2 (Octave, Priscilla), 2020 0, 2021 1 (Rick), 2022 1 (Roslyn), 2023 2 (Norma, Otis), 2024 1 (Kristy), 2025 1 (Sonia) [8].
- NHC genesis-outlook verification: the high bins verified at ≥60% in 2007–08; later East Pacific verification showed genesis *underpredicted* in the high bins [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Kalshi / Polymarket | no season-count market found | 2026-10-19 | Only stale East Pacific name and hurricane contracts [7] |
| Manifold | none found | 2026-10-19 | — |

### What would change my mind

- **EP94's fate over the next 48–72 hours.** That one event moves about 0.8 of the mass between 22 and 23. A depression that stays weak, or a disturbance that gets absorbed, would push 22 to the mode.
- **A second disturbance appearing in the NHC outlook by Oct 22–24.** That would shift substantial mass to 24.

### Sources

1. Wikipedia, "2026 Pacific hurricane season" — https://en.wikipedia.org/wiki/2026_Pacific_hurricane_season (accessed 2026-10-19)
2. NHC, Eastern Pacific Tropical Weather Outlook, 1100 AM PDT Oct 19 2026 — https://www.nhc.noaa.gov/text/MIATWOEP.shtml and https://www.nhc.noaa.gov/gtwo.php?basin=epac (accessed 2026-10-19)
3. Florida Tech, "Tropical Cyclone Climatology" (NHC 1971–2009 cumulative dates) — https://www.fit.edu/media/site-specific/wwwfitedu/environmental-health-and-safety-ehs/documents/Tropical-Cyclone-Climatology.pdf; NHC climatology — https://www.nhc.noaa.gov/climo/ (accessed 2026-10-19)
4. NHC home page, TS Trudy Public Advisory #25 — https://www.nhc.noaa.gov/ (accessed 2026-10-19)
5. ITV News, "Hurricane Trudy strengthens to a Category 3 storm off Mexico's Pacific coast", 2026-10-16 — https://www.itv.com/news/2026-10-16/trudy-strengthens-to-category-3-hurricane-off-mexican-coast (accessed 2026-10-19)
6. NHC Joint Hurricane Testbed, Hart & Fuelberg genesis-verification reports — https://www.nhc.noaa.gov/jht/13-15reports/Final_HartFuelberg_JHT15.pdf; NHC, "About the GTWO" — https://www.nhc.noaa.gov/aboutgtwo/aboutgtwo4.shtml (accessed 2026-10-19)
7. SimpleFunctions Kalshi mirror, East Pacific hurricane-name markets — https://simplefunctions.dev/answer/hurricanenames (accessed 2026-10-19)
8. Wikipedia, 2014–2025 Pacific hurricane season articles and timelines, e.g. https://en.wikipedia.org/wiki/2023_Pacific_hurricane_season and https://en.wikipedia.org/wiki/Timeline_of_the_2015_Pacific_hurricane_season (accessed 2026-10-19)

**Question**: [How many named storms will the 2026 Pacific hurricane season have recorded as of October 29, 2026?](https://www.metaculus.com/questions/46151/)
**Date**: 2026-10-19
**Forecast**: Median 23.1 named storms, IQR [22.7, 23.5]
**Thesis**: The count is 22 on Wikipedia today. The NHC gives disturbance EP94 a 90% chance of forming within 7 days, so Vance (the 23rd storm) is likely by Oct 29, at about 82%. Since 2014, 1–2 storms have been named in Oct 17–29 in 11 of 12 seasons, but no second area is flagged yet, so a 24th storm sits at about 26%. The forecast depends most on whether EP94 actually reaches tropical-storm strength.
