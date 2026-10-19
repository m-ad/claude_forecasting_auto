# Will the 2026 Eastern Pacific hurricane season's accumulated cyclone energy exceed 350 units as of October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46128/ |
| **Tournament** | minibench — one shot, window 2026-10-19T02:21:37Z -> 2026-10-19T05:21:37Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-29 |
| **Status** | closed |
| **Current forecast** | Median 60.0%, IQR [48.0%, 72.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES if the "Current Season Northeast Pacific Ocean ACE" total on Colorado State University's (CSU) real-time page for the Northeast Pacific is **strictly greater than 350.0** when read on 2026-10-29. Accumulated cyclone energy (ACE) is the sum of squared 6-hourly maximum winds (kt²/10⁴) while a system is at least a tropical storm. The CSU "Northeast Pacific" total includes the Central Pacific (the question's 336.7 for Oct 16 only matches the combined Eastern plus Central Pacific figure). If CSU is not updated, its latest displayed value counts. If CSU is gone for good, Climatlas is the fallback. So the question is whether Hurricane Trudy's remaining life plus any new storm adds enough ACE, as recorded by roughly Oct 28–29, to push the total past 350.0.

### Outside view

No clean reference class exists: this is a running total near a threshold, ten days out. The useful prior is climatology for the late season. Eastern Pacific ACE after about Oct 20 is usually a few units, and in hyperactive El Niño years (1997, 2015, 2018) it is typically around 5–20, driven by one or two late storms. With the total at 343.1 and Trudy dying, the question reduces to "will a new storm in the next ~9 days produce about 4+ ACE?" In active El Niño seasons, a late-October system that the National Hurricane Center (NHC) rates high-chance usually becomes a named storm, and often a hurricane. That gives a prior of roughly 50–60%.

### Inside view

- **Current total.** Climatlas shows Northeast Pacific ACE at **343.1** ("data through 2026-10-19", generated 01:46Z Oct 19) [3]. Wikipedia also quotes 343.1, as Eastern Pacific 235.0 plus Central Pacific 108.1 [2].
- **Is 343.1 up to date?** Starting from the question's 336.7 (Oct 16) and adding Trudy's 6-hourly fixes, 343.1 fits data through about 18Z Oct 18 (my main case, ~70%). It also fits data through about 18Z Oct 17 (~30%), which would leave about 6 more Trudy units uncounted.
- **Trudy's remaining ACE.** The NHC discussion at 21Z Oct 18 has Trudy at 85 kt, then 80 kt (12h), 65 kt (24h), 50 kt (36h) and 40 kt (48h). It becomes post-tropical by 60h, possibly sooner, under rising shear and dry air [4]. That is about **2.5–3.4 more ACE**, so the total after Trudy is about **346–346.5** in the main case and about **352** in the stale case.
- **New system.** The NHC 7-day formation chance for the low south of Guatemala and El Salvador is **90%** (20% in 48h). A depression is expected around midweek (~Oct 21–22), moving W–WNW and staying well offshore [5], which means open warm water in an El Niño year. Reaching ~4 ACE by Oct 28 needs either a tropical storm averaging ~45 kt for ~5 days, or a short-lived hurricane.
- **Model.** P(named storm with enough time) ≈ 0.75 × P(≥ ~4.5 ACE before reading | named) ≈ 0.65, plus small extras (a second system), gives ≈ 0.50 in the main case. The stale case gives ≈ 0.90. Combined: 0.7 × 0.50 + 0.3 × 0.90 ≈ **0.62**. I shade to **0.60** for CSU vs Climatlas differences and a possible update lag in CSU's page.

### Evidence

- 2026-10-19: Climatlas summary: Northeast Pacific (EPAC) ACE 343.1, 298% of normal, 22 named storms / 12 hurricanes / 10 major hurricanes, "record-high pace", Trudy (EP21) active [3].
- 2026-10-19 (page accessed): Wikipedia: combined Pacific ACE 343.1 "as of October 17" (Eastern Pacific 235.0 + Central Pacific 108.1). Trudy is the only active storm [2].
- Question background: CSU and Ryan Maue's Climatlas at ~336.7 on Oct 16. The 2018 record (~318) was passed in mid-October [1].
- NHC discussion #18, 21Z Oct 17: Trudy at 85 kt, forecast 90 kt at 06Z Oct 18 [6]. AFP, Oct 16: Trudy weakened from Category 3 to Category 1 [7].
- NHC discussion #22, 21Z Oct 18: 85 kt, rapid weakening from ~12h, post-tropical by 60h, dissipated by 96h [4].
- NHC outlook, 2333Z Oct 18: 20% / 90% formation chance for the low south of Guatemala; a depression is likely midweek [5].
- I could not fetch the CSU page itself (HTTP 403).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | |
| Kalshi / Polymarket / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

- **Which data 343.1 covers.** If it predates Trudy's Oct 18 fixes, YES is very likely (~0.9). If it already includes 00Z Oct 19, the margin left is ~4.5 units.
- **The new disturbance.** If it develops late (after ~Oct 24), stays a weak tropical storm, or never forms, the answer is NO. If it becomes a hurricane by ~Oct 25, YES is nearly certain.

### Sources

1. Metaculus question 46128, text cached in `raw/metaculus-question-2026-10-19.json`: https://www.metaculus.com/questions/46128/ (accessed 2026-10-19)
2. Wikipedia, "2026 Pacific hurricane season": https://en.wikipedia.org/wiki/2026_Pacific_hurricane_season (accessed 2026-10-19)
3. Climatlas tropical summary: https://climatlas.com/tropical/summary.txt (accessed 2026-10-19)
4. NHC, Hurricane Trudy Discussion #22, 21Z Oct 18: https://www.nhc.noaa.gov/text/MIATCDEP1.shtml (accessed 2026-10-19)
5. NHC Eastern North Pacific Tropical Weather Outlook, 2333Z Oct 18: https://www.nhc.noaa.gov/text/MIATWOEP.shtml (accessed 2026-10-19)
6. NHC, Hurricane Trudy Discussion #18: https://www.nhc.noaa.gov/archive/2026/ep21/ep212026.discus.018.shtml (accessed 2026-10-19)
7. crhoy.com / AFP, "México espera lluvias y oleaje por el poderoso huracán Trudy": https://crhoy.com/mundo/mexico-espera-lluvias-y-oleaje-por-el-poderoso-huracan-trudy/ (accessed 2026-10-19)
8. CSU real-time page (resolution source; returned 403 to me): https://tropical.atmos.colostate.edu/Realtime/index.php?loc=northeastpacific (accessed 2026-10-19)

**Question**: [Will the 2026 Eastern Pacific hurricane season's accumulated cyclone energy exceed 350 units as of October 29, 2026?](https://www.metaculus.com/questions/46128/)
**Date**: 2026-10-19
**Forecast**: Median 60.0%, IQR [48.0%, 72.0%]
**Thesis**: Northeast Pacific ACE is 343.1 (Climatlas, Oct 19), and the dying Hurricane Trudy should add only ~3 more units (NHC). That leaves the total near 346, so YES most likely needs the low south of Guatemala (NHC: 90% 7-day formation chance) to become a tropical storm or hurricane worth ~4+ ACE before Oct 29. The forecast is most sensitive to whether 343.1 already includes Trudy's Oct 18 fixes.
