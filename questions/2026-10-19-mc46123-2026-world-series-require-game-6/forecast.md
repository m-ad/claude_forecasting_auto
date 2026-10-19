# Will the 2026 World Series require a Game 6?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46123/ |
| **Tournament** | minibench — one shot, window 2026-10-19T00:19:04Z -> 2026-10-19T03:19:04Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-31 |
| **Status** | closed |
| **Current forecast** | Median 57.0%, IQR [53.0%, 61.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES if a Game 6 of the 2026 World Series (Milwaukee Brewers vs. the Guardians–Rays ALCS winner) is played, scheduled for 30 Oct 2026. That happens exactly when the series stands 3–2 after Game 5. It resolves NO if either team wins 4–0 or 4–1, and also NO if the series is cancelled or shortened so that no Game 6 can happen. A Game 6 that officially starts but is suspended or postponed still counts as YES. The source is Baseball-Reference's 2026_WS page, or credible reporting if that page is unavailable. Rain postponements only move dates. They do not change whether a sixth game is needed, so this is in effect "the series goes 6+ games".

### Outside view

Reference class: every best-of-seven World Series, 1905–2025 (n = 117, from the Baseball-Reference series list [2]). The lengths were 21 four-game series, 28 five-game, 27 six-game and 41 seven-game, so **68/117 = 58.1%** reached a Game 6. The recent sub-sample, 2000–2025, gives 14/26 = 53.8%: the 2020–2022 series and 2025 went six or more games, while 2023 and 2024 ended in five. A coin-flip model (each game 50/50) gives 62.5%. Real series run a little shorter than that because the two teams are rarely equal.

### Inside view

The opponent is not yet known: the ALCS was Cleveland 2–1 as of 16 Oct [1][4]. I found no Game 4 or Game 5 result [4][5]. The Brewers are clear favourites, at about -170 on DraftKings to win the title against +330 (Guardians) and +475 (Rays) [3]. Removing the bookmaker margin gives Milwaukee about 61% to win the series. That corresponds to about a 0.56–0.57 chance of winning any single game. An independent-games model with p = 0.57 gives P(4 games) = 14.0%, P(5) = 26.0% and **P(≥6) = 60.0%**. With p = 0.60 it is 57.6%. Home field (Milwaukee hosts Games 1, 2, 6 and 7) barely changes the chance of reaching Game 6.

Each source pulls a little differently. The game model says 60–61%, history says 58% and the last 26 years say 54%. A clear favourite raises the chance of a sweep or a 4–1 result: Milwaukee swept both of its earlier rounds, which hints at a larger edge than the odds imply. Small-sample streakiness also points that way. I put the probability slightly below the long-run base rate, at **57%**. The risk that the series is cancelled is negligible.

### Evidence

- ALCS: the Rays won Game 2 3–1 to level the series at 1–1 (13–14 Oct) [4]. A Game 4 preview on 16 Oct had Cleveland up 2–1 [5]. I did not find the Game 4 or Game 5 results.
- After sweeping the NLCS, the Brewers were -170 to win the World Series (implied 62.96% before removing the margin). The Guardians were +330 and the Rays +475 [3]. The World Series starts 23 Oct.
- 13 Oct (before the NLCS sweep): Brewers +105, Dodgers +350, Guardians +400, Rays +475 [6].
- Historical series lengths from Baseball-Reference: 21/28/27/41 for 4/5/6/7 games [2].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | |
| DraftKings World Series winner | Brewers -170 / CLE +330 / TB +475 | ~2026-10-16 | via SI [3]; no market on series length found |
| Polymarket / Kalshi series length | not found | 2026-10-19 | no exact-games market surfaced in searches |

### What would change my mind

- A large mismatch with the AL champion, for example a battered Rays or Guardians team coming off a seven-game ALCS against a rested Brewers rotation. Brewers odds of about -250 or longer would mean a bigger single-game edge and push the forecast toward 52–54%.
- A sportsbook exact-games or total-games price. It would replace the model-based estimate if it differed by more than about 5 points.

### Sources

1. NBC Sports, "How to watch Guardians vs Rays in 2026 MLB ALCS": https://nbcsports.com/mlb/news/how-to-watch-guardians-vs-rays-in-2026-mlb-alcs-schedule-tv-stream-info-preview-everything-to-know (accessed 2026-10-19)
2. Baseball-Reference, World Series history: https://www.baseball-reference.com/postseason/world-series.shtml (accessed 2026-10-19)
3. Sports Illustrated, "World Series odds: Brewers set as odds-on favorites after sweeping Dodgers": https://www.si.com/betting/world-series-odds-brewers-set-as-odds-on-favorites-after-sweeping-dodgers-01m52kz736d4 (accessed 2026-10-19, search snippet)
4. My Suncoast, "Tampa Bay tops Guardians 3-1 in Game 2": https://www.mysuncoast.com/2026/10/14/tampa-bay-hosting-guardians-hopes-evening-alcs-game-2/ (accessed 2026-10-19)
5. Bleacher Nation, "Guardians vs Rays Game 4 injury report, probable starters, Oct 16": https://www.bleachernation.com/stats-and-news/2026/10/16/guardians-vs-rays-game-4-injury-report-updates-probable-starters-oct-16/ (accessed 2026-10-19)
6. Sports Illustrated, "2026 World Series odds: Brewers jump to favorite": https://www.si.com/betting/2026-world-series-odds-brewers-jump-to-favorite-guardians-favored-over-rays-in-al (accessed 2026-10-19)

**Question**: [Will the 2026 World Series require a Game 6?](https://www.metaculus.com/questions/46123/)
**Date**: 2026-10-19
**Forecast**: Median 57.0%, IQR [53.0%, 61.0%]
**Thesis**: 58% of best-of-seven World Series since 1905 reached a Game 6 (68/117, Baseball-Reference), and 54% did from 2000 to 2025. A game-by-game model using the Brewers' ~61% title odds after removing the bookmaker margin (DraftKings -170) gives ~60%. The forecast is most sensitive to how big Milwaukee's per-game edge over the AL champion really is: a bigger edge makes a sweep or a 4–1 result more likely.
