# How many cumulative confirmed Ebola cases will the DRC's 2026 outbreak have reported as of October 31, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46182/ |
| **Tournament** | minibench — one shot, window 2026-10-26T05:01:38Z -> 2026-10-26T08:01:38Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-26 / 2026-10-26 / 2026-11-07 |
| **Status** | open |
| **Current forecast** | Median 10350, IQR [10280, 10430] (v1, 2026-10-26) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-26

### What resolves YES

The question resolves to the cumulative number of **laboratory-confirmed** cases in the DRC (excluding Uganda, Kenya, Nigeria and any other country; excluding suspected and probable cases) in the 2026 Bundibugyo-virus outbreak, for the **reporting date 31 October 2026**. If that date has no figure, the latest reporting date on or before it is used. The primary source is the ECDC outbreak page, which lags by a few days. The INSP daily sitreps or other credible sources (WHO, CDC) are used if ECDC has no figure. The range runs from 9,277 (a closed lower bound) to 11,500 (an open upper bound). Note that 31 October 2026 is a Saturday. ECDC updates only on weekdays, so the figure will probably come from a report published in early November or from INSP. There is roughly one day of ambiguity about whether the "reporting date" means data *up to* 30 or 31 October. That is worth about ±65 cases.

### Outside view

For a numeric count over a short horizon, the prior is to extend the recent trend. The cumulative count was 8,116 on 27 Sep, 8,728 on 6 Oct, 9,144 on 12 Oct, 9,277 on 14 Oct, 9,552 on 18 Oct and 9,704 on 20 Oct. CDC gives 9,816 for about 22–23 Oct, and Wikipedia's tables give 9,876 for about 23 Oct. Daily increments have held at about 55–76 per day for a month, with no clear trend (about 49/day in the week to 27 Sep, about 68/day in early October, about 57/day for 20–23 Oct). Ebola epidemics in the plateau phase usually change incidence over weeks, not days: the 2018–20 Kivu outbreak held its peak plateau for about two months and then declined slowly. Projecting from about 9,850 on 23 Oct over 8 days at 55–70/day gives roughly 10,290–10,410.

### Inside view

- **Anchor:** about 9,850 confirmed cases on about 23 Oct (the CDC figure of 9,816 and the Wikipedia/INSP-derived 9,876 bracket it).
- **Rate:** central 63/day, with a plausible range of 45–85/day over the 8 remaining days. The geographic spread is real (an eighth province, Nord-Ubangi, around 17 Oct; exported cases in Kenya and Nigeria). New provinces have so far added only a handful of cases, though, and Ituri and North Kivu still drive the totals. The 20–23 Oct increments (about 57/day) were slightly below early October, which argues against acceleration.
- **Reporting quirks:** the resolution may pick up the figure for data up to 30 Oct (Saturday 31 Oct is not an ECDC update day). Backlog dumps and weekend reporting gaps add noise of ±50–100. Downward reclassifications have happened in this outbreak before (May/June), but not recently, so I keep only a thin lower tail.
- **Result:** median about 10,350, IQR 10,280–10,430, and a 90% interval of 10,120–10,600. The tails are wider than the trend alone would justify, to cover the anchor discrepancy and reporting artefacts.

### Evidence

- ECDC page: 9,704 confirmed and 4,687 deaths as of 21 Oct (data to 20 Oct), fetched 2026-10-26 [1].
- CDC situation summary: DRC 9,816 confirmed and 4,757 deaths, as of 22–23 Oct [2].
- Wikipedia country/province tables: DRC 9,876 for 22–24 Oct; 9,000 milestone on 10 Oct [3].
- Secondary report of the INSP sitrep: 9,552 confirmed and 4,602 deaths as of 18 Oct; 8 provinces and 66 health zones [4].
- UKHSA: 8,116 confirmed as of 27 Sep, +343 in a week [5].
- WHO DON (as of 20 Oct): 9,704 confirmed. Kenya has 9 cases and Nigeria 1 imported case, neither counted here [6].
- CDC count for 15 Oct: 9,212 for the DRC [7]. The spread to Nord-Ubangi (2 cases) is in [8].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-26 | |
| Polymarket / Kalshi | none found on DRC case counts | 2026-10-26 | only Kalshi country-spread contracts |
| Manifold | none found | 2026-10-26 | |

### What would change my mind

- A sustained jump to over 90 cases/day (from a new urban cluster, or a lab backlog clearing) would push the result past 10,550.
- A recount or reclassification of confirmed cases, or a collapse in testing during insecurity, would pull it below 10,200.
- The most sensitive input is the true 23–25 Oct level, which I could not pin down to better than ±40 cases.

### Sources

1. ECDC, "Ebola disease: Multi-country outbreak 2026", https://www.ecdc.europa.eu/en/ebola-outbreak-democratic-republic-congo-and-uganda (accessed 2026-10-26)
2. CDC, "Ebola Outbreak: Current Situation", https://www.cdc.gov/ebola/situation-summary/index.html (accessed 2026-10-26)
3. Wikipedia, "2026 Central Africa Ebola epidemic", https://en.wikipedia.org/wiki/2026_Central_Africa_Ebola_epidemic (accessed 2026-10-26)
4. mesvaccins.net news item (INSP data to 18 Oct), https://www.mesvaccins.net/web/news/24511 (accessed 2026-10-26; search snippet only)
5. UKHSA, "Outbreaks under monitoring, week 39", https://www.gov.uk/government/publications/outbreaks-under-monitoring-in-2026/outbreaks-under-monitoring-week-39-week-ending-27-september-2026 (accessed 2026-10-26; search snippet)
6. WHO Disease Outbreak News DON622, https://www.who.int/emergencies/disease-outbreak-news/item/2026-DON622 (accessed 2026-10-26; search snippet)
7. Contagion Live, "Ebola outbreak in DRC tops 9,235 confirmed cases, CDC reports", https://www.contagionlive.com/view/ebola-outbreak-in-drc-tops-9235-confirmed-cases-cdc-reports (accessed 2026-10-26; search snippet)
8. ACP, "DRC: Nord-Ubangi, the eighth province affected by the Ebola outbreak", https://acp.cd/anglais/drc-nord-ubangi-the-eighth-province-affected-by-the-ebola-outbreak/ (accessed 2026-10-26; search snippet)
9. NCBI/MMWR, "Ebola Virus Disease Outbreak — DRC, August 2018–November 2019", https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6936163/ (accessed 2026-10-26; search snippet)

**Question**: [How many cumulative confirmed Ebola cases will the DRC's 2026 outbreak have reported as of October 31, 2026?](https://www.metaculus.com/questions/46182/)
**Date**: 2026-10-26
**Forecast**: Median 10350 cases, IQR [10280 cases, 10430 cases]
**Thesis**: The trend gives the answer here. The DRC count was about 9,850 confirmed cases on about 23 Oct (CDC 9,816; INSP-derived 9,876), and daily increments have held at 55–76 for a month (ECDC, CDC, UKHSA). Eight more days at about 63/day gives about 10,350. The result is most sensitive to whether incidence breaks out of that plateau, and to which reporting date (30 or 31 Oct) the resolver picks.
