# What will be the highest observed water level (ft above MLLW) at NOAA's La Jolla, CA tide gauge (station 9410230) on November 26-27, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46619/ |
| **Tournament** | minibench — one shot, window 2026-11-18T12:34:49Z -> 2026-11-18T15:34:49Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-18 / 2026-11-18 / 2026-11-28 |
| **Status** | open |
| **Current forecast** | Median 8.08, IQR [7.88, 8.27] (v1, 2026-11-18) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-18

### What resolves YES

The maximum preliminary 6-minute observed water level (ft, MLLW) at NOAA station 9410230 (La Jolla) from 2026-11-26 00:00 to 2026-11-27 23:59 PST. Two morning high tides are in the window: predicted 6.838 ft at 09:15 PST on Nov 26 and 6.498 ft at 10:05 PST on Nov 27 (CO-OPS predictions, fetched 2026-11-18 [1]). Nov 26 is 0.34 ft higher, so it almost certainly sets the maximum unless Nov 27's residual is larger by more than that. Resolution ≈ 6.84 + the observed-minus-predicted residual at the Nov 26 high, plus a few hundredths from 6-minute wave noise. The question is annulled if data near either high tide is missing. The range is 6.5–8.8 with both bounds open. For comparison, the October 2026 record was ~7.97 ft MLLW (2.65 ft above MHHW + 5.32 ft), and the record before that was 7.81 ft (2015-11-25) [4].

### Outside view

Reference class: the gauge's daily-maximum residual (observed max minus predicted high) over the past 7 weeks of the same Kelvin-wave regime. The calcoasttides residual table [3] shows La Jolla at +12 to +18 in (1.0–1.5 ft) continuously since early October, and +14.6 to +17.9 in on Nov 10–17. Recent daily-max residuals at the high tide, which I computed from the 6-minute data [2]: Nov 10 +1.41, 11 +1.40, 12 +1.52, 13 +1.57, 14 +1.44, 15 +1.26, 16 +1.26, 17 +1.03, 18 (04:42) +1.19 ft. A persistence baseline gives 6.84 + ~1.25 ≈ 8.1 ft.

### Inside view

- **Persistence:** Kelvin-wave anomalies last for weeks. No source reports the anomaly weakening. NASA JPL's Willis expects sea level to keep rising through the New Year, and a third, stronger wave has reached San Francisco [5][6]. I keep a central residual of ~+1.2 ft. The Nov 15–18 slide from ~1.5 to ~1.1–1.25 ft looks like the end of the Nov 12–14 swell/surge, not decay of the baseline. The 24-hour residual held at +15 in through Nov 17 [3].
- **Downside:** the residual could ease to +0.7–0.9 ft (a calm, high-pressure week) → 7.55–7.75.
- **Upside:** NWS forecasts several swell pulses through Thanksgiving week [7]. Wave setup at Scripps Pier added ~0.2–0.3 ft on Nov 12–13. Residual +1.5–1.8 → 8.35–8.65.
- Distribution: p5 7.50, p10 7.65, p25 7.88, p50 8.08, p75 8.27, p90 8.46, p95 8.60.

### Evidence

- CO-OPS predictions [1]: Nov 25 08:29 6.955 (just outside the window), Nov 26 09:15 6.838, Nov 27 10:05 6.498 ft MLLW.
- CO-OPS observed 6-minute data, Nov 10–18 [2]: daily maxima 7.379, 7.189, 7.058, 6.792, 6.306, 5.726, 5.339, 4.833, 5.348 ft, against predicted highs of 5.973, 5.791, 5.539, 5.227, 4.864, 4.467, 4.079, 3.808, 4.16 ft.
- NOAA NOS [4]: La Jolla reached 2.65 ft above MHHW on Oct 24–30, and NOAA predicts above-normal tides on Nov 22–27.
- NOAA's Dusek: Thanksgiving tides will be about half a foot higher than October's highest [8]. Kelvin-wave lift typically tops out around 18 in [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-18 | |
| Kalshi / Polymarket / Manifold | none found | 2026-11-18 | |
| CBS LA forecaster | 8.4–8.5 ft Thanksgiving-week tides | 2026-11 | different station/datum, not comparable directly |

### What would change my mind

- The residual on the Nov 24–25 morning highs: if it is below +0.8 ft, the median drops toward 7.6; if it is above +1.5 ft, it rises toward 8.35.
- A large west-northwest swell or a storm system arriving on Nov 26 (upside tail).

### Sources

1. https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&interval=hilo&station=9410230&begin_date=20261105&end_date=20261127&datum=MLLW&units=english&time_zone=lst&format=csv (accessed 2026-11-18)
2. https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=water_level&station=9410230&begin_date=20261110&end_date=20261118&datum=MLLW&units=english&time_zone=lst&format=csv (accessed 2026-11-18)
3. https://www.calcoasttides.com/blog/kelvin-wave-california-2026 (accessed 2026-11-18)
4. https://oceanservice.noaa.gov/news/nov26/california-record-water-levels.html (accessed 2026-11-18)
5. https://www.yahoo.com/news/weather-news/articles/californias-flooding-problem-peak-thanksgiving-130000477.html (accessed 2026-11-18)
6. https://www.kpbs.org/news/environment/2026/11/13/this-years-el-nino-is-already-breaking-records (accessed 2026-11-18; search snippet only)
7. https://www.yahoo.com/news/weather-news/articles/king-tides-return-southern-california-192345821.html (accessed 2026-11-18; search snippet only)
8. https://weather.com/2026/10/31/news/climate/thanksgiving-king-tides-california-florida-flooding (accessed 2026-11-18; search snippet only)
9. https://tidesandcurrents.noaa.gov/datums.html?id=9410230 (accessed 2026-11-18; search snippet only)

**Question**: [What will be the highest observed water level (ft above MLLW) at NOAA's La Jolla, CA tide gauge (station 9410230) on November 26-27, 2026?](https://www.metaculus.com/questions/46619/)
**Date**: 2026-11-18
**Forecast**: Median 8.08 ft, IQR [7.88 ft, 8.27 ft]
**Thesis**: The Nov 26 09:15 PST predicted high is 6.84 ft MLLW. Since early October the gauge has run +1.0–1.6 ft above prediction at the high tides (about +1.25 ft on Nov 15–18) because of the El Niño Kelvin wave, and nobody reports it fading. A persistence forecast therefore gives ~8.1 ft. The main sensitivity is whether the residual holds near +1.2 ft or eases or swells over the next 8 days.
