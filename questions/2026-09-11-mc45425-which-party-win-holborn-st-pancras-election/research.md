# Research log — Which party will win the Holborn and St Pancras by-election?

Working notes. Rough is fine; **completeness beats polish**.

## Question mechanics

- **Resolution source**: the declaration by Camden Council, the returning authority. Polling day
  is **Thursday 2026-10-08**; the result declares in the early hours of 2026-10-09.
- **Confirmed from the question itself**: resolves as *"the political party of the candidate
  officially declared elected"*. The option list is exactly **three — Other, Labour Party,
  Green Party** — so Liberal Democrat, Conservative, Reform UK and any independent all fold into
  **Other**. Fine print: a candidate switching party after nominations close resolves on the
  party shown in the official result; and if the by-election is cancelled by a general election,
  constituency abolition or another electoral event, the question is **annulled**. The question
  **closes 2026-10-07 23:00 UTC**, the eve of the poll.
- The parallel Polymarket market is on **candidates**, not parties; its two live prices map
  one-to-one onto Labour (Sagal Abdi-Wali) and Green (Zack Polanski).
- **Cause of the vacancy**: Sir Keir Starmer, already out as Prime Minister since 2026-06-22 and
  as Labour leader, announced on 2026-09-01 that he would stand down as MP and was appointed
  Steward of the Chiltern Hundreds the same day. The writ was moved 2026-09-07.
- **Nominations close 4pm, 2026-09-15** — four days after this forecast. The candidate list is
  therefore **not final**, which is a live source of uncertainty rather than a detail.
- **Edge case**: an "independent/other" winner is not absurd in this seat — an independent took
  second place here in 2024 — so the residual option is not a rounding artefact.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Westminster seats defended by Labour in this parliament | 3 | 2025-05 – 2026-06 | **1 hold of 3 (33%)** | Runcorn & Helsby (lost to Reform by 6 votes), Gorton & Denton (lost to Green), Makerfield (held) | yes, primary |
| Same, plus the Caerphilly Senedd defence | 4 | 2025-10 – 2026-06 | 1 of 4 (25%) | + Caerphilly (Labour to 11.0%, third) | yes, as the pessimistic bound |
| Governing party holds a mid-term by-election defence, long run | many | post-war | governments systematically underperform; gains from opposition are very rare | House of Commons Library | yes, as direction |
| 30pp majorities overturned in a by-election | several | 1994–2026 | happens regularly: Gorton & Denton 36.7pp, Mid Bedfordshire 24,664 votes, Wellingborough 36pp, Tiverton 25,155 | Wikipedia by-election list | yes |
| By-election turnout | 5 in this parliament | 2025–2026 | 38.0–58.8%, long-run average ~50% | HoC Library CBP-8060 | yes, for the turnout band |

The classes disagree sharply with the markets, and that gap is the whole question. A naive
reading of "Labour has held 1 of 3" would put this near 33%. Every market says 59–78%. The
reconciliation is that the reference class is drawn almost entirely from the pre-Burnham period.

## Decomposition

This is a **two-horse race with no third force**, which makes it unusually tractable.

Baseline: the May 2026 local elections **within this constituency's wards** gave
**Labour 38.8, Green 28.8, Con 10.0, Reform 8.5, LD 6.9** — a 10-point gap. The Greens need a
5-point swing from that baseline. From the 2024 general election baseline
(Labour 48.9, Feinstein 18.9, Green 10.4) they need much more.

Four forces act on that 10-point gap between May and 8 October:

1. **The Burnham recovery (pro-Labour, large).** Starmer resigned as leader 2026-06-22; Burnham
   was acclaimed unopposed 2026-07-17 and became PM 2026-07-20. On YouGov's own consistent
   series Labour has gone **18% (late April) → 23% (6–7 September)** while the Greens have gone
   **15% → 12%**. The broader September field has Labour 22–28 and Greens 8–14. Polanski's net
   approval has fallen from −13.4% in April to −24.3% in September; Burnham's favourability is 46%.
2. **The unowned Feinstein vote (pro-Green, large).** Andrew Feinstein took **18.9% and second
   place** here in 2024 as a pro-Gaza independent. He is **not standing**, and he has
   **endorsed Polanski**. No obvious alternative home exists for that vote unless a left
   independent files by 15 September. Electoral Calculus's 59/40 projection still parks ~12% in
   an "other" bucket that no longer has a candidate; reallocating it plausibly flips the seat.
3. **The by-election effect (pro-Green).** Low turnout — the plausible band here is 35–45%
   against 54.1% in 2024 — amplifies the motivated opposition. The Greens had canvassers on
   doorsteps before they even had a candidate. Polanski is the **party leader**, which buys
   national media and a national activist surge that no ordinary challenger gets.
4. **Local counter-evidence (pro-Labour, and it is recent and specific).** In the **Regent's
   Park ward by-election on 2026-07-09 — inside this constituency — Labour gained the seat from
   the Greens** (Lab 32%, Grn 27%, Ind 23%) on 21.9% turnout. And in the **Makerfield
   by-election on 2026-06-18 Labour's share rose 9.6pp on turnout up 6.3pp**, though Burnham was
   personally the candidate there.

What has to be true for a Green win: essentially all of Feinstein's 18.9% plus a further few
points of 2024 Labour voters, on a turnout skewed toward students and activists, against a
locally-rooted Labour candidate and a Prime Minister still inside his honeymoon.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-11 | Polymarket gamma-api `holborn-and-st-pancras-by-election-winner` | Abdi-Wali (Lab) 78.0%, Polanski (Grn) 21.5%; $39.7k volume, $319k liquidity, $14.1k in 24h | top of the market range |
| 2026-09-11 | Polymarket CLOB history, same market | opened 2026-09-02 at 0.235; **0.640 on 5 Sep; 0.780 on 11 Sep** — the jump tracks Labour's candidate selection on 9 Sep collapsing the other Labour names | the 78% is young and still repricing, not a settled consensus |
| 2026-09-11 | Betfair exchange, 2026-09-01 | Labour 1.38 (72.5%), Green 3.18 (32.1%) | real-money exchange, deeper UK political liquidity |
| 2026-09-11 | bet365 board 2026-09-07, normalised (overround 109.1%) | Labour ~67%, Green ~31%, all others ~2% | bookmaker consensus |
| 2026-09-11 | Oddschecker / OLBG / Gambling.com money-flow notes | **75% of bets in 24h (3 Sep) and 64% over the week to 10 Sep backed the Greens**; Green price shortened 3/1 → 2/1 | money one-way toward the Greens while polling moves the other way |
| 2026-09-11 | Electoral Calculus seat page | Lab 34.6, Grn 30.5; **P(Lab) 59%, P(Grn) 40%** | the most Green-friendly quantitative source; but it is a GE model, not a by-election model |
| 2026-09-11 | PollCheck seat page and GB polling average | seat model Lab 39.5 / Grn 27.9; national average Lab 26.1, Ref 23.0, Con 20.0, Grn 11.0, LD 10.7 | the Burnham recovery |
| 2026-09-11 | YouGov VI series, Apr → Sep 2026 | Lab 18 → 23; Grn 15 → 12; Ref 26 → 23 | the single most important trend |
| 2026-09-11 | Wikipedia 2026 Camden council election + seat-ward breakdown | borough Lab 32.8 / Grn 27.1; **seat wards Lab 38.8 / Grn 28.8** | the baseline |
| 2026-09-11 | New Statesman, 2026-09-07 and 2026-09 | adjusted locals give Labour only **+3pp**; Greens down 4pp nationally but only 2pp in London; internal Green dissent over Polanski (6 of 11 Camden Green councillors nominated his rival) | narrows the gap, but flags Polanski's local weakness |
| 2026-09-11 | New Statesman 2026-09-03; Jewish Chronicle | **Feinstein not standing, endorses Polanski** | the largest single pro-Green fact |
| 2026-09-11 | On London / Fitzrovia News, Regent's Park ward by-election 2026-07-09 | **Labour gain from Green** in this constituency, 21.9% turnout | the largest single pro-Labour fact |
| 2026-09-11 | Guardian 2026-09-06 | Reform's Zia Yusuf attacked Abdi-Wali's Somali birth; condemned across parties, including by Reform's own Nadine Dorries | anti-mobilises Reform in a 21.7%-Muslim, 45%-born-abroad seat |
| 2026-09-11 | Kalshi API `KXHOLBORNVOTE` | vote-share brackets listed but **no bids, asks, volume or open interest** | no usable Kalshi signal |
| 2026-09-11 | Manifold | Labour 76.4%, Green 16.7%; **35 unique bettors** | play-money and thin, discounted |
| 2026-09-12 | metaculus-aggregations skill, post 45425 (after the upstream fix landed) | options **Other / Labour Party / Green Party**; close 2026-10-07T23:00Z; annulled if a general election intervenes; status `upcoming`, n=6, **CP not revealed**. Comments are only the author and moderator agreeing the close date | collapses LD/Con/Reform/Independent into a single **Other** |

## Dead ends and ruled-out hypotheses

- **metaculus.com was unreachable for the first half of this session** (Cloudflare 403 on every
  path). **Fixed mid-session** by rebasing onto upstream commit ba7514b / PR #21. Operational
  notes: `--history` hangs on these questions, and a fetch takes 100–200s, so background it.
- **Lib Dem and Conservative paths ruled out quantitatively**, not by assertion: LD 5.8% in 2024
  (fourth) and 6.9% in the seat's wards in May; their Camden gains are concentrated in Hampstead
  & Highgate, not here; priced 50/1–979/1. Conservatives 7.2% in 2024, 10.0% in May, priced
  66/1–430/1.
- **Reform UK ruled out on inner-London evidence**: 6.1% here in 2024, 8.5% in May; Hackney
  mayoral 5.3% with zero council seats; Islington 6.14% with zero seats; Reform's London
  breakthrough was in Havering and Bexley. The seat is ~73% Remain and 639th of 650 on
  Electoral Calculus's cultural-left index. Reform is also **not confirmed to be standing** —
  Wikipedia's infobox says TBD.
- **No constituency poll exists.** Checked and confirmed absent; PollCheck says so explicitly.
  This is the highest-value piece of information that does not yet exist.
- **A stale aggregate** circulating as "Ref 28 / Lab 18 / Grn 15" is inconsistent with every
  individual September poll and was rejected as spring-2026 data.
- **Al Jazeera's "Greens approximately 20%"** (2026-09-04) contradicts all fourteen September
  polls; treated as stale.

## Open questions to chase next time

- **The nomination list, after 2026-09-15.** Does Your Party or the Camden People's Alliance
  stand? A left independent splits the anti-Labour vote and is worth several points to Labour.
  Do the Lib Dems and Conservatives field candidates at all?
- Any constituency poll — would dominate everything above.
- The CP, once revealed; the question is `upcoming` at n=6 with no Pro or gold cohort.
- Camden ward by-elections between 9 July and 8 October (PollCheck's tables are JS-rendered and
  could not be extracted; camden.gov.uk is itself Cloudflare-protected).
- Whether Green national polling stabilises or keeps sliding through late September.

---

## v2 research log — 2026-09-24 (Re-analysis)

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-24 | Metaculus 45425, pre-fetched `raw/metaculus-2026-09-24.json` | CP Lab 79.8 / Grn 19.2 / Oth 1.0 (n=97); Pros 85.0 / 14.0 / 1.0 (n=9, IQR 76–95); gold medalists 80.8 / 18.2 / 1.0 (n=29). CP revealed 09-17 | all cohorts 4–9pp above v1; no material disagreement between cohorts |
| 2026-09-24 | Metaculus comments | sai_39: PollCheck 41.7/37.8, P 70%; Galloway standing; Green conference clash. matru: seat polls missed by 8–12pp this parliament (Gorton, Makerfield), so ~65% is a fair poll-based starting point | supports staying under the market |
| 2026-09-24 | Polymarket gamma-api | Abdi-Wali 0.845 (bid 0.84 / ask 0.85, last 0.90); Polanski 0.12 (0.11/0.13); volume $60.1k, liquidity $242k | +6.5pp since 09-11 |
| 2026-09-24 | Wikipedia by-election page / ITV / Camden SOPN via search | 15 candidates; Galloway (Workers), Newman (Reform), Cameron (Con), Stillman (LD); CPA and James Giles endorse Polanski; no Your Party candidate | tripwire 1 partially fired, +3 |
| 2026-09-24 | Oddschecker 2026-09-21 | Labour 1/8 best (1/4 a week earlier); Green 7/1 best, 9/2 worst; Workers 125/1; 64% of bets the prior week on the Greens | bookmakers moved *against* the bet count, so the large stakes are on Labour (LR ~1.3) |
| 2026-09-24 | PollCheck by-election page | new by-election model Lab 41.7 / Grn 37.8 / Ref 7.8; P 70/30; still no constituency poll | the most Green-friendly anchor; keeps me below the market |
| 2026-09-24 | YouGov 13–14 Sep, 20–21 Sep | Grn 11 → 14; Lab 23 flat; PollCheck 7-poll avg Lab 26.7 (09-23) | small Green rebound, −1; tripwire (15%+ in two polls) not fired |
| 2026-09-24 | Lord Ashcroft focus groups, 2026-09-21 | 2024 Lab voters: Polanski interest "faded" (hypnotherapy, council tax, NATO); Abdi-Wali seen as vague on housing; most expect Labour | small pro-Labour |
| 2026-09-24 | Guardian via inkl, 2026-09-18 | Green executive refused Polanski's request to postpone the 2–4 Oct Brighton conference (~3,000 attendees) | small pro-Labour (diverts activists in the final week) |
| 2026-09-24 | Telegraph via Yahoo, 2026-09-23 | Galloway expected to take "hundreds, if not a few thousands" of votes; he got 0.4% in Glasgow | caps the Galloway effect at about +3 |
| 2026-09-24 | Middle East Eye | Abdi-Wali skipped the 22 Sep King's Cross hustings; Polanski attended | small pro-Green, netted into the campaign row |
| 2026-09-24 | Camden Council upcoming elections (search) | no ward by-election before 10-08 | tripwire not fired |
| 2026-09-24 | Search for constituency polls (Survation / Find Out Now / JL Partners / Ashcroft) | none published; Ashcroft ran focus groups only | the key missing datum persists |

**Dead ends (v2)**: the Betfair betting blog returned 403, so there is no fresh exchange price.
PollCheck's GB polls table is JS-rendered, so only the 7-poll average was extracted. No non-YouGov
September poll with Greens at 15% or above was found.

**Open for v3 (2026-10-01, T−7)**: any constituency poll; the Green national share in several
pollsters; whether Polymarket and the books hold after the Green conference; Galloway's campaign
traction.

## v4 research log — 2026-10-02 (Update)

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-10-02 | Polymarket gamma API | Abdi-Wali 0.86 (0.85/0.87), Polanski 0.14 (0.13/0.15); event volume $66.0k (+$4k since v3) | flat |
| 2026-10-02 | metaculus-aggregations, post 45425 (first attempt 403, retry 6 min later OK) | CP 82.4 (n=117), Pros 84.0 (n=11), gold 83.8 (n=34); DeRuina (30 Sep) argues the ward-level gap is ~3pt after adjusting for uncontested wards | cohorts +3; small pro-Green comment |
| 2026-10-02 | search "voting intention ... 30 September 2026" | PollCheck 7-poll avg Lab 26.7 / Ref 23.3 / LD 10.4 / Grn 9.7; More in Common Sept MRP Grn 8 | small pro-Labour |
| 2026-10-02 | Left Foot Forward (Oct) | Stats for Lefties model Lab 39 / Grn 32 / Con 10 / Ref 9 (locals + national polls; not a poll) | small pro-Labour |
| 2026-10-02 | The Critic (1 Oct) | Polanski Bengali video in standard Bangla, not Sylheti; conference story leaked as dysfunction; Galloway "8–25%" estimate (implausible) | small pro-Labour |
| 2026-10-02 | UnHerd, Bastani (Oct) | Labour campaign lacks energy; Abdi-Wali "cagey and lightweight"; Polanski not resident | small pro-Green |
| 2026-10-02 | Wikipedia by-election page | Williamson resigned as Workers deputy leader over Galloway's candidacy, urged Polanski support; no polls section | small pro-Green |
| 2026-10-02 | search Survation / Find Out Now / JL Partners + seat | no constituency poll found | none |
| 2026-10-02 | The New World, Kellner (7 Sep) | 9 left-v-left by-elections in 60 years, Labour lost 5, avg −24pp; Southall 2007 the honeymoon exception | outside-view dissent, noted |

**Open for v5 (T−1, 2026-10-06/07)**: any constituency poll; post-conference Green national
share; Polymarket/bookmaker moves in the final 48h; Galloway campaign news.
