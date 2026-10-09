# Research log — Will there be a bilateral ceasefire in the Russo-Ukrainian conflict before 2027?

Metaculus post 41138 (question 40839). Session date **2026-08-28**.

## Question mechanics

- **Resolution source**: Metaculus admin judgement on credible international reporting. No
  scheduled data release — this is decided by the world, not by a data cutoff.
- **Scheduled close**: 2026-12-31. The ceasefire must **go into effect during 2026**.
- **The two branches** (either suffices):
  1. a bilateral ceasefire that *lasts* ≥ 30 consecutive days entirely inside 2026; or
  2. a bilateral ceasefire *intended* to last ≥ 30 days (or indefinitely) per the agreement
     text or joint statement — **even if immediately violated**.
- **Fine print**: must be mutually agreed by Russia and Ukraine and apply to *all kinetic
  fighting by both sides*. Minor violations do not break it while both sides say it stands.
- **Edge cases and ambiguities**:
  - Branch 2 is the operative one. Comment by `Jgalt` (2026-07-24) corrects `josheee`
    (2026-07-10), who read the question as requiring an actual 30-day hold. The bar is an
    *announced* comprehensive bilateral ceasefire with ≥30-day/indefinite stated intent.
    `josheee` was at 10% on the stricter reading; the looser reading is worth a few pp more.
  - Branch 1 becomes unreachable after 2026-12-01 (30 days must fit inside 2026). Branch 2
    stays live to 2026-12-31.
  - **Effective date, not announcement date.** An agreement announced in late December with a
    1 January 2027 effective date resolves **NO**. This differs from Polymarket, which
    explicitly counts announcement regardless of when it starts.
  - **Partial ceasefires do not count**: the air-only ceasefire under discussion (US/Ukraine,
    July 2026), energy-infrastructure moratoria and Black Sea arrangements all fail "all
    kinetic fighting".
  - **Two mirrored unilateral declarations do not count** — the sibling question 35969 spells
    this out explicitly; 41138's "mutually agreed" implies the same.
  - Already ruled out by the admin (question still open at 12% on 2026-08-27): the
    **April 2026 Easter truce** (32 hours, bilateral, general) and the **May 2026 Victory Day
    truce** (3 days, bilateral, US-brokered). Both bilateral and comprehensive; both fail on
    intended duration. This is the key structural fact: the *mutual-agreement* step is
    demonstrably achievable, so the ≥30-day-intent clause is the entire binding constraint.

## Reference classes considered

| Class | n | Window | Base rate | Scaled to 125 days | Source | Kept? |
|---|---|---|---|---|---|---|
| A. This exact Metaculus question, run annually | 4 calendar years (2022, 2023, 2024, 2025) | 2022–2025 | 0/4 YES; Laplace (0+1)/(4+2)=16.7%/yr | 1−(1−0.167)^0.342 ≈ **6.0%** | Metaculus #10050, #13985, #31121, #35969 | ✅ primary |
| B. Hazard within this war | 0 qualifying events in 54 months | Mar 2022 – Aug 2026 | Laplace 1.79%/month | 1−(1−0.0179)^4.1 ≈ **7.1%** | own tally, verified against Wikipedia truce articles | ✅ |
| C. Interstate war termination (Correlates of War, 1823–2003) | 95 wars | full dataset | median duration 139 d, mean 408 d, 79% end within 2 yrs | this war at ~1,650 d is deep in the fat right tail → low per-quarter termination hazard, **~5%** | Clauset (2018) *Sci. Adv.*; freerangestats replication (2026-05-13) | ✅ but weak: it measures *war end*, not *announced ceasefire* |
| D. Ceasefire frequency in protracted conflict (ETH/PRIO Civil Conflict Ceasefire dataset) | 2,200+ ceasefires | 1989–2020 | ceasefires are *common* in long conflicts | pushes **up**, but dataset is civil-conflict and counts short/unilateral/partial deals that 41138 excludes | Clayton et al., *JCR* 2023 | ⚠️ kept as a directional caution only |

**Blend**: A and B agree closely (6–7%); C is a soft floor; D is the one upward pull.
Outside-view prior taken as **7%** for the remaining 125 days.

**Calibration note on class A**: the CP in this series has been persistently *too high* in the
Trump era. #31121 ("before 2026") peaked at **76% in March 2025** and resolved NO. #41138 opened
at 50–66% in December 2025 and is now 12%. At the equivalent calendar point (late August),
#13985 sat at ~10% and #31121 at ~16%; both went to ~0. Today's 12% is squarely inside that
band. Two NOs at 10–16% is not evidence of miscalibration by itself, but the peak-to-zero
pattern in both Trump-era iterations is a reason not to drift upward on diplomatic optimism.

## Decomposition

Because Ukraine has repeatedly *accepted* a ceasefire-first sequence (March 2025 Jeddah;
Zelensky's 2026-06-04 open letter proposing an immediate frontline ceasefire), the question
collapses to nearly a single decision: **will Putin agree to a ≥30-day/indefinite comprehensive
ceasefire taking effect before 2026-12-31?**

Paths, treated as roughly independent:

| Path | Mechanism | P |
|---|---|---|
| 1 | Comprehensive settlement/framework signed, ceasefire is its implementation | 4% |
| 2 | Russia drops "settlement first" and accepts a standalone ceasefire under US pressure or fiscal duress | 3% |
| 3 | Russia accepts a long truce tactically (consolidate, absorb a mobilisation wave, split US from Europe) | 2% |
| 4 | Resolution surprise — admin reads some other event as qualifying | 1% |

`1 − (0.96 × 0.97 × 0.98 × 0.99) ≈ 9.6%`. Rounded down slightly for the effective-date
constraint (below) → **9%**.

**Timing squeeze inside the 125 days**: Russian State Duma elections 18–20 September 2026, with
a widely-expected post-election mobilisation of 300k–500k, effectively removes September–October
from the Russian side. A December breakthrough plausibly carries a January effective date, which
resolves NO. The usable window is materially shorter than 125 days.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-08-28 | `metaculus_aggregations.py 41138` | CP 12.0% IQR[9,15] n=299; Pro 12.0% IQR[5,17] n=23; Gold 12.0% IQR[9,15] n=96. 965 forecasters total. CP mean 15.7% ≫ median → right-skewed community. | anchor; all three cohorts identical |
| 2026-08-28 | CP history 41138 | 50% (Dec 2025) → 40% (Feb) → 31% (Mar) → 20% (Apr–Jun) → 16% (Jul) → 12% (27 Aug). Monotone decay since March. | ↓ |
| 2026-08-28 | Metaculus comments (12) | `Jgalt` establishes the loose branch-2 reading; `GOLDEN-BLUE` (May) on the failed Russian spring offensive; `RuslanBes`/`wd28` (Feb) on both economies grinding down without either collapsing. | criteria clarified ↑, evidence mixed |
| 2026-08-28 | Metaculus #10050, #13985, #31121, #35969 | Predecessor questions for 2022/2023/2025 all resolved **NO**; #35969 resolved "Not before 2026". #31121 required an actual 30-day hold — 41138 is **looser**. | base rate ↓, criteria ↑ |
| 2026-08-28 | Wikipedia, April 2026 Russo-Ukrainian truce | 32 h, 11–13 Apr, bilateral (Zelensky proposed, Putin set the window), general scope, 469 Ukrainian-claimed violations, full fighting resumed on expiry. | fails ≥30 d intent |
| 2026-08-28 | Wikipedia, May 2026 Russo-Ukrainian truce; Moscow Times 2026-05-08 | 9–11 May Victory Day, 3 days, US-brokered by Trump, plus POW exchange. Preceded by *duelling unilateral* declarations (Ukraine 5–6 May, Russia 8–9 May) per Moscow Times 2026-05-04. | fails ≥30 d intent; but proves Trump can extract a bilateral announcement |
| 2026-08-28 | Polymarket gamma API, `russia-x-ukraine-ceasefire-before-2027` | **Market closed, resolved YES**, $14.5M volume. May-2026 monthly market resolved YES on $141M volume. Rules count announcement only, exclude "humanitarian pauses" but have no duration test. | **not comparable** — resolved on the 3-day truce |
| 2026-08-28 | Manifold API, `russia-x-ukraine-ceasefire-in-2026` | **14.8%**, 82 traders, $13.7k volume. Description matches 41138 closely: entire front line, long-term intent required, no minimum hold. Creator note 2026-01-08 makes the intent requirement explicit. | ✅ genuine comparable, slightly above me |
| 2026-08-28 | Manifold, assorted | "Ukraine war ends in 2026?" 12.7%. Polymarket-mirror "by Dec 31" 18% (stale, underlying already resolved). May-31 mirror resolved **CANCEL** at 89.5% → the Polymarket resolution was contested. | ↔ |
| 2026-08-28 | Kalshi API (`/events`, paginated; series probes) | No open Russia–Ukraine ceasefire market found. A third-party mirror (kalshi-uk.co.uk) quotes 48% and cites 25.5% in May — unverifiable and almost certainly the loose announcement definition. | dropped, not cited as evidence |
| 2026-08-28 | Bloomberg 2026-08-26 (via aggregators + Meduza + Japan Times) | **"Putin Moves to Escalate War in Ukraine as Talks at Dead End."** Three Kremlin sources: every mechanism for peace talks has collapsed; Russia weighing intensified conventional ballistic strikes on central Kyiv and infrastructure. Meduza adds that a growing number of Russian officials think escalation could eventually mean a tactical nuclear weapon. Kremlin publicly denied the report. | **↓ strongest single item** |
| 2026-08-28 | Al Jazeera 2026-08-21 | Ryabkov: Russia will consider "new ideas" only if they match Putin's goals and "realities on the ground". Putin's conditions unchanged: all of Donbas, demilitarisation, no NATO. Kushner/Witkoff have no visit scheduled. | ↓ |
| 2026-08-28 | Sputnik India 2026-08-27; anews 2026-08-25 | Peskov: US–Russia contacts continue "at the working level"; no date for a next trilateral round; talks should be private. | ↔ process alive but empty |
| 2026-08-28 | Al Jazeera 2026-08-12 | Zelensky says Ukraine has handed the US new proposals to end the war. | ↑ small |
| 2026-08-28 | Moscow Times 2026-08-20 (op-ed) | Three years of US mediation have produced only Black Sea/energy restraints and a three-day ceasefire. Ukrainian polling: **57% reject withdrawal from held Donbas even with security guarantees**. | ↓ |
| 2026-08-28 | CFR, Thomas Graham, 2026-07-10 | Putin has **expanded** territorial demands to include "Novorossiya"; Russia escalating aerial assault; Trump's stance now more supportive of Ukraine. Any deal would be "fragile" and the first step in a years-long negotiation. | ↓ |
| 2026-08-28 | ISW / Critical Threats, 2026-08-12 and 2026-08-01 | Spring–Summer 2026 offensive has made **no operationally significant gains** 2.5 months in. 29 Jan–12 Aug: Russia seized ~383 km², lost ~234 km²; Ukraine liberated ~627 km² in the Oleksandrivka direction. Russian losses ~30k/month, ~60% KIA. Zelensky warns Russia plans to mobilise several hundred thousand by end-2026 and again in 2027, with compulsory mobilisation expected after the September Duma elections. | ↓ (Russia planning for 2027, not for peace) |
| 2026-08-28 | Russia Matters; Moscow Times 2026-07-21 & 2026-07-02; EUobserver; Saratoga Foundation; globalsecurity.org | Duma elections **18–20 Sep 2026**, first since the full-scale invasion. Widely expected post-election mobilisation; Ukraine's Center for Countering Disinformation puts it at **>500,000 in autumn 2026**; analysts frame a 300k–500k phased programme as building **operational depth for 2027**. Russian officials deny any plans. | **↓ strong** |
| 2026-08-28 | CNBC 2026-08-15; Moscow Times 2026-05-12; Reuters/Investing; Kyiv Post; NEST Centre | 2026 growth cut **1.3% → 0.4%**; Q1 GDP **−0.3%**; oil & gas revenue **−30%** (H1 2026 at 64% of H1 2024); Q1 defence spending 5.9tn ₽ (~$75bn) = **48% of all state spending**; H1 deficit ~6tn ₽ (~$77bn), **60% above the full-year target**; VAT rising 20%→22% on 2027-01-01. | ↑ (the one real YES driver) |
| 2026-08-28 | Institut Jacques Delors; European Parliament briefing; Consilium | Ukraine's 2026–27 gap ~€135.7bn; EU **€90bn** support loan agreed, reparations-loan mechanism up to €210bn under discussion. | ↓ (removes the forcing function on Kyiv) |
| 2026-08-28 | Foreign Policy (pk) — air ceasefire push, late July 2026 | US and Ukrainian officials discussed an **air-only** ceasefire to put to Russia ahead of Zelensky's Washington visit. Peskov called discussion of it premature. | ↓ — the live proposal is one that *cannot* resolve this question YES |
| 2026-08-28 | Kyiv Independent / Kyiv Post — Lavrov | Russia will not accept a ceasefire without a long-term settlement; "no freeze without eliminating the root causes" (Galuzin). Reaffirmed August 2026 alongside threats of "harsher" strikes. | ↓ — the sequencing gap is unmoved |
| 2026-08-28 | NV.ua 2026-08-18 | Ukrainian military intelligence deputy chief: Russia shows **no signs of ceasefire readiness on the battlefield**. | ↓ |
| 2026-08-28 | FutureSearch, `russia-x-ukraine-ceasefire-agreement-by-december-31-2026` | 38%, but dated **2026-06-11** and written against the loose "formal general pause" definition whose Polymarket analogue has since resolved. | not comparable; not used as an anchor |
| 2026-08-28 | Trilateral process history | Talks suspended since February 2026 after the outbreak of the Iran war; Geneva February round ended without breakthrough; March round cancelled. Manifold "Russia-Ukraine ceasefire before end of Iran War" resolved NO. | ↓ |

## Dead ends and ruled-out hypotheses

- **Kalshi** — no open, verifiable market located via the public API across ~1,600 open events;
  third-party mirrors quote numbers I could not confirm against Kalshi itself. Excluded rather
  than cited at low confidence.
- **Polymarket as an anchor** — resolved YES in May 2026 on a 3-day truce. Its $14.5M and $141M
  volumes say nothing about *this* question. Anyone quoting "the market says a ceasefire happened
  in 2026" is answering a different question. Also note the Manifold mirror of the May market
  resolved CANCEL, i.e. the resolution was disputed.
- **FutureSearch 38%** — stale (June) and loose-definition. Not an anchor.
- **"Sentinel Team" weekly** — searched; no dated, numeric Russo-Ukrainian ceasefire forecast
  found for August 2026. Nothing cited.
- **archive.is** — blocked in this environment; the Bloomberg 2026-08-26 piece was reconstructed
  from Japan Times, Meduza and wire aggregation rather than the original.
- **Metaculus #35969** as a live date cross-check — it resolved ("Not before 2026"). Secondary
  reporting cites live Metaculus date questions with medians of **April/November/December 2027**;
  I could not verify those post IDs directly, so they are noted, not relied on.

## Open questions to chase next time

1. Did a mobilisation decree follow the 18–20 September Duma elections, and at what size?
2. Has any trilateral (US–Russia–Ukraine) round actually convened since February 2026?
3. Did Russia respond to the air-ceasefire proposal, and did the sequencing language shift?
4. Find and verify the live Metaculus *date* question on first bilateral ceasefire — it is the
   natural consistency check on this binary.
5. Russian Q3 budget execution: does the deficit trajectory force a 2027 fiscal choice that
   changes the calculus?

---

## Session 2026-09-24 — v2 re-analysis

**Trigger:** review 3 days overdue (due 2026-09-21), and the CP tripwire fired: CP 6.0% on
2026-09-22, outside [7%, 20%]. Mode: re-analysis.

### Metaculus (raw/metaculus-2026-09-24.json, fetched 2026-09-24 by the parent session)

- CP 6.0% IQR [4, 8], mean 7.4%, n=313 (978 all-time). Pro 6.0% [5.0, 7.5] n=24. Gold 6.0% [5, 8] n=97.
- CP path: 12% (28 Aug) → 11% (30 Aug) → 10% (31 Aug–9 Sep) → 9% (10 Sep) → 8% (15 Sep) →
  7% (19 Sep) → 6% (22 Sep). A steady slide with no single step change.
- Comments: no new comments since v1. The latest is still Jgalt's from 2026-07-24.

### Markets (fetched 2026-09-24)

| Market | Value | Note |
|---|---|---|
| Polymarket "ceasefire agreement by Dec 31, 2026" | 23% (bid .22/ask .24), $2.68M vol, 1-month change −3pp | Criteria: any mutually agreed *general* pause; an agreement reached before the date counts even if it takes effect later. Looser than #41138 on duration and effective date |
| Polymarket ladder Oct 31 / Nov 30 / Jan 31 2027 / Mar 31 2027 | 8% / 14.5% / 29% / 37.5% | The steep Dec–Jan ramp looks like holiday-truce and deal-announcement mass |
| Polymarket May 31 / Jun 30 / Aug 31 2026 rungs | resolved NO | Odd given that the sibling "ceasefire by end of 2026" market resolved YES on the May truce. This "agreement" event may have been listed after May or read the May truce differently. Not investigated further |
| Manifold "Russia x Ukraine ceasefire in 2026?" | 13.8%, 82 traders | was 14.8% at v1 |

### Tripwire searches

| Tripwire | Search | Result |
|---|---|---|
| Kremlin ceasefire-first | "Peskov ceasefire Ukraine September 2026"; "Kremlin lasting peace not temporary ceasefire" | Opposite. Peskov (22 Sep): "lasting peace… not a ceasefire, which… will achieve nothing" |
| Summit scheduled | "Trump Putin call summit October 2026" | Trump–Putin call on 8 Sep. Trump: summit only when Putin is ready to sign. Kremlin: Putin–Zelensky meeting before expert talks is a "waste of time" |
| Air ceasefire accepted | "Russia rejects air ceasefire energy ceasefire proposal September 2026" | Rejected. Trump proposed an energy ceasefire on 14 Sep and Russia declined. Only a reciprocal halt on strikes against the capitals during the 5–6 Sep envoy visit (partial) |
| Mobilisation decree | "Russia mobilization decree after Duma elections"; "…announced Putin September 2026" | None as of ~22 Sep. Putin called it "nonsense" on 1–2 Sep. Kyiv Independent expects a fragmented call-up; contract signings Jan–Aug 234k vs 260k in 2025 |
| Trilateral round | "trilateral talks resume October Ushakov Umerov" | Not yet convened. Peskov (13 Sep): October possible. Kyiv preparing for October. Last round Geneva, February |

### General developments since 2026-08-28

- 5 Sep: Witkoff and Kushner met Putin for 3 hours plus dinner. Putin ordered a 3-day halt on
  strikes against Kyiv; the halt on the capitals was reciprocal.
- 6 Sep: Witkoff and Kushner made their first visit to Kyiv. Zelensky: "we expect the war will
  continue". No ceasefire proposal came out of it.
- 8 Sep: Trump–Putin call. Ushakov says "specific measures" to accelerate an end were discussed.
- 11–13 Sep: BRICS summit in New Delhi. Xi and Modi offered to help facilitate a settlement.
- 14 Sep: Trump proposed an energy ceasefire. Russia declined.
- 18–20 Sep: Duma elections; United Russia ~58%. On 19–20 Sep Ukraine hit Moscow Oblast with its
  largest strike package of the war (Sobyanin: 1,600 drones downed).
- ISW: Ukraine is contesting the initiative; at the current rate Russia would not take Donetsk
  Oblast before ~2032.
- 22–23 Sep, UNGA: Zelensky met Trump and offered a reciprocal energy ceasefire and a leaders'
  trilateral. Kremlin answered "peace, not truce" and called a leaders' meeting "a waste of time".
- Fiscal: full-year deficit forecast of 5.5–6tn ₽. No new decisive data.

### Dead ends this session

- CNBC 2026-09-23 and Ukrainska Pravda 2026-09-03 ("Trump says meeting with Putin will take place
  as war nears end") returned 403 on fetch. I used search summaries only and did not rely on the
  UP headline.
- Wikipedia "2026 Russo-Ukrainian truce" is a disambiguation page, with no new truce after May.

### Integration

Outside view over 98 days: 4.8% (series) and 5.5% (hazard). Scenario table: 5.5% YES. The
Polymarket 23% after removing short-truce (~10pp) and announce-now-effective-2027 (~4pp) mass
comes to ~6–9%. Final: 6.0%, IQR [4.0, 9.0].

### Open questions for next time

1. Did the October trilateral convene? Who attended, and did it produce any text?
2. Mobilisation decree, or a formalised "fragmented" call-up?
3. Is there any US deadline or sanctions threat (the Graham sanctions bill) with a date attached?
4. Does a holiday truce proposal emerge for late December, and would its stated duration be
   ≥30 days?

---

## 2026-10-09 — v3 update session

**Metaculus:** the browser/aggregation path is blocked by Cloudflare (verified by the parent
agent). API JSON (bot key) cached as `raw/metaculus-api-2026-10-09.json`: status open, no
resolution, 984 forecasters all-time, criteria unchanged. No fresh CP/Pro/gold; last seen
6/6/6% on 2026-09-23.

**Markets (2026-10-09):**
- Polymarket ladder (gamma API): Oct 31 4.15%, Nov 30 8%, Dec 31 14.5% (bid 14 / ask 15,
  $2.75M), Jan 31 2027 22.5%, Mar 31 2027 32.5%. Dec 31 was 23% on 09-24. Saved to
  `raw/polymarket-ceasefire-agreement-by-2026-10-09.json`.
- Manifold "ceasefire in 2026": 7.5% (85 traders), down from 13.8%. Saved to
  `raw/manifold-ceasefire-2026-2026-10-09.json`.

**News since 2026-09-24:**
- 25 Sep: Bloomberg reports that Trump asked Zelensky to meet Putin in Moscow; Zelensky declined.
- 1 Oct: Putin at Valdai calls a refinery-for-shipping strike truce "simply ridiculous", issues a
  Kaliningrad nuclear warning, and says he prefers to end the war via talks with a neutral
  Ukraine (Al Jazeera).
- 1 Oct: Turkey and the UN, with the Centre for Humanitarian Dialogue, convene Black Sea truce
  talks for early October (Bloomberg; Ukrainska Pravda). Partial in scope, so it cannot resolve
  YES.
- 1–3 Oct: Russia strikes the Pivdennyi and Northern bridges in Kyiv. The Russian MFA promises
  "mass retaliatory strikes" and tells foreigners to leave.
- 3–4 Oct: the US proposes a technical-level trilateral by end-October (UAE likely), with an
  agenda of an energy truce and the grain corridor. Kyiv agrees. Moscow has not answered as of
  7 Oct (Tykhyi, Ukrainian MFA). Sources say Trump privately doubts an energy truce before
  winter (Kyiv Independent).
- No mobilisation decree; Peskov denies a 300k plan.

**Dead ends:** CNBC 10-05, Censor.net and Ukrainska Pravda returned 403 on fetch, so only
search summaries were used. No October Peskov or Ushakov quote on the trilateral was found.

**Integration:** outside view over 83 days ≈ 4.4%. Scenario YES mass 4.5%. Polymarket after
stripping short truces and announce-only deals comes to ~4–6%. Final: 4.5%, IQR [3.0, 7.0].
