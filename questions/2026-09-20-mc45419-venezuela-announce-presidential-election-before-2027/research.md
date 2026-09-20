# Research log — Will Venezuela announce a presidential election before 2027? (MC 45419)

All dates ISO. Session date: 2026-09-20. Every number below was fetched live in this
session unless marked otherwise.

---

## 0. Question mechanics

Fetched `raw/metaculus-2026-09-20.json` via the `metaculus-aggregations` skill.
The plain fetch failed (Cloudflare, status 0); `METACULUS_FORCE_TLS12=1` worked.

- `status: "upcoming"`, `nr_forecasters: 6`, `cp_reveal_time: 2026-09-23T17:00Z`.
- **All three cohorts return empty histories** (`recency_weighted`, `metaculus_pros`,
  `gold_medalists` — HTTP 200, 0 history points, `latest: null`). There is therefore
  **no CP, no Pro and no gold number to anchor on or to disagree with**. No comments either.
- `scheduled_close_time: 2026-12-31T23:59Z`.

Resolution criteria, verbatim:

> This question resolves as **Yes** if, before January 1, 2027, Venezuela officially
> announces a new presidential election. In order to count, the announcement must be made
> by a person or entity with the legal authority to do so, the announcement must name a
> specific election date, and voting must be scheduled to take place before January 1, 2028.

Fine print: empty.

Three conjunctive conditions. The third one — **voting scheduled before 2028** — is what
separates this question from the Polymarket contract, which only requires the vote be
scheduled before 2030. Metaculus YES ⊂ Polymarket YES.

Who has "legal authority": under Venezuelan law the **CNE** (Consejo Nacional Electoral)
convokes elections and fixes the date. Art. 233 of the 1999 constitution obliges a new
election within 30 days of a declared *falta absoluta* (absolute absence) of the president —
so a TSJ/AN declaration would also force a dated convocation.

## 1. Situation as of 2026-09-20 (timeline)

| Date | Event | Source |
|---|---|---|
| 2026-01-03 | US operation captures Maduro; extradited, pleads not guilty in US federal court | Wikipedia *2026 US intervention in Venezuela*; Al Jazeera liveblog 2026-01-05 |
| 2026-01-05 | TSJ installs VP **Delcy Rodríguez** as acting president, calling the absence **temporary** (Art. 234), not absolute (Art. 233) — explicitly avoiding the 30-day election trigger | Wikipedia *Next Venezuelan presidential election*; cronica.uno |
| 2026-01-07 | Rubio's three-stage plan: stabilisation → economic recovery/reconciliation → democratic transition | CRS R49186 |
| 2026-02-10 | AN president **Jorge Rodríguez rules out** a new presidential election in the near future | Al Jazeera |
| 2026-04-03 | 90-day mark passes; TSJ declines to re-qualify the absence | Efecto Cocuyo, Acceso a la Justicia |
| 2026-05-23 | **Machado** says she will run again and return from exile before end-2026; estimates ~40 weeks / 7–9 months of preparation for a credible vote | NBC/PBS; CRS R49186 |
| 2026-06-28 | Twin earthquakes, >5,000 dead — first major test of the transition, consumes state capacity | GIS Reports |
| **2026-07-02/03** | **The 180-day maximum for a *falta temporal* expires.** No re-qualification. The acting government is now, on the plain text of the constitution, past its limit | eldiario.com 2026-07-03; CRS R49186 ("exceeded the 180-day period") |
| 2026-08-04/07 | Rubio: transition will take "not years, but certainly months and weeks" | CRS R49186; voz.us |
| 2026-08-06/12 | **Round 1** of US-backed dialogue, Caracas. Government led by Jorge Rodríguez, opposition by **Dinorah Figuera** — *Machado excluded*. Agreement on a process to renew the TSJ + a committee on the CNE | Venezuelanalysis 2026-08-07; CRS R49186 |
| 2026-08-19 | Opposition negotiator **Ramón López**: new CNE this year; *"el cronograma electoral será facultad del nuevo CNE"*; a presidential election "has not been formally discussed" | El Universal |
| ~2026-08-27 | US–Venezuela oil agreement: majority US control of ~1/5 of reserves for a century | Mercopress 2026-09-02 |
| 2026-08-27 | AN approves TSJ-law partial reform in **first reading** | El País (via Metaculus background) |
| **2026-09-02** | **Trump: "I don't think they're ready yet… Delcy wants it, but they are not ready yet."** No timetable | Mercopress, Business Standard, ANI |
| 2026-09-02 | **Delcy Rodríguez**: elections "without a doubt" when the country is ready — *"I don't set the date"* | Bloomberg |
| 2026-09-14 | **Alianza por Venezuela** (9 organisations) demands a "free, fair and verifiable" presidential election with Machado as candidate | Reuters via Metaculus background; Infobae |
| 2026-09-14 | Machado: talks with the State Department "give reasons to believe there will be a new CNE before year-end" | Reporte Confidencial |
| 2026-09-17 | **Round 2** opens (Meliá Caracas), agenda: justice, civil/political guarantees, freedom of expression. Digital-media blocks lifted same day. Machado again absent | CNN Español, Diario Libre, Infobae |
| 2026-09-18 | White House confirms a Trump–Delcy Rodríguez **pull-aside** at UNGA, ~2026-09-22 | ABC News, US News, WSLS |
| 2026-09-19 | Round 2 extended to 2026-09-23; technical committee on freedom of expression; "parity monitoring commission" created. **Nothing on the CNE or a calendar** | Infobae |

Nothing in the record announces, or schedules, a presidential election.

## 2. Outside view

### Class A — post-autocrat transitions, time to a dated presidential election

n ≈ 20 irregular removals of an incumbent autocrat since 1990. Announced a *specific*
presidential election date within 12 months of the removal:

- **YES (~8):** Peru 2000 (weeks), Turkmenistan 2006 (days), Uzbekistan 2016 (days),
  Algeria 2019 (days, annulled, re-announced Sept 2019), Kyrgyzstan 2020 (weeks),
  Bolivia 2019 (~2.5 months), Zimbabwe 2017 (~6 months), Egypt 2013 (~8 months).
- **NO (~12):** Tunisia 2011, Egypt 2011 (~13 months), Madagascar 2009, Sudan 2019,
  Mali 2020, Guinea 2021, Chad 2021, Burkina Faso 2022, Niger 2023, Gabon 2023 (~17 months),
  Syria 2024, Bangladesh 2024 (~16 months).

Raw 12-month base rate ≈ **40%**. But the distribution is strongly **bimodal**: where the
answer is yes it is almost always within *weeks*, because the ruling apparatus wanted a
quick legitimating vote. Venezuela is 8.5 months in with nothing. Conditioning on survival
to t = 8.5 months leaves the ~12 slow cases; of those, roughly **0–1 announced a dated
presidential election in the following 3.5 months**. Conditional hazard for a 3.4-month
window ≈ **1/12 ≈ 8%**.

Scaling check: `P ≈ 1 − exp(−λt)` with the slow-branch λ implied by ~1 announcement per
~3 years of transition gives ~9% over 3.4 months. Consistent.

### Class B — Venezuelan dialogue processes that produced an election

Vatican 2014, Dominican Republic 2016–17, Oslo/Barbados 2019, Mexico/Barbados 2021–23.
**One of four** produced a presidential election (Barbados Oct 2023 → vote 2024-07-28).
Lag from the enabling agreement to the CNE's dated convocation in that one case:
2023-10-17 → 2024-03-05, **≈ 4.5 months**. The mechanical step is fast once the political
decision exists (2024: AN consultation 2026-02-01 → date announced 2024-03-05, ~4 weeks).
Here the enabling agreement (a renewed CNE) does not yet exist.

### Class C — status-quo prior

"Will X change by date D" with D 3.4 months out, no legal deadline, and the actor who
controls X publicly saying no: the status quo is the heavy favourite. Pulls toward ≤10%.

## 3. Inside view — decomposition

**Path A (institutional sequence).** TSJ renewed → new CNE seated → CNE publishes a
*cronograma* naming a presidential election date.

- A1: new CNE designated and sworn by ~2026-12-20 (leaving days to publish a date).
  For: both negotiating sides say "this year"; Machado cites the State Department;
  TSJ-law first reading done 2026-08-27; AN expanded the judicial nominations committee
  in September (JURIST). Against: TSJ is sequenced *first* and is not finished; round 2
  (Sept 17–23) did not touch the CNE; negotiation deadlines slip as a rule.
  **P(A1) ≈ 0.40.**
- A2 | A1: that body names a specific presidential election date before 2027.
  A newly seated CNE normally audits the REP (electoral register — badly degraded, ~8m
  emigrants) before convoking. The political decision is explicitly not taken
  ("not formally discussed" — López). **P ≈ 0.21.**
- A3 | A2: the named date falls before 2027-12-31. Machado's 7–9 months from a December
  announcement lands mid/late 2027; GIS expects the process to begin mid/late 2027.
  A stalling government could name a 2028 date instead. **P ≈ 0.80.**

0.40 × 0.21 × 0.80 = **6.7%**.

**Path B (top-down / legal shock).** The *sitting* CNE also has legal authority, so
Path A is sufficient but not necessary. Triggers: a Trump–Delcy deal (UNGA pull-aside
2026-09-22 or later) producing a public date; a TSJ declaration of *falta absoluta*
(legally overdue since 2026-07-02) forcing an Art. 233 convocation within 30 days;
regime split or mass mobilisation. Each is individually unlikely and the whole legal
architecture since 2026-01-05 exists to avoid the second. **P(B) ≈ 0.04.**

Combined: 1 − (1−0.067)(1−0.04) ≈ **10.4%**.

**Actors and incentives.** Chavismo would lose a free vote badly (2024 tally sheets:
González ~67% vs Maduro ~30%; 2026 polling has Machado at 72% favourable) — Delcy
Rodríguez, Cabello and the military have existential reasons to delay, and no legal
deadline binds them. The US has already collected its prize (the oil agreement) and
Trump has said "not ready"; the external forcing function is largely spent. The faction
of the opposition at the table (Figuera, López) is the weaker one; Machado — who wants
speed — is excluded and still cannot return.

**Disconfirming evidence I went looking for and did not find:** no report of a draft
electoral calendar; no government statement naming a year, let alone a date; no CNE
designation (I checked the National Assembly's own site — the top "new CNE rectors"
page is dated 2023-08-24 and is the Amoroso board, not a 2026 event; a search snippet
claiming a 2026-09-14 designation of the 2021 board was a hallucination and is
**discarded**); round 2's published outcomes contain nothing electoral.

## 4. Other forecasters (all fetched 2026-09-20)

| Source | Value | Criterion | Note |
|---|---|---|---|
| Metaculus CP / Pro / gold | **unavailable** | — | question `upcoming`, CP reveal 2026-09-23, n=6 |
| Polymarket "scheduled by 2026-12-31" | **16.0¢** (bid 15 / ask 17) | date announced, vote before **2030** | $130k volume on this leg, $623k event, liquidity $11.2k |
| Polymarket, same leg, trend | 23% (2026-08-04) → 16% (2026-08-18) → 16% (2026-09-20) | | drifting down, then flat |
| Polymarket Jan-31-2026 / Mar-31-2026 legs | resolved **NO** | | |
| Octagon AI model | **11.4%** vs market 15% (2026-08-18) | Polymarket criterion | independent model, −3.6pp edge vs market |
| Kalshi KXELECTVENEZUELA-27JAN01 | last 5.9¢, bid 2.9 / ask 6.8 | election **held** before 2027 | implausibly high → visible longshot inflation |
| Kalshi KXELECTVENEZUELA-27JUN01 | last 20¢, bid 21 / ask 22 | election **held** before 2027-06-01 | very thin (6-lot trades) |
| Manifold "Presidential Election in Venezuela by EOY 2026?" | 14.8% | held, ambiguous | 37 traders, play money — discounted |
| Manifold "Free & Fair Presidential Election by EOY 2026?" | 8.4% | held | 22 traders — discounted |
| Sentinel Team | no Venezuela election item found | | searched, dead end |

Converting Polymarket to this question's criterion: 16% × P(date < 2028 | announced) ≈
16% × 0.80 ≈ **12.8%**; Octagon's 11.4% × 0.80 ≈ **9.1%**.

Kalshi's 5.9¢ on "election *held* before 2027-01-01" — with no date announced, no CNE and
102 days left — is not a credible 5.9%; true value is ~1%. That calibrates the longshot
inflation on these thin Venezuela contracts at roughly 3–5× at the low end, and argues for
discounting the Jun-2027 leg (21.5%) rather than reading it as a floor.

## 5. Reconciliation

| Method | Value |
|---|---|
| Outside view, conditional hazard (Class A) | 8% |
| Inside-view decomposition | 10.4% |
| Polymarket-derived, longshot-adjusted | ~11% |
| Octagon-derived | 9.1% |
| **Settled** | **9.5%** |

Spread between methods is 8–11pp — no method disagrees with another by more than 3pp,
so no >10pp justification is owed.

## 6. Searches run (phrasings)

EN: "Venezuela presidential election announcement 2026"; "Venezuela Maduro news September
2026"; "Venezuela opposition talks electoral roadmap CNE new council September 2026";
"Venezuela CNE appointment November 2026"; "Trump Venezuela not ready elections";
"Machado Venezuela elections calendar year-end"; "Venezuela electoral calendar 2027
analysts"; "Rubio State Department electoral roadmap timeline"; "Kalshi Venezuela election
scheduled market"; "Sentinel Team weekly forecast Venezuela"; "Trump Delcy Rodríguez UNGA".
ES: "nuevo CNE designación cronograma electoral 2027"; "falta absoluta artículo 233 TSJ
ausencia temporal plazo"; "cronograma electoral anuncio CNE esta semana";
"segunda ronda diálogo Caracas septiembre 2026".

Dead ends: venezuelablog.org "Venezuela Weekly" hit is a 2019 article; venezuelanews
substack "Cronograma electoral en 72h" is 2024; Kalshi web pages return HTTP 429 (used the
API instead); Sentinel has no matching item; Kalshi's own January-2026 blog post (47% for a
vote before 2027) is nine months stale and must not be used.
