# How many AIS-visible commercial ship crossings of the Strait of Hormuz will hormuz.now record for 26 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46579/ |
| **Tournament** | minibench — one shot, window 2026-11-16T08:29:24Z -> 2026-11-16T11:29:24Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-27 |
| **Status** | closed |
| **Current forecast** | Median 6.2, IQR [4.6, 8.6] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

The question resolves to the headline "commercial crossings" count on hormuz.now's archive page for one UTC day, 26 November 2026 (https://hormuz.now/traffic/2026-11-26), as shown at 2026-11-27 12:00 UTC. That count covers AIS-visible cargo ships and tankers of at least 80 m (or 5,000 dwt), each counted once per direction as it crosses the Musandam–Kuhestak line. The range is 0–30 with an open upper bound. The latest complete day is 15 Nov, so the target is 11 days ahead. hormuz.now's own CSV (fetched 16 Nov) gives 6, 4, 13, 6, 5, 6, 6 for 9–15 Nov: 46 in 7 days, or 6.6 a day. 16 Nov has 3 so far (partial). It is not annulled unless hormuz.now publishes nothing for the day.

### Outside view

The reference class is hormuz.now's own complete daily totals, 20 Oct–15 Nov (n = 27; 19 Oct, the first logged day, shows 0). They range from 4 to 13, with mean 7.6 and median 6. The empirical quartiles are about 5 and 9.5, and 3 of the 27 days (11%) reached 13. No day was below 4 or above 13. The 7-day average peaked at 9.3 in early November and has since drifted down to 6.3–6.6.

### Inside view

The regime is stable. Attacks continue (more than 34 vessels in October, more tanker fires 8–14 Nov), the US blockade continues, and about 500 ships wait on the Gulf of Oman side. Attack days have not pushed the count below 4. A Qatari interim deal (reopening plus an $8bn asset release) is on the table, but there is no implementation and Trump has said the US "doesn't need a deal". After the June memorandum of understanding, the first-day count was only ~7 and recovery took weeks, so even a deal around 20 Nov would add only modestly by 26 Nov. I set the median at 6, slightly below the 27-day mean, to reflect the recent drift. The upper tail is wider than the empirical one to allow for a deal or convoy surge. The lower tail allows for escalation, a feed artefact or ships going AIS-dark (low counts such as 0–2 are possible but have not been seen).

| pct | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| crossings | 2.5 | 3.4 | 4.6 | 6.2 | 8.6 | 11.5 | 14.0 |

### Evidence

- hormuz.now daily CSV, 20 Oct–15 Nov: 7, 11, 6, 9, 6, 4, 8, 5, 6, 11, 13, 12, 10, 5, 7, 7, 9, 13, 5, 5, 6, 4, 13, 6, 5, 6, 6 [1]. 30-day total: 200 [2].
- PortWatch's counts run about half of hormuz.now's (3 on 8 Nov) [5]. Windward counted 10 on 12 Nov, 8 of them dark, and 9 on 13 Nov, all dark [6]. These are different measures, not the resolution source.
- 15 Nov: no deal. Qatar is still mediating, and analysts expect the stalemate to persist [3][4].
- 16 Nov: hormuz.now status "Restricted", with 501 ships waiting on the Gulf of Oman side [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | no market on daily counts; "normal traffic" contracts (PortWatch 7-day average ≥ 60) price low odds | stale (Jul–Oct) | [7] |

### What would change my mind

- A signed and implemented US–Iran/Qatar deal before ~24 Nov would raise my distribution towards 10–25.
- A major escalation or a broad shift to AIS-dark transits would lower it towards 0–3.

### Sources

1. hormuz.now daily CSV, https://hormuz.now/api/daily.csv (accessed 2026-11-16)
2. hormuz.now data/FAQ pages, https://hormuz.now/data, https://hormuz.now/faq (accessed 2026-11-16)
3. Straits Daily Brief 14 Nov 2026, https://straits.live/briefs/2026-11-14 (accessed 2026-11-16)
4. 1News, "Trump's shifting Iran stance leaves path to peace uncertain", https://www.1news.co.nz/2026/11/15/trumps-shifting-iran-stance-leaves-path-to-peace-uncertain/ (accessed 2026-11-16)
5. Gulf News, "Hormuz shipping below normal but not stalled: UKMTO", https://gulfnews.com/world/mena/hormuz-shipping-below-normal-but-not-stalled-ukmto-1.500741839 (accessed 2026-11-16)
6. Windward insights, https://insights.windward.ai/ (search snippet, accessed 2026-11-16)
7. Kalshi, Hormuz recovery odds, https://news.kalshi.com/p/strait-of-hormuz-recovery-odds-2026 (accessed 2026-11-16)
8. Lloyd's List Intelligence, Strait of Hormuz Brief 5 Nov 2026, https://www.lloydslistintelligence.com/resources/blog/strait-of-hormuz-brief-5-november-2026 (accessed 2026-11-16)

**Question**: [How many AIS-visible commercial ship crossings of the Strait of Hormuz will hormuz.now record for 26 November 2026?](https://www.metaculus.com/questions/46579/)
**Date**: 2026-11-16
**Forecast**: Median 6.2 crossings, IQR [4.6, 8.6]
**Thesis**: hormuz.now's own daily series has held at 4–13 crossings a day (median 6) for four weeks, with the 7-day average drifting down to ~6.5 under continuing attacks and the US blockade (hormuz.now CSV; Gulf News; Straits brief). A Qatari interim deal is pending but unimplemented, so it widens only the upper tail. The forecast is most sensitive to whether a reopening is implemented before 26 Nov.
