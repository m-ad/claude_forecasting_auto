# Research log — How many politicians will leave their cabinet positions in the UK government before 2027?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: **unknown** at v1. Metaculus API (bot key, 2026-09-26) returns
  `resolution_criteria`, `fine_print`, `description` = null; status "upcoming"; open_time
  2026-09-28 17:00 UTC; cp_reveal_time 2026-09-30 17:00 UTC; close 2026-12-31 23:59 UTC;
  scheduled resolve 2027-01-01 12:30 UTC. Tournament: Metaculus Cup Fall 2026 (peer scoring).
  Options: "0", "1", "2", "3 or more". nr_forecasters = 7 pre-open.
- Page scrape (metaculus-scraper) failed: `net::ERR_CERT_AUTHORITY_INVALID` through the proxy.
  Not retried — the API is authoritative that the text is not published yet.
- Likely resolution source once published: GOV.UK ministers page / Wikipedia Burnham ministry.
- Edge cases and ambiguities:
  - Window start: almost certainly question open (2026-09-28). From 1 Jan 2026 it would already
    be 3+ — implausible design.
  - Exit vs. sideways move (R1 vs R2) — weighted 0.75 / 0.25.
  - "Attending cabinet" ministers included? (R1b, weight 0.20).
  - Announcement in Dec effective in Jan.
  - PM himself leaving counts (he is a cabinet member) and triggers 3+.

## Current cabinet (GOV.UK, 2026-09-26)

Full cabinet (23): Burnham (PM), Haigh (First Sec/CDL), Healey (Chancellor), Miliband (Foreign),
Mahmood (Home), Streeting (Defence), Cooper (Health), Norris (Justice), Powell (Education),
McFadden (DWP), J. Reynolds (Business), Rayner (MHCLG), H. Alexander (Transport), Fahnbulleh
(Energy), Nandy (DCMS), Eagle (Defra), Bryant (NI), D. Alexander (Scotland), Kinnock (Wales),
Midgley (Chief Whip), Baroness Smith (Lords), Campbell (Commons), Phillipson (Women & Equalities).
Attending (5): E. Reynolds (CST), E. Reeves (AG), Falconer, Narayan, Pennycook.
First-time cabinet: Norris, Fahnbulleh, Eagle, Bryant, Kinnock, Midgley.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| A. UK cabinet exits in Oct–Dec windows | 24 yrs | 2002–2025 | 0: 42%, 1: 38%, 2: 8%, 3+: 12%; mean ≈ 0.95 | compiled below (Wikipedia ministry pages + recall of well-documented events) | yes, primary |
| B. First ~6 months after a new PM's cabinet | 6 | 2007–2024 | 0: 3, 1: 2, 2: 0, 3+: 1 | same | yes, cross-check |
| A minus planned reshuffles / PM collapses (idiosyncratic) | 24 | 2002–2025 | ≈ 0.6 exits per window | same | yes, λ anchor |

Class A detail (people who ceased to be cabinet members, roughly 28 Sep–31 Dec):
2002 Estelle Morris (23 Oct) · 2003 none · 2004 Blunkett (15 Dec) · 2005 Blunkett (2 Nov) ·
2006 none · 2007 none · 2008 reshuffle 3 Oct (Ruth Kelly, Des Browne) · 2009 none · 2010 none ·
2011 Liam Fox (14 Oct) · 2012 Andrew Mitchell (19 Oct) · 2013 reshuffle 7 Oct (Michael Moore) ·
2014 none · 2015 none · 2016 none · 2017 Fallon (1 Nov), Patel (8 Nov), Green (20 Dec) ·
2018 Raab, McVey (15 Nov) · 2019 Alun Cairns (6 Nov) · 2020 none · 2021 Lord Frost (18 Dec) ·
2022 Kwarteng, Braverman, Truss, Sunak's 25 Oct clear-out, Williamson (8 Nov) → 3+ ·
2023 Braverman, Coffey, Quin (13 Nov reshuffle) → 3+ · 2024 Louise Haigh (29 Nov) ·
2025 none found (searched; Rayner resigned 5 Sep 2025, outside window).
Caveat: compiled partly from memory; the Wikipedia "List of resignations from government"
UK section ends in 2010 and the IfG resignations data-vis returned 403. A missed minor
attending-cabinet exit would shift "0" down by ~4pp per year corrected.

## Decomposition

count = Poisson(λ_idio) + regime tail.
- λ_idio = 0.62 for ~95 days (0.6 base × ~1.05: new-cabinet vetting risk + Budget + open split,
  offset by honeymoon + Burnham backing Mahmood + Rayner cleared).
- Regime tail 5%: planned reshuffle ~2%, PM falls / gilt-crisis clear-out ~3% (Polymarket PM-out
  6.3% thin → ~3%). Tail mass puts 90% on 3+, 10% on 2.
- Readings: R1 0.55, R1b (λ×1.2) 0.20, R2 cascade 0.25.
- Mixture: 49.9 / 28.1 / 12.1 / 9.9 → published 50 / 28 / 12 / 10.
- Model script kept in the session scratchpad only (not committed; numbers reproduced in
  forecast.md scenario and sensitivity tables).

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-26 | Metaculus API post 45250 | criteria null, upcoming, CP hidden to 09-30, n=7 | criteria ambiguity priced in |
| 2026-09-26 | "UK cabinet reshuffle September 2026" | Starmer→Burnham transition; shadow cabinet reshuffle (Cleverly quit 29 Aug) — opposition, irrelevant | context |
| 2026-09-26 | Wikipedia 2026 Labour leadership crisis | Local elections 7 May; Streeting quit 14 May; Healey quit 11 Jun; Makerfield by-election 18 Jun; Starmer resigned 22 Jun; Burnham unopposed 16–17 Jul, PM 20 Jul | window starts in a new, fresh cabinet |
| 2026-09-26 | Wikipedia Burnham ministry + GOV.UK ministers | 23 full + 5 attending; 15 dismissed at formation; no changes since | base cabinet |
| 2026-09-26 | IfG "Six things…" (29 Jul) | 82 ministers took new roles; 24 new to government | new-team vetting risk |
| 2026-09-26 | IfG ministers resigning explainer (12 Jun) | Starmer govt had 20 resignations — record for tenure stage | high-turbulence era, but pre-Burnham |
| 2026-09-26 | Burnham snap election | Ruled out (Bloomberg 2 Jun); petition rejected 24 Aug | no election churn |
| 2026-09-26 | Labour conference 2026 | Liverpool, starts ~27 Sep; Burnham "undisputed star" (ITV 25 Sep) | honeymoon |
| 2026-09-26 | Rayner HMRC | Cleared, no penalty, 14 May 2026 | removes tail |
| 2026-09-26 | Mahmood vs Burnham | ~80 MPs asked to water down reforms; Burnham backed Mahmood (HuffPost); Rayner condemned Mahmood's care-worker settlement rule 26 Sep, Nandy defended | small ↑ |
| 2026-09-26 | Healey Budget | 28 Oct 2026; gilts 30y 5.89% (1 Sep, highest since 1998), 10y ~5.22–5.25%; headroom £26bn→~£13.8bn (Deutsche est.); borrowing overshoot £3.5bn | ↑ Chancellor/regime risk |
| 2026-09-26 | Streeting at Defence | Seen as Burnham containing chief rival (Newton Dunn); Dannatt criticism | minor |
| 2026-09-26 | Fahnbulleh | private-school "hypocrisy" story (LBC) | tiny ↑ |
| 2026-09-26 | Heidi Alexander | only routine reappointment coverage; NATS air-traffic outage 21 Sep put pressure on the NATS chief, not on her; no reason found for her 9.2% Polymarket price | none |
| 2026-09-26 | Ministerial code investigations | nothing on a Burnham cabinet minister; FDA letter urging independent process | none |
| 2026-09-26 | Ipsos 10–15 Sep | Labour +4 over Reform; Burnham favourability 40% (+8) | ↓ |
| 2026-09-26 | Polymarket gamma API | "First to leave Burnham Cabinet" (to end-2027): Healey 13.5, Fahnbulleh 10.4, H. Alexander 9.2, Cooper 6.2, Miliband 5.9 … Mahmood 2.4, Bryant 2.2; $114k vol. "Burnham out by Dec 31" 6.3% ($8k) | cross-check only |
| 2026-09-26 | Manifold API | Q4-2026 any cabinet resignation 41%; Burnham cabinet resignation in 2026 40% (5 bettors) | consistent, discounted |
| 2026-09-26 | "Burnham mini reshuffle expected after budget" | nothing found | ↓ reshuffle tail |

## Submissions to Metaculus

| Date (UTC) | Version | Values submitted | Account | Note |
|---|---|---|---|---|
| 2026-09-26 17:35 | v1 | 0: 0.50, 1: 0.28, 2: 0.12, 3+: 0.10 | bot key (author_id 309213) | operator-requested; POST /api/questions/forecast/ q=45442 → HTTP 201, confirmed in `my_forecasts`; placed while question still "upcoming" |

## Dead ends and ruled-out hypotheses

- Metaculus page render: TLS error through proxy (not a Metaculus 403).
- IfG data-visualisation page: 403.
- Wikipedia "List of ministerial resignations in the United Kingdom" / "List of resignations
  from the British Cabinet": 404.
- Kalshi, GJOpen, INFER, Sentinel, Mantic: no matching question found (Kalshi not queried by
  API; search only).

## Open questions to chase next time

- Read the published resolution criteria (2026-09-28): exits vs moves; attending cabinet;
  start date; announcement vs effective date.
- Metaculus CP / Pro / gold at reveal (2026-09-30).
- Budget reception 28 Oct: gilt moves, any cabinet dissent.
- Why is Heidi Alexander priced 9% on Polymarket's first-to-leave? (Possible rumour I missed.)
- Greater Manchester mayoral by-election — does any minister want the job?

## Update log — 2026-10-02 (v3)

Metaculus snapshot pre-fetched by the parent session (`raw/metaculus-2026-10-02.json`, 14:45 UTC);
no Metaculus endpoint called from this run.

| Date | Search / source | Finding | Effect |
|---|---|---|---|
| 2026-10-02 | Metaculus 45250 snapshot | Criteria unchanged; n=68. CP 0: 64.6 · 1: 24.1 · 2: 7.3 · 3+: 4.0 (IQR on 0 [59.7, 68.2]); Pro (n=8) 60.4/24.9/9.5/5.1; gold (n=26) 62.6/25.3/9.1/3.0. 3 comments (Koboh, DeRuina, Theomachado 63/20/12/5); DeRuina flags triple-lock split + mini-reshuffle path; no admin ruling on sideways moves | tripwire 1 not fired; cohorts lower on 3+ |
| 2026-10-02 | GOV.UK ministers page | All 18 listed posts held by fine-print incumbents; no vacancies | count = 0 |
| 2026-10-02 | Wikipedia Burnham ministry | No changes since 20 July; no scandals/investigations listed | count = 0 |
| 2026-10-02 | Mahmood settlement reforms | 28 Sep: signalled retreat on retrospective 5→10/15y ILR (BBN Times); Rayner "un-British", forced climbdown (BritBrief 29 Sep); Burnham "Team Angela and Shabana"; Rayner: collective responsibility "not dead", "do politics differently" (HuffPost) | ↓ resignation risk |
| 2026-10-02 | Triple lock | Burnham 29 Sep speech: scrap triple lock in 2030 to fund free social care; Powell (deputy leader, Education) told Sky/LBC party "absolutely committed" just before; D. Alexander equivocal; Phillipson (not on list) warned of "intergenerational warfare"; Unite hostile. No resignation threats | small ↑ |
| 2026-10-02 | Gilts | 30y touched ~6.03% on 1 Oct (highest since 1998), back below 6% on 2 Oct (AOL / Trading Economics snippets; roic.ai 403) | tripwire 3 approaching, not fired |
| 2026-10-02 | Healey conference speech | Fiscal rules "in lockstep" with PM; £6bn shipyard contracts; Budget 28 Oct confirmed | no Treasury rift |
| 2026-10-02 | Defence funding row (The Lead) | Pressure over Defence Investment Plan funding into Budget; Burnham resisting welfare cuts to fund it | small ↑ (Streeting/Healey) |
| 2026-10-02 | Conference commentary (Inside Croydon) | Criticism came from sacked ex-ministers (Kyle, Reed), not from the 18 | none |
| 2026-10-02 | Fahnbulleh | Conference speech, devolving Warm Homes Plan; no row found | none |
| 2026-10-02 | Cooper | Routine coverage (Sure Start, care workforce); no pressure story behind her Polymarket rise 6.2→10.5% ($1.7k vol) | ignored |
| 2026-10-02 | Independent Adviser referrals | None found for any Burnham cabinet minister | tripwire 2 not fired |
| 2026-10-02 | Reshuffle speculation | None found | ↓ planned-reshuffle mass 2%→1.5% |
| 2026-10-02 | Polymarket gamma API | Burnham out by Dec 31: 6.3% (bid 5.7/ask 6.9, ~$8k) flat; first-to-leave (to end-2027, $126k): Healey 13.5, Cooper 10.5, Fahnbulleh 10.45, Miliband 6.65 | tripwire 4 not fired |
| 2026-10-02 | Manifold API | Q4-2026 any cabinet resignation 41% (9 bettors); Burnham cabinet resignation in 2026 40% (5 bettors) | unchanged |

### Cascade re-check (prompted by cohort 3+ at 3–5% vs my 11.5%)

Single senior exits since 2017 and whether they triggered a sideways move among senior posts
(from memory of well-documented events; not re-sourced this session — flag as recall):
Fallon 2017 → Williamson from Chief Whip (not a "top 18"-equivalent post) — no; Patel 2017 →
Mordaunt from outside cabinet — no; Green 2017 → Lidington (Justice→CDL), Gauke (DWP→Justice) —
yes, 3 total; Rudd 2018 → Javid (Housing→Home), Brokenshire in — yes, 2 total; Rudd 2019 → Coffey
from outside — no; Kwarteng 2022 → Hunt from backbenches — no; Braverman 2022 → Shapps from
outside — no; Raab 2023 → Chalk from outside — no; Haigh 2024 → H. Alexander from outside — no;
Rayner 2025 → full reshuffle — yes, 3+. So ~3/10 cascade, and cascades often reach 3+. Kept
cascade p = 0.30, trimmed "adds two" share 60%→40%.

### Model (v3)

λ = 0.50 over 2–31 Oct–Dec (90 days); cascade p 0.30 (+1: 60%, +2: 40%) → 0: 60.7 · 1: 21.2 ·
2: 9.2 · 3+: 8.9; regime 4.5% (1.5% planned reshuffle → 3+; 3% PM change split 40/30/15/15) →
0: 59.1 · 1: 21.2 · 2: 9.2 · 3+: 10.5 → published 59.0 / 21.5 / 9.0 / 10.5.

### Open questions to chase next time

- Budget 28 Oct: gilt reaction, any cabinet dissent (Streeting on defence funding; Powell on
  pensions), any post-Budget mini-reshuffle talk.
- Mahmood's formal settlement consultation response (autumn) — does Burnham overrule her?
- Any admin comment on whether sideways moves count.

## 2026-10-16 (v4 update)

- Metaculus pre-fetched snapshot (`raw/metaculus-2026-10-16.json`, 01:06 UTC): CP 64.8/24.2/7.0/4.0 (n=93), Pro 68.9/21.2/5.9/4.0 (n=9), gold 64.4/24.1/7.4/4.0 (n=29). Three new comments (VectorWright 11 Oct, DaiLothbrook 12 Oct, Vlad25 13 Oct): no new facts.
- GOV.UK ministers (WebFetch 16 Oct): same 18 in same roles, no vacancies. Wikipedia "Premiership of Andy Burnham" (edited 13 Oct): no cabinet changes since 20 July; items on early prisoner releases, Russia/Brexit claim, EU ties, "Burnham Bounce" polling (9 Oct).
- Healey/Burnham letter to cabinet: no new money, fund pledges within budgets (Times via Devdiscourse; Express & Star 403). Budget still 28 Oct. CGT rise not ruled out.
- 30y gilt ~6.034% reported 7 Oct (roic.ai, 403 on fetch, snippet only). No evidence of >6.25%.
- Polymarket gamma API: Burnham out by Dec 31 = 6.05% (5.2/6.9), $31k vol. First-to-leave: Healey 13.5, Fahnbulleh 10.35, D. Alexander 6.55, Powell 5.4, McFadden 4.25, Cooper 4.45; nobody resolved.
- Searches with no hits: October cabinet resignation; Independent Adviser referral of Burnham ministers; Mahmood/Rayner/Fahnbulleh split in Oct; Powell triple-lock follow-up after conference.
- Model: λ 0.50 → 0.44 (decay less than proportional, Budget ahead) +0.01 (spending letter) = 0.45; cascade 0.30 (60/40); reshuffle 1.2%, PM change 3%. Result 62.3/20.1/8.4/9.1 → 62.5/20/8.5/9.
