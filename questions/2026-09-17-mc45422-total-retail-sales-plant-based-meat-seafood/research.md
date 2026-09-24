# Research log — What will be the total retail sales of plant-based meat and seafood in 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- **Resolution source**: the Good Food Institute's (GFI) *2027 State of the Industry* report,
  plant-based volume. The number GFI prints is **licensed from Euromonitor International**,
  category "meat and seafood substitutes" (chilled, frozen, shelf-stable), **Retail Value RSP,
  current prices (i.e. including inflation)**. It is a **global** figure, not a US one:
  the question background quotes "$2.2 billion in 2015 → $6.6 billion in 2025", which is the
  global series. GFI's *US* series is a separate SPINS-commissioned dataset that printed
  $1.0 bn for 2025 and is not what resolves this.
- **Excluded from the category**: tofu, tempeh, seitan and inherently plant-based foods
  (chickpeas, kale). Included: plant-based-positioned meat and seafood analogues.
- **Release schedule**: GFI's plant-based SOTI report has landed in April in recent years
  (2024 report Apr 2024; 2025 report published 2025-04-29; 2026 report April 2026). Expect the
  2027 report ≈ April 2027. The fine print annuls the question if no report appears before 2028
  — low risk, but GFI ran a 2024 deficit ($28.1 M revenue vs $35.4 M expenses per ProPublica
  filings) so a scope cut is not unthinkable.
- **Naming change**: from 2026 GFI titles reports by *publication* year, not data year. So the
  "2027 State of the Industry report" covers calendar 2026. The fine print's "first official
  estimate for the year 2026 made during 2027" matches.
- **Edge cases and ambiguities**:
  1. **Restatement.** The level is *not* a stable series. GFI's own report says "Data may
     differ from previous reports." The 2024 report printed **$6.4 bn for 2023**; the 2025
     report printed **$6.1 bn for 2024 and called it +4%** — i.e. the 2023 base was silently
     restated down ~8%. What resolves is the level printed in 2027, not 6.6 × (1 + true growth).
  2. **Exchange-rate basis unstated.** GFI's figure notes say "current prices" but never say
     whether Euromonitor's USD aggregate is at fixed or year-on-year exchange rates. ~55% of
     the market is Europe, so this is worth ±1–2 pp of reported growth.
  3. **Scope change.** If GFI switched provider, or folded tofu/tempeh in, the level could move
     far outside the question's 5–9 bn band. Small (~4%) but it is the only route to the tails.
- **Question status on 2026-09-17**: `upcoming`. CP reveal time 2026-09-20T20:55Z, 3 forecasters,
  **all three aggregation cohorts empty**. This forecast is genuinely unanchored.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| **A. Reported YoY growth of this exact series** | 4 | 2022–2025 | +8%, +5%, +4%, +8% → mean **+6.3%**, sd 2 pp | GFI SOTI reports 2023–2026 | Kept — but it is growth *after* restatement, not what resolves |
| **B. Report-headline → next report-headline ratio** | 4 | 2021→2025 | +8.9%, +4.9%, −4.7%, +8.2% → mean **+4.3%**, median +6.6%, sd **6.4 pp** | headlines 5.6 / 6.1 / 6.4 / 6.1 / 6.6 | **Kept as primary** — this is literally the quantity asked |
| C. Post-boom CAGR of the series | — | 2021–2025 | $5.6 bn → $6.6 bn = **+4.2%/yr** | as above | Kept as a cross-check |
| D. Full-decade CAGR | — | 2015–2025 | $2.2 bn → $6.6 bn = **+11.6%/yr** | GFI 2026 report | Rejected — dominated by the 2017–2021 boom that ended |
| E. Commercial market-research CAGRs (IMARC, Mordor, MarketsandMarkets, market.us) | many | 2026–2035 | +9% to +19%/yr, levels $1.7 bn to $21 bn | vendor sites | **Rejected** — mutually inconsistent by an order of magnitude, different scopes, promotional. Not evidence |

The gap between A (+6.3%) and B (+4.3%) is the **average restatement drag, ≈ −2 pp/yr**.

## Decomposition

Euromonitor weights implied by the 2026 report: Europe **$3.6 bn (54.5%)**, US **≈$1.55 bn
(23.5%)** (report: Europe + US = 78% of dollar sales; Europe + North America > 80%), rest of
world **≈$1.45 bn (22%)**.

Bottom-up 2026, local currency nominal:

| Block | Weight | 2026 central | Why |
|---|---|---|---|
| Europe | 54.5% | **+3%** | 2025 Circana six-market panel ≈ flat for meat alternatives (FR +13.5%, DE +0.2%, IT +2.0%, ES −6.3%, UK −7.3%, NL −10.5% → value-weighted **−0.7%**); price gap narrowing; discounters (excluded from Circana) gaining share |
| US | 23.5% | **−7%** | SPINS 2025 −10% dollars / −11% units, distribution −8%; Beyond Meat FY2025 revenue −15.6%, Q2 2026 −8.2%; Euromonitor's US series historically declines more gently than SPINS |
| Rest of world | 22.0% | **+8%** | APAC/LatAm/MEA growing off a low base, with local food inflation |
| FX translation | — | **+1.2 pp** | ECB reference rates: EUR/USD annual average 1.0824 (2024) → 1.1300 (2025, **+4.40%**) → 1.1620 (2026 YTD, **+2.84%**); GBP/USD +2.06%; JPY −5.6% |

→ bottom-up ≈ **+2.6%**.

**The bottom-up fails to reproduce the 2025 print.** Running the same construction on 2025
(Europe ≈ +2%, US −6 to −10%, RoW +10%, FX +2.3 pp) gives ≈ +4.2% against GFI's reported
**+8%**. A persistent ≈ +2.5 pp wedge is carried forward, on the reading that Euromonitor's
coverage (discounters, more countries, more channels, trade-survey top-down estimates) is
genuinely wider than any transaction panel I can see. Central reported growth **≈ +4.6%**;
the failure to reconcile is priced as extra variance, not as a reason to pick a side.

Monte Carlo (`scripts` not committed; see forecast.md § Scenarios) with the wedge, the FX
uncertainty, a 20% chance of a ~−8% downward level break, 10% of a ~+6% upward re-base and 4%
of a scope change gives **median $6.86 bn, IQR [$6.59 bn, $7.11 bn]**, total multiplicative
sd 6.6 pp — matched deliberately to reference class B's 6.4 pp.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-17 | `metaculus_aggregations.py 45422` (needed `METACULUS_FORCE_TLS12=1`) | status `upcoming`, CP reveal 2026-09-20, **all three cohorts empty**, n=3, range 5–9 bn open both ends, type numeric | No community anchor exists; forecast is independent |
| 2026-09-17 | GFI 2026 SOTI plant-based report (72-pp PDF, downloaded and text-extracted) | 2025 global PB meat & seafood **$6.6 bn, +8% nominal, +4% real, volume +3%**, "primarily driven by growth in Europe"; Europe + US = 78% of dollars | Sets the base and the growth decomposition |
| 2026-09-17 | Same PDF, Data collection notes p.28 | Euromonitor licensed; "Data may differ from previous reports"; SPINS methodology changed, "we do not recommend comparing data released in prior years" | **Key finding** — restatement is explicit, not speculative |
| 2026-09-17 | gfi.org/resource/analyzing-plant-based-meat-and-seafood-sales | Europe $3.6 bn (~55%), US SPINS $1.0 bn 2025 (−10%), US foodservice $291 M (−7%), 2017 US $682 M | Gives the regional weights |
| 2026-09-17 | Green Queen, 2026 GFI report write-up | Global PB food $28.9 bn (+3%); Europe $10.1 bn, APAC $9.2 bn, NA $6.9 bn (all PB food, not meat) | Confirms the headline |
| 2026-09-17 | AgFunderNews (2025 report, 2024 data) | Global PB meat **$6.1 bn, +4%** in 2024; US −7% to $1.2 bn in 2024 | Reference class A/B |
| 2026-09-17 | Green Queen (2025 report, pub. 2025-04-29) | 2024: PB food $28.6 bn (+5%), PB meat $6.1 bn (+4%) | Confirms 2024 = $6.1 bn |
| 2026-09-17 | Search: GFI 2024 report / 2023 data | 2023 global PB meat printed at **$6.4 bn**; PB food $29 bn | **The restatement smoking gun**: $6.4 bn (2023) → $6.1 bn (2024) reported as *+4%* |
| 2026-09-17 | GFI Europe European plant-based sales data | 2025 meat-alternative value by country: FR €171.3 M +13.5%, DE €750.8 M +0.2%, IT €233.9 M +2.0%, NL €108.1 M −10.5%, ES €65.3 M −6.3%, UK £294.6 M −7.3%; FR volume +16.8% on −2.8% price | Value-weighted −0.7%; Europe is flat-to-soft on the panel, not booming |
| 2026-09-17 | GFI Europe blog + Circana | Circana excludes Lidl/Aldi, whose share rose 2023–25, so the panel "may overstate the contraction"; EU6 plant-based food & drink €16.3 bn, +5.1%; Germany +7.2% value / +4.2% volume | **Reconciles** the Euromonitor/panel gap; supports the +2.5 pp wedge |
| 2026-09-17 | ECB reference rates via frankfurter.dev, daily 2024–2026 | EUR/USD annual avg 1.0824 / 1.1300 / 1.1620 (YTD); GBP/USD +3.11% then +2.06%; USD/JPY +5.97% in 2026 | FX tailwind roughly **halves** 2025 → 2026 (+2.3 pp → +1.2 pp) |
| 2026-09-17 | Beyond Meat 8-K/A, SEC EDGAR, filed 2026-04-09 | FY2025 net revenue **$275.5 M, −15.6%**; volume −15.9%; Q4 US retail −6.5% on "weak category demand and reduced points of distribution" | US block confirmed deteriorating |
| 2026-09-17 | Beyond Meat Q2 2026 coverage (primary IR page 503'd) | Q2 2026 revenue **−8.2% to $68.8 M**, volume −9.5%, reduced US distribution; company denies bankruptcy; debt runway extended to 2030 | Decline continuing but decelerating vs FY2025 |
| 2026-09-17 | EU labelling: trilogue 2026-03-05 | **31 animal terms banned** (chicken, beef, pork, breast, thigh); "burger", "sausage", "nuggets" **survive** | Materially softer than feared; little 2026 sales impact given transition periods. Retained only as a tripwire |
| 2026-09-17 | STAT / MAHA coverage of 2026 US Dietary Guidelines (pub. 2026-01-07) | First federal guidance to explicitly discourage ultra-processed foods; drops the advisory committee's "prioritise plant protein" language | Real but second-order: US is 23.5% of the number and already falling |
| 2026-09-17 | JAMA Network Open, Sørensen et al., 2026-01-26 (PMC12836129) | Danish cohort, 293 GLP-1 initiators vs 884 matched: annual edible spend 52,523 → 35,051 DKK; **shift from ultraprocessed to unprocessed** | Structural headwind for an ultra-processed category, but Danish, small, no PB-meat breakout — small weight |
| 2026-09-17 | *Food Policy* "GLP-1 use and protein demand" (ScienceDirect 403 here; finding via search index) | GLP-1 effects "consistent for animal proteins but inconsistent or absent for plant-based options" | **Disconfirms** the strong GLP-1-kills-plant-based story. Reduces the GLP-1 drag |
| 2026-09-17 | Choices Magazine Q3 2025, Sun, Caputo & Taylor | PBMA price $8.61–10.46/lb vs beef $2.25–5.32/lb; 45% of households buy chicken alternatives on <20% of trips; risk of staying "niche products for sustainability-focused consumers" | Caps the upside: no mechanism for a step-change in 2026 |
| 2026-09-17 | Kalshi / Polymarket / Manifold search | **No market on this or any adjacent alt-protein quantity** | No market cross-check available |

## Dead ends and ruled-out hypotheses

- **"Global plant-based meat is steadily increasing"** (the question's own background). Half
  right at best: the *reported* series rose 2015→2025, but it printed a **−4.7% year**
  (2023 → 2024 headlines) and the US block has fallen every year since 2021. Treat the
  background as advocacy framing, not a trend statement. Called out in forecast.md.
- **Rebuilding the number bottom-up from panels.** Tried and abandoned. SPINS (US), Circana
  (EU6 supermarkets, no discounters), NIQ Homescan and Euromonitor disagree on scope by ~2×
  for Europe — the six-country Circana meat-alternative total is ≈€1.67 bn against
  Euromonitor's €/$3.6 bn for all of Europe. The right object to forecast is *the Euromonitor
  series on its own terms*, not reality.
- **Commercial market-research forecasts** (IMARC $21.23 bn by 2026; FMR $13 bn; Mordor
  $11.04 bn in 2026; market.us CAGR 17%). Mutually contradictory, scope-incompatible with
  Euromonitor's $6.6 bn. Excluded entirely.
- **EU "veggie burger ban" as a 2026 demand shock.** Ruled out: the 5 March 2026 trilogue
  spared format names and such rules carry multi-year transitions.
- **Metaculus cohort disagreement.** Not applicable — no cohort data exists yet.
- **Beyond Meat bankruptcy as a 2026 category event.** Company denies filing; debt pushed to
  2030. Even a filing removes maybe 3–4% of the global number, not 20%.

## Open questions to chase next time

1. **Does Euromonitor report GFI's global aggregate at fixed or year-on-year exchange rates?**
   Worth ±1–2 pp. Check the figure footnotes in the 2027 report, or ask GFI.
2. **Will GFI Europe publish 2026 country data before the SOTI report?** Its country decks
   (e.g. the Spain 2023–2025 deck, June 2026) usually precede it and cover 55% of the number.
3. Any GFI Europe / Circana **H1 2026** European read — none was published as of 2026-09-17.
4. The **2025 base restatement**: once the 2027 report is out, record what it says 2025 was,
   to extend reference class B to n = 5.
5. Whether GFI's 2024 operating deficit forces a scope cut to the licensed Euromonitor data.

---

## 2026-09-24 — v2 update log

- **Metaculus** (pre-fetched snapshot `raw/metaculus-2026-09-24.json`): CP revealed 2026-09-20 at
  $6.80 bn and moved to $6.85 bn [6.54, 7.13] (n=15) by 2026-09-23. Pro $6.78 bn [6.51, 7.08] (n=2), gold
  $6.77 bn [6.44, 7.16] (n=5), gold stable since reveal. 0 comments. Resolution text is the same as v1.
- **FX** (Frankfurter/ECB, `raw/ecb-fx-eurusd-cy2026-retrieved-2026-09-24.json`): 187 fixings, YTD
  EUR/USD mean 1.1618; last 1.1411 (2026-09-23). For FY < 1.13 the remaining ~66 fixings would need to
  average ≈1.040, so the v1 FX tripwire is dead. It is replaced with a Q4 < 1.10 tripwire. At ~1.14 for Q4 the FY average ≈1.156
  (+2.3% vs 2025).
- **Searches run**: "plant-based meat sales 2026 Europe Circana first half"; "plant-based meat sales
  September 2026"; "Good Food Institute Euromonitor plant-based meat retail 2026 news"; "plant-based
  meat US sales 2026 year to date decline SPINS Circana"; "Beyond Meat news September 2026". No 2026
  category data from any provider. Only 2025 figures resurfaced. Beyond Meat had product launches
  (Steak Filet retail expansion, Phytosphere portfolio) and a small convertible-note exchange, with no revenue news.
- **Integration**: blended ~20% weight on the gold/Pro cohort, which is independent crowd information that did not
  exist at v1. It moved the median −$0.02 bn and widened p25 by −$0.03 bn. Result: $6.84 bn [6.56, 7.12].
