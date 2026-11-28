# How much precipitation will San Francisco International Airport record on Thanksgiving Day (November 26, 2026)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46587/ |
| **Tournament** | minibench — one shot, window 2026-11-16T13:31:36Z -> 2026-11-16T16:31:36Z |
| **Type** | multiple_choice |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | resolved |
| **Current forecast** | Median 48.0%, IQR [38.0%, 58.0%] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The "YESTERDAY" precipitation value in the NWS CLISFO daily climate report dated 2026-11-27, which covers Thursday 2026-11-26 (Pacific calendar day; the CLI day runs midnight–midnight local standard time) at SFO (USW00023234). A trace ("T") counts as 0.00. Buckets: 0.00 / 0.01–0.09 / 0.10–0.49 / 0.50–0.99 / ≥1.00 in. The target is 10 days out from today (2026-11-16), so this is a medium-range weather question: deterministic skill for a single day at a single station is low, but regime-level signals (CPC hazards, ensemble-mean pattern) carry information.

### Outside view

Climatological daily chance of measurable rain at SFO in late November is ~22–24% (Weather Spark, [5]); SFBayWeather gives about one Thanksgiving in four with measurable rain (1991–2020) and notes a slightly higher rate in El Niño years [6]. Conditional on a wet day, late-November SFO amounts are right-skewed: roughly 40% 0.01–0.09, 40% 0.10–0.49, 13% 0.50–0.99, 7% ≥1.00 (my estimate from typical daily-amount distributions at coastal California stations; not fetched — flagged as an assumption). Climatological buckets: ~0.77 / 0.09 / 0.09 / 0.03 / 0.02.

### Inside view

The regime around Thanksgiving is clearly wetter than normal:
- CPC hazards outlook (issued 2026-11-15) has a **moderate risk of heavy precipitation for northern California Nov 24–25** and a slight risk for much of California Nov 23–29, with ensemble tools giving 40–50% odds of >2 in over 3 days in northern California — but also "a reduction of exceedance probabilities towards the middle of week-2", i.e. around Nov 26 [1].
- The SF Chronicle (c. 2026-11-14) reports the NWS flagging an increased risk of heavy precipitation and strong winds **Nov 25–27** [2]; CPC 6–10/8–14-day outlooks favour above-normal precipitation for California Nov 21 – Dec 4 [3]. A strong El Niño is forecast for winter 2026–27 [4].
- The NWS MTR discussion of 2026-11-16 04:14 PST covers only through Sunday Nov 22 [7]: a strong storm Nov 17–19, then another system from Sat Nov 21.

So an AR-type event is favoured in the Nov 24–27 window, but the timing at day 10 is uncertain by ±1–2 days, and the CPC's strongest signal sits on Nov 24–25 with tapering by mid-week; Nov 26 may be post-frontal showers or a break. I raise P(measurable) from ~23% to ~52% (+29 pp), and shift the wet-day amount distribution heavier given an active, AR-fed pattern.

Final: 0.00 in 48% · 0.01–0.09 in 17% · 0.10–0.49 in 20% · 0.50–0.99 in 9% · ≥1.00 in 6%.

### Evidence

- CPC Probabilistic Hazards Outlook, made 2026-11-15: moderate heavy-precip risk N. California Nov 24–25; slight risk Nov 23–29; reduction in exceedance probabilities mid week-2 [1].
- NWS (via SF Chronicle, ~2026-11-14): increased risk of heavy precipitation and strong winds Nov 25–27, possible brief break the weekend before [2].
- NOAA/CPC outlook reported 2026-11-12: above-normal precipitation favoured for California Nov 21 – Dec 4 [3].
- The Watchers 2026-11-16: two atmospheric rivers, Bay Area 2–3 in from the Nov 17–19 storm [4].
- NWS MTR AFD 2026-11-16: long term only to Nov 22, rain returning from Sat Nov 21 [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-16 | |
| Kalshi/Robinhood "Where will it rain" | no Nov 26 market found; SF Nov 17 contract 35¢ | 2026-11-16 | daily rain markets only list a few days ahead |
| Farmers' Almanac | sunny Pacific Southwest Thanksgiving | ~2026-10-27 | no skill; ignored |

### What would change my mind

The main sensitivity is timing: if the ensemble AR timing were to settle on Nov 24–25 with ridging behind it, the 0.00 bucket should be ~65–70%; if the front lands on Nov 26 itself, the ≥0.10 buckets would dominate. Without day-7 deterministic guidance today, I keep it near a coin flip on any measurable rain.

### Sources

1. CPC Probabilistic Hazards Outlook — https://www.cpc.ncep.noaa.gov/products/predictions/threats/threats.php (accessed 2026-11-16)
2. SF Chronicle, "Bay Area to get mostly dry weather but scary waves on Saturday — and then more storms" — https://www.sfchronicle.com/weather-forecast/article/rain-storm-weather-san-francisco-california-22529476.php (accessed 2026-11-16, via search snippet; page did not load)
3. "Will Thanksgiving be cold, dry or wet in California? Latest NOAA outlook" — https://www.yahoo.com/news/weather-news/articles/thanksgiving-cold-dry-wet-california-160926373.html (accessed 2026-11-16, search snippet)
4. The Watchers, "2 atmospheric rivers to bring heavy Sierra snow and California flood risk" — https://watchers.news/2026/11/16/2-atmospheric-rivers-to-bring-heavy-sierra-snow-and-california-flood-risk/ (accessed 2026-11-16, search snippet)
5. Weather Spark, November at SFO — https://weatherspark.com/m/145212/11/Average-Weather-in-November-at-San-Francisco-International-Airport-California-United-States (accessed 2026-11-16, via question text)
6. SFBayWeather, Thanksgiving weather in San Francisco — https://www.sfbayweather.com/learn/thanksgiving-weather-san-francisco (accessed 2026-11-16, search snippet)
7. NWS San Francisco Bay Area AFD, 2026-11-16 04:14 PST — https://forecast.weather.gov/product.php?site=MTR&product=AFD&issuedby=MTR (accessed 2026-11-16)

**Question**: [How much precipitation will San Francisco International Airport record on Thanksgiving Day (November 26, 2026)?](https://www.metaculus.com/questions/46587/)
**Date**: 2026-11-16
**Forecast**: Median 48.0% (0.00 in (no measurable precipitation)), IQR [38.0%, 58.0%]
**Thesis**: Climatology gives ~23% chance of measurable rain at SFO on a late-November day, but CPC (Nov 15) flags heavy-precipitation risk for northern California Nov 24–25 and NWS an increased risk Nov 25–27 in a strong-El Niño, AR-active pattern; I lift measurable rain to ~52%. The forecast is most sensitive to whether the storm's timing lands on Nov 26 or a day earlier.

## Resolution — 2026-11-28

Resolved **0.00 in (no measurable precipitation)** (synced from the Metaculus API). The bot's forecast was 0.48 [0.38, 0.58]. Official spot peer score: +0.17.
