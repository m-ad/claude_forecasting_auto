# Research log — What first round vote share will Iliana Iotova win in the 2026 Bulgarian Presidential election?

## Question mechanics

- **Type**: numeric, `%`. Metaculus range **35–55**, **open at both bounds** (values outside are
  possible and carry tail mass).
- **Resolution source**: the **Bulgarian Central Election Commission** (ЦИК), https://results.cik.bg/
  — the percentage received by Iliana Iotova in the **first round** on **2026-10-25**.
- **Annulment clause**: if the election is postponed or cancelled such that no result is declared
  on or before 2026-12-31, the question is **annulled** (not resolved 0).
- **Edge cases**:
  - CIK reports share of **valid votes cast**; the "I support no one" option on the Bulgarian
    ballot counts as a valid vote and therefore sits in the denominator. This is not a rounding
    detail — in 2021 that option took 2.7% of first-round votes.
  - A second round is scheduled for **2026-11-01**; it is irrelevant to this question.
  - Bulgaria requires **both** >50% of votes **and** ≥50% turnout to win in round one. **No
    candidate has ever done it** — Parvanov took 64.05% in 2006 and still needed a runoff because
    turnout was 42.5%. So "will there be a runoff" ≈ certain (a sociologist quoted in
    dunavmost put it at 99.9%) and tells us *nothing* about whether Iotova clears 50% of votes.

## Political situation (established facts)

| Date | Event |
|---|---|
| 2026-01-23 | Rumen Radev resigns; **Iliana Iotova** becomes Bulgaria's first female president, by Constitutional Court ruling, as VP succeeding to the office |
| 2026-04-19 | **Parliamentary election.** Radev's new **Progressive Bulgaria (PB)** takes **43.91% and 131 of 240 seats** — an absolute majority. GERB–SDS 13.18% (−27 seats), PP–DB 12.42%, DPS 7.01%, Vazrazhdane/Revival 4.19%, MECh 3.18%, Velichie 3.06%, **BSP–OL 2.97% (below threshold — the Socialists lose parliamentary representation for the first time since 1991)**. Turnout **50.70%** |
| 2026 | **Radev becomes Prime Minister** |
| 2026-06-23→07-11 | Global Metrics poll, n=1,503, TAPI face-to-face |
| 2026-07-24 | Iotova announces her candidacy — **by initiative committee, not by party** |
| 2026-07-29 | Election date set: **25 October 2026**, runoff 1 November |
| 2026-08-07 | Radev-government "first 100 days" poll: **Iotova has the highest approval rating of any senior Bulgarian state official** |
| 2026-08-30 | **Borissov (GERB)**: Iotova is "an exceptionally strong candidate", she "outplayed all the politicians" by announcing on her own, she "has outgrown the rest of the political class", and her candidacy "united all the left, socialists, communists". **"GERB does not take part in elections it cannot win"** — GERB will run only to win, not on the Olympic principle. Proposes instead a **unification of the right** |
| 2026-09-01 | **Andrey Gyurov** (former caretaker PM, ex-BNB deputy governor) confirms his candidacy, backed by PP, DB, DSB |
| 2026-09-02 | **Vazrazhdane registers** with the CEC and will field its own ticket; nominee due "within ten days". Sociologist Kancho Stoychev: journalist **Petar Volgin** would be a strong contender if nominated |
| **2026-09-22** | **Candidate registration deadline** |
| 2026-09-25 | Official campaign begins |

## The one poll that exists, read carefully

**Global Metrics, 23 Jun – 11 Jul 2026, n = 1,503, face-to-face TAPI.** Two different questions
were reported and they are routinely conflated:

1. **Support-readiness** ("would you more likely or definitely support X?"): **Iotova ≈ 50%**,
   Gyurov 23%, Daniel Valchev 18%, Ivan Hristanov 12%. **The pollster explicitly warns this
   "is not an election forecast, since the question measures readiness to support a given person,
   rather than choice among mutually exclusive candidates."** The Metaculus background's
   "around half of respondents said they would be likely to support her" is this number, and it
   must **not** be used as a vote-share estimate.
2. **Vote intention by party-of-candidate**, among those planning to vote:

| Candidate's backing | % |
|---|---|
| **Progressive Bulgaria (→ Iotova)** | **39.7** |
| PP–DB (→ Gyurov) | 13.3 |
| GERB–SDS | 11.5 |
| Vazrazhdane | 5.5 |
| **BSP–OL (→ now backs Iotova)** | **4.8** |
| Anticorruption bloc | 4.4 |
| DPS | 3.6 |
| MECh (→ Vasilev) | 2.2 |
| Others | 14.9 |

Sum ≈ 99.9. Separately, 26.4% expressed no preference.

**Iotova's assembled base ≈ 39.7 + 4.8 = 44.5%**, because BSP–OL now formally backs her (she is
listed as the BSP candidate, running via initiative committee with PB, BSP, PDSD, SDP, DNN and
"Изправи се БГ" behind her). That is the honest starting point — not 50%.

## Candidate field (bg.wikipedia, as of 2026-09-05 — incomplete, registration closes 09-22)

Iotova & Kiril Valchev · **Andrey Gyurov** & Georgi Kandev (PP/DB/DSB) · Radostin Vasilev (MECh) ·
Nikolay Nenchev (BZNS) · Ivan Hristanov (Edinenie) · Aleksandar Tomov (BSDE) · Yolo Denev ·
Georgi Dimov · Lachezar Avramov. **Neither GERB nor Vazrazhdane has yet named a candidate.**

## Reference classes considered

| Class | Data | Implication | Kept? |
|---|---|---|---|
| **A. Bulgarian first-round winner shares, 1992–2021** | 44.66 (Zhelev '92) · 44.07 (Stoyanov '96) · 36.39 (Parvanov '01) · 64.05 (Parvanov '06) · 40.11 (Plevneliev '11) · 25.44 (Radev '16) · 49.42 (Radev '21) | median **44.1**, mean 43.5, huge spread | **kept — primary** |
| **B. Incumbent presidents seeking a full term** | Zhelev '92 44.66 · Stoyanov '01 34.95 (lost) · Parvanov '06 64.05 · Radev '21 49.42 | mean ≈ 48.3 | kept |
| **C. Dominant governing party's candidate with a fragmented opposition** | Radev '21: backers (BSP ~10 + ITN ~9.5 + PP ~25.7 of the Nov-2021 vote) → he took 49.42%, a modest over-performance of the assembled base | supports a small positive coattail on 44.5% | kept |
| **D. Party share → presidential share** | PB 43.91% (Apr 2026, turnout 50.7%) vs. Iotova's expected presidential-turnout share | near-parity is the default | kept |
| E. Polling-error class for Bulgaria | 2021 accurate (Radev polled ~48–52, got 49.42); **2016 catastrophic** (Tsacheva led the polls, got 21.96% vs Radev's 25.44%) | σ on the leader's share is large — **≥ 4 pp** | kept for the width, not the centre |

Classes A–D converge on **44–48%**. Class E is why the band is wide rather than tight.

## Decomposition

Start: **44.5%** (PB + BSP–OL vote intention, Global Metrics, late June/early July).

| Adjustment | Reasoning | Δ |
|---|---|---|
| GERB's decision, probability-weighted | P(GERB fields its own) ≈ 0.30 → Iotova ~42–44. P(GERB backs Gyurov / a "united right") ≈ 0.40 → ~45–47 (denominator shrinks less than the consolidation costs her). P(GERB stands aside, voters abstain) ≈ 0.30 → ~47–50. Borissov's 2026-08-30 remarks point hard at *not* running | **+1.5** |
| Presidential turnout is lower than parliamentary (2021: 38.2% vs 40.2%; expect ~35–42% here vs. 50.70% in April) | low turnout in Bulgaria rewards organised machines; PB + BSP is the largest | **+1.0** |
| Six months of governing incumbency by election day; Bulgarian governments shed support fast | offset partly by Iotova's approval being the highest of any senior official | **−1.5** |
| Campaign consolidation of the anti-Radev vote behind Gyurov, plus the risk that Vazrazhdane nominates **Petar Volgin**, who would take sovereigntist/pro-Russian voters otherwise reachable by Iotova's camp | Stoychev names Volgin as able to challenge *both* camps | **−1.0** |
| Undecideds (26.4% no preference) breaking against the establishment candidate | standard, modest | **−0.5** |
| Fragmentation: 9+ tickets, many minor, shaving the "others" pool more than the leader | | **+0.5** |
| **Net** | | **+0.0 → ≈ 44.5**, rounded up for Borissov's public read on her strength and the BSP consolidation → **≈ 45.4** |

**Distribution** (mass by bin):

| Bin | Mass | Cumulative |
|---|---|---|
| < 40% | 13% | 13 |
| 40–43% | 17% | 30 |
| 43–46% | 25% | 55 |
| 46–49% | 21% | 76 |
| 49–52% | 15% | 91 |
| > 52% | 9% | 100 |

→ **median 45.4**, **p25 42.1**, **p75 48.9**. Roughly 1–2% of mass sits below the question's
35 bound and ~2% above 55 — appropriate for open bounds.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-05 | Metaculus #45262 JSON | Numeric, range 35–55, open both ends; CP hidden until 2026-09-10T17:00Z, n=16; comment by tejvn supplies the full 1992–2021 first-round table and predicts Iotova 1st / Gyurov 2nd | sets range and class A |
| 2026-09-05 | en.wikipedia 2026 Bulgarian presidential election | Candidate list; two-round system; "no candidate has ever won in the first round" | mechanics |
| 2026-09-05 | **bg.wikipedia** Президентски избори (2026) | Full 9-ticket list; **Global Metrics vote-intention breakdown** (PB 39.7 / PP-DB 13.3 / GERB 11.5 / Vazrazhdane 5.5 / BSP-OL 4.8 / anticorruption 4.4 / DPS 3.6 / MECh 2.2 / others 14.9); runoff 2026-11-01 | **the core numeric input** |
| 2026-09-05 | **BTA 2026-07-28/29** on the Global Metrics study | Separates the two questions: **~50% support-readiness** vs. **39.7% vote intention**; pollster's explicit warning that the 50% "is not an election forecast" | ↓↓ prevents a 5-pp anchoring error straight out of the question background |
| 2026-09-05 | en.wikipedia 2026 Bulgarian parliamentary election | PB **43.91% / 131 seats**; GERB 13.18; PP–DB 12.42; DPS 7.01; Revival 4.19; **BSP–OL 2.97, below threshold**; turnout 50.70% | class D anchor |
| 2026-09-05 | **Mediapool / BNT / dir.bg / eurocom / Glasove, 2026-08-30**, Borissov | "Iotova is an exceptionally strong candidate", "outplayed all the politicians", "united all the left"; **"GERB does not take part in elections it cannot win"**; proposes uniting the right | ↑ raises P(no GERB candidate) and validates her strength |
| 2026-09-05 | BTA 2026-08-20, Borissov | GERB's candidate decision "will become clear in September"; intended candidate had been Burgas mayor Dimitar Nikolov, "what happened, happened" | GERB in disarray on this |
| 2026-09-05 | BTA 2026-09-01/02, Vazrazhdane | Registered with the CEC; own ticket; nominee within ten days; five names considered as of end-July | open variable |
| 2026-09-05 | **BTA Media Review 2026-09-03** | Stoychev: GERB under pressure to field a candidate, opposition in crisis; **Volgin would be a strong Vazrazhdane contender**; Damyanova: race "unclear" pending GERB's decision; central intrigue = who becomes the main alternative to Iotova's camp | ↓ small, adds the Volgin downside |
| 2026-09-05 | Balkan Insight 2026-09-01 and 2026-08-04 | Gyurov confirms; "Iotova has quite a comfortable lead in polling" (Zlatina Zehirova, Dnevnik) — Balkan Insight direct fetch returned **403**, content via search index | ↑ mild |
| 2026-09-05 | BTA 2026-09-04, Iotova | VP candidate = Kiril Valchev; initiative-committee members announced 8 Sept; pledges not to turn the Consultative Council into a campaign arena | field detail |
| 2026-09-05 | Sofia Globe 2026-07-29 | Election date set for 25 October | mechanics |
| 2026-09-05 | dunavmost — sociologist | "99.9% probability of a runoff" | **not** informative about her share — the ≥50%-turnout rule forces a runoff regardless |
| 2026-09-05 | factcheck.bg / clubz.bg | Fabricated "sociological surveys" and renamed Facebook groups circulating since late August | **treat any un-attributed poll seen from here on as suspect** |
| 2026-09-05 | Alpha Research (Sofia Globe, 2026-03-29) | Pre-election: PB 30.8%, GERB–SDS 21.2% — PB then *outperformed* to 43.91% on 19 April | ↑ Bulgarian polls understated PB by ~13 pp five months ago; a real upside risk here |
| 2026-09-05 | Search: Polymarket / Kalshi / Manifold / politpro on Bulgarian presidential vote share | **No market found** on Iotova's vote share | no external anchor |

## Dead ends and ruled-out hypotheses

- **"Around half would support her" = ~50% vote share.** This is the single most likely error, and
  it is seeded by the Metaculus background itself. It is a support-readiness number the pollster
  explicitly disclaimed as not a forecast.
- **"99.9% chance of a runoff" implies she is under 50%.** No — the ≥50%-turnout requirement forces
  a runoff even at 64% of the vote (Parvanov, 2006).
- **Using the 2016 Radev analogy** (challenger wins from nowhere): the structural position is
  inverted here; Iotova is the establishment/governing-camp candidate, not the insurgent.
- **Social-media polling**: factcheck.bg documents fabricated surveys circulating since late
  August. Ignored anything not traceable to a named agency.
- No prediction market exists on this.

## Open questions to chase next time

1. **Does GERB field a candidate?** Decision due before the 22 September registration deadline —
   worth ±3 pp on its own.
2. **Does Vazrazhdane nominate Petar Volgin?** Due ~12 September. A strong Volgin costs Iotova
   sovereigntist votes.
3. **Any campaign-period poll** from Trend, Gallup International Balkan, Alpha Research, Market
   Links, Myara or Global Metrics with a *named-candidate vote-intention* question.
4. Turnout expectation — the lower it goes, the better for Iotova.
5. Does DPS (3.6%) endorse anyone?

---

## 2026-09-24 — v2 re-analysis log

Metaculus from pre-fetched `raw/metaculus-2026-09-24.json` (not re-fetched). News snapshot in
`raw/news-2026-09-24.json`.

| Date | Source | Finding | Effect |
|---|---|---|---|
| 2026-09-24 | Metaculus JSON | CP 45.45 [42.24, 49.13] n=110; Pro 45.73 [42.79, 48.75] n=10; Gold 45.52 [42.45, 48.73] n=32; 112 forecasters | cohorts agree; ~at v1 median; set after GERB news |
| 2026-09-24 | Metaculus comments | Theomachado: party-bloc → presidential share deltas (+0.4 '06, +0.4 '11, +3.3 or −3.0 '21); Russell-viper: right-skew; DaiLothbrook: 45.4 with Market Links personal-capital note | corroborates ~45–46 |
| 2026-09-24 | BTA 1199851 / Sofia Globe / Novinite | **GERB will not field or back a candidate** (8 Sep) | tripwire fired, +2.0 |
| 2026-09-24 | BTA 1203254 | Borissov (13 Sep): won't vote Iotova; won't harm Gyurov; no one asked GERB | trims GERB effect |
| 2026-09-24 | BTA 1209204 | Vazrazhdane: Kostadinov (P) + Volgin (VP), 22 Sep | partial tripwire, −0.3 |
| 2026-09-24 | en.wikipedia | 27–28 pairs; Iotova backed by PB, BSP-OL, ISBG, VMRO-BND; DPS registered, no candidate; only poll = Global Metrics | fragmentation −0.5, VMRO +0.3 |
| 2026-09-24 | BTA Media Review 23 Sep | 24 nomination committees; GERB+DPS ~700k voters without candidate | context |
| 2026-09-24 | dir.bg / dunavmost / epicenter — Raichev | ~1.1m votes Iotova, Gyurov 450k–540k, turnout < 3m; half of GERB abstains | analysis not poll; ≈40–45%, neutral |
| 2026-09-24 | Investor.bg — Gallup | govt approval 42% after 100 days | approval tripwire not fired |
| 2026-09-24 | Balkan Insight 14 Sep | some GERB members on Iotova's committee | small ↑ |
| 2026-09-24 | Petel.bg — Alpha Research's Dimitrova (6 Sep) | "Iotova enters strong, elections not predetermined"; no numbers | none |
| 2026-09-24 | Octagon / Polymarket | winner market 74% Iotova, **zero volume**; no vote-share market | ignored |
| 2026-09-24 | Searches for Trend / Gallup / Alpha / Market Links / Myara horse-race polls | **none found** | band stays wide |

Dead ends: no DPS endorsement; no September named-candidate poll; Balkan Insight paywalled.

Next time: first campaign poll (campaign starts 25 Sep); whether GERB tacitly helps Gyurov; DPS.
