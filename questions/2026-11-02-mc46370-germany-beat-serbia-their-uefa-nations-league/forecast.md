# Will Germany beat Serbia in their UEFA Nations League match on 13 November 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46370/ |
| **Tournament** | minibench — one shot, window 2026-11-02T01:18:46Z -> 2026-11-02T04:18:46Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | open |
| **Current forecast** | Median 70.0%, IQR [64.0%, 75.0%] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

YES if UEFA's official match page for Serbia vs Germany (UEFA Nations League 2026/27 League A Group A2, matchday 5, Fri 13 Nov 2026, Stadion Rajko Mitić, Belgrade, 19:45 UTC) shows Germany scoring more goals than Serbia over 90 minutes plus stoppage time. A draw or a Serbia win resolves NO. There is no extra time in a league-phase match, so only the 1X2 result counts. If the match is postponed, the question resolves on whatever result UEFA records later, including one awarded by disciplinary decision. Arithmetic: after four matchdays Germany has 5 points against 8 each for the Netherlands and Greece. With two games left Germany needs a win here to keep a realistic top-two chance, so heavy rotation is unlikely. Serbia has 0 points, is out of top-two contention, and is playing to avoid finishing bottom.

### Outside view

The reference class is a strong European side playing away at a clearly weaker one, where the bookmaker market prices the favourite at about 1.20–1.25 decimal odds. Favourites at that price win about 75–80% of the time (an approximate figure from memory, not sourced). The direct anchor is the FanDuel three-way line for this fixture: Serbia +900, draw +500, Germany −475. With the bookmaker margin removed, that gives Germany 75.6%, a draw 15.3% and Serbia 9.1% [3]. Two other reference points: Germany was about 80% (odds 1.18–1.25) at home to Serbia on 1 Oct [4], and about 52–54% away at the stronger Greece on 4 Oct [4].

### Inside view

- **Behind closed doors (+).** UEFA has ordered the match played without spectators, and German fans are barred too, as a sanction for racist behaviour by Serbian fans [5]. That removes most of the hostile-crowd home advantage, which is why a Belgrade price close to the Munich price is plausible.
- **Serbia are weak (+).** They have lost all four group games, two of them at home to Greece and the Netherlands (1–2 each), and six of their last seven matches in 2026, including 0–3 against Cape Verde [1][6]. Coach Paunović is reportedly suspended from the bench for this match (single source, nova.rs [7]).
- **Germany's form is poor (−).** Under Klopp they have one win in four and three goals scored: 1–1 at the Netherlands, 0–1 at home to Greece, 2–0 against Serbia, 0–0 in Greece [1][2]. Some of that is finishing variance (a disallowed goal and 15 shots to 1 in the first half in Greece [8]). Musiala and Havertz were injured in September, and the November squad is named on 5 Nov [2].
- **Single-game draw risk (−).** International away favourites often draw. A 0–0 or 1–1 is the main route to NO, and the +500 draw price looks a little thin to me. A model estimate (wincomparator, snippet only) gives Germany 61% [9].

Net: I start from the 75.6% market price and take off about 5 pp for Germany's poor finishing and the draw risk, partly crediting the lower model estimate. Median **70%**. The IQR of 64–75% reflects one bookmaker line on an early, thin market and unknown squad news.

### Evidence

- 2026-10-04 standings: NED 8, GRE 8, GER 5 (W1 D2 L1, 3–2), SRB 0 (L4, 3–8) [1].
- 2026-10-01: Germany 2–0 Serbia in Munich (Bischof 39', Wirtz 61'), Klopp's first win [2][6].
- 2026-10-22: UEFA orders Serbia vs Germany behind closed doors; €50k fine [5].
- 2026-07: Nagelsmann resigned after a round-of-32 penalty loss to Paraguay at the World Cup; Klopp appointed 24 Jul [10].
- FIFA ranking (2 Oct 2026): Germany 12th, Serbia 40th [6].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-02 | — |
| FanDuel 3-way | GER −475 / D +500 / SRB +900 → 75.6% Germany, margin removed | 2026-11-02 | search snippet; page returned 403 |
| wincomparator model | 61% Germany | 2026-11-02 | snippet only |
| Polymarket / Kalshi | none found | 2026-11-02 | — |
| Manifold | none for this match | 2026-11-02 | — |

### What would change my mind

- Germany's 5 Nov squad: a weakened or rotated XI (e.g. Wirtz absent) would bring the price down toward 60%.
- Pre-match bookmaker consensus: if several books price Germany around 1.40 instead of 1.21, the forecast should go toward 65%.

### Sources

1. Wikipedia, 2026–27 UEFA Nations League A — https://en.wikipedia.org/wiki/2026%E2%80%9327_UEFA_Nations_League_A (accessed 2026-11-02)
2. 90min.de, Klopp squad announcement date — https://www.90min.de/zweite-landerspielperiode-fur-klopp-termin-fur-kaderbekanntgabe-steht (accessed 2026-11-02)
3. FanDuel Sportsbook, Serbia v Germany — https://sportsbook.fanduel.com/soccer/uefa-nations-league-a/serbia-v-germany-36167680 (accessed 2026-11-02, via search snippet)
4. The Football Faithful, Germany vs Serbia odds 1 Oct — https://thefootballfaithful.com/germany-vs-serbia-prediction-betting-tips-01-10-2026/ ; Sportytrader Greece–Germany — https://www.sportytrader.com/en/betting-tips/greece-germany-376592/ (accessed 2026-11-02)
5. bluewin, "Serbia vs. Germany without spectators", 22 Oct 2026 — https://www.bluewin.ch/en/sport/football/serbia-vs.-germany-without-spectators-li.3644878 (accessed 2026-11-02)
6. Times of Oman, Klopp's first win — https://timesofoman.com/article/177566-uefa-nations-league-jurgen-klopp-gets-first-win-as-germany-manager-with-2-0-victory-over-serbia (accessed 2026-11-02)
7. nova.rs, Paunović suspended — https://nova.rs/paunovic-suspendovan-ne-moze-da-vodi-srbiju/ (accessed 2026-11-02)
8. Neos Kosmos, Greece 0–0 Germany — https://neoskosmos.com/en/2026/10/05/sport/greece-hold-germany-0-0-secure-third-and-keep-nations-league-quarter-final-hopes-in-their-hands/ (accessed 2026-11-02)
9. wincomparator, Serbia–Germany prediction — https://www.wincomparator.com/predictions/serbia-germany-8318328/ (accessed 2026-11-02, snippet only)
10. UPI, Klopp hired as Germany coach — https://www.upi.com/Sports_News/Soccer/2026/07/24/germany-Jurgen-Klopp-hired-national-team-coach/1371784894293/ (accessed 2026-11-02)

**Question**: [Will Germany beat Serbia in their UEFA Nations League match on 13 November 2026?](https://www.metaculus.com/questions/46370/)
**Date**: 2026-11-02
**Forecast**: Median 70.0%, IQR [64.0%, 75.0%]
**Thesis**: Bookmakers price Germany at about 76% with the margin removed (FanDuel −475) to win in a Belgrade match UEFA has ordered played behind closed doors, against a Serbia side with 0 points from four games. I shade that down to 70% for Germany's poor finishing under Klopp (one win and three goals in four games) and the risk of a draw. The forecast is most sensitive to the November squad news and to whether other bookmakers confirm the ~1.21 price.
