# What will the Northern Sierra 8-Station Precipitation Index be for November 26, 2026 (water-year-to-date, inches)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46594/ |
| **Tournament** | minibench — one shot, window 2026-11-16T16:38:29Z -> 2026-11-16T19:38:29Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | resolved |
| **Current forecast** | Median 8.4, IQR [7.2, 9.8] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the cumulative water-year 'RAIN' value (inches) that CDEC first publishes for station 8SI on the row dated 11/26/2026. Later revisions don't count. The question's range runs from 1 to 16 in, and both bounds are open. The last row published (fetched 2026-11-16 around 17:10Z) is 11/16 = 3.44 in: 0.72 on 11/13, +1.43 on 11/14, +0.07 on 11/15 and +1.22 on 11/16 [1]. The question text quotes 0.72 in, which is now stale. From the 11/16 row to the 11/26 row there are 10 more daily increments (11/17–11/26), so the answer is 3.44 + the precipitation of those 10 days, plus any part of today's rain still to post. The index can only rise, so the resolution is at least 3.44.

### Outside view

The 1991–2020 November average for the 8SI is about 5.3 in, or roughly 0.18 in/day [6]. A climatological 10-day increment is about 1.8 in, which gives a status-quo median near 5.2 in. Late-November 10-day totals are very skewed: anywhere from 0 to more than 8 in.

### Inside view

The forecast is conditioned on three pieces:
- **Rest of the Nov 15–16 storm.** NWS Sacramento expected another 1.0–1.5 in at Sierra points on Monday [2]. Part of this is probably already in the 1.22 in on the 11/16 row. I add +0.5 in (range 0.2–0.9) to the index.
- **Tuesday night to Friday morning storm.** NWS gives 2–3.5 in liquid over the mountains, slightly decreased in the north [2]. KCRA says this storm will bring the highest totals so far [3]. A Winter Storm Watch is up for the northern Sierra [4]. For the Nov 13–14 storm, NWS forecast 1–3 in and the index gained 1.43, so the index runs at about the midpoint of the NWS mountain range. I add +2.5 in (range 1.3–3.5).
- **Nov 20–26.** NWS has "increasing confidence" that an active pattern returns at the weekend and continues into Thanksgiving week [2]. CPC's 8–14 day outlook favours above-normal precipitation [5]. I add +2.0 in, with a wide range of 0.3–5.

Total: 3.44 + 0.5 + 2.5 + 2.0 ≈ 8.4 in. The distribution is skewed to the right, and the floor is about 4.5 in, which is practically certain to be exceeded.

### Evidence

- CDEC 8SI daily, fetched 2026-11-16: the Nov 14 storm added 1.43 in, Nov 16 (so far) added 1.22 in, and the cumulative is 3.44 in [1].
- NWS STO Area Forecast Discussion, 03:48 PST 2026-11-16: today 1.0–1.5 in in the Sierra. Tuesday night to Friday morning 2–3.5 in. An active pattern from the weekend into Thanksgiving week [2].
- KCRA, Nov 14–16: Wednesday–Thursday is an Impact Day, with foothills 2–3 in and the highest totals so far [3]. Winter Storm Watch for the N Sierra from Tuesday evening to early Friday, 1–2 ft of snow above 5,000 ft [4].
- CPC 8–14 day outlook, issued Nov 14: above-normal precipitation favoured in California for Thanksgiving week [5]. The Nov 15 6–10 day discussion was only partly readable and possibly mixed.
- November 2025 total: 7.7 in against an average of 5.3 (145%) [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | none found | 2026-11-16 | only daily city rain markets |
| NWS STO | 2–3.5 in mountains Tue–Fri | 2026-11-16 | point amounts, not the index |

### What would change my mind

The biggest assumption is that Nov 20–26 stays active and adds about 2 in. A drying ridge after Friday would pull the outcome toward about 6.5 in. A second atmospheric river (AR) over Thanksgiving week could push it past 12 in. The midweek storm verifying low (under 1.5 in on the index) would also take about 1 in off the median.

### Sources

1. CDEC 8SI daily data, https://cdec.water.ca.gov/dynamicapp/QueryDaily?end=2026-11-16&s=8SI (accessed 2026-11-16)
2. NWS Sacramento Area Forecast Discussion, https://forecast.weather.gov/product.php?site=STO&issuedby=STO&product=AFD (accessed 2026-11-16)
3. KCRA, live updates Nov 16, https://www.kcra.com/article/northern-california-rain-snow-updates-november-16/74439964 (accessed 2026-11-16)
4. myMotherLode, Winter Storm Watch, https://mymotherlode.com/news/local/11312048/sierra-nevada-winter-weather-advisory.html (accessed 2026-11-16)
5. Yahoo/USA Today, NOAA Thanksgiving outlook California, https://www.yahoo.com/news/weather-news/articles/thanksgiving-cold-dry-wet-california-160926373.html (accessed 2026-11-16)
6. CDEC 8-Station monthly table, https://cdec.water.ca.gov/cgi-progs/products/TAB_ESI.pdf (accessed 2026-11-16)
7. CW3E AR Outlook 12 Nov 2026, https://cw3e.ucsd.edu/cw3e-ar-outlook-12-november-2026/ (accessed 2026-11-16)

**Question**: [What will the Northern Sierra 8-Station Precipitation Index be for November 26, 2026 (water-year-to-date, inches)?](https://www.metaculus.com/questions/46594/)
**Date**: 2026-11-16
**Forecast**: Median 8.4 in, IQR [7.2 in, 9.8 in]
**Thesis**: CDEC already shows 3.44 in as of 11/16, after two storms. NWS expects 2–3.5 in liquid over the mountains Tuesday–Friday, and CPC favours a wet Thanksgiving week, so the index should gain about 5 in by Nov 26. The outcome depends most on whether Nov 20–26 stays active.

## Resolution — 2026-11-28

Resolved **7.29** (synced from the Metaculus API). The bot's forecast was 8.4 [7.2, 9.8]. Official spot peer score: +18.84.
