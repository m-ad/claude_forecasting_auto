# How many dengue cases will Singapore's NEA report for the epidemiological week ending Saturday 24 October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46134/ |
| **Tournament** | minibench — one shot, window 2026-10-19T06:51:22Z -> 2026-10-19T09:51:22Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-29 |
| **Status** | closed |
| **Current forecast** | Median 67, IQR [59, 75] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the number on the NEA dengue cases page [1] under "No. of reported cases" for E-week 42 (Sun 18 Oct to Sat 24 Oct 2026). The value is read as of 23:59 SGT on 29 Oct 2026. That is the provisional first print, and later upward revisions do not count. If the value is not up by then, resolution waits for it. The range runs 30–130 and both bounds are open.

### Outside view

The reference class is NEA's recent weekly counts, which are the series itself. E-weeks 35–40 were 87, 73, 74, 82, 71 and 79 [1]. That is a mean of about 78 with a week-to-week standard deviation of about 6, all inside a 71–88 band. Late August and September also ran 73–88 [2]. Singapore's traditional peak season runs May–October [1], so late October usually sits flat to declining. In 2025 the count was 55 in E-week 45 [3], a much lower year: 3,990 cases for the whole year [4]. Starting from a persistence prior, I expect about 75 ± 10.

### Inside view

The daily counts for E-week 41 (11–16 Oct) on the NEA page, last updated 17 Oct, are 4, 11, 12, 10, 9 and 3 (Friday, as of 11am). That makes 49 cases with Friday partial and Saturday missing [1]. Sunday through Thursday averaged about 9.2 a day, against about 11.3 for E-week 40. Extrapolating gives roughly 62–70 for the full week. So E-week 41 looks like the lowest in about two months, consistent with the end of peak season. I project E-week 42 at about 67 (median), allowing for a continued mild decline and some mean reversion toward the 70s.

Two factors widen the tails. First, the resolving figure is a provisional print a few days after the week closes, which pushes it slightly low. Second, a DENV-3 serotype shift was flagged in mid-2026 as a risk for a rise [5]. 2026 has been running about 70% above 2025 [question background]. I kept the tails wide on both sides.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| Cases | 46 | 51 | 59 | 67 | 75 | 84 | 90 |

### Evidence

- E-weeks 35–40 on the NEA page were 87, 73, 74, 82, 71 and 79. The cumulative total for 2026 through E-week 40 is 2,643. The page was last updated 17 Oct 2026 [1] (accessed 2026-10-19).
- The partial E-week 41 count is 49 through Friday 11am. The daily counts slowed versus E-week 40 [1] (accessed 2026-10-19).
- E-week 39 had 71 cases, 11 fewer than the week before, and two red clusters remained open [2] (accessed 2026-10-19).
- In 2025, E-week 45 had 55 notifications [3]. The 2025 full-year total was 3,990, a 7-year low [4].
- In mid-2026 there was a DENV-3 serotype switch, and reporting warned that cases may rise [5]. That report is stale for October.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no market on this weekly count |

### What would change my mind

- The settled E-week 41 total. If it comes in at about 75 or more, the slowdown was an artefact of the partial week, and the median should be about 72. If it comes in at about 55 or less, the decline is sharper and the median should be in the high 50s.
- If NEA updates later than usual, a partial or very early print could show for E-week 42 at read time. That would bias the result low.

### Sources

1. NEA, Dengue cases page — https://www.nea.gov.sg/dengue-zika/dengue/dengue-cases (accessed 2026-10-19)
2. littlebigreddot, "Dengue cases fall to 71 a week as NEA keeps two red clusters open in peak season" — https://littlebigreddot.com/?p=28192 (accessed 2026-10-19)
3. CDA/MOH Weekly Infectious Disease Bulletin EW 45 — https://isomer-user-content.by.gov.sg/18/b04c8edd-aadf-4349-8c49-688a6c018124/Weekly%20Infectious%20Disease%20Bulletin%20EW%2045.pdf (accessed 2026-10-19, via search snippet)
4. Asia News Network, "Dengue cases in Singapore hit 7-year low in 2025 amid global decrease" — https://asianews.network/?p=248223 (accessed 2026-10-19, via search snippet)
5. Asia News Network, "Dengue cases in Singapore low but increasing, numbers may rise further with dengue strain change" — https://asianews.network/?p=290728 (accessed 2026-10-19, via search snippet)
6. Bernama, "Singapore Records Highest Weekly Dengue Cases Of 2026" — https://web29.bernama.com/nnn/news.php?id=2569134 (accessed 2026-10-19, via search snippet)

**Question**: [How many dengue cases will Singapore's NEA report for the epidemiological week ending Saturday 24 October 2026?](https://www.metaculus.com/questions/46134/)
**Date**: 2026-10-19
**Forecast**: Median 67 cases, IQR [59 cases, 75 cases]
**Thesis**: Weekly counts held at 71–87 in E-weeks 35–40, but the partial E-week 41 daily counts point to about 62–70 as the May–October peak season winds down (NEA). I project a mild further decline for E-week 42's provisional first print, with wide tails. The forecast is most sensitive to the settled E-week 41 total.
