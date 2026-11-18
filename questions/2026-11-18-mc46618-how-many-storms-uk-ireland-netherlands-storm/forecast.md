# How many storms will the UK–Ireland–Netherlands storm-naming group have named by the end of 28 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46618/ |
| **Tournament** | minibench — one shot, window 2026-11-18T11:19:14Z -> 2026-11-18T14:19:14Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-18 / 2026-11-18 / 2026-11-28 |
| **Status** | open |
| **Current forecast** | Median 2.19, IQR [1.85, 2.64] (v1, 2026-11-18) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-18

### What resolves YES

The answer is the number of 2026/27 west-group names (Austen, Boelo, Chloe, Dano, …) whose "Date named" in the Met Office UK Storm Centre table is on or before 28 Nov 2026 (UK date, which is GMT/UTC in November). Storms named by other naming groups do not count. When I fetched the table on 2026-11-18 it showed **2**: Austen (named 20 Oct) and Boelo (named 22 Oct). Chloe's row was blank [1]. The count can only go up, so 2 is the floor. The question turns on whether Chloe gets a naming date in the 11 days from 18 to 28 Nov, and much less on Dano. A storm hitting on 29–30 Nov but announced by 28 Nov would count. A storm named on 29 Nov would not.

### Outside view

**Reference class:** west-group namings in the 18–28 Nov window, seasons 2015/16 to 2025/26 (n = 11), from Wikipedia season pages and Met Office storm pages [6][7]:

- **At least one naming:** 3–4 of 11 seasons, about 30%. These were Angus (19 Nov 2016), Arwen (25 Nov 2021), Bert (21 Nov 2024) and Conall (26 Nov 2024). Clodagh (2015) is borderline, named 28 or 29 Nov.
- **Two or more namings:** 1 of 11 seasons (2024).

**Prior:** P(≥3) ≈ 30%, P(≥4) ≈ 8%.

### Inside view

- **Quiet so far.** Nothing has been named since 22 Oct. The large Atlantic low that the Met Office's 12 Nov 10-day trend flagged ("winds could also become strong enough to cause impacts") [3] passed on 17 Nov with only a yellow snow warning and no name [4][8].
- **This week settles.** The 16 Nov week-ahead forecast has colder, brighter weather later in the week and light winds with frost on Friday night [4]. That likely rules out a naming before about 21–22 Nov.
- **What is left.** The effective window is roughly 22–28 Nov, about 6–7 days. That counts the 1–3 day lead between naming and impact.
- **The long range leans unsettled.** The Met Office long-range outlook for 26 Nov–10 Dec gives "Atlantic weather systems bringing spells of rain and strong winds at times" [5]. This is a generic signal: none of my sources names a specific deep low.
- **Net effect.** I start from the ~30% base rate, take about 5 pp off for the shortened window and add about 3 pp back for the unsettled outlook. That gives **P(≥3) ≈ 28%** and **P(≥4) ≈ 6%**. P(≥4) requires two namings in under a week, which happened only in 2024 (Bert and Conall).

**Distribution:**

| Count | Probability |
|---|---|
| 2 | 72% |
| 3 | 22% |
| 4 | 5% |
| 5 | 0.8% |
| ≥6 | 0.2% |

### Evidence

- **Resolution source (Met Office storm centre, 2026-11-18):** only Austen and Boelo are named. Chloe is blank [1]. Scout 1 found the same on the Met Office and Met Éireann pages [1][2].
- **Met Office 10-day trend (12 Nov):**
  - "A powerful Atlantic jet stream is expected to help develop a large area of low pressure."
  - Impacts were possible from 16 Nov.
  - No storm was named for it [3].
- **Met Office week-ahead (16 Nov):**
  - Strong winds on Tuesday 17 Nov.
  - Colder and brighter later in the week, with light winds on Friday night.
  - No warnings mentioned [4].
- **17 Nov warnings:** only a yellow snow warning for northern England and southern Scotland. No wind warnings found [8].
- **Long range (11 Nov, covering 26 Nov–10 Dec):** changeable and unsettled, with strong winds at times [5].
- **Ireland and the Netherlands:** no Nov 2026 Met Éireann orange or KNMI code-orange warnings found. KNMI names a storm only when it issues code orange or red [9].
- **Base-rate table** from the scout's Wikipedia pass [6][7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-18 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-18 | no market on Nov 2026 UK storm naming |

### What would change my mind

- **Upward:** a deep Atlantic low appearing in the 23–28 Nov model runs with amber-level winds forecast for Ireland or western Britain. That would push P(≥3) above 60%. Met Éireann in particular names readily.
- **Downward:** a blocking high taking hold for 22–28 Nov would push P(2) above 85%.

### Sources

1. https://weather.metoffice.gov.uk/warnings-and-advice/uk-storm-centre/index (accessed 2026-11-18)
2. https://www.met.ie/forecasts/storm-names (accessed 2026-11-18)
3. https://www.metoffice.gov.uk/blog/2026/10-day-trend-cold-and-frosty-before-a-wetter-and-windier-change (accessed 2026-11-18)
4. https://www.metoffice.gov.uk/blog/2026/week-ahead-a-wintry-start-before-colder-brighter-weather-arrives (accessed 2026-11-18)
5. https://www.lbc.co.uk/weather/met-office-forecast-rain-november/ (accessed 2026-11-18; search snippet), plus the Met Office long-range text quoted in the question
6. https://en.wikipedia.org/wiki/2024–25_European_windstorm_season (accessed 2026-11-18)
7. https://en.wikipedia.org/wiki/2021–22_European_windstorm_season (accessed 2026-11-18)
8. https://www.metoffice.gov.uk/about-us/news-and-media/media-centre/weather-and-climate-news/2026/snow-warning-in-force-as-unsettled-weather-continues- (accessed 2026-11-18; search snippet)
9. https://www.knmi.nl/kennis-en-datacentrum/uitleg/naamgeving-van-stormen (accessed 2026-11-18; search snippet)
10. https://www.yourweather.co.uk/news/forecasts/storm-chloe-next-could-another-atlantic-low-bring-a-third-named-storm-to-the-uk.html (accessed 2026-11-18)

**Question**: [How many storms will the UK–Ireland–Netherlands storm-naming group have named by the end of 28 November 2026?](https://www.metaculus.com/questions/46618/)
**Date**: 2026-11-18
**Forecast**: Median 2.19 storms, IQR [1.85, 2.64] storms (P(2) 72%, P(3) 22%, P(≥4) 6%)
**Thesis**: In about 30% of seasons since 2015 the west group named a storm between 18 and 28 Nov. This year the 17 Nov low went unnamed and the rest of this week settles, which leaves about 22–28 Nov, a period the Met Office expects to be unsettled. The count stays at 2 unless a deep Atlantic low turns up in the last week of November.
