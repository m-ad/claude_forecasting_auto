# Research log — Who will win the 2026 World Chess Championship?

Working notes. Rough is fine; **completeness beats polish**.

## Question mechanics

Read from the **official FIDE regulations** (FIDE Council document CM2-2026_06), not from
secondary write-ups, because two widely-repeated claims about this match are simply false.

- **Players**: **Gukesh Dommaraju** (IND, b. 2006-05-29), defending champion, vs
  **Javokhir Sindarov** (UZB, b. 2005-12-08), winner of the 2026 Candidates. Youngest
  combined-age title match ever; Sindarov turns 21 *during* the match, on 8 December.
- **Format**: **14 classical games**, first to **7½** points, play stops immediately on 7½.
  Time control 120 min/40 moves, +30 min, 30-sec increment **from move 41 only**. No draw
  offers before Black's 40th move.
- **Schedule**: Game 1 **2026-11-24**, 15:00 CET; rest days 27 Nov, 1, 5, 9 Dec; Game 14
  **2026-12-11**; tiebreaks and closing **2026-12-12**. Geneva, Switzerland. FIDE is itself
  the organiser (Art. 1.2). Prize fund **US$2.5m**. Art. 4.6.2: *"No postponement of any game
  is allowed."*
  - **Date trap**: FIDE's own 2026-07-28 host announcement still says "25 November to
    15 December" and has never been corrected on fide.com. The FIDE Council changed it in late
    August to 22 Nov – 13 Dec. Many secondary outlets still carry the old window.
- **TIEBREAK — two myths killed.** Art. 4.4.1: *"If the score after fourteen games is equal,
  the tie-break shall be played."* There is **no draw-odds retention for the champion**. And
  there is **no Armageddon**: the ladder is 4 games at 15+10, then 2 at 10+5, then 2 at 3+2,
  then **repeated 3+2 pairs with colours reversed until decisive**. Several secondary sources
  describe an "Armageddon elimination" and at least one automated summary asserted the champion
  retains on a drawn match — both wrong, and both would have materially changed this forecast.
- **Replacement (Art. 2.2–2.4)**: if a player withdraws, **Anish Giri** replaces him, then
  Fabiano Caruana, then the highest-rated eligible player on the September 2026 list.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Higher-rated player wins the WCC match | 11 | 2006–2024 | **8 of 11 = 72.7%** | Wikipedia match infoboxes, pre-match Elo | yes, primary |
| Favourite with a pre-match gap ≥ 55 Elo wins | 6 | 2012–2024 | 6 of 6 (the only ≥55 loss is 2006's +70 reunification match) | same | yes |
| Defending champion retains | 9 | 2008–2024 | **7 of 9 = 77.8%** | same | yes — but see below |
| Defending champion who is the *rating underdog* retains | 2 | Anand 2013, Ding 2024 | **0 of 2** | same | yes — this is the class Gukesh is in |
| Match goes to tiebreaks | 11 | 2006–2024 | 5 of 11 = 45.5% | same | partially |
| …restricted to **14-game** matches | 6 | 2006, 2008, 2010, 2021, 2023, 2024 | **2 of 6 = 33%** | same | yes, the relevant one |

The two headline classes **conflict**: "higher-rated wins 73%" favours Sindarov, "champion
retains 78%" favours Gukesh. The tiebreaker is the third class — both champions who lost in
this era (Anand 2013, Ding 2024) were the rating underdog, exactly as Gukesh is now, and both
lost. That sub-class is 0 for 2. Small n, but it is the only one that conditions on the actual
configuration.

## The model, and why the model family is the whole argument

Two standard ways to turn an Elo gap into a match probability disagree by ~15 points here,
and the disagreement is entirely about **the win:loss odds ratio**, not the draw rate.

**(a) Davidson**: fix the win:loss **odds** at `10^(D/400)` and let draws eat both sides
proportionally. At +75 that is odds of **1.54**. Draws then compress the favourite's edge.

**(b) Expected-score-preserving**: fix the Elo expected score (0.606 at +75) and let draws
absorb the remainder, `w = E − d/2`. At a 0.64 draw rate that implies w = 0.266, l = 0.094,
i.e. odds of **2.74** — an "equivalent Elo gap" of ~160 from a nominal 75.

I initially rejected (b) outright on the grounds that it drives the underdog's loss rate toward
zero and goes infeasible past a bound (75 Elo at a 0.80 draw rate). That rejection was too
quick — the mechanism is a real modelling choice, not self-evidently absurd — so it was tested
against the match record rather than asserted.

**What actually happened in title matches, 2008–2024, from the higher-rated player's side:**

| Sample | record | mean gap | observed odds | Davidson predicts | ratio |
|---|---|---|---|---|---|
| All ten matches | 23W – 12L | +48 | **1.92** (95% CI 0.95–3.85) | 1.32 | 1.45 |
| **Carlsen's five** | 11W – 2L | +65 | **5.50** | 1.45 | **3.79** |
| **The other five** | 12W – 10L | +31 | **1.20** (95% CI 0.52–2.78) | **1.20** | **1.00** |

**This is the finding that settles the question.** On the full sample the favourite's odds look
steeper than Davidson (1.92 vs 1.32), which is what would justify a number well above 70%.
**Strip Carlsen's five matches and the observed odds land exactly on Davidson's prediction —
1.20 against 1.20.** The entire apparent steepening is one player who was widely held to be
stronger than his rating gap and an exceptional match performer. Sindarov, a 20-year-old in his
first match of this format, is not that player.

(Data-entry correction made during this analysis: an earlier pass credited the higher-rated
player with 3 wins in 2010. Topalov, 2805, was the higher-rated player and **lost** that match
5½–6½, so the row is 2W–3L. Fixing it moves the all-matches odds from 2.18 to 1.92 and does not
change the conclusion.)

Title probability at the nominal +75 gap as a function of the assumed odds (draw rate 0.64,
P(Sindarov wins the tiebreak) 0.58):

| win:loss odds | equiv. multiple of nominal Elo | P(tiebreak) | P(Sindarov) |
|---|---|---|---|
| 1.20 | 0.42x | 17.8% | 61.9% ← non-Carlsen empirical |
| **1.54** | **1.00x** | **15.9%** | **69.5%** ← Davidson at the nominal gap |
| 1.92 | 1.51x | 13.9% | 77.2% ← all-matches empirical |
| 2.18 | 1.81x | 12.7% | 80.9% |
| 2.74 | 2.34x | ~10% | ~86.5% ← expected-score-preserving |

![P(Sindarov) against the win:loss odds](charts/odds-sensitivity.png)

**The draw rate is not load-bearing** (under Davidson, 66.8–71.4% across draw rates of
0.55–0.75). The odds ratio is. Draw-rate calibration: 2024 Gukesh–Ding 64.3% drawn,
2021 Carlsen–Nepomniachtchi 63.6%, 2023 Ding–Nepomniachtchi 57.1%.

**Inverting the model**: the market's 70% implies odds of ~1.56 — essentially Davidson at the
nominal gap. Caruana's 55% implies odds of ~1.10, an effective gap of only ~14 Elo.

### The Metaculus comment claiming 87%

@Theomachado posted a serious, well-specified dissent on 2026-09-11: a draw-aware Davidson
model fitted on 69.6k classical OTB games from ten years of TWIC, run by exact dynamic
programming plus a 10k Monte Carlo, returning **87% Sindarov**. Reported components: a fitted
β under which Sindarov's +75 is worth **0.574** expected per game rather than Elo's 0.606;
form persistence of only **k = 0.10** over six months (SE 0.057, 4,095 player-months), so
Gukesh's −0.086/game slump is worth about **−19 Elo, not −54**; and a check that title matches
do not distort Elo (over 84 classical games of 2013–2024 matches the model expected the
favourite to score 46.2 against an actual 47.0).

My first hypothesis was that 87% came from applying an all-levels draw rate (~35–40%) to an
elite match. **That is wrong**: holding expected score at 0.574, *higher* draw rates raise the
match probability (75.5% at d=0.30 rising to 85.8% at d=0.70), because fixing the expected
score while draws absorb mass mechanically steepens the win:loss odds. So the 87% is a
consequence of the expected-score-preserving step, which the match data above shows is
defensible — not an artefact of a bad draw rate.

Three reservations, and together they are why I do not go near 87%.

1. **His validation check is on score, not on odds.** "The model expected the favourite to
   score 46.2, actual 47.0" is reproduced by *both* families essentially by construction. It
   does not test the win:loss odds ratio, which is the quantity actually in dispute — and the
   non-Carlsen table above tests exactly that and comes out at Davidson.
2. **His own point 2 cuts against his conclusion.** If form barely persists (k = 0.10), then
   Gukesh's rating — which has absorbed 91 points of slump — *understates* his true strength,
   and Sindarov's 2778 — which absorbed a 2908 Candidates outlier — *overstates* his. Both
   push the effective gap below the nominal 75, not above it.
3. **Fitting β on all of TWIC and applying it to a title match** mixes rating levels with very
   different draw structures. That is not fatal, but it is not the same estimand.

I take his point 2 seriously in the *other* direction, though: it is the best argument for
shading the nominal gap down, and it is part of why I sit slightly under the market rather than
on it.

## Player strength — the numbers that drive everything

FIDE list, 1 September 2026: **Sindarov 2778, world #4** (all-time peak). **Gukesh 2703,
world #32.** Gap **75**.

| List | Gukesh | Sindarov | Gap |
|---|---|---|---|
| Sep 2024 | 2764 | 2677 | Gukesh +87 |
| **Oct 2024** | **2794** (Gukesh peak) | 2668 | +126 |
| Sep 2025 | 2767 | 2722 | +45 |
| Mar 2026 | 2748 | 2745 | +3 |
| **Sep 2026** | **2703** | **2778** | **Sindarov +75** |

A **162-point relative swing in 24 months**. Gukesh is 91 below his own peak and has fallen on
essentially every list since September 2025.

Faster time controls, September 2026: rapid **Sindarov 2732 / Gukesh 2686** (+46);
blitz **Sindarov 2725 / Gukesh 2659** (+66). Both gaps were ~zero a year ago. **There is no
safe harbour for Gukesh in the tiebreak.**

2026 classical form: **Gukesh 15/39 = 38.5%** (+5 −14 =20) — Tata Steel 10th of 14, Prague 9th
of 10, Norway Chess **last of 6**, Chennai **last of 8**, and no classical game since July.
**Sindarov 23½/36 = 65.3%** (+12 −1 =23) — Tata Steel 2nd (TPR 2833), **Candidates 1st with
10/14, unbeaten, TPR 2908**, the highest score in the modern double-round-robin format.

Head-to-head, all verifiable games: classical Sindarov 1 win and 2 draws (**the win is from
Sharjah 2022**, when both were very different players); rapid **Gukesh 1–0** (GCT Warsaw,
2026-05-06); blitz **Sindarov 2–0** (2026-05-08 and 05-09). Aggregate Sindarov 3–1 with 2 draws.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-12 | Metaculus aggregations skill (fixed upstream; see note) | see `forecast.md` header and `raw/metaculus-45216-2026-09-12.json` | resolution criteria and cohorts |
| 2026-09-11 | FIDE regulations PDF CM2-2026_06 | 14 games, no draw odds, no Armageddon, no postponement, Giri as first reserve | killed two myths that would have changed the number |
| 2026-09-11 | ratings.fide.com profiles 46616543 and 14205483 | full monthly rating charts, classical/rapid/blitz | the 75-point gap and the 162-point swing |
| 2026-09-11 | Polymarket gamma-api + CLOB | Sindarov 0.700 / Gukesh 0.295; $67.7k volume, $769k liquidity; **stable 0.615–0.70 since 13 May** | primary market anchor |
| 2026-09-11 | Kalshi `KXCHESSWORLDCHAMPION-CHESS26` | Sindarov $0.70 (258,818 contracts), Gukesh $0.32 (218,738) — **~480k contracts, much the deepest venue** | independent corroboration |
| 2026-09-11 | bet365 via OLBG; chessdom aggregation | Sindarov 4/11, Gukesh 2/1 → normalised 68.8 / 31.2; venue range 63–73% | third venue |
| 2026-09-11 | Chess.com, "Carlsen, Caruana give predictions" | **Caruana: "slight money on Sindarov, maybe 55-45"**; Carlsen: *"impossible not to say Sindarov"*; Carlsen on path-dependence: an early Gukesh lead makes him "a significant favourite" | the only explicit expert number, and it dissents |
| 2026-09-11 | Wikipedia WCC infoboxes 2006–2024 | the base-rate tables above | outside view |
| 2026-09-11 | ChessBase, Olympiad line-ups | **Gukesh on board 4** for India behind Erigaisi, Praggnanandhaa and Nihal Sarin; he played **board 1 in 2024 with 9/10 and a 3056 TPR**. Sindarov board 1 for the hosts | his own federation's assessment; also the key tripwire |
| 2026-09-11 | Manifold (9–14 traders — near-worthless) | P(tiebreak) 18–27%, conditional Sindarov ~59% | brackets the model's 16% |
| 2026-09-11 | Chess.com, Wikipedia | Dvorkovich suspended as FIDE president over EU sanctions; **Anand interim president**; match is in Switzerland; no title sponsor or playing hall announced | organiser turbulence, not match risk |

## Dead ends and ruled-out hypotheses

- **Model family (a)** — discarded for the reason above. Recorded because a spreadsheet will
  hand you 93% and it is an artefact.
- **"Champion retains on a drawn match"** — false under Art. 4.4.1. Would have added ~9 points
  to Gukesh had it been believed.
- **"Armageddon decides the tiebreak"** — false; repeated 3+2 pairs instead.
- **The third classical head-to-head game** — event, date and colours could not be identified;
  365chess, chessgames and chesstv are all blocked or broken. Sources split between "3 games"
  and "leads 1.5–0.5" (2 games). Does not move anything: the only decisive classical game is
  from 2022.
- **FIDE rapid/blitz world *rankings*** — ratings.fide.com's top lists are JS-rendered and
  2700chess is Cloudflare-blocked. The *ratings* themselves are verified from player profiles.
- **Betfair, Pinnacle, and any correct-score / method-of-victory / tiebreak market** — none
  found at any bookmaker. Only Manifold prices the tiebreak, with 9–14 traders.
- **Health, visa, scheduling risk** — searched and found nothing for either player. Chess media
  did report 2026 injuries for Firouzja and Aronian, so the absence is mildly informative.
  Both players declined the competing Total Chess World Championship (Budapest, 10–21 Nov).

## Open questions to chase next time

- **The Olympiad, Samarkand, 15–27 September 2026.** Both players compete; it is the best
  pre-match information that will exist, and it lands ~9 weeks before Game 1. Gukesh's
  performance rating on board 4 is the single highest-value observable.
- Whether a title sponsor and playing hall are announced, and whether FIDE moves the dates again.
- Opening-preparation signals: seconds hired, training-camp reporting.
- Whether Gukesh plays any classical chess at all between the Olympiad and 24 November.
