# How many Japanese educational facilities will the MHLW report as fully or partially closed due to influenza-like illness this season, cumulative through the week ending October 25, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46152/ |
| **Tournament** | minibench — one shot, window 2026-10-19T18:32:34Z -> 2026-10-19T21:32:34Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 8915, IQR [2441, 10587] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The value is the season-to-date **cumulative** facility count (施設数 累計: nurseries, kindergartens, elementary, junior-high and senior-high schools with a 休校, 学年閉鎖 or 学級閉鎖) in the MHLW/JIHS インフルエンザ様疾患発生報告 for week 44 of 2026 (Oct 19–25), as first published (~Oct 30). **Critical misreading in the question text:** the figures it calls cumulative, 937 (week 40) and 1,703 (week 41), are the **weekly** (今週) totals. In the reports themselves the cumulative totals are 3,073 (week 40) and **4,793** (week 41) [1][2]. Read literally, the criteria ask for the cumulative figure. But the resolver is an LLM, and news coverage quotes the weekly figure as "X facilities" [3][4]. It may therefore resolve on the week-44 weekly figure instead. I forecast a mixture: 65% that the cumulative figure is used, 35% the weekly figure. Both bounds are open.

### Outside view

- **Cumulative reading.** The total is 4,793 plus three weeks of new closures (weeks 42–44) plus small revisions (+17 in week 41). Weekly closures have tracked roughly 130–165 × the national sentinel average (cases per reporting clinic):
  - week 41 of 2026: 1,703 at 12.81;
  - week 44 of 2025: 2,307 (the question's "early November 2025" figure) at 14.90;
  - week 46 of 2025: 6,235 at 37.73 [5][6].
- If the sentinel average stays at 12–15 for three weeks, that adds about 5,000–6,500 closures, for a total of about 10,000–11,000.
- **Weekly reading.** The status quo is about 1,700 per week.
- **Reference class.** No clean one. Early-season H1N1 (influenza A subtype) waves have run either way: 2009 kept growing until week 48, while Okinawa this season peaked in week 39 and is already falling.

### Inside view

- **Growth is decelerating.** The sentinel average went 7.17 → 11.35 → 12.81 (+58%, then +13%). NHK called the latest rise "slight" [4].
  - Okinawa (37.07 → 31.34) and Aichi (falling for three weeks) are past their peaks.
  - Hokkaido (9.21 → 16.21), Kanto and Tohoku are still rising [4].
- **Week 42 (Oct 12–18) has the Sports Day holiday**, so it had four school days. Mie prefecture's own count fell in that week: cases 407 → 245, closures 18 → 14 [7]. That one prefecture is weak evidence of a national plateau.
- **Closures can outrun cases.** Closures nearly doubled from week 40 to week 41 while cases rose 13%, because the wave is moving into school-age children. The ratio of closures to the sentinel average may keep rising.
- **The model** (`model.py`, Monte Carlo):
  - weekly log-growth: drift +3%/week, path SD 15%, weekly noise 10%;
  - week 42 scaled down 5–20% for the holiday;
  - revisions of 0–60.
  - Week-44 weekly count: median 1,870 (IQR 1,350–2,580).
  - Cumulative total: median 10,040 (IQR 9,000–11,390; 5–95%: 7,900–14,060).
  - The 65/35 mixture gives the percentiles below. The median is inside the cumulative mode; the IQR spans both modes.

| pct | 5 | 10 | 25 | 35 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|---|
| value | 1,115 | 1,425 | 2,441 | 6,780 | 8,915 | 10,587 | 12,221 | 13,344 |

### Evidence

- **Week 41 report (made 2026-10-16) [1]:**
  - This week: 1,703 facilities (休校 31, 学年閉鎖 333, 学級閉鎖 1,339).
  - Cumulative: 4,793 (休校 79, 学年閉鎖 890, 学級閉鎖 3,824).
  - Same week in 2025: about 328.
- **Week 40 report (made 2026-10-09) [2]:** 937 this week, 3,073 cumulative.
- **Sentinel average:** 7.17 (week 39), 11.35 (week 40), 12.81 (week 41), with 47,746 cases (about 5× a year earlier). 29 prefectures were above 10 [3][4].
- **Strain and timing:** H1N1pdm09 dominates this season, which was declared on Aug 28, the second-earliest since 1999 [8].
- **2025 comparison:** week 44 had a sentinel average of 14.90; week 46 had 6,235 weekly closure facilities at 37.73 [5][6].
- **Mie prefecture, week 42:** closures and cases both fell [7].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no market on this series |

### What would change my mind

- **The resolver's interpretation (cumulative vs weekly)** moves the answer by about 8,000. Wording that pointed clearly at the weekly figure would shift weight to the low mode.
- **The national week-42 data (due ~Oct 23).** A sentinel average below 11 points to a cumulative total of about 9,000; above 16 points to more than 11,500.

### Sources

1. JIHS/MHLW, インフルエンザ様疾患発生報告 第6報 (week 41), https://id-info.jihs.go.jp/surveillance/idwr/diseases/influenza/school/2026/infl26_27-06.pdf (accessed 2026-10-19)
2. JIHS/MHLW, 第5報 (week 40), https://id-info.jihs.go.jp/surveillance/idwr/diseases/influenza/school/2026/infl26_27-05.pdf (accessed 2026-10-19)
3. Weathernews, "インフルエンザ患者数 昨年同時期の5倍以上", 2026-10-16, https://weathernews.jp/news/202610/160261/ (accessed 2026-10-19)
4. Resemom 2026-10-16, https://resemom.jp/article/2026/10/16/87922.html ; NHK 2026-10-16, https://news.web.nhk/newsweb/na/nd-20261016de60515 ; CBnews https://www.cbnews.jp/news/entry/20261016170735 (accessed 2026-10-19, via research scout)
5. Weathernews, 2025-11-21, https://weathernews.jp/news/202511/210136/ (accessed 2026-10-19, via research scout)
6. MHLW, 2025 week-44 influenza release, https://www.mhlw.go.jp/content/001576812.pdf (search summary, accessed 2026-10-19)
7. Mie Prefecture, weekly influenza-like-illness closure table, https://www.pref.mie.lg.jp/common/content/001280361.pdf (search summary, accessed 2026-10-19)
8. Kumamoto Nichinichi, "インフル、異例の早さで流行入り", https://kumanichi.com/articles/2035203 (search summary, accessed 2026-10-19)
9. JIHS report index, https://id-info.jihs.go.jp/surveillance/idwr/diseases/influenza/school/flulike.html (accessed 2026-10-19)

**Question**: [How many Japanese educational facilities will the MHLW report as fully or partially closed due to influenza-like illness this season, cumulative through the week ending October 25, 2026?](https://www.metaculus.com/questions/46152/)
**Date**: 2026-10-19
**Forecast**: Median 8915 facilities, IQR [2441, 10587]
**Thesis**: The official cumulative count was already 4,793 after week 41. The 1,703 the question calls cumulative is that week's figure. Three more weeks of about 1,500–2,500 closures (growth slowing, sentinel 12.81, +13%) put the cumulative total near 10,000. I keep 35% on a weekly-figure resolution near 1,900. The forecast is most sensitive to which figure the resolver uses.
