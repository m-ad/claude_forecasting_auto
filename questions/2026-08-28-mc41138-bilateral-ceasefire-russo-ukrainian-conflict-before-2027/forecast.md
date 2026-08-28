# Will there be a bilateral ceasefire in the Russo-Ukrainian conflict before 2027?

| | |
|---|---|
| **Source** | Metaculus #41138 — https://www.metaculus.com/questions/41138/will-there-be-a-bilateral-ceasefire-in-the-russo-ukrainian-conflict-before-2027/ |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2025-12-19 (first CP point) / 2026-12-31 / 2026-12-31 |
| **Status** | open |
| **Current forecast** | **Median 9.0%, IQR [6.5%, 13.0%]** (v1, 2026-08-28) |
| **Community (as of 2026-08-27)** | CP 12.0% (n=299) · Pro 12.0% (n=23) · Gold 12.0% (n=96) |
| **Next review** | 2026-09-21 |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-08-28

### What resolves YES

A bilateral ceasefire between Russia and Ukraine must **go into effect during calendar 2026**
and either (a) last ≥ 30 consecutive days entirely inside 2026, or (b) be **intended** to last
≥ 30 days or indefinitely per the agreement text or a joint statement — *even if it is broken
immediately*. The fine print requires it to be mutually agreed and to cover **all kinetic
fighting by both sides**; minor violations do not break it while both governments say it stands.
There is no scheduled resolution source: a Metaculus admin judges it on credible international
reporting.

Four edge cases carry real weight:

1. **Branch (b) is the operative one.** The bar is an *announced* comprehensive bilateral
   ceasefire with ≥30-day or indefinite stated intent — not a ceasefire that actually holds.
   The top comment thread turns on exactly this: `josheee` (2026-07-10) forecast 10% reading
   the question as requiring a 30-day hold, and `Jgalt` (2026-07-24) corrected him from the
   text. The looser reading is worth several points.
2. **Effective date, not announcement date.** A deal announced on 28 December to start on
   1 January 2027 resolves **NO**. Polymarket's analogous market explicitly counts the
   announcement; Metaculus does not.
3. **Partial ceasefires fail.** The air-only ceasefire the US and Ukraine were preparing to put
   to Russia in late July 2026 [17], energy-infrastructure moratoria and Black Sea arrangements
   all fail "all kinetic fighting". This matters because the *live* proposal on the table is
   one that cannot resolve this question YES.
4. **Two mirrored unilateral declarations fail**, as the sibling question #35969 spells out [4].
   That is how the May 2026 sequence began [8].

Already implicitly ruled out by the admin, since the question was still open at 12% on
2026-08-27: the **April 2026 Easter truce** (32 hours) and the **May 2026 Victory Day truce**
(3 days) [6][7]. Both were bilateral and comprehensive in scope; both fail on intended duration.
**That is the single most clarifying fact about this question** — the mutual-agreement machinery
demonstrably works, so the ≥30-day-intent clause is the entire binding constraint.

### Outside view

| Class | n | Base rate | Scaled to the remaining 125 days |
|---|---|---|---|
| **A. This exact question, run annually** — Metaculus #10050 (before 2023), #13985 (before 2024), #31121 (before 2026), #35969 | 4 calendar years | 0/4 YES; Laplace (0+1)/(4+2) = 16.7%/yr | 1−(1−0.167)^0.342 ≈ **6.0%** |
| **B. Hazard within this war** | 0 qualifying events in 54 months | Laplace 1.79%/month | 1−(1−0.0179)^4.1 ≈ **7.1%** |
| **C. Interstate war termination** — Correlates of War 1823–2003 [20][21] | 95 wars | median duration 139 d, mean 408 d, 79% end within 2 yrs | this war at ~1,650 d sits deep in the fat right tail → **~5%** |
| **D. Ceasefire frequency in protracted conflict** — ETH/PRIO Civil Conflict Ceasefire dataset [22] | 2,200+ ceasefires, 1989–2020 | ceasefires are *common* in long conflicts | pushes **up**, but the dataset is civil-conflict and counts short, unilateral and partial deals that #41138 excludes |

A and B agree closely; C is a soft floor and measures the wrong thing (war *end*, not announced
ceasefire); D is the only upward pull and is the weakest class. **Outside-view prior: 7%.**

![CP trajectories of the annual ceasefire question series](charts/cp-trajectory-annual-series.png)

Two things in that chart do the work. First, this is the **fifth consecutive year** of the same
question and the previous four all resolved NO. Second, both Trump-era iterations spiked and
then decayed to zero: #31121 peaked at **76% in March 2025** and resolved NO; #41138 opened at
50–66% in December 2025. At the equivalent calendar point in late August, #13985 sat at ~10%
and #31121 at ~16%. Today's 12% is squarely inside that band, and both predecessors went to
~0 from there.

One correction to the base rate, in the YES direction: #31121 required the ceasefire to
**actually stand** 30 days. #41138 only requires stated intent. The series is therefore an
under-estimate of the hazard for *this* question. Note, though, that the looser criterion would
not have changed any past year's outcome — no ≥30-day-intent bilateral ceasefire was ever even
*announced*. In March 2025 Ukraine accepted a 30-day unconditional ceasefire and Russia refused,
so it never became bilateral.

### Inside view

Ukraine has repeatedly accepted a ceasefire-first sequence: Jeddah in March 2025, and Zelensky's
open letter of 2026-06-04 proposing an immediate frontline ceasefire, bilateral talks and an
all-for-all prisoner exchange. The US wants a deliverable. So the question very nearly collapses
to a single decision: **will Putin agree to a ≥30-day or indefinite comprehensive ceasefire
taking effect before 2026-12-31?**

Paths to YES, treated as roughly independent:

| Path | Mechanism | What has to be true | P |
|---|---|---|---|
| 1 | Comprehensive settlement or framework signed; the ceasefire is its implementation | Russia moderates from "all of Donbas + Novorossiya + demilitarisation + no NATO", **or** Ukraine concedes Donbas | 4% |
| 2 | Russia drops "settlement first" and takes a standalone ceasefire under US pressure or fiscal duress | Kremlin reverses an 18-month-old, repeatedly restated position | 3% |
| 3 | Russia accepts a long truce tactically — consolidate, absorb a mobilisation wave, split the US from Europe | Putin chooses pause over escalation, which he has not done since 2022 | 2% |
| 4 | Resolution surprise — the admin reads some other event as qualifying | criteria are tight and the admin has already passed on two 2026 truces | 1% |

`1 − (0.96 × 0.97 × 0.98 × 0.99) ≈ 9.6%`, trimmed to **9%** for the effective-date constraint.

**The window is shorter than 125 days.** Russia holds State Duma elections on **18–20 September
2026** — the first since the full-scale invasion — and analysts across the spectrum expect a
mobilisation of 300k–500k immediately afterwards, deliberately held back until the vote is past
[13][14][15]. That effectively removes September and October on the Russian side. A December
breakthrough plausibly carries a January effective date, which resolves NO. The realistic
window is perhaps six weeks in November–early December.

### Evidence

**What updated me down.**

- **Bloomberg, 2026-08-26 (two days before this forecast): "Putin Moves to Escalate War in
  Ukraine as Talks at Dead End"** [10]. Three people close to the Kremlin say every mechanism for
  peace talks has collapsed and Russia is weighing intensified conventional ballistic strikes on
  central Kyiv and on infrastructure in other cities. Meduza's write-up adds that a growing
  number of Russian officials believe escalation could eventually mean a tactical nuclear weapon
  [11]. The Kremlin publicly denied the report. Even discounting single-sourced Kremlinology and
  the denial, this is the freshest direct read on intent. **LR ≈ 0.6.**
- **The post-Duma mobilisation plan** [13][14][15]. Ukraine's Center for Countering
  Disinformation puts it above 500,000 for autumn 2026; independent analysts describe a phased
  300k–500k programme explicitly aimed at building **operational depth for 2027**. A state
  conscripting half a million men in Q4 is not a state signing a comprehensive ceasefire in Q4.
  **LR ≈ 0.6.**
- **Russia's negotiating position has hardened, not softened.** Thomas Graham (CFR, 2026-07-10)
  notes Putin has *expanded* his territorial demands to include "Novorossiya" [16]. Ryabkov on
  2026-08-21: new ideas are welcome only if they match Putin's goals and "realities on the
  ground"; the conditions remain all of Donbas, demilitarisation, no NATO [12]. Lavrov continues
  to refuse a ceasefire absent a long-term settlement, and Galuzin's "no freeze without
  eliminating the root causes" is unchanged [18]. **LR ≈ 0.7.**
- **The live proposal is the wrong shape.** What the US and Ukraine were preparing in late July
  was an **air-only** ceasefire [17] — which by construction cannot resolve this question YES.
  Peskov called even discussing it premature. When the negotiators' own ambition has shrunk to a
  partial measure, the comprehensive measure is not close.
- **Absence of expected evidence.** If a qualifying ceasefire were coming by December, I would
  expect a scheduled summit, a named trilateral round, or shuttle diplomacy in motion. Peskov on
  2026-08-27: contacts continue "at the working level", no date for a next trilateral round, and
  talks should be private [19]. Kushner and Witkoff have no visit scheduled [12]. Trilateral
  talks have been suspended since February 2026, when the Iran war pulled US attention away.
  Nothing is on the calendar.
- **Ukraine has no forcing function.** The EU's **€90bn** support loan covers 2026–27 against a
  ~€135.7bn gap, with a reparations-loan mechanism of up to €210bn under discussion [23][24].
  Ukrainian polling shows **57% reject withdrawal from held Donbas even with security
  guarantees** [9]. Trump's posture has shifted *toward* Ukraine [16], which reduces rather than
  increases the pressure on Kyiv to sign something bad.
- **The battlefield gives Russia no exit ramp it wants and no defeat that forces one.** ISW:
  the Spring–Summer 2026 offensive has made no operationally significant gains 2.5 months in;
  between 29 January and 12 August Russia seized ~383 km² and lost ~234 km², while Ukraine
  liberated ~627 km² around Oleksandrivka [25][26]. Ukrainian military intelligence, 2026-08-18:
  Russia shows no signs of ceasefire readiness on the battlefield [27]. Stalemate is the
  condition under which this war has already run for three years.

**What updated me up.**

- **Russia's fiscal position is genuinely deteriorating.** 2026 growth cut from 1.3% to 0.4%;
  Q1 GDP −0.3%; oil and gas revenue down ~30% (H1 2026 at 64% of H1 2024); Q1 defence spending
  5.9tn ₽ (~$75bn), 48% of all state spending; H1 deficit ~6tn ₽ (~$77bn), **60% above the
  full-year target**; VAT rising 20%→22% [28][29][30][31]. This is the one mechanism that could
  change Putin's mind. **LR ≈ 1.4** — but it operates on a multi-quarter horizon, and Russia
  still has the National Wealth Fund and a captive domestic debt market. It is a 2027–28 driver
  priced into a 2026 question.
- **Trump-brokered surprise is a live mechanism.** The May 2026 three-day truce came out of a
  "surprise diplomatic intervention" by Trump [8], and Zelensky handed Washington new proposals
  on 2026-08-12 [12]. A US-brokered announcement of a "30-day ceasefire" is precisely the kind
  of deliverable this process generates, and Ukraine would say yes. **LR ≈ 1.3.**
- **The loose resolution criterion.** Announcement with ≥30-day intent suffices; no hold
  required. **LR ≈ 1.5** relative to the historical series.

Odds arithmetic from the 7% prior: `0.0753 × (0.6 × 0.6 × 0.7) × (1.4 × 1.3 × 1.5) ≈ 0.050`,
i.e. ~4.8%. That is lower than my scenario decomposition (9.6%) and lower than I am willing to
go against three agreeing cohorts. The LRs are almost certainly over-stated — the negative items
are correlated (they are all the same underlying fact: Russia intends to fight into 2027), and
counting them as three independent updates triple-counts. Collapsing the negatives into one
LR ≈ 0.65 gives `0.0753 × 0.65 × 2.7 ≈ 0.117` → ~11.7%. The honest range across methods is
**5–12%**, and I settle at **9%**.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP (recency-weighted) | **12.0%**, IQR [9%, 15%] (n=299) | 2026-08-27 | mean 15.7% ≫ median → right-skewed; 965 forecasters have ever forecast |
| Metaculus Pro | **12.0%**, IQR [5%, 17%] (n=23) | 2026-08-27 | same centre, wider band, more downside mass |
| Metaculus gold medalists | **12.0%**, IQR [9%, 15%] (n=96) | 2026-08-27 | identical to CP |
| Manifold — "Russia x Ukraine ceasefire in 2026?" | **14.8%** (82 traders, $13.7k) | 2026-08-28 | ✅ closest genuine comparable: entire front line, long-term intent, no minimum hold. Play-money → discount |
| Manifold — "Ukraine war ends in 2026?" | 12.7% (42 traders) | 2026-08-28 | harder bar than a ceasefire, so ~equal pricing is odd; thin market |
| Polymarket — "ceasefire by end of 2026" | **resolved YES** ($14.5M vol) | May 2026 | ❌ **not comparable** — announcement-only, no duration test; resolved on the 3-day Victory Day truce |
| Polymarket — "ceasefire by May 31, 2026" | resolved YES ($141M vol) | May 2026 | the resolving event; the Manifold mirror of it resolved **CANCEL**, i.e. disputed |
| FutureSearch | 38% | 2026-06-11 | ❌ stale and loose-definition ("formal general pause") |
| Kalshi | — | — | no open market found via the public API across ~1,600 open events; third-party mirrors quote 48% unverifiably. Excluded |
| Sentinel Team / GJOpen / INFER | — | — | no dated numeric forecast on this question found |

**Cohort agreement, and where I sit.** Community, Pro and gold medalists are at *exactly* 12.0%
— unusual, and it means there is no cohort-disagreement signal to mine. That is a real reason
for restraint: when the better-track-record cohorts agree with the crowd, the prior that I am
the one who is wrong is high. I am 3pp below, inside the methodology's 10pp tolerance, on four
grounds:

1. **Freshness.** The Bloomberg dead-end report [10] landed on 26 August; the CP moved only
   0.127 → 0.120 across 26–27 August. It is barely digested.
2. **A shorter effective window than the nominal one.** Duma elections plus a mobilisation wave
   consume September–October; a December deal plausibly takes effect in January and resolves NO.
   I do not think the crowd is pricing the effective-date clause.
3. **Definitional bleed.** With Polymarket having paid out YES on a 3-day truce and a Manifold
   Polymarket-mirror still quoting 18%, some forecasters are plausibly pricing "a ceasefire is
   announced" rather than "a ≥30-day-intent ceasefire takes effect". `josheee`'s comment argues
   exactly this about the crowd. The right-skewed CP mean (15.7% vs 12.0% median) is what that
   would look like.
4. **Series history.** Both Trump-era iterations of this question over-priced diplomatic
   optimism by a wide margin and decayed to zero.

Against all that: Pro forecasters carry an IQR down to 5%, so my number is well within their
distribution rather than contrarian; and Manifold's comparable market sits *above* the CP. I
have not found a fact the cohorts missed — I have found a weighting I would do differently. That
justifies 3pp, not 6pp.

### Scenarios

| # | Scenario | Weight | Implies |
|---|---|---|---|
| 1 | **Grinding continuation.** Russia mobilises after the September Duma vote, escalates strikes, fights into 2027. Working-level US–Russia contacts continue without a trilateral round. | 66% | NO |
| 2 | **Talks resume but produce only partial measures.** Kushner/Witkoff shuttle returns; an air ceasefire, an energy moratorium or a POW deal lands; no comprehensive ceasefire. | 16% | NO (partial measures explicitly fail the criteria) |
| 3 | **Another short symbolic truce.** A Christmas/New Year truce of days, as in April and May 2026. | 8% | NO (fails ≥30-day intent) |
| 4 | **Framework deal, effective 2026.** US-brokered settlement or standalone ≥30-day ceasefire signed and in effect by 31 December. | 7% | **YES** |
| 5 | **Framework deal, effective 2027.** Agreement announced in December, ceasefire starts in January. | 2% | NO — and it will *feel* like YES in the press |
| 6 | **Resolution surprise** — the admin counts something I have judged non-qualifying. | 1% | **YES** |

Weights sum to 100%; YES mass = 7% + 1% = **8%**. Rounded up to **9%** to reflect that scenario 1
is doing a lot of work at 66% and I would rather err toward the cohorts than away.

### Sensitivity

| Assumption | If instead | Forecast becomes |
|---|---|---|
| Branch (b) applies: an *announced* ≥30-day-intent ceasefire suffices, no hold required (`Jgalt`'s reading) | The admin in practice requires the ceasefire to actually stand 30 days | **5.0%** |
| Russia mobilises after the 18–20 September Duma elections and is resourcing 2027 | No mobilisation decree by 2026-10-31 and the Kremlin signals a pause instead | **15%** |
| The ceasefire must be *in effect* by 2026-12-31 | Announcement alone sufficed (Polymarket's rule) | **13%** |
| Russia's fiscal deterioration bites on a 2027–28 horizon | It forces a decision inside Q4 2026 (e.g. NWF liquid assets publicly exhausted) | **16%** |

### What would change my mind (tripwires)

- [ ] **Kremlin drops "settlement first."** Putin, Lavrov or Peskov, on the record, accepts a
      ceasefire-first sequence, by **2026-11-30** → **+15pp** (this is the single load-bearing
      belief; it has held since 2022).
- [ ] **A Putin–Trump or Putin–Zelensky summit is scheduled with a public date** for before
      **2026-12-15** → **+6pp**.
- [ ] **Russia publicly accepts the US/Ukrainian air-ceasefire proposal** by **2026-10-31** →
      **+4pp**. The air ceasefire itself cannot resolve this question YES, but acceptance would
      mean the sequencing objection has cracked.
- [ ] **Russian mobilisation decree of ≥100,000 announced after the 18–20 September Duma
      elections**, by **2026-10-31** → **−3pp** (to ~6%).
- [ ] **No trilateral US–Russia–Ukraine round convenes by 2026-10-31** → **−2pp**; mechanical
      decay alone should take this below 5% by 1 December absent news.
- [ ] **Metaculus CP moves outside [7%, 20%]** → stop nudging and re-derive from scratch; a move
      that large means the world changed or I misread the criteria.

### Sources

1. Will there be a bilateral ceasefire in the Russo-Ukrainian conflict before 2027? — Metaculus #41138 — https://www.metaculus.com/questions/41138/will-there-be-a-bilateral-ceasefire-in-the-russo-ukrainian-conflict-before-2027/ (accessed 2026-08-28)
2. Will there be a bilateral cease-fire or peace agreement in the Russo-Ukraine conflict before 2023? — Metaculus #10050 (resolved NO) — https://www.metaculus.com/questions/10050/bilateral-ceasefire-between-russia--ukraine/ (accessed 2026-08-28)
3. Bilateral Ceasefire in Ukraine before 2024? — Metaculus #13985 (resolved NO) — https://www.metaculus.com/questions/13985/bilateral-ceasefire-in-ukraine-before-2024/ (accessed 2026-08-28)
4. When will a bilateral ceasefire or peace agreement in the Russo-Ukraine conflict first go into effect? — Metaculus #35969 (resolved "Not before 2026") — https://www.metaculus.com/questions/35969/when-will-russia-ukraine-ceasefire-occur/ (accessed 2026-08-28)
5. Will there be a bilateral ceasefire in the Russo-Ukraine conflict before 2026? — Metaculus #31121 (resolved NO) — https://www.metaculus.com/c/future-perfect/31121/ceasefire-in-the-russo-ukraine-conflict-before-2026/ (accessed 2026-08-28)
6. April 2026 Russo-Ukrainian truce — Wikipedia — https://en.wikipedia.org/wiki/April_2026_Russo-Ukrainian_truce (accessed 2026-08-28)
7. May 2026 Russo-Ukrainian truce — Wikipedia — https://en.wikipedia.org/wiki/May_2026_Russo-Ukrainian_truce (accessed 2026-08-28)
8. Russia and Ukraine Agree to U.S.-Brokered Ceasefire This Weekend — The Moscow Times, 2026-05-08 — https://www.themoscowtimes.com/2026/05/08/russia-and-ukraine-agree-to-us-brokered-ceasefire-this-weekend-a92721 (accessed 2026-08-28); and Ukraine and Russia Declare Separate Temporary Ceasefires — The Moscow Times, 2026-05-04 — https://www.themoscowtimes.com/2026/05/04/ukraine-and-russia-declare-separate-temporary-ceasefires-a92680
9. Tear Down the Wall of Silence Around Negotiations To End Russia-Ukraine War — The Moscow Times, 2026-08-20 — https://www.themoscowtimes.com/2026/08/20/tear-down-the-wall-of-silence-around-negotiations-to-end-russia-ukraine-war-a93533 (accessed 2026-08-28)
10. Putin Moves to Escalate War in Ukraine as Talks at Dead End — Bloomberg, 2026-08-26 — https://www.bloomberg.com/news/articles/2026-08-26/putin-moves-to-escalate-war-in-ukraine-with-talks-at-dead-end (paywalled; content confirmed via The Japan Times, 2026-08-27 — https://www.japantimes.co.jp/news/2026/08/27/world/putin-escalate-war-ukraine-talks/) (accessed 2026-08-28)
11. Kremlin sources tell Bloomberg that Putin is preparing to escalate the war in Ukraine — Meduza, 2026-08-26 — https://meduza.io/en/feature/2026/08/26/kremlin-sources-tell-bloomberg-that-putin-is-preparing-to-escalate-the-war-in-ukraine-a-growing-number-of-russian-officials-believe-that-could-eventually-mean-a-tactical-nuclear-weapon (accessed 2026-08-28)
12. Russia says ready for 'new ideas' on Ukraine war that match Putin's goals — Al Jazeera, 2026-08-21 — https://www.aljazeera.com/news/2026/8/21/russia-ready-for-new-ideas-on-ukraine-war-that-match-putins-goals (accessed 2026-08-28); and Zelenskyy says Ukraine has sent proposals to US to end war with Russia — Al Jazeera, 2026-08-12 — https://www.aljazeera.com/news/2026/8/12/zelenskyy-says-ukraine-has-sent-proposals-to-us-to-end-war-with-russia
13. Should Russia Brace for a New Mobilization? — The Moscow Times, 2026-07-21 — https://www.themoscowtimes.com/2026/07/21/should-russia-brace-for-a-new-mobilization-a93256 (accessed 2026-08-28)
14. Will Putin Resume Mobilization? If So, When and Why? — Russia Matters — https://www.russiamatters.org/blog/will-putin-resume-mobilization-if-so-when-and-why (accessed 2026-08-28)
15. Russia's Force-Generation Strategy After the Duma Elections — Saratoga Foundation — https://www.saratoga-foundation.org/p/new-report-russias-force-generation (accessed 2026-08-28); and Russia Is Gearing Up for Nationwide Elections — The Moscow Times, 2026-07-02 — https://www.themoscowtimes.com/2026/07/02/russia-is-gearing-up-for-nationwide-elections-this-is-what-you-need-to-know-a93142
16. The Time Is Ripe for Russia-Ukraine Peace Talks, But Putin Could Escalate Conflict — Thomas Graham, Council on Foreign Relations, 2026-07-10 — https://www.cfr.org/articles/the-time-is-ripe-for-russia-ukraine-peace-talks-but-putin-could-escalate-conflict (accessed 2026-08-28)
17. Russia-Ukraine Air Ceasefire Talks: Inside the 2026 Push — Foreign Policy (pk), July 2026 — https://foreignpolicy.pk/russia-ukraine-air-ceasefire-talks-2026/ (accessed 2026-08-28)
18. Russia seeks to 'remove root causes of conflict,' not ceasefire — Lavrov — Kyiv Independent — https://kyivindependent.com/russia-seeks-to-remove-causes-of-conflict-not-ceasefire-lavrov-on-istanbul-talks-with-ukraine/ (accessed 2026-08-28); and Lavrov Rejects Ceasefire and Threatens Ukraine With "Harsher" Russian Strikes — Kyiv Post, August 2026 — https://www.kyivpost.com/post/82360
19. Russia, US Keep Up Working-Level Engagement on Ukraine Settlement: Kremlin — Sputnik India, 2026-08-27 — https://sputniknews.in/20260827/12073006.html (accessed 2026-08-28); and Kremlin says no talks planned with US envoys this week — anews, 2026-08-25 — https://www.anews.com.tr/world/2026/08/25/kremlin-says-no-talks-planned-with-us-envoys-this-week
20. Trends and fluctuations in the severity of interstate wars — Aaron Clauset, *Science Advances* (2018) — https://www.science.org/doi/10.1126/sciadv.aao3580 (accessed 2026-08-28)
21. Durations of wars — freerangestats, 2026-05-13 (Correlates of War replication: median 139 days, mean 408 days) — https://freerangestats.info/blog/2026/05/13/war-durations (accessed 2026-08-28)
22. Introducing the ETH/PRIO Civil Conflict Ceasefire Dataset — Clayton et al., *Journal of Conflict Resolution* (2023) — https://journals.sagepub.com/doi/10.1177/00220027221129183 (accessed 2026-08-28)
23. EU support to Ukraine in 2026: the saga of the reparations loan — Institut Jacques Delors — https://institutdelors.eu/en/publications/eu-support-to-ukraine-in-2026-the-saga-of-the-reparations-loan/ (accessed 2026-08-28)
24. Financing Ukraine in 2026 and 2027 — European Parliament Research Service briefing — https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/779267/EPRS_BRI(2025)779267_EN.pdf (accessed 2026-08-28)
25. Russian Offensive Campaign Assessment, August 12, 2026 — ISW / Critical Threats — https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-august-12-2026 (accessed 2026-08-28)
26. Russian Offensive Campaign Assessment, August 1, 2026 — ISW / Critical Threats — https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-august-1-2026 (accessed 2026-08-28)
27. Russia shows no signs of ceasefire readiness on the battlefield — The New Voice of Ukraine, 2026-08-18 — https://english.nv.ua/nation/russia-shows-no-signs-of-ceasefire-readiness-on-the-battlefield-50633527.html (accessed 2026-08-28)
28. Ukraine war: Russia's wartime economy faces growing pressure — CNBC, 2026-08-15 — https://www.cnbc.com/2026/08/15/ukraine-war-russia-economy-putin-oil.html (accessed 2026-08-28)
29. Russia Cuts 2026 Growth Forecast as Oil Revenues and Wartime Pressures Weigh on Economy — The Moscow Times, 2026-05-12 — https://www.themoscowtimes.com/2026/05/12/russia-cuts-2026-growth-forecast-as-oil-revenues-and-wartime-pressures-weigh-on-economy-a92733 (accessed 2026-08-28)
30. Russia's Budget Bleeds: Oil Revenue Down 30%, War Spending Nears $229 Billion — Kyiv Post — https://www.kyivpost.com/post/79047 (accessed 2026-08-28)
31. Russia downgrades 2026 economic growth forecast to 0.4% from 1.3% — Reuters via Investing.com — https://www.investing.com/news/economy-news/russia-downgrades-2026-economic-growth-forecast-to-04-from-13-deputy-pm-says-4678535 (accessed 2026-08-28)
32. Russia x Ukraine ceasefire by end of 2026? — Polymarket (resolved YES, $14.5M volume) — https://polymarket.com/event/russia-x-ukraine-ceasefire-before-2027 (raw event JSON snapshot in `raw/`, accessed 2026-08-28)
33. Russia x Ukraine ceasefire in 2026? — Manifold Markets, 14.8% — https://manifold.markets/HillaryClinton/russia-x-ukraine-ceasefire-in-2026 (accessed 2026-08-28)

**Date**: 2026-08-28
**Forecast**: Median 9.0%, IQR [6.5%, 13.0%]
**Thesis**: The mutual-agreement machinery works — Russia and Ukraine struck bilateral truces in April and May 2026 [6][7] — so the entire binding constraint is the ≥30-day-intent clause, which requires Putin to abandon the "settlement first" position he has held since 2022 [18]; with the Kremlin telling Bloomberg on 26 August that talks are at a dead end and escalation is coming [10], a 300k–500k mobilisation expected right after the 18–20 September Duma elections [13][15], and Ukraine funded through 2027 by the EU's €90bn loan [23], nothing forces a deal inside the ~six usable weeks left. I sit 3pp under an unusually unanimous Metaculus (CP = Pro = gold = 12.0%) chiefly because the community appears not to be pricing the *effective-by-31-December* clause, and because this is the fifth annual run of a question whose four predecessors all resolved NO after spiking on diplomatic optimism [2][3][5].
