# What will be the winning margin in Brazil’s 2026 presidential election runoff?

| | |
|---|---|
| **Source** | Metaculus #45735 — https://www.metaculus.com/questions/45735/what-will-be-the-winning-margin-in-brazils-2026-presidential-election-runoff |
| **Type** | numeric (percentage points of valid votes; range 0–8, closed lower / open upper bound) |
| **Opened / Closes / Resolves** | 2026-10-06 / 2026-10-25 / 2026-10-27 |
| **Status** | open |
| **Current forecast** | **Median 4.0, IQR [2.2, 6.1]** (v2, 2026-10-09) |
| **Community (as of 2026-10-09)** | fresh CP unavailable 2026-10-09 (Cloudflare block); API shows 57 forecasters, aggregations hidden from bot key |
| **Next review** | 2026-10-11 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v2 — Update — 2026-10-09

### Revision table

| Driver | Direction | Effect on median | Note |
|---|---|---|---|
| **Prior (v1, 2026-10-05)** | — | **3.6, IQR [1.8, 5.7]** | signed margin centre F +3.3, scale 3.1 |
| First post-R1 runoff polls: Datafolha (6–8 Oct) F 52 / L 48 valid; PoderData (5–7 Oct) F 49 / L 44 total ≈ F +5.4 valid [1][2] | up | +0.3 | Average ≈ F +4.8 of valid votes. Above my +3.3 centre, but below the 5pp tripwire. The pollsters swung about 5pp toward Flávio, matching their R1 miss. |
| Caiado (6 Oct) and Zema (5 Oct) endorse Flávio; Cury and Renan neutral; PSD frees state branches [3] | up | +0.1 | The pro-Lula endorsement tripwire did not fire, and the actual moves went the other way. Caiado's 2.18% already leaned 43/19 to Flávio, so the extra effect is small. |
| Polymarket, Flávio: 82.65% → 85.7% ($178M event) [4] | up | +0.1 | Consistent with a signed mean of about +3.6 at a scale of 3. My centre of +3.9 puts about 2pp more probability on a Flávio win than the market does. |
| Counterweight: post-R1 polls catch the winner's momentum, 16 days remain, and 2022 shows the trailing side closing 3–4pp; no AtlasIntel or Quaest post-R1 poll yet | down | −0.1 | Keeps the spread wide (scale 3.0, not 2.5) |
| **New (v2)** | | **4.0, IQR [2.2, 6.1]** | signed centre F +3.9, scale 3.0, t(6). P(Flávio wins) 0.88; P(\|M\| > 8) 0.11 |

### Tripwire check (from v1)

| Tripwire | Status | Evidence |
|---|---|---|
| First post-R1 polls (Datafolha / Quaest / AtlasIntel) average a Flávio lead of ≥ 5pp of valid votes by 2026-10-12 | **partial** | Datafolha F +4.3 and PoderData F +5.4 (valid votes) average ≈ +4.8. AtlasIntel (due 9 Oct) and Quaest are not yet published [1][2][5]. Half of the +1.0 move applied. |
| Same polls average within ±1pp by 2026-10-12 | not fired | — |
| Caiado / PSD leadership or Cury endorses Lula before 2026-10-18 | not fired (reverse) | Caiado endorsed **Flávio** on 6 Oct. Cury is neutral and leaving politics. The PSD frees its state branches [3]. |
| Final AtlasIntel runoff poll shows \|margin\| ≥ 6, by 2026-10-24 | pending | — |
| Polymarket odds tighten to 60/40 or closer before 2026-10-20 | not fired | Widened to 85.7 / 13.5 [4] |

### What resolves YES

Unchanged from v1. The question is the absolute TSE margin in percentage points of valid votes in the 2026-10-25 runoff, on a 0–8 scale with an open upper bound. The API status was re-checked on 2026-10-09: open, scheduled close 2026-10-25 11:00 UTC, scaling unchanged [6].

### Outside view

Unchanged from v1.

### Inside view (changes only)

- **Polls now agree with the transfer model.** v1's mechanical transfer estimate was F +4.1, and the
  first two post-R1 polls average F +4.8. After R1 the pollsters corrected toward the right, by
  about 5pp in Datafolha's case (L +1 total on 3 Oct, F +4 total on 6–8 Oct). The open question is
  whether they have now overcorrected. In 2022 the final runoff polls overstated Lula by about 2pp
  (Datafolha's final poll had Lula at 52 valid; the result was 50.9). That error ran in the same
  direction as the 2026 R1 miss, toward the right. I give no further credit for hidden right-wing
  votes beyond what the polls now show. Instead I centre at +3.9, between the polls (+4.8), the
  market-implied value (+3.6) and the prior (+3.3).
- **The structure favours a small margin, not a blowout.** Rejection is high on both sides (46%
  for Lula, 43% for Flávio; Datafolha [1]), and only about 6% of voters say they could change
  their vote. That limits how far the margin can widen past 8. P(>8) is 11% (v1: 10%), which
  reflects the shift in centre, not a heavier tail.
- **Lula's route back:** debates and Northeast turnout. With 16 days left the scale stays at 3.0.
  A comeback to a coin-flip (|M| < 2) still has about 23% probability.

### Evidence (new since v1)

- Datafolha, 6–8 Oct, n=2,520, ±2: Flávio 49 / Lula 45 total, **52 / 48 valid**. Blank, null or none 5%; undecided 1%. Rejection: Lula 46, Flávio 43 [1].
- PoderData, 5–7 Oct, n=3,000, ±1.8: Flávio 49 / Lula 44 total, **≈ 52.7 / 47.3 valid**. Source is the Wikipedia polling table; I could not open the original Poder360 article [2].
- An AtlasIntel post-R1 poll (n≈5,000, online, ±1) was scheduled for 9 Oct. It was not yet published when I searched [5]. No Quaest, Paraná Pesquisas or Real Time post-R1 poll was found.
- Endorsements: Zema (5 Oct) and Caiado (6 Oct, with Tarcísio present) back Flávio. Cury and Renan stay neutral, though Renan says Flávio "already won". The PSD is neutral nationally [3].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | no cached value; last snapshot 2026-10-05 was pre-reveal (hidden) | 2026-10-05 | fresh CP unavailable 2026-10-09 (Cloudflare block). The API on 2026-10-09 shows 57 forecasters and 223 forecasts, with aggregations hidden from the bot key [6]. |
| Metaculus Pro | unavailable | — | same |
| Metaculus gold medalists | unavailable | — | same |
| Polymarket, winner | Flávio 85.65% / Lula 13.5% | 2026-10-09 | $178M event volume; Flávio market ~$18.5M, Lula market ~$21.0M [4] |
| Kalshi, winner | not retrieved (API rate-limited) | 2026-10-09 | v1: 82% Flávio (2026-10-05) |
| Runoff margin market | none found (Polymarket search) | 2026-10-09 | — |

### Scenarios

| # | Scenario | Weight (v1 → v2) | Implies (abs. margin) |
|---|---|---|---|
| 1 | Flávio comfortable: polls hold or widen | 0.21 → 0.27 | ≥ 6 |
| 2 | Flávio narrow: some reversion toward the 2022 pattern | 0.45 → 0.44 | 2–6 |
| 3 | Coin-flip finish | 0.27 → 0.23 | 0–2 |
| 4 | Lula clear comeback | 0.07 → 0.06 | 2–6 |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Centre +3.9 (blend) | Trust the post-R1 polls fully (+4.8) | median ≈ 4.9, IQR [2.9, 7.0] |
| Centre +3.9 | Market-implied (+3.6) | median ≈ 3.8 |
| Scale 3.0 | 2.3 (frozen electorate, high rejection) | median ≈ 3.9, IQR [2.4, 5.6] |

### What would change my mind (tripwires)

- [ ] AtlasIntel and Quaest post-R1 runoff polls (by 2026-10-13) both show Flávio ≥ +6 valid → up 0.8 pp
- [ ] Those polls show Flávio ≤ +2 valid (or a Lula lead) → down 1.0 pp
- [ ] Any major pollster shows a Lula gain of ≥ 3pp in margin between consecutive post-R1 waves, by 2026-10-20 → down 0.8 pp
- [ ] Final AtlasIntel / Datafolha runoff polls (by 2026-10-24) show \|margin\| ≥ 7 valid → up 1.2 pp
- [ ] Polymarket winner odds drop to 70/30 or closer before 2026-10-22 → down 1.0 pp; ≥ 93/7 → up 0.7 pp

### Sources

1. Brasil de Fato, "Datafolha, segundo turno: Flávio Bolsonaro 49%, Lula 45%", 2026-10-08 — https://www.brasildefato.com.br/2026/10/08/datafolha-segundo-turno-flavio-bolsonaro-49-lula-45/ (accessed 2026-10-09)
2. Wikipedia, "Opinion polling for the 2026 Brazilian presidential election" (second-round table: PoderData 5–7 Oct; Datafolha 6–7 Oct) — https://en.wikipedia.org/wiki/Opinion_polling_for_the_2026_Brazilian_presidential_election (accessed 2026-10-09)
3. Gazeta do Povo, "Candidatos derrotados no 1º turno começam a definir apoio a Flávio e Lula", 2026-10-06 — https://www.gazetadopovo.com.br/eleicoes/2026/candidatos-derrotados-no-1o-turno-comecam-a-definir-apoio-a-flavio-e-lula/ (accessed 2026-10-09)
4. Polymarket Gamma API, event `brazil-presidential-election` — https://polymarket.com/event/brazil-presidential-election (accessed 2026-10-09; cached `raw/polymarket-winner-2026-10-09.json`)
5. Brasil de Fato, "Datafolha, Quaest, AtlasIntel; quando saem as pesquisas de 2º turno", 2026-10-06 — https://www.brasildefato.com.br/2026/10/06/datafolha-quaest-atlasintel-quando-saem-as-pesquisas-de-2o-turno-entre-lula-e-flavio/ (accessed 2026-10-09)
6. Metaculus API post 45735 (bot key; metadata only) — cached `raw/metaculus-api-2026-10-09.json` (retrieved 2026-10-09 by the parent session)
7. CNN Brasil, Datafolha runoff page (3 Oct wave: Lula 47 / Flávio 46 total) — https://www.cnnbrasil.com.br/eleicoes/datafolha-2-turno/ (accessed 2026-10-09)
8. Metaculus question #45735, text via /api-proxy/posts — https://www.metaculus.com/questions/45735/ (accessed 2026-10-05; cached `raw/question-text-2026-10-05.json`) — carried forward from v1 [1], still relied on for the resolution digest
9. Wikipedia, 2014 / 2018 / 2022 Brazilian general election pages (TSE figures) — https://en.wikipedia.org/wiki/2014_Brazilian_general_election , https://en.wikipedia.org/wiki/2018_Brazilian_general_election , https://en.wikipedia.org/wiki/2022_Brazilian_general_election (accessed 2026-10-05) — carried forward from v1 [2], still relied on for the outside view and the 2022 comparison
10. Terra, "Lula x Flávio no 2º turno: para onde vão os votos de Cury, Renan e Caiado?" (Quaest 3 Oct) — https://www.terra.com.br/noticias/brasil/lula-x-flavio-no-2-turno-para-onde-vao-os-votos-de-cury-renan-e-caiado,b7bbee5dbd3518dbdbf298eb4d751a5cuzttmjkm.html (accessed 2026-10-05) — carried forward from v1 [4], still relied on for the transfer model
11. Rio Times, "Flávio and Lula head to Brazil runoff, 99.9% counted" — https://www.riotimesonline.com/brazil-election-first-round-results-lula-flavio-2026/ (accessed 2026-10-05) — carried forward from v1 [7], still relied on for the first-round baseline
12. Rio Times, "What prediction markets say about Brazil's runoff", 2026-10-05 — https://www.riotimesonline.com/brazil-runoff-prediction-markets-polymarket-kalshi-odds/ (accessed 2026-10-05) — carried forward from v1 [12], the Kalshi 82% figure cited under Other forecasters

**Date**: 2026-10-09
**Forecast**: Median 4.0, IQR [2.2, 6.1]
**Thesis**: The first post-R1 runoff polls (Datafolha F 52/48 valid; PoderData ≈ F +5.4) and the Caiado and Zema endorsements of Flávio confirm v1's transfer model (F +4.1). Polymarket has firmed to 86% Flávio. I centre the signed margin at F +3.9, between the polls and the market-implied value, with a wide 3.0pp spread, since AtlasIntel and Quaest have not yet reported and 16 days remain for a 2022-style comeback.

---

## v1 — Initial forecast — 2026-10-05

### What resolves YES

Resolves to the **absolute** gap, in percentage points of **valid votes** (blank and null
excluded), between first and second place in the presidential runoff of **2026-10-25**, as
published by the Tribunal Superior Eleitoral (TSE, Brazil's electoral court): winner's
valid-vote share minus runner-up's share. Example from the question: 52.4 vs 47.6 gives 4.8. The final
nationwide TSE figure is used, including corrections [1]. Because the gap is the same whichever
candidate wins, a narrow Lula win and a narrow Flávio win both resolve near 0. The question range
is 0–8 with an **open upper bound**: anything above 8 lands in the overflow bin. The TSE count is
electronic and essentially final on election night, so revision risk is negligible.

### Outside view

**Brazilian runoffs since 2002** (winner's margin, valid votes, TSE): 2002 22.5, 2006 21.7,
2010 12.1, 2014 3.3, 2018 10.3, 2022 1.8 [2]. Median 11.2. But the class has a clear
regime break: the three polarised Bolsonaro/PT-era contests show **1.8–10.3**, and the two
closest (2014, 2022) both followed close first rounds.

**First-round-to-runoff dynamics:** in close first rounds the runoff margin stayed small:
2014 (R1 gap 8.0) → 3.3; 2022 (R1 gap 5.2) → 1.8, with the trailing candidate gaining. In 2026
the R1 gap is **1.87** (Flávio 47.03%, Lula 45.16%) [3]. Only **7.8%** of valid votes went to
eliminated candidates, so the transfer pool is small, which caps how far the margin can swing.

Outside-view prior for |margin|: median ≈ 3, with most mass between 1 and 6.

### Inside view

**1. Mechanical vote transfer.** Quaest (3 Oct) measured runoff preferences of eliminated
candidates' voters: Cury (2.89%) 34 Flávio / 23 Lula / 41 blank-null-abstain; Renan Santos (2.24%)
60 / 11 / 27; Caiado (2.18%) 43 / 19 / 36; Zema (0.27%) is openly anti-PT [4][5]. Applying these
to the first-round valid votes:

- Flávio +3.6pp, Lula +1.5pp, giving 50.7 vs 46.7 before renormalising.
- That is **52.0 vs 48.0, margin ≈ 4.1 for Flávio**.

**2. Polling error.** AtlasIntel's final first-round poll had Lula +2.9 on valid votes (47.0 vs
44.1); Datafolha had Lula about +3. The result was **Flávio +1.9**, a miss of about 5pp toward the
right [6][7]. The same polls' runoff simulations showed a tie (Atlas 47.6 vs 47.4, Lula +0.2)
[6][8]. If even half that error persists, the runoff polls imply Flávio +2 to +3.

**3. Endorsements.** None of the eliminated candidates endorsed anyone. Cury and Renan are
explicitly neutral; Caiado's PSD "freed" its state branches. Renan nonetheless called Flávio the
"next president". Zema leans against the PT [5][9]. This is mildly pro-Flávio by default, since
those electorates lean right.

**4. Lula's levers:** incumbency, the state machine, Northeast turnout mobilisation, debates, and
three weeks to campaign. In 2022 Bolsonaro, the trailing candidate, cut a 5.2pp R1 deficit to
1.8. Turnout swings on a small transfer pool can move the margin by 1–3pp either way.

**Signed-margin model** (Flávio − Lula): centre **+3.3**, scale 3.1, Student-t with 6 degrees of
freedom. That gives P(Flávio wins) ≈ 84%, close to the markets' 82–83%. Its absolute value has
median 3.6, quartiles 1.8 / 5.7, 10th–90th percentiles 0.7–7.9, and P(>8) ≈ 10%.

### Evidence

- First-round final (TSE via press): Flávio 56,104,503 (47.03%), Lula 53,879,538 (45.16%);
  119.3M valid votes; turnout 78.9% [3][10].
- Others: Cury 2.89, Renan Santos 2.24, Caiado 2.18, Zema 0.27, six others < 0.2 each [7].
- Pre-R1 runoff polls: AtlasIntel 23–28 Sep: Flávio 47.7 vs Lula 47.6 [8]. AtlasIntel 3 Oct:
  Lula 47.6 vs Flávio 47.4 [6]. Datafolha 17 Sep: Lula 46 vs 44 [1]. PoderData: Flávio 45 vs
  44 [11]. All within ±2.
- Congressional results are mixed: pro-Lula candidates won more Chamber seats, pro-Bolsonaro more
  Senate seats [10]. They are not informative about the presidential margin.
- No post-R1 runoff poll published as of 2026-10-05. **That is the single most important missing
  input** and is the reason for a 4-day review cadence.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | hidden | 2026-10-05 | CP reveal 2026-10-08 17:00 UTC; 6 pre-open forecasters |
| Metaculus Pro | hidden | 2026-10-05 | |
| Metaculus gold medalists | hidden | 2026-10-05 | |
| Polymarket, winner | Flávio 82.65% / Lula 17.5% | 2026-10-05 | $173M event volume; ~$17M on each of these two markets |
| Kalshi, winner | Flávio 82% / Lula 18% | 2026-10-05 | via Rio Times [12] |
| Polymarket / Kalshi runoff margin | no market found | 2026-10-05 | first-round margin market closed |

A winner probability of about 83% is consistent with a signed mean of about +3.3 and a scale of
about 3. My distribution is calibrated to that.

### Scenarios

| # | Scenario | Weight | Implies (abs. margin) |
|---|---|---|---|
| 1 | Flávio comfortable: transfers plus persistent shy-right polling error | 0.21 | ≥ 6 |
| 2 | Flávio narrow: transfers roughly as Quaest measured, Lula mobilisation partly offsets | 0.45 | 2–6 |
| 3 | Coin-flip finish (2022-style): Lula turnout surge or a debate shift | 0.27 | 0–2 |
| 4 | Lula clear comeback | 0.07 | 2–6 (rarely more) |

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Quaest transfer splits hold | Transfers split evenly (abstention-heavy, both sides) | median ≈ 2.4 |
| R1 polling error toward the right is not corrected by turnout | Lula's machine closes the gap as in 2022 | median ≈ 2.0 |
| Spread (scale) 3.1pp | Scale 2.0pp (polarised, frozen electorate) | median 3.4, IQR [2.2, 4.6] |

### What would change my mind (tripwires)

- [ ] First post-R1 runoff polls (Datafolha / Quaest / AtlasIntel), by 2026-10-12, average a Flávio lead of ≥ 5pp of valid votes → up 1.0 pp (median)
- [ ] The same polls average within ±1pp, by 2026-10-12 → down 0.8 pp
- [ ] Caiado or the PSD leadership, or Cury, endorses Lula, before 2026-10-18 → down 0.5 pp
- [ ] Final AtlasIntel runoff poll, by 2026-10-24, shows |margin| ≥ 6 → up 1.2 pp
- [ ] Polymarket winner odds move to 60/40 or closer, before 2026-10-20 → down 1.0 pp

### Sources

1. Metaculus question #45735, text via /api-proxy/posts — https://www.metaculus.com/questions/45735/ (accessed 2026-10-05; cached `raw/question-text-2026-10-05.json`)
2. Wikipedia, 2014 / 2018 / 2022 Brazilian general election pages (TSE figures): 2014 51.64–48.36, 2018 ≈55.1–44.9, 2022 50.90–49.10; R1 2014 41.59/33.55, 2022 48.43/43.20 — https://en.wikipedia.org/wiki/2014_Brazilian_general_election , https://en.wikipedia.org/wiki/2018_Brazilian_general_election , https://en.wikipedia.org/wiki/2022_Brazilian_general_election (accessed 2026-10-05). 2002/2006/2010 margins (61.3–38.7, 60.8–39.2, 56.1–43.9) are recalled TSE totals, **not re-verified this session**; they only affect the long-run class, which I down-weight.
3. 2026 Brazilian general election — https://en.wikipedia.org/wiki/2026_Brazilian_general_election (accessed 2026-10-05)
4. Terra, "Lula x Flávio no 2º turno: para onde vão os votos de Cury, Renan e Caiado?" (Quaest 3 Oct) — https://www.terra.com.br/noticias/brasil/lula-x-flavio-no-2-turno-para-onde-vao-os-votos-de-cury-renan-e-caiado,b7bbee5dbd3518dbdbf298eb4d751a5cuzttmjkm.html (accessed 2026-10-05)
5. Agência Brasil, "Renan descarta apoio no 2º turno; PSD de Caiado libera bases estaduais", Oct 2026 — https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/renan-descarta-apoio-no-2o-turno-psd-de-caiado-libera-bases-estaduais (accessed 2026-10-05)
6. O Tempo, "AtlasIntel: Lula tem 47% e Flávio Bolsonaro, 44,1% das intenções de votos válidos", 2026-10-03 — https://www.otempo.com.br/eleicoes/2026/pesquisas/2026/10/3/lula-tem-47-e-flavio-44-1-das-intencoes-de-votos-validos-indica-atlasintel (accessed 2026-10-05)
7. Rio Times, "Flávio and Lula head to Brazil runoff, 99.9% counted" — https://www.riotimesonline.com/brazil-election-first-round-results-lula-flavio-2026/ (accessed 2026-10-05)
8. Poder360, "Flávio tem 47,7% e Lula, 47,6% no 2º turno, diz AtlasIntel" — https://www.poder360.com.br/poder-eleicoes-2026/flavio-tem-477-e-lula-476-no-2o-turno-diz-atlasintel/ (accessed 2026-10-05)
9. Midiamax, "Cury, Caiado e Renan Santos não declaram apoio para o 2° turno; Zema vai contra o PT" — https://midiamax.com.br/brasil/2026/cury-caiado-renan-santos-nao-declaram-apoio-2-turno-zema-vai-contra-pt/ (accessed 2026-10-05)
10. CNBC, "Brazil election headed to runoff…", 2026-10-04 — https://www.cnbc.com/amp/2026/10/04/brazil-presidential-election-lula-bolsonaro.html (accessed 2026-10-05)
11. Poder360, "Flávio tem 45% e Lula registra 44% no 2º turno, diz PoderData/Aya" — https://www.poder360.com.br/poderdata/flavio-tem-45-e-lula-registra-44-no-2o-turno-diz-poderdata-aya/ (accessed 2026-10-05)
12. Rio Times, "What prediction markets say about Brazil's runoff", 2026-10-05 — https://www.riotimesonline.com/brazil-runoff-prediction-markets-polymarket-kalshi-odds/ (accessed 2026-10-05)
13. Polymarket Gamma API, event `brazil-presidential-election` — https://polymarket.com/event/brazil-presidential-election (accessed 2026-10-05; cached `raw/polymarket-winner-2026-10-05.json`)
14. Exame, "Pesquisa AtlasIntel: vantagem de Lula no 2º turno contra Flávio Bolsonaro cai para 4,5 pontos" (trend context) — https://exame.com/brasil/pesquisa-atlasintel-vantagem-de-lula-no-2o-turno-contra-flavio-bolsonaro-cai-para-45-pontos/ (accessed 2026-10-05)
15. Yahoo/Reuters, "Flavio Bolsonaro draws even with Lula in Brazil election matchup, Datafolha shows" — https://www.yahoo.com/news/articles/flavio-bolsonaro-draws-even-lula-161733328.html (accessed 2026-10-05)

**Date**: 2026-10-05
**Forecast**: Median 3.6, IQR [1.8, 5.7]
**Thesis**: Flávio leads by 1.87pp after round 1, with only 7.8% of valid votes in play. Quaest's transfer splits (Renan 60/11, Caiado 43/19, Cury 34/23 for Flávio/Lula) mechanically imply a Flávio margin of ≈4. Pre-runoff polls showed a tie but underestimated Flávio by ~5pp in round 1, and markets (~83% Flávio) agree with a signed mean of ≈+3.3. Folding in Lula's mobilisation and the 2022 comeback precedent gives an absolute margin with median ≈3.6 and IQR 1.8–5.7.
