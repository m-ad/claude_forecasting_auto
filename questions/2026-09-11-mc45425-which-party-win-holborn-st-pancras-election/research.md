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
