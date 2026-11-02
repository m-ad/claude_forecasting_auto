# How many first-place votes will the winner of the 2026 National League MVP Award receive?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46382/ |
| **Tournament** | minibench — one shot, window 2026-11-02T05:46:21Z -> 2026-11-02T08:46:21Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 29.27, IQR [27.9, 29.94] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the number of first-place votes the 2026 NL MVP winner gets, out of 30 BBWAA ballots (two writers from each of the 15 NL cities). The count comes from the BBWAA release and its ballot breakdown at bbwaa.com, published after the MLB Network announcement on 2026-11-12. If two players tie on points and share the award, the higher first-place count counts. The range is closed at 0–30, and a unanimous winner resolves 30. Ballots were cast before the postseason, so the Cubs' Wild Card exit does not matter. The question depends on the winner, whoever that is. In practice that means Pete Crow-Armstrong (PCA): if he wins, it is his count, and if Shohei Ohtani pulls an upset, it is Ohtani's count, which would almost certainly be below 20. Arithmetic: each Ohtani (or other) first-place vote takes one off a PCA sweep, so 2 dissenters gives 28. The cached question text says Ohtani "did not pitch". That is wrong: he made 14 starts with a 1.79 ERA (85⅔ IP) before shutting down after July 3 [2][4].

### Outside view

Reference class: MVP winners in either league since 2014 who were clear favourites, i.e. they led their league in WAR with no rival of comparable value. The first-place counts were Trout '14 30, Harper '15 30, Bryant '16 29, Betts '18 28, Yelich '18 29, Freeman '20 28, Judge '22 28, Acuña '23 30, and Ohtani '21/'23/'24/'25 30 each. That is n ≈ 12: about half were unanimous, about 85 % got 28 or more, and none got fewer than 28. The counts for Ohtani '24/'25, Acuña '23, Freeman '20 and Goldschmidt '22 are from the question text; the rest are from memory, and I flag them as such. Contested races are a separate class with much lower counts: Harper '21 17, Judge '25 17, Bellinger '19 19, Goldschmidt '22 22. The base rate for a clear favourite is roughly P(30) ≈ 0.45, P(29) ≈ 0.2, P(28) ≈ 0.15, with a small tail for races that turn out more contested than they looked.

### Inside view

This race belongs to the clear-favourite class:
- PCA hit .280/.372/.570 with 45 HR (tied for the MLB lead) and 41 SB, the seventh 40-40 season ever. He had 9.8 bWAR and 10.6 fWAR, leading MLB in both, plus elite centre-field defence [3].
- In MLB.com's final poll (Sep 22), he took **all 38 first-place votes** [2]. In the Aug 25 poll he had 29 of 37 [4].
- He won the MLBPA Players Choice Player of the Year over finalist Ohtani [5].
- Markets had him at about 89 % on Kalshi in early September and -390 at FanDuel in late August, before his strong finish [6][7].

The runner-up is the one source of risk. Ohtani is a four-time MVP with a two-way narrative: 1.79 ERA over 85⅔ IP, and a bat at 30 HR and 142 wRC+ as of Sep 22 [2]. A comparable case is 2022, when Judge's historic season still lost two first-place votes to two-way Ohtani. Here Ohtani's case is clearly weaker than in 2022 (a half-season of pitching, a modest bat), but BBWAA panels contain contrarians and value-per-inning voters. Against that, 38/38 on a 38-person expert panel is strong evidence that dissent is rare.

The MLB.com poll nudges the outside view up slightly: P(30) = 0.45. I keep a fat lower tail for an upset or a split.

| Outcome | P |
|---|---|
| 30 | 0.45 |
| 29 | 0.22 |
| 28 | 0.13 |
| 27 | 0.07 |
| 26 | 0.04 |
| 25 | 0.025 |
| 20–24 | 0.04 |
| < 20 (incl. an Ohtani win) | 0.025 |

Continuous-CDF percentiles (the 30 bin spans 29.5–30.5): p5 22.6, p10 25.75, p25 27.9, p50 29.27, p75 29.94, p90 30.28, p95 30.39.

### Evidence

- **Sep 22, 2026:** MLB.com final MVP poll. NL points: PCA 190 with 38/38 first-place votes, Ohtani 135, Misiorowski and De La Cruz 61 each, Schwarber 32. Ohtani's line in the poll: 30 HR, 142 wRC+, 1.79 ERA, 95 K over 85⅔ IP, done pitching for the season [2].
- **Sep 29, 2026:** CBS: PCA's final line as above, "the overwhelming favorite to win the National League MVP" [3].
- **Aug 25, 2026:** MLB.com fifth poll: PCA 177 points with 29 of 37 first-place votes, Ohtani 154 with 8 [4]. Ohtani last pitched July 3.
- **Aug 19, 2026:** ESPN player survey: PCA 15, Ohtani 4 (search snippet).
- **Oct 28, 2026:** PCA won Players Choice Player of the Year and NL Outstanding Player [5].
- **Early Oct 2026:** The Cubs lost the Wild Card series to San Diego [8]. This came after balloting, so it is irrelevant.
- **Nov 2, 2026:** No BBWAA writer ballot reveals or pro-Ohtani 2026 MVP pieces found from September to November (four searches).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Kalshi NL MVP | PCA 89 %, Ohtani 11 % | 2026-08-31/09-09 | stale; prices the winner, not the count [6] |
| FanDuel | PCA -390, Ohtani +300 | late Aug 2026 | stale [7] |
| Polymarket NL MVP | PCA ~98.9 % | undated | search snippet only, unverified |
| Unanimity prop | none found | 2026-11-02 | |

### What would change my mind

- The BBWAA finalists list (announced Nov 2) leaving out Ohtani, or putting a pitcher (Misiorowski) alongside him. Either would shift the dissent risk slightly.
- Any writer publicly revealing a non-PCA first-place vote, which would cap the outcome at 29 or below.

### Sources

1. Metaculus question text, cached at `raw/metaculus-question-2026-11-02.json`; BBWAA voting FAQ https://bbwaa.com/voting-faq (accessed 2026-11-02)
2. MLB.com, "Our final MVP poll has clear frontrunners…", Sep 22, 2026 https://www.mlb.com/news/yordan-alvarez-pete-crow-armstrong-lead-final-2026-mvp-poll (accessed 2026-11-02)
3. CBS Sports, PCA season among best Cubs seasons ever https://cbssports.com/mlb/news/pete-crow-armstrong-best-cubs-seasons-ever-playoffs (accessed 2026-11-02)
4. Yardbarker / MLB.com fifth MVP poll, Aug 25, 2026 https://www.yardbarker.com/mlb/articles/mlb_announces_nl_mvp_poll_update_on_tuesday/s1_17615_44218679 (accessed 2026-11-02)
5. Chicago Sun-Times, PCA Players Choice Player of the Year, Oct 28, 2026 https://chicago.suntimes.com/cubs/2026/10/28/cubs-pete-crow-armstrong-player-of-the-year-players-choice-awards-nl-mvp (accessed 2026-11-02)
6. SI, PCA overwhelming Ohtani in NL MVP Kalshi market https://www.si.com/prediction-markets/pete-crow-armstrong-overwhelming-shohei-ohtani-in-nl-mvp-kalshi-market-01m1c7yfst1k (accessed 2026-11-02)
7. Bleacher Nation, latest NL MVP odds https://www.bleachernation.com/?p=2750526 (accessed 2026-11-02, snippet)
8. The Big Lead, Cubs Wild Card loss to Padres https://www.thebiglead.com/cubs-crow-armstrong-argues-umpire-controversial-call/ (accessed 2026-11-02, snippet)

**Question**: [How many first-place votes will the winner of the 2026 National League MVP Award receive?](https://www.metaculus.com/questions/46382/)
**Date**: 2026-11-02
**Forecast**: Median 29.3 first-place votes, IQR [27.9, 29.9]
**Thesis**: The reference class is clear-favourite MVP winners since 2014, about half of whom were unanimous and none of whom got fewer than 28. Pete Crow-Armstrong fits it: 40-40, 45 HR, MLB-leading 10.6 fWAR, and all 38 first-place votes in MLB.com's final poll [2][3]. The forecast is most sensitive to how many writers reward Shohei Ohtani's two-way half-season (1.79 ERA over 85⅔ IP), which is the main route to a 28–29 count rather than a 30.
