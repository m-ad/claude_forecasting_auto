# What will Japan's national average of influenza cases per sentinel medical institution be for the week ending October 25, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46174/ |
| **Tournament** | minibench — one shot, window 2026-10-20T17:21:32Z -> 2026-10-20T20:21:32Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-20 / 2026-10-31 |
| **Status** | closed |
| **Current forecast** | Median 15.8, IQR [13.6, 18.5] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

The question resolves to the single national influenza figure, cases per sentinel institution (定点当たり報告数), for the week ending Sunday 25 October 2026. Japan's Institute for Health Security (JIHS) publishes it in the Infectious Diseases Weekly Report (IDWR), expected around Friday 30 October. The first published value counts. The question text calls this "week 44", but the week of 19–25 October 2026 is epidemiological week 43. I forecast the week ending 25 October, because the title, the date and the 31 October resolve date all point to it. If a resolver instead read the true week 44 (26 Oct–1 Nov), that would add a little upside, which the right tail absorbs. Both bounds (8 and 35) are open.

### Outside view

**This season's series** (national cases per sentinel, retrieved 2026-10-20 [2][3]):

| Week | Value |
|---|---|
| wk37 | 5.54 |
| wk38 | 8.48 |
| wk39 | 7.17 |
| wk40 | 11.35 |
| wk41 (5–11 Oct) | 12.81 |

- Week 39 contained three public holidays (21–23 Sep), which depress sentinel reporting. Averaged over weeks 38→40, growth was about +16 % a week. Week 41 alone was +13 %.

**Reference class**: past seasons at the point the national figure crossed 10–15, and the value two weeks later [5][6][7]:

| Season | Value at the crossing | Two weeks later | Ratio |
|---|---|---|---|
| 2023 (also an unusually early season) | wk41: 11.07 | 19.68 | 1.78x |
| 2024 | wk49: 9.03 | 42.66 | 4.7x |
| 2025 | wk44: 14.90 | 37.73 | 2.5x |

- 2023 then plateaued and dipped: 21.13, then 17.35.
- Base rate: once past 10, Japanese flu waves usually keep rising over the next two weeks, often steeply. A flat or falling two-week stretch does happen (2023, weeks 44→46).

### Inside view

**Momentum**: this wave is growing much more slowly than the explosive 2024 and 2025 November–December waves.
- Its weekly growth of 13–16 % looks like the slow phase of 2023 (9.57, 9.99, 11.07).
- The season began in August, and Okinawa is already past the warning level. Some regions may be nearing their peak and could drag the national average down.

**Holiday effect**: Week 42 (12–18 Oct) contains the Sports Day holiday, so it may print low. Week 43 is a normal school week, and late October is when school-driven transmission usually accelerates (2023: +48 % in week 42).

**Projection**: two more weeks at 10–15 % growth gives 15.5–17. A plateau gives about 13. Re-acceleration as in 2023 gives 20+. A turnover gives 11–12.

**Forecast**: median 15.8, skewed right because growth compounds and the 2023 analogue reached 1.78x in two weeks.

### Evidence

- wk40 2026: 11.35, up from 7.17 (MHLW release of 9 Oct, via Nikkan Yakugyo / nk.jiho) [2].
- wk41 2026: 12.81 for 5–11 Oct (headline published 19 Oct 2026) [2].
- wk37 5.54 and wk38 8.48 [3]. The season start (above 1.0 nationally) came in 17–23 Aug, unusually early [4].
- Week 41 detail [10][11]:
  - 47,746 reports, 5.3 times the same week of 2025; 29 prefectures above 10.
  - Okinawa is falling (37.07, then 31.34). The populous Kanto region is still rising (Kanagawa 21.60, Saitama 20.99, Chiba 19.55, Tokyo 15.88).
  - Aichi, Shizuoka and Okayama are flat or falling.
- The JIHS IDWR rapid index lists weeks 1–41, so week 42 is not yet published as of 2026-10-20 [1].
- Okinawa issued an alert at 10.34 in week 36 [8].
- No reports of a slowdown were found. In Mie prefecture's school-closure tallies, the partial week of 12–18 Oct kept being revised upward [9].
- Historical trajectories for 2023–2025 come from MHLW figures relayed by prefectural and news pages [5][6][7]. They were not all opened directly, so treat them as approximate.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-20 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-20 | no market on Japanese flu data |

### What would change my mind

- **The week 42 print** (out around 23 Oct, after this forecast). A reading at or below 12.8 despite the holiday would point to a plateau and a median near 13. A reading of 15 or more would point to 18–20.
- **Signs that the early-onset regions have peaked**: Okinawa and Kyushu falling while eastern Japan has not yet taken off.

### Sources

1. JIHS IDWR rapid 2026 index — https://id-info.jihs.go.jp/en/surveillance/idwr/rapid/2026/index.html (accessed 2026-10-20)
2. Nikkan Yakugyo (nk.jiho), week 40 2026 influenza report, with the week 41 headline — https://nk.jiho.jp/article/305841 (accessed 2026-10-20)
3. nk.jiho week 38/39 2026 reports — https://nk.jiho.jp/article/305652 , https://nk.jiho.jp/article/305496 (accessed 2026-10-20)
4. Kumamoto Nichinichi, early season start — https://kumanichi.com/articles/2034945 (accessed 2026-10-20)
5. Kanagawa EIKEN, 2023 weeks 36–41 — https://www.pref.kanagawa.jp/sys/eiken/003_center/0005_ryukou/influenza/231023_influenza_06.html ; nk.jiho, 2023 week 43, 19.68 — https://nk.jiho.jp/article/185207 ; week 44, 21.13 — https://nk.jiho.jp/article/185404 (accessed 2026-10-20)
6. MHLW, 2025 week 43 and week 46 releases — https://www.mhlw.go.jp/content/001589611.pdf , https://www.mhlw.go.jp/content/001600539.pdf (via search summaries, accessed 2026-10-20)
7. MHLW / Osaka City, 2024 weeks 48–52 — https://www.mhlw.go.jp/content/001370524.pdf , https://www.city.osaka.lg.jp/kenko/cmsfiles/contents/0000028/28410/2024zenkokuteiten52w.pdf (via search summaries, accessed 2026-10-20)
8. Okinawa Prefecture, influenza alert, 11 Sep 2026 — https://www.pref.okinawa.jp/_res/projects/default_project/_page_/001/041/412/20260911_influenza.pdf (accessed 2026-10-20)
9. Mie Prefecture school-closure report, Oct 2026 — https://www.pref.mie.lg.jp/common/content/001279911.pdf (accessed 2026-10-20)
10. ReseMom, week 41 influenza — https://resemom.jp/article/2026/10/16/87922.html (accessed 2026-10-20)
11. CB News via Yahoo Japan, week 41 — https://news.yahoo.co.jp/articles/6ee2f77670a389d07be0ef043c57445dfb10d20d (accessed 2026-10-20)

**Question**: [What will Japan's national average of influenza cases per sentinel medical institution be for the week ending October 25, 2026?](https://www.metaculus.com/questions/46174/)
**Date**: 2026-10-20
**Forecast**: Median 15.8 cases/sentinel, IQR [13.6, 18.5]
**Thesis**: The national figure was 12.81 in week 41 (5–11 Oct), growing about 13–16 % a week; past waves that crossed 10–15 (2023, 2024, 2025) all kept rising over the next two weeks, by 1.8x to 4.7x. This early, slow-moving season most resembles 2023, so I project modest compounding to about 16, with a right skew. The forecast is most sensitive to whether the week 42 print shows a plateau.
