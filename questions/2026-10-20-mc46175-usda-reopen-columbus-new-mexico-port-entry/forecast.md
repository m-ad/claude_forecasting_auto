# Will the USDA reopen the Columbus, New Mexico port of entry to Mexican cattle imports before October 31, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46175/ |
| **Tournament** | minibench — one shot, window 2026-10-20T19:11:51Z -> 2026-10-20T22:11:51Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-20 / 2026-10-31 |
| **Status** | closed |
| **Current forecast** | Median 83.0%, IQR [76.0%, 89.0%] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

YES if, at any point from October 29 to 23:59 ET on October 30, 2026, the APHIS "Current Status of New World Screwworm" page shows Columbus, NM open to live cattle imports from Mexico. That means either a reopening date on or before October 30 is listed, or the page says outright that the port is open. A reopening that is later paused still counts. An announced date after October 30 does not count. Credible news reports are used only if the page is unavailable or no longer reports port status. On the last check (page last modified 2026-10-14), Columbus was listed as "To be determined".

### Outside view

The reference class is this same phased reopening in 2026. USDA announced two earlier steps and carried out both on schedule:

- Douglas, AZ: announced July 24 for August 24. It reopened on schedule, even though Sonora reported its first screwworm case a few days before.
- Santa Teresa, NM: announced September 17 for September 24. It reopened on schedule, even though a case was confirmed in a horse in Grant County, NM that same week.

On a time-left basis alone, a port with no date has perhaps a 30–40% chance of reopening within 10 days. Rollins' stated 30-day cadence points to late October, which supports the higher end of that range. Once USDA has publicly named a date about a week out, the reference class is "announced reopening date honoured", which has gone 2 for 2 in 2026. The counterexample is 2025: dates were announced (Columbus was set for July 14, 2025), and the border was then re-closed in July 2025 after new cases.

### Inside view

On October 19, 2026, Meatingplace reported that "the USDA said Monday" Columbus will be the third crossing reopened, as of October 26 [1]. This fits several other reports:

- Chihuahua's cattle union had already announced October 26 and 750 head per day, pending official confirmation (Tiempo, October 6 [2]; Ag Bull, October 19 [3]).
- Rollins had said publicly that reopenings would follow a 30-day cadence [4].

October 26 leaves four days of slack before the window. USDA is going ahead despite the October 15 cases in Grant County, NM (the county next to Luna County, where Columbus is) [1]. That suggests the known risks are already priced in.

Remaining risks:

- **New detections cause a pause before October 26.** Chihuahua's case count is still rising, and the pause clause exists. Roughly 7–10%.
- **The reopening slips past October 30.** Roughly 3–4%.
- **The APHIS page is stale or worded so that a literal LLM resolver reads it as not open.** The page was updated promptly for the earlier two ports. Roughly 3–4%.

I could not open the USDA press release itself, so the October 26 date rests on trade-press reports. Combined, that gives about 83%.

### Evidence

- 2026-07-24: USDA announces the phased reopening, Douglas, then Santa Teresa, then Columbus. The timeline is flexible and can be paused if risk rises in Sonora or Chihuahua [5].
- 2026-08-24: Douglas reopens. 2026-09-24: Santa Teresa reopens; it was announced on 09-17 [6].
- 2026-09-21: Rollins says USDA is "looking at reopening a port in Columbus" if containment holds [7].
- 2026-10-06: Chihuahua union says US authorities notified a Palomas–Columbus reopening on October 26 [2].
- 2026-10-14: The APHIS page is last modified; Columbus is not yet dated [5].
- 2026-10-15: Two NWS (New World screwworm) cases are confirmed in Grant County, NM, near Columbus [1][3].
- 2026-10-19: Meatingplace reports USDA said Columbus reopens October 26 [1].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-20 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-20 | no market on this event |

### What would change my mind

- An APHIS or USDA notice before October 26 that pauses the reopening or moves it past October 30.
- A cluster of new screwworm detections in northern Chihuahua or Luna County.

On the other side, seeing the APHIS page list "Columbus, NM: October 26, 2026" would push the forecast to about 95%.

### Sources

1. Meatingplace, "Third Border Crossing To Open Next Week Despite Screwworm", 2026-10-19: https://meatingplace.com/third-border-crossing-to-open-next-week-despite-screwworm/ (accessed 2026-10-20)
2. El Heraldo / Tiempo, "Abrirán al ganado puerto Chihuahua-Columbus el 26 de octubre": https://www.tiempo.com.mx/local/abriran-al-ganado-puerto-chihuahua-columbus-el-26-de-octubre/ (accessed 2026-10-20, search summary)
3. Ag Bull Trading, "Chihuahua Cattlemen's Union expects Columbus, N.M., to Reopen Oct. 26 at 750 Head Daily": https://agbull.com/u-s-mexico-border-chihuahua-cattlemens-union-expects-columbus-n-m-to-reopen-oct-26-at-750-head-daily (accessed 2026-10-20, search summary)
4. Ag Bull Trading, "USDA Targets a 60-Day Reopening of New Mexico Cattle Ports": https://www.agbull.com/usda-targets-a-60-day-reopening-of-new-mexico-cattle-ports/ (accessed 2026-10-20, search summary)
5. USDA APHIS, Current Status of New World Screwworm: https://www.aphis.usda.gov/animals/animal-health/livestock-and-poultry-disease/stop-screwworm/current-status (accessed 2026-10-20)
6. Drovers, "Santa Teresa Livestock Port Set to Reopen Sept. 24": https://www.drovers.com/news/santa-teresa-livestock-port-set-reopen-sept-24 (accessed 2026-10-20, search summary)
7. Insurance Journal, 2026-09-21: https://www.insurancejournal.com/news/west/2026/09/21/885709.htm (accessed 2026-10-20, via research scout)

**Question**: [Will the USDA reopen the Columbus, New Mexico port of entry to Mexican cattle imports before October 31, 2026?](https://www.metaculus.com/questions/46175/)
**Date**: 2026-10-20
**Forecast**: Median 83.0%, IQR [76.0%, 89.0%]
**Thesis**: USDA reportedly said on 2026-10-19 that Columbus will reopen to Mexican cattle on October 26 (Meatingplace; Chihuahua union reports agree). The two earlier announced reopenings this year both happened on schedule despite nearby screwworm cases. The forecast is most sensitive to a pause triggered by new detections before October 26, and to whether the APHIS page reflects the reopening by October 30.
