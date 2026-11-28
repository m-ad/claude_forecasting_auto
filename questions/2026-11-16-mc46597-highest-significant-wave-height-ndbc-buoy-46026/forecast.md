# What will be the highest significant wave height at NDBC buoy 46026 (18 NM west of San Francisco) on November 26, 2026 (UTC)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46597/ |
| **Tournament** | minibench — one shot, window 2026-11-16T18:42:35Z -> 2026-11-16T21:42:35Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | resolved |
| **Current forecast** | Median 2.8, IQR [2.3, 3.5] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the largest WVHT value (metres, one decimal place) in the NDBC realtime file `46026.txt` across all rows stamped 2026-11-26 00:00 to 23:50 UTC. Rows with "MM" are ignored, and the question is annulled if the day has no valid value. The target day is 10 days after today (2026-11-16), so it is beyond deterministic swell-forecast skill. The answer is therefore a climatology-plus-regime question. Bounds are 1.0 to 7.0 m and both are open; the 7.0 m upper bound was actually reached on 2026-11-14 [1].

### Outside view

Reference class: daily maximum WVHT at 46026 in late November. I could not retrieve NDBC's historical files (403) or the climatic summary [3]. I therefore rely on the question's stated climatology: typical days peak at 2 to 3.5 m, calm days near 1.5 m, and major groundswell days above 4 to 5 m. I cross-checked this against the buoy's own last 30 days [1]:

- 17 to 24 October: daily maxima of 1.5, 2.2, 2.2, 1.9, 2.0, 1.5, 2.4 and 2.6 m (median about 2.1 m).
- 1 to 16 November: 1.5\*, 1.8, 2.7, 2.9, 2.5, 3.2, 3.4, 3.2, 4.4, 3.1, 2.9, 4.0, 4.5, 7.0, 4.4 and 6.6 m (median about 3.2 m). \*1 November is a partial day.

The seasonal ramp from October to late November pushes the median up. Prior: median about 2.6 m, 10th to 90th percentile about 1.8 to 4.2 m, right-skewed.

### Inside view

- **Active pattern.** Five of the last eight days peaked at 4 m or more. The NWS San Francisco office's area forecast discussion of 16 November [2] expects more long-period swell from 18 November and a rain system from 21 November, with below-normal temperatures through the extended period. The NOAA winter outlook frames 2026-27 as an El Niño winter [4], which favours an active Pacific storm track into California.
- **Limited persistence.** Regime persistence at a 10-day lead is weak, so I moved the median up by only about 0.2 m, to 2.8 m, and fattened the upper tail.
- **Asymmetric tails.** The downside is bounded: in winter, residual swell rarely leaves the daily maximum below 1.6 m. The upside goes to 5 to 7 m in a direct hit, as on 14 November. The distribution is skewed accordingly.

### Evidence

- 46026 realtime file, read 2026-11-16 [1]: daily maxima were 7.0 m on 14 November and 6.6 m on 16 November (at 09:40 UTC), easing to about 4.2 m by 18:20 UTC on the 16th with a 16 to 17 s period.
- NWS MTR area forecast discussion, 10:24 PST on 16 November [2]: "Long period swells 12 to 16 feet high at 14 to 16 seconds"; larger swells arriving from Wednesday 18 November; rain from Saturday 21 November. It gives no outlook for 26 November.
- SF Standard, 6 November 2026 [5]: 12 to 16 ft breakers in an earlier event, confirming an active early season.
- NDBC station status [6]: the buoy is transmitting and its next service is April 2027. Some met sensors have failed but the wave data is flowing, so an annulment is unlikely.
- No 2026 Thanksgiving-week swell or storm forecast was found in any search.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-16 | |
| Kalshi / Polymarket | none found | 2026-11-16 | no wave-height markets |
| Surf forecasters (Surfline, Stormsurf) | none found for 26 Nov | 2026-11-16 | lead time too long |

### What would change my mind

- A large North Pacific low forecast for around 22 to 24 November that aims west-northwest swell at central California would push the median toward 4 m or more.
- A blocking ridge over the northeast Pacific in the week 2 outlook would pull it toward 2 m.
- Historical November data showing that 46026's daily maxima run materially lower than the question's 2 to 3.5 m "typical" range would also lower it.

### Sources

1. https://www.ndbc.noaa.gov/data/realtime2/46026.txt (accessed 2026-11-16)
2. https://forecast.weather.gov/product.php?site=MTR&issuedby=MTR&product=AFD (accessed 2026-11-16)
3. https://www.ndbc.noaa.gov/data/climatic/46026.pdf (accessed 2026-11-16; fetch failed)
4. https://www.usharbors.com/2026/10/el-nino-looms-large-over-u-s-winter-outlook/ (accessed 2026-11-16; search snippet)
5. https://sfstandard.com/2026/11/06/san-francisco-beach-hazard-dangerous-waves/ (accessed 2026-11-16; search snippet)
6. https://www.ndbc.noaa.gov/wstat.shtml (accessed 2026-11-16; search snippet)

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| WVHT (m) | 1.7 | 1.9 | 2.3 | 2.8 | 3.5 | 4.4 | 5.0 |

**Question**: [What will be the highest significant wave height at NDBC buoy 46026 (18 NM west of San Francisco) on November 26, 2026 (UTC)?](https://www.metaculus.com/questions/46597/)
**Date**: 2026-11-16
**Forecast**: Median 2.8 m, IQR [2.3 m, 3.5 m]
**Thesis**: At a 10-day lead this is climatology: a late-November daily maximum WVHT at 46026 is typically 2 to 3.5 m. I nudged it up and fattened the right tail for the very active November swell regime (7.0 m on 14 November and 6.6 m on 16 November in the buoy's own file), an El Niño winter, and more NWS-forecast swell through 22 November. The biggest swing factor is whether a North Pacific storm lines up a west-northwest groundswell for Thanksgiving Day.

## Resolution — 2026-11-28

Resolved **5.7** (synced from the Metaculus API). The bot's forecast was 2.8 [2.3, 3.5]. Official spot peer score: -16.38.
