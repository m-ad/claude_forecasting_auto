# How many total goals will be scored in the Singapore vs Paraguay match on 13 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46384/ |
| **Tournament** | minibench — one shot, window 2026-11-02T06:18:41Z -> 2026-11-02T09:18:41Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 2.6, IQR [1.55, 3.9] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to Singapore's goals plus Paraguay's goals at the end of regulation time (90 minutes plus stoppage time). The source is the ESPN match page (gameId 401916338) for the friendly on 13 Nov 2026 at the National Stadium, Kallang, kick-off 12:00 UTC. Penalty shoot-out goals are excluded. Postponement, cancellation or abandonment annuls the question. The outcome is a discrete count from 0 to 8, with an open top bin for 9 or more; for example, a 2-1 result resolves as 3. I treat the event as a single match with no reporting-period arithmetic, so the forecast is a distribution over a count. The question closes 11 days before the match, so neither squad is known yet.

### Outside view

- **Paraguay under Alfaro.** Paraguay's 10 matches in 2026 produced 1, 3, 4, 5, 1, 0, 2, 1, 2 and 1 total goals, a mean of about 2.0 [4][7]. Their only weak opponent in that run, Nicaragua (ranked about 130th), lost 4-0.
- **Singapore against stronger Asian sides, 2023-26.** The totals were 5, 7, 4, 4, 3, 6 and 2, a mean of about 4.4 [5][6][8]. These were Korea 5-0 and 7-0, China 2-2 and 4-1, Thailand 1-3 and 2-1, and Malaysia 6-0.
- **Strong South American sides in Asian friendlies.** Argentina 6-0 Singapore (2017, Kallang) and Indonesia 0-2 Argentina (2023) [9].
- **Reference total.** For a heavy favourite (~85 % win probability) in an international friendly, the usual total is about 2.5-3 goals.

### Inside view

I ran a Poisson model with lognormal uncertainty on each team's scoring rate: Paraguay expected goals 2.3 (σ_log 0.3), Singapore 0.5 (σ_log 0.4). It gives Paraguay win / draw / loss of 77 / 16 / 8 % and a mean total of 2.9. The market's 1X2 implies a draw nearer 10 %, which points to a slightly wider margin. I shade the median down about 0.3 goals, for three reasons:
- Alfaro's sides are conservative.
- Paraguay's first post-World-Cup window is billed as a time to test players, and they play Japan four days later. Rotation and a slower second half are likely.
- Paraguay have kept clean sheets in 4 of their last 5 matches.

The right tail stays fat because Singapore conceded 6, 7 and 5 to stronger sides, and Argentina scored 6 at this stadium.

| Total goals | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| Probability (approx.) | 7 % | 18 % | 23 % | 20 % | 14 % | 9 % | 5 % | 4 % |

### Evidence

- **Fixture.** Confirmed for 13 Nov 2026, 20:00 SGT, as the opener of the Mizuho Blue Challenge. Paraguay play Japan on 17 Nov [1][2].
- **Paraguay's recent results.** 2-0 v Bolivia (27 Sep 2026) and 1-0 v Colombia (2 Oct 2026) [4]. At the World Cup: lost 1-4 to the USA, beat Türkiye 1-0, drew 0-0 with Australia and 1-1 with Germany (won on penalties), then lost 0-1 to France [7].
- **Singapore's recent results.** Malaysia 6-0 Singapore (1 Oct 2026) [5], plus 0-2 v Indonesia and 1-0 v Bangladesh. In August they lost 1-3 to Thailand at home and won 2-1 away [6].
- **Squads.** Neither squad for the November window had been announced as of 2026-11-02.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | |
| Megapari (via OddsCalendar) | 1X2: Singapore 17.0 / draw 10.0 / Paraguay ~1.1-1.2 (the Paraguay price was garbled) | 2026-11-02 | implies roughly 85 % Paraguay win; no totals line [3] |
| Polymarket / Kalshi | none | 2026-11-02 | Polymarket is banned in Singapore |

### What would change my mind

- **Paraguay's November squad.** A full-strength attack (Almirón, Enciso, Sanabria), with a pre-announced plan to start them, would move the median to about 3. A heavily experimental squad would move it toward 2.
- **A totals line once books open.** An O/U 3.5 line favouring the over, or 2.5 priced near even, would shift the distribution by about ±0.4 goals.

### Sources

1. The Kallang, Mizuho Blue Challenge event page: https://www.thekallang.com.sg/en/things-to-do/events/mizuho-blue-challenge-the-kallang-football-series-singapore.html (accessed 2026-11-02)
2. SCMP, "Singapore host Brazil, Japan, Paraguay": https://www.scmp.com/sport/football/article/3366171/singapore-host-brazil-japan-paraguay-star-studded-football-festival (accessed 2026-11-02)
3. OddsCalendar, Singapore vs Paraguay: https://www.oddscalendar.com/football/international/international-friendlies/singapore-vs-paraguay/1640083 (accessed 2026-11-02)
4. Wikipedia, Paraguay national football team results (2020–present): https://en.wikipedia.org/wiki/Paraguay_national_football_team_results_(2020%E2%80%93present) (accessed 2026-11-02, search snippet); Drawpie, Colombia vs Paraguay recap: https://drawpie.com/blog/colombia-vs-paraguay-recap/ (accessed 2026-11-02)
5. Malay Mail, "Malaysia thrash Singapore 6-0": https://www.malaymail.com/news/sports/2026/10/02/malaysia-thrash-singapore-6-0-but-miss-out-on-fifa-asean-cup-final/237312 (accessed 2026-11-02)
6. The Star, Thailand 4-3 on aggregate v Singapore: https://www.thestar.com.my/aseanplus/aseanplus-news/2026/08/18/thailand-advances-into-asean-hyundai-cup-2026-final-after-a-4-3-aggregate-win-over-singapore (accessed 2026-11-02)
7. Copa América, Paraguay's road at World Cup 2026: https://copaamerica.com/en/news/paraguay-road-world-cup-2026 (accessed 2026-11-02)
8. Free Malaysia Today, "S. Korea trounce Singapore 7-0": https://www.freemalaysiatoday.com/category/sports/2024/06/06/lee-son-score-twice-as-s-korea-trounce-singapore-7-0 (accessed 2026-11-02)
9. ASEAN Football, "Argentina outclass Lions": https://www.aseanfootball.org/v3/argentina-outclass-lions/ (accessed 2026-11-02, search snippet)

**Question**: [How many total goals will be scored in the Singapore vs Paraguay match on 13 November 2026?](https://www.metaculus.com/questions/46384/)
**Date**: 2026-11-02
**Forecast**: Median 2.6 goals, IQR [1.55, 3.9] goals
**Thesis**: Paraguay (ranked 33rd, ~85 % win implied by Megapari's 1X2) are heavy favourites over a leaky Singapore (6-0 loss to Malaysia on 1 Oct, 7-0 to Korea in 2024), so I expect roughly 2.3 Paraguay goals plus 0.5 from Singapore. I shade that down because Alfaro's low-scoring, clean-sheet style (2026 matches averaged about 2.0 total goals) and likely rotation in a friendly four days before Japan pull the total toward 2-3. The total is most sensitive to Paraguay's November squad and the attacking intent of their starting XI.
