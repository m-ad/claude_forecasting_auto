# Will the openai/math repository's history log show more than three total withdrawn manuscripts as of October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46131/ |
| **Tournament** | minibench — one shot, window 2026-10-19T03:18:17Z -> 2026-10-19T06:18:17Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 12.0%, IQR [7.0%, 19.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES if, at 23:59 UTC on 2026-10-29, `history.md` in github.com/openai/math (main branch) explicitly marks as withdrawn or retracted at least one manuscript besides the three withdrawn on 2026-10-07 (the Weil-classes eightfolds paper and its two K3 dependents). Revisions, errata, corrections and re-titlings do not count, and re-listing the original three does not count. If history.md disappears, an equivalent official repository record or credible reporting is used instead. Read literally, the withdrawal has to be designated as such and logged inside the next ~10.8 days.

### Outside view

No clean reference class exists for "a corporate dump of 722 AI-written preprints." The closest analogue is the repository's own track record. One internal audit found one fatal error, which took down three dependent papers on day 1, and fixed 14 others by revision. In the 11 days since (Oct 8–19) no manuscript has been withdrawn, and no commit has changed the manuscripts since Oct 8 [1][2]. That gives a crude Poisson rate of fatal-error withdrawal *events* after day 1 of 0 in about 11 days. With a weak prior of roughly 0.3–0.5 events per month left after the launch audit, P(≥1 event in 10.8 days) comes out around 10–17%. Status quo: no further withdrawal.

### Inside view

- **Pushing toward YES.** There are 719 manuscripts, and only about 42% (or by another count 162/722) of the main results are Lean-formalized [3][5]. Experts publicly expect more errors (Townsend, Sutherland) [3][4], scrutiny is intense, and OpenAI has said it will "withdraw papers if no fixes can be found." The papers form dependency chains, so one fatal error can pull several papers at once. That helps the "≥1 more" threshold.
- **Pushing toward NO.** (a) OpenAI clearly prefers repair to withdrawal: 14 revisions against 1 root-cause withdrawal. (b) The repo has been quiet. Its only commits since Oct 8 lock PR conversations (Oct 12), which cuts off the easiest public channel for error reports [2]. (c) Reviewing deep research mathematics takes outside experts weeks to months. A fatal flaw has to be found, confirmed as unfixable by OpenAI and written into history.md, all within ~10 days. (d) The most prominent outside critique, "Navier-Stokes lost in translation," argues that the Lean proof doesn't match the prose. It does not show the result is false, and OpenAI disputes it [6]. That is not the kind of thing that produces a withdrawal soon.
- Net: I nudge slightly below the naive Poisson figure because the repo is quiet and OpenAI prefers fixes, and I keep the tail open because of dependency cascades and possible batch updates. **12%.**

### Evidence

- 2026-10-19: history.md lists only the Oct 7 entry: three withdrawals plus revisions to 14 manuscripts, and 13 citation updates [1].
- 2026-10-19: commit log for main. Oct 6 initial commit; Oct 8 "Update manuscripts and Lean formalizations" (the Oct 7 errata); Oct 12 "Lock pull request conversations when opened." Nothing later [2].
- 2026-10-07/14: reporting on the withdrawals. OpenAI says an internal audit found the errors. Townsend: "suspects there will be more errors found" [3][4].
- 2026-10-06 onward: Bastounis/Circelli/Hansen preprint on the Navier-Stokes Lean translation gap, which is a critique of faithfulness rather than a refutation [6].
- No report found (searches on 2026-10-19) of any newly identified fatal error in a specific openai/math manuscript after Oct 7.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

A credible outside mathematician publicly showing that a specific openai/math result is false (not just unverified), or any new commit touching history.md, would raise this sharply. A second errata batch made up only of revisions would lower it further.

### Sources

1. https://github.com/openai/math/blob/main/history.md (raw: https://raw.githubusercontent.com/openai/math/main/history.md) (accessed 2026-10-19)
2. https://github.com/openai/math/commits/main (accessed 2026-10-19)
3. https://retractionwatch.com/?p=136176 (accessed 2026-10-19)
4. https://www.ilfoglio.it/en/science/2026/10/14/news/openai-withdraws-three-demonstrations-after-one-day-and-calls-the-mathematical-pact-into-question--410393 (accessed 2026-10-19)
5. https://aiweekly.co/alerts/openai-pulls-three-ai-generated-math-papers-over-sign-error (accessed 2026-10-19)
6. https://aiweekly.co/alerts/paper-flags-gap-in-openais-lean-verified-navier-stokes-proof (accessed 2026-10-19)
7. https://rits.shanghai.nyu.edu/ai/openai-drops-722-math-manuscripts-from-an-unreleased-model (accessed 2026-10-19)

**Question**: [Will the openai/math repository's history log show more than three total withdrawn manuscripts as of October 29, 2026?](https://www.metaculus.com/questions/46131/)
**Date**: 2026-10-19
**Forecast**: Median 12.0%, IQR [7.0%, 19.0%]
**Thesis**: As of Oct 19, history.md still lists only the three Oct 7 withdrawals, and no commit has changed a manuscript since Oct 8. OpenAI has preferred revising to withdrawing (14 to 1), so a new fatal flaw would need to be found, judged unfixable and logged within about 10 days. The forecast is most sensitive to whether an outside expert shows a specific result is false before Oct 29.
