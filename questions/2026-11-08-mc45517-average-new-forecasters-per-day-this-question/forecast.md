# What will the average new forecasters per day be on this question before this question closes?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/45517/ |
| **Tournament** | bot-testing-area — one shot, window 2026-09-06T06:00:00Z -> 2028-09-05T06:00:00Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-09-06 / 2028-09-05 / 2028-09-06 |
| **Status** | open |
| **Current forecast** | Median 0.33, IQR [0.23, 0.46] (v1, 2026-11-08) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-08

### What resolves YES

The question resolves to the number of forecasters shown in the Metaculus UI for this question on its close date (2028-09-05 06:00 UTC), divided by the number of days it was open, rounded to two decimals. Days open: 2026-09-06 → 2028-09-05 = 365 + 365 = **730 days** (2028 is a leap year, but Feb 29 2028 falls in the second year, which ends on Sep 5 rather than Sep 6). Bounds: 0.1/day = 73 forecasters, 0.8/day = 584 forecasters, both open. So the forecast is really for the total count of unique accounts on this question after two years: value = N / 730. The question is about 63 days old today. It sits in the "bot-testing-area" project, the practice space Metaculus recommends to bot makers.

### Outside view

No direct reference class with published counts. Proxy: how many bot accounts are active. FutureEval Spring 2026 had 173 bots (111 external, about 65 run by Metaculus) [2]. Fall 2025 had 134 [4]. Q2 2025 had 54 bot makers [5]. The testing area holds only a handful of questions (one per type) [1, 3], so any bot that tests there tends to forecast on all of them. Over about six tournament seasons (Fall 2026 to Summer 2028), each with tens of new bot accounts plus re-registrations, the pool of unique accounts that ever touch the testing area could plausibly reach 100–400. A naive "one season's worth of bots", about 150, gives 0.21/day.

### Inside view

- Upward: this is the official place to test and the tournament rules discourage testing elsewhere [3]. Bots keep running for two years. Some bot makers start bots that forecast on every open question in a project. Our own bot forecast here.
- Downward: many bot makers test on MiniBench warmups or practice questions instead [1]. Counts are unique forecasters, not forecasts. Interest could fade, or the testing area could be replaced.
- Net: median about 240 forecasters, i.e. **0.33/day**. The distribution is right-skewed: participation in bot forecasting is growing and the upper bound is open. The interval is wide on both sides because I have no current count for this question.

### Evidence

- Bot testing area announced in the 2026 FutureEval announcements: practice questions for bot makers, one of each type [1, 3] (accessed 2026-11-08).
- Spring 2026: 173 bots, 111 excluding Metaculus-run ones [2].
- Fall 2025: 134 bots; Spring 2026 survey: 48 tournament bot makers plus 10 MiniBench-only [4, 5].
- Fall 2026 MiniBench started 2026-09-21, tournament questions from 2026-09-28 [3]. This question opened 2026-09-06, just before the Fall onboarding wave.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-08 | |
| Polymarket / Kalshi / Manifold | none found | 2026-11-08 | no market on this quantity |

### What would change my mind

The current forecaster count on this question after 63 days. If it were already 100 or more, the median would rise to about 0.45. If it were under 25, the median would fall to about 0.2. The other key fact is whether Metaculus keeps directing new bot makers to the testing area through 2028.

### Sources

1. EA Forum, "Announcing Metaculus Summer 2026 FutureEval Bot Tournament" — https://forum.effectivealtruism.org/posts/ZfLAN557rGWACKtmc/announcing-metaculus-summer-2026-futureeval-bot-tournament (accessed 2026-11-08)
2. LessWrong, "FutureEval Spring results: pros beat bots but the gap is…" — https://www.lesswrong.com/posts/wZBbDqzfBjYG58CxK/futureeval-spring-results-pros-beat-bots-but-the-gap-is (accessed 2026-11-08)
3. EA Forum, "Announcing Fall 2026 FutureEval Bot Tournament" — https://forum.effectivealtruism.org/posts/hrJrsgMCwsdBuAqgQ/announcing-fall-2026-futureeval-bot-tournament (accessed 2026-11-08)
4. EA Forum, "FutureEval Forecasting Bot-Maker Survey: What Winners Did Differently" — https://forum.effectivealtruism.org/posts/CauF6PstTHK3goE2g/futureeval-forecasting-bot-maker-survey-what-winners-did (accessed 2026-11-08)
5. EA Forum, "What AI forecasting strategy works best? Spring 2026 survey" — https://forum.effectivealtruism.org/posts/tJoxFWkRev5wrEBar/what-ai-forecasting-strategy-works-best-spring-2026-survey (accessed 2026-11-08)
6. Longterm Wiki, "AI Forecasting Benchmark Tournament" — https://www.longtermwiki.com/wiki/E10 (accessed 2026-11-08)

**Question**: [What will the average new forecasters per day be on this question before this question closes?](https://www.metaculus.com/questions/45517/)
**Date**: 2026-11-08
**Forecast**: Median 0.33 forecasters, IQR [0.23 forecasters, 0.46 forecasters]
**Thesis**: The value is the total number of unique forecasters after 730 days, divided by 730. The bot ecosystem has about 130–175 bots per season [2, 4], and the testing area is the recommended practice space [1, 3], so about 240 unique accounts over two years is the central case. The forecast is most sensitive to how many new bots actually test on this question, which I could not observe directly.
