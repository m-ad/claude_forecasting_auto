# How many advance votes will have been cast in New Zealand's 2026 general election through 29 October 2026 (the fourth day of advance voting)?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46164/ |
| **Tournament** | minibench — one shot, window 2026-10-20T04:32:21Z -> 2026-10-20T07:32:21Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-10-20 / 2026-10-20 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 310000, IQR [278000, 342000] (v1, 2026-10-20) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-20

### What resolves YES

The question resolves to a number: the cumulative count of in-person advance votes cast inside New Zealand (overseas votes excluded) from Monday 26 October through Thursday 29 October 2026, the first four days of advance voting. The count is taken from the Electoral Commission's informal daily advance-voting statistics page for 2026. If only daily figures are published, the four days are summed. The informal figure published at the time decides it, not the later official count. Credible media citing the Commission are the fallback. The question is annulled only if no figure exists at all. Both bounds (150k and 500k) are open. The days line up with 2023: a 12-day window starting on a Monday, so 29 Oct 2026 corresponds to Thu 5 Oct 2023.

### Outside view

The reference class is the first four days of advance voting at past NZ general elections, from the Commission's daily tables [1][2]:

| Election | Days 1–4 cumulative | Advance total | Days 1–4 share |
|---|---|---|---|
| 2017 (Mon 11–Thu 14 Sep) | 226,824 | 1,240,740 | 18.3% |
| 2020 (Sat 3–Tue 6 Oct; COVID year, 14-day window) | 366,182 (411,779 from the first Monday) | 1,976,996 | ~19–21% |
| 2023 (Mon 2–Thu 5 Oct), current table | 339,032 | 1,640,204 | 20.7% |

**Caveat on the 2023 row.** The current 2023 table was revised in February 2024 to include special votes [1]. The figures published live during the campaign were about 13% lower:

- Day 1 was reported at 56,557 and then 58,308, against 65,845 in today's table [3][4].
- Days 1–3 were reported at 204,191, against 235,415 [3].
- The official count of ordinary advance votes for 2023 was 1,385,171 [5], about 84.5% of the 1,640,204 in the table.

Scaling day 4 of 2023 by the same ratio puts the live, campaign-time figure through 5 Oct 2023 at about **294,000**. That is the most directly comparable base value. A 2023-like campaign therefore gives roughly 290–300k on the live basis, or about 340k if 2026 reports specials as well. Early turnout varies widely between elections: 2020 ran about 30% ahead of 2023 in the first three days.

### Inside view

**Upward pressures**
- The advance share keeps rising: 47% of votes in 2017, about 61% in 2023 (question text).
- The 2026 race is close. 1News-Verian had National 28 and Labour 28 (8–12 Oct), and Anacta had Labour 29 and National 28. Close races plausibly bring out early voters [6].
- The ODT reports about 850 advance voting places for 2026 [7]. In 2023 there were "more than 400" on day 1, rising later [8]. These figures are not strictly comparable.
- If the 2026 page counts all votes taken, specials included (the basis of today's 2023 table), the 2023 analogue is 339k rather than 294k.

**Downward pressures and flat factors**
- Enrolling or changing details during the voting period is no longer possible [9]. In 2023 that produced a large stream of special votes, more than 600,000 in total. Removing it shrinks the specials component whichever basis is reported.
- Enrolment is flat: 3.68m against 3.69m.
- The 2023 start was slow, and 2026 could repeat it.

**Net judgement.** Take ordinary advance votes at about 294k on the 2023 basis. Add modest growth of about 3–5% from the trend and the tight race, plus a partial specials component in case the page counts them. That gives a central estimate of about 310k. The spread is wide because pace varies roughly ±25% between elections and the reporting basis is uncertain. The left tail allows for a slow start and an ordinary-only basis. The right tail allows a 2020-like surge and a specials-inclusive count.

| Percentile | 5 | 10 | 25 | 50 | 75 | 90 | 95 |
|---|---|---|---|---|---|---|---|
| Votes | 228,000 | 247,000 | 278,000 | 310,000 | 342,000 | 375,000 | 398,000 |

### Evidence

- **2023, current Commission table [1]:** 65,845 / 80,899 / 88,671 / 103,617 on 2–5 Oct. Total 1,640,204. Revised Feb 2024 to include special votes. Accessed 2026-10-20.
- **2023, live reporting:** 1News (6 Oct 2023) gave 58,308 on day 1 and 204,191 for days 1–3, against more than 264,000 in 2020 [3]. Newshub had day 1 at 56,557, described as preliminary [4].
- **2023, official result [5]:** 1,385,171 advance votes, excluding special declaration votes (search snippet).
- **2017 [2]:** 39,570 / 48,238 / 66,084 / 72,932.
- **2020 [10]:** 92,434 / 66,821 / 105,489 / 101,438 (Sat–Tue), described as approximate.
- **2026 arrangements:** advance voting 26 Oct–6 Nov, enrolment deadline midnight Sun 25 Oct, no enrolment during voting [9][11]. About 2,300 voting places and about 850 advance voting places (ODT, 10 Aug 2026) [7].
- **2026 polls:** National and Labour level at about 28–29% in early-to-mid October [6] (scout summary of the Wikipedia polling page).

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-20 | — |
| Polymarket NZ 2026 turnout brackets | 80–82%: ~36%; ≥84%: ~15–26% | May–Jul 2026 (stale aggregator snapshots) | very thin; total turnout, not advance votes |
| Kalshi / Manifold | none found | 2026-10-20 | — |

### What would change my mind

- **Reporting basis.** If the 2026 page reports specials together with ordinary votes, as today's 2023 table does, the centre moves up by about 15–25k. A strictly ordinary-only basis moves it down by about 10k.
- **Day-1 pace.** If day 1 (Mon 26 Oct) came in at about 70k or more, or below about 50k, I would shift the whole distribution by roughly that ratio.

### Sources

1. Electoral Commission, 2023 General Election voting statistics: https://elections.nz/democracy-in-nz/historical-events/2023-general-election/voting-statistics (accessed 2026-10-20)
2. Electoral Commission, 2017 advance voting statistics: https://elections.nz/democracy-in-nz/historical-events/2017-general-election/advance-voting-statistics-for-the-2017-general-election (accessed 2026-10-20)
3. 1News, "Five questions about the first week of voting, answered" (6 Oct 2023): https://www.1news.co.nz/2023/10/06/five-questions-about-the-first-week-of-voting-answered (accessed 2026-10-20)
4. Newshub, "Election 2023: Kiwis not rushing to polls, voter turnout down on 2020": https://newshub.co.nz/home/politics/2023/10/election-2023-kiwis-not-rushing-to-polls-voter-turnout-down-on-2020.html (search snippet, accessed 2026-10-20)
5. Electoral Commission, 2023 official result, advance votes: https://electionresults.govt.nz/electionresults_2023/advance-votes.html (search snippet, accessed 2026-10-20)
6. Opinion polling for the 2026 New Zealand general election: https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_New_Zealand_general_election (scout summary, accessed 2026-10-20)
7. ODT, "Election 2026 by the numbers" (10 Aug 2026): https://www.odt.co.nz/news/national/election-2026-by-the-numbers-uwt3mw4v (accessed 2026-10-20)
8. Electoral Commission / MPIA, "Voting underway for 2023 general election": https://mpia.govt.nz/latest-news/voting-underway-for-2023-general-election/ (search snippet, accessed 2026-10-20)
9. 1News, "Key dates and new voting rules as NZ's election countdown begins" (25 Jan 2026): https://www.1news.co.nz/2026/01/25/key-dates-and-new-voting-rules-as-nzs-election-countdown-begins (accessed 2026-10-20)
10. Electoral Commission, 2020 advance voting statistics: https://elections.nz/stats-and-research/2020-general-election-advance-voting-statistics/ (accessed 2026-10-20)
11. Electoral Commission, 2026 General Election: https://www.elections.nz/2026-general-election (accessed 2026-10-20)

**Question**: [How many advance votes will have been cast in New Zealand's 2026 general election through 29 October 2026 (the fourth day of advance voting)?](https://www.metaculus.com/questions/46164/)
**Date**: 2026-10-20
**Forecast**: Median 310,000 votes, IQR [278,000 votes, 342,000 votes]
**Thesis**: Anchored on the same four days in 2023: about 294k as reported live during the campaign (339k in today's table, which now includes special votes). Nudged up for the rising advance-vote share and a tight National–Labour race. The result is most sensitive to whether the 2026 daily page counts special votes and to the day-1 turnout pace.
