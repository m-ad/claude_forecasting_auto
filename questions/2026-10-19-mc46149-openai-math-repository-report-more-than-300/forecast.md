# Will the openai/math repository report more than 300 top-line results formalized in Lean as of October 29, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46149/ |
| **Tournament** | minibench — one shot, window 2026-10-19T16:57:22Z -> 2026-10-19T19:57:22Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-29 |
| **Status** | closed |
| **Current forecast** | Median 20.0%, IQR [12.0%, 30.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES only if, when `history.md` in github.com/openai/math is read on 2026-10-29 (UTC), its **most recent entry** gives a numerator above 300 for "total percentage of top-line results formalized" (or a cumulative count above 300). If history.md gives no numerator, the README percentage × the stated total (719 today), rounded, is used instead. 300 or fewer, including a drop caused by more withdrawals, resolves NO. If the repository is permanently gone, the question is annulled. So YES needs OpenAI to push a new batch containing at least one new *top-line* formalization and record it in history.md within the next 10 days. A history entry that only covers fixes or withdrawals does not count.

### Outside view

There is no clean reference class. The nearest one is the repository's own update record. Since launch on 2026-10-06 (13 days ago) it has had exactly one content update: the 10-07 batch, merged 2026-10-08 [1][2]. The only other commit (10-12) locked pull-request conversations. In the 11 days since the last content change, nothing has landed. If substantive updates arrive as a Poisson process at roughly 1 per 2–4 weeks, the chance of at least one in a 10-day window is about 30–50%. The first batch was a post-launch cleanup (withdrawals and fixes) that happened right after release, so that rate is probably too high for steady state. Corporate "we will update as we obtain them" pledges tend to see slowing, irregular updates once the launch news cycle is over. Prior: about 25%.

### Inside view

- **Against:** There have been no content commits for 11 days [2]. Only 6 new formalizations came out of the first post-launch batch [1][5], so the formalization pipeline looks slow. OpenAI is also "exploring community-hosted repositories" [3], which could move future work out of this repo. And an update could be fixes or withdrawals only, which would leave the count at ≤300.
- **For:** OpenAI made an explicit, public commitment to add formalizations [3][4]. The first batch was dated 10-07, so a roughly 3-week cadence would put the next one around 10-28, inside the window. OpenAI also has reputational reasons (the Navier–Stokes critique, the sign-error withdrawals) to show more machine-checked results, and any batch with even one new top-line formalization resolves YES.
- I moved slightly down from the 25% prior because of the 11-day silence and the slow pipeline. Final: about 20%.

### Evidence

- history.md has a single dated entry, **October 7, 2026**: 3 withdrawals, 14 manuscripts with repairs, 13 citation updates, "6 formalizations and 5 other additions". It states "300 / 719 = ~42%". Fetched 2026-10-19 [1].
- Commits on main: 10-06 initial commit; 10-08 "Update manuscripts and Lean formalizations" (PR #1); 10-12 "Lock pull request conversations" (PR #2). Nothing since. Fetched 2026-10-19 [2].
- The README says "~42% top-line results formalized" and "719 manuscripts organized into 372 families", and promises to keep adding Lean formalizations "as we obtain them". It gives no schedule [3].
- Secondary coverage dated as late as 10-09 reports no changes after 10-08 [5]. A search on 2026-10-19 found no news of a later update [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

- Any commit to openai/math after 10-12 that touches `lean/` or history.md, or a tweet from an OpenAI researcher (e.g. Dan Roberts) announcing a new batch. Either would push this above 60%.
- An announcement that the materials are moving to a community-hosted repository would push it below 10%.

### Sources

1. openai/math history.md — https://github.com/openai/math/blob/main/history.md (accessed 2026-10-19)
2. openai/math commit log — https://github.com/openai/math/commits/main (accessed 2026-10-19)
3. openai/math README — https://github.com/openai/math (accessed 2026-10-19)
4. OpenAI, "Sharing AI progress in mathematics" — https://openai.com/index/sharing-ai-progress-in-mathematics/ (accessed 2026-10-19, via search)
5. Redreamality, "OpenAI Math's Correction Week" — https://redreamality.com/blog/ai-math-verification-lean-faithfulness/ (accessed 2026-10-19)
6. Developers Digest, "OpenAI Math Repo: What the Lean Proofs Do and Don't Verify" — https://www.developersdigest.tech/blog/openai-math-repo-lean-proofs-what-they-verify-2026 (accessed 2026-10-19)
7. zeli.app report of Dan Roberts' update post — https://zeli.app/ru/story/50002650 (accessed 2026-10-19, via search)

**Question**: [Will the openai/math repository report more than 300 top-line results formalized in Lean as of October 29, 2026?](https://www.metaculus.com/questions/46149/)
**Date**: 2026-10-19
**Forecast**: Median 20.0%, IQR [12.0%, 30.0%]
**Thesis**: The repository has had one content update since launch (the 10-07 batch, merged 10-08: 6 new formalizations, bringing it to 300/719) and nothing for 11 days, so the status quo of 300 is the base case. YES needs a new batch with at least one new top-line formalization recorded in history.md by 10-29. OpenAI's public pledge to keep adding formalizations, and a possible ~3-week cadence, keep that chance material.
