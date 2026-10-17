# Research log — What first round vote share will José Maria Neves win in the 2026 Cape Verdean presidential election?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: official first-round result (Comissão Nacional de Eleições, CNE / Constitutional
  Court) — percentage of **valid** votes (blank votes do not count toward the 50% threshold per CNE).
- Dates: first round **Sunday 15 November 2026**; runoff (if needed) 29 November. Campaign 29 Oct–13 Nov.
- Six admitted candidates (CNE Edital n.º 01/EleiçõesPresidenciais/2026, BO II Série n.º 187, 2026-09-30):
  José Maria Neves (incumbent, PAICV-backed), Joana Rosa (ex-Justice Minister, MpD-backed, first woman
  candidate), Antero Tavares (judge), Casimiro de Pina (jurist; 1.80% in 2021), Gilson Alves (doctor;
  0.76% in 2021), Loisito Tavares de Sousa (lecturer; admitted on appeal).
- Edge cases: diaspora vote included (counted later; small); rounding to two decimals by CNE.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Cape Verde incumbent presidents seeking re-election | 3 (1996 Mascarenhas Monteiro unopposed ~80%; 2006 Pires 51.0% vs Veiga; 2016 Fonseca 74% vs no major-party rival) | 1996–2016 | 3/3 re-elected, all in first round; share 51–80% | own recollection (flagged), Wikipedia election pages | yes |
| Contested two-major-party first rounds | 2001 (Pires 46.5), 2006 (51.0), 2011 (Fonseca 37.8 in 4-way), 2021 (Neves 51.79) | 2001–2021 | winner ≈ 46–52% when both blocs field strong candidates | Wikipedia; 2021 exact from Wikipedia | yes |
| Neves 2021 first round | 1 | 2021 | 51.79% vs Veiga 42.39%, minors 5.83% combined | Wikipedia 2021 Cape Verdean presidential election | yes (anchor) |
| May 2026 legislative vote | 1 | 2026 | PAICV ~48%, MpD 44.75% (≈52/48 two-party) | Africanews / Wikipedia / IPU | yes |

## Decomposition

Share = (1 − minors) × two-party share(Neves vs Rosa).
- Minors (4 candidates): 2021 minors 5.8% with 5 candidates; now 4, one of them a judge with no
  track record → 4–7%, centre 5%.
- Two-party share: legislative baseline 52%; + incumbency/presidential-personal vote (Neves approval
  72% in Afrobarometer 2022, highest-trust office after the army; 2024 round showed a decline in trust);
  + MpD demoralised after losing government, Rosa less known than Veiga (ex-PM, party founder);
  − possible "balance"/cohabitation instinct now that PAICV governs; − honeymoon fatigue unlikely by Nov.
  Centre 60%, SD ≈ 5.
- Neves ≈ 0.95 × 60 ≈ 57%.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-17 | "Cabo Verde eleições presidenciais 2026 ... candidatos" | CNE: six candidates final; 15 Nov / 29 Nov; campaign 29 Oct–13 Nov | mechanics |
| 2026-10-17 | Wikipedia 2026 Cape Verdean presidential election | no polls listed | — |
| 2026-10-17 | Wikipedia 2021 Cape Verdean presidential election | Neves 96,035 votes, 51.79%; Veiga 42.39%; turnout 47.99% | anchor |
| 2026-10-17 | Cape Verde 2026 parliamentary election | PAICV won 37/72 seats, ~48%; MpD 33 seats, 44.75%; Carvalho PM | +2 on two-party |
| 2026-10-17 | Afrobarometer Cabo Verde | 2022: 72% approve President, ~65% trust; 2024 R10: general decline in trust (no figure) | mild + |
| 2026-10-17 | Observador 2026-10-01 / 2026-10-02 | Rosa campaign framing; Neves seeks re-election "Cabo Verde 2050" | — |
| 2026-10-17 | Expresso das Ilhas 2026-09-20 | Neves and Rosa the two main names | — |
| 2026-10-17 | Polymarket cape-verde-presidential-election-winner-2026 | Neves 84% win, Rosa 10.6% ($28.5K total vol); "outright first-round win" 64% ($31, ignore) | consistent with median ~56–57 |

## Dead ends and ruled-out hypotheses

- No opinion poll found for 2026 (Afrosondagem, Inforpress, A Nação searches empty). Cape Verde rarely
  publishes presidential polls.
- boatos.org "resultado" page lists Brazilian candidates — junk, ignored.
- Polymarket lists Janine Lélis, Péricles Tavares, Milton Paiva — not on the final CNE list.

## Open questions to chase next time

- Any poll published during the campaign (29 Oct–13 Nov).
- Turnout signal (low turnout historically helps the better-organised machine).
- Whether MpD is fully mobilised behind Rosa (internal leadership fight after May defeat?).
