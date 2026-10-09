# Research log — What will be the winning margin in Brazil's 2026 presidential election runoff?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: final TSE nationwide result, runoff 2026-10-25. |winner − runner-up| in pp
  of valid votes (blank and null excluded). Includes corrected official figures.
- Range 0–8, closed lower and open upper bound (values above 8 land in the overflow bin). Unit
  "Percentage points". Closes 2026-10-25 11:00 UTC. CP reveal 2026-10-08 17:00 UTC.
- Text retrieved via the browser API path on 2026-10-05; cached `raw/question-text-2026-10-05.json`.
- Edge cases: the margin is absolute, so the winner's identity does not matter; TSE totals are
  final on election night.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| Brazilian presidential runoffs, winner margin | 6 | 2002–2022 | 22.5, 21.7, 12.1, 3.3, 10.3, 1.8 | Wikipedia/TSE (2014, 2018, 2022 verified) | down-weighted (regime change) |
| Polarised-era runoffs (2014, 2018, 2022) | 3 | 2014–2022 | 1.8–10.3 | same | yes |
| R1→R2 margin change in close races | 2 | 2014, 2022 | trailing candidate gained 3.4–4.7pp | same | yes |

## Decomposition

Transfer model (Quaest 3 Oct splits, Flávio/Lula/other):
- Cury 2.89 × (.34/.23)
- Renan 2.24 × (.60/.11)
- Caiado 2.18 × (.43/.19)
- Zema 0.27 × (.7/.1)
- Others 0.6 × (.3/.3)

Result: Flávio +3.63, Lula +1.53. That gives 50.66 vs 46.69, normalised to **52.0 / 48.0 (F +4.1)**.

Polling error in R1: AtlasIntel Lula +2.9 against an actual F +1.87, a miss of ~4.8pp to the right.
Datafolha similar.

Model: signed margin ~ 3.3 + 3.1·t(6). P(F) 0.836; |M| percentiles: p5 0.37, p10 0.74,
p25 1.82, p50 3.58, p75 5.68, p90 7.89, p95 9.46. P(|M| > 8) 0.095.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-05 | Wikipedia 2026 election; CNBC; Rio Times | R1: F 47.03 (56.10M), L 45.16 (53.88M); valid 119.3M; turnout 78.9% | baseline |
| 2026-10-05 | Rio Times | others: Cury 2.89, Renan 2.24, Caiado 2.18, Zema 0.27 | transfer pool 7.8% |
| 2026-10-05 | Terra (Quaest 3 Oct) | transfer splits above | F +4.1 mechanical |
| 2026-10-05 | Agência Brasil; Midiamax; JGB | no endorsements; PSD frees branches; Renan says F "next president"; Zema anti-PT | mild F |
| 2026-10-05 | O Tempo / Exame (AtlasIntel 3 Oct) | R1 L 47.0 vs F 44.1 valid; R2 L 47.6 vs F 47.4 | polls underestimated F ~5pp |
| 2026-10-05 | Poder360 (AtlasIntel 23–28 Sep) | R2 F 47.7 vs L 47.6 | tie |
| 2026-10-05 | Poder360 PoderData | R2 F 45 vs L 44 | tie |
| 2026-10-05 | Polymarket Gamma API | F 82.65% / L 17.5%; $173M event | calibrates the signed mean |
| 2026-10-05 | Rio Times prediction markets | Kalshi F 82%; Polymarket rose from 63% → 85% after R1 | — |
| 2026-10-05 | Polymarket search "margin" | only the R1 margin market (closed); no R2 margin market | — |

## Dead ends and ruled-out hypotheses

- Guardian article (from the question background) is blocked for fetch. Used Rio Times and Wikipedia instead.
- No post-R1 runoff polls yet (2026-10-05).

## Open questions to chase next time

- First post-R1 Datafolha, Quaest and AtlasIntel runoff polls (expected ~Oct 8–12).
- Metaculus CP reveal (Oct 8).
- Debate schedule; any late endorsements (Caiado, Kassab/PSD, Cury); turnout campaigns.

## 2026-10-09 update (v2)

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-10-09 | Brasil de Fato (Datafolha 6–8 Oct) | F 49 / L 45 total, 52/48 valid; rejection L 46, F 43; 6% could change vote | up (F +4.3 valid) |
| 2026-10-09 | Wikipedia polling table | PoderData 5–7 Oct F 49 / L 44 (≈ F +5.4 valid); Datafolha 3 Oct pre-R1 L 47 / F 46 | up |
| 2026-10-09 | Gazeta do Povo 6 Oct | Caiado endorsed Flávio (6 Oct, with Tarcísio); Zema voted Flávio (5 Oct); Cury/Renan neutral; PSD neutral and frees its branches | mild up |
| 2026-10-09 | Polymarket Gamma | F 85.65 / L 13.5; $178M event | up slightly |
| 2026-10-09 | AtlasIntel / Quaest search | AtlasIntel post-R1 poll scheduled 9 Oct but not found; no Quaest post-R1 poll | open |
| 2026-10-09 | Kalshi API | 429 rate-limited; not retrieved | — |
| 2026-10-09 | Metaculus | browser path Cloudflare-blocked; API: open, 57 forecasters, aggregations hidden | no CP |

Model v2: signed margin ~ 3.9 + 3.0·t(6). P(F) 0.88; |M| p5 0.47, p10 0.92, p25 2.19, p50 4.05, p75 6.14, p90 8.3, p95 9.8; P(>8) 0.114; P(<2) 0.226.
A "PoderData F 53 / L 47 valid" headline surfaced in search; probably the same 5–7 Oct wave (≈52.7/47.3). Not independently verified.

Next: AtlasIntel (9 Oct+) and Quaest post-R1 waves; debate dates; Kalshi price.
