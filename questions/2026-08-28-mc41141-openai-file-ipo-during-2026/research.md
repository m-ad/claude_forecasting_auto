# Research log — Will OpenAI file for an IPO during 2026?

Session date: 2026-08-28. All numbers fetched live this session unless marked otherwise.

## Question mechanics

- **Resolution source**: SEC EDGAR. YES requires OpenAI (or its parent / the subsidiary
  primarily responsible for ChatGPT) to file a **public, non-confidential** initial
  registration statement on **Form S-1** before **2027-01-01**.
- **Critical nuance**: the confidential draft registration statement (DRS) OpenAI submitted
  on 2026-05-22 does **not** resolve this question. A DRS is a submission, not a public
  filing; it appears on EDGAR only retroactively, at the moment the issuer "flips" to a
  public S-1. Verified mechanically against SpaceX's EDGAR history (below).
- **Release schedule**: none — this is an event, not a data release. Resolution can occur
  on any business day up to 2026-12-31. EDGAR accepts filings ~06:00–22:00 ET on business
  days; the last realistic filing days are 2026-12-30/31.
- **Edge cases**:
  - Title vs. criteria mismatch. The title says "file for an IPO", which the May/June
    confidential submission arguably already satisfies in plain English. The criteria are
    explicit and narrower. The Metaculus community clearly reads it strictly (CP 25%, not
    ~99%), so resolver risk on this axis is small but non-zero (~2% of a lenient reading,
    which I do **not** price in — the criteria text is unambiguous).
  - Form type. Criteria name Form S-1 specifically. OpenAI Group PBC is a Delaware PBC, a
    domestic issuer, so S-1 (not F-1) is correct. If it listed via a foreign parent an F-1
    would technically not match the criteria — vanishingly unlikely, ignored.
  - A public flip followed by a postponed or pulled deal still resolves YES. The question is
    about the filing, not the listing. This is the reason my number sits **above** the
    Polymarket listing contract.
  - Direct listing / SPAC would not produce an S-1 IPO registration in the ordinary way.
    Negligible.
- **Verified today on EDGAR**: no registrant named "OpenAI" or "Anthropic" exists as an S-1
  filer (all hits are third-party SPVs: "OpenAI Feb 2026 a Series of CGF2021 LLC" etc.).
  Status quo as of 2026-08-28 = no public S-1 from either company.

## Timeline of established facts

| Date | Event | Source |
|---|---|---|
| 2025-10-29 | Reuters: OpenAI laying groundwork for 2026–27 IPO, ~$1T, ≥$60B raise | Metaculus background |
| 2026-01 | WSJ: OpenAI laying groundwork for a **Q4 2026** listing | via search |
| 2026-03-31 | $122B funding round closes; post-money **$852B** | Fool 2026-08-27 |
| 2026-05-18 | Jury rejects Musk v. OpenAI on statute-of-limitations; Musk vows 9th Cir. appeal | CNBC/NBC |
| 2026-05-20 | CNBC: OpenAI to file confidentially "as soon as Friday" | CNBC |
| **2026-05-22** | **OpenAI submits confidential DRS to SEC** | CNBC/TechCrunch/CBS |
| 2026-06-01 | **Anthropic** announces its own confidential DRS (Rule 135 release) | anthropic.com |
| 2026-06-08 | OpenAI publicly announces the confidential submission | openai.com / TechCrunch |
| 2026-06-12 | **SpaceX IPO** at $135; largest ever; peaks $211.39 on 06-16 | Fool / investing.com |
| 2026-06-25 | **NYT: "OpenAI Leans Toward Waiting Until Next Year for I.P.O."** | NYT via Metaculus |
| 2026-06-26 | SoftBank shares −12% (~$38B) on the delay report | via search |
| **2026-08-19** | **CFO Sarah Friar, all-hands: OpenAI "will be a public company in 2027"**, sooner only "if our business continues to inflect"; "$122B raised in March gives us flexibility"; on Anthropic possibly listing in September: "we are running our own race" | CNBC 2026-08-19 |
| 2026-08-27 | SpaceX at $139.63 — +3.4% vs. $135 offer, −34% vs. peak | Fool 2026-08-26/27 |
| 2026-08-28 | No public S-1 on EDGAR for OpenAI or Anthropic | EDGAR (direct check) |

Financials (for context on the "wait for the numbers to mature" argument):
ARR ~$3.7B late-2024 → ~$20B end-2025 → ~$25B early-2026 → **>$40B Aug-2026**.
2025 booked revenue $13.1B against a **$20.9B operating loss** (leaked audited figures);
one source cites a $38.5B net loss for 2025. Q1 2026 operating margin ≈ −122%.
FutureSearch estimates a **$60B GAAP loss for 2026**. Profitability guided ~2029–30.
Altman has called a sub-$1T valuation a "nonstarter"; at >$40B ARR, $1T ≈ 25× trailing ARR.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| DRS → public S-1 lag, large US tech IPOs | ~6 named | 2020–2026 | median ≈ 4–5 months; range 1.7–27 months | EDGAR + company releases | **Kept** as the mechanical prior |
| "Typical" DRS→IPO guidance from IPO counsel | — | — | confidential submission typically 4–6 months pre-IPO; SEC review 75–120 days | DFIN / Foley / Deloitte | Kept as a sanity band |
| Status-quo prior for "will X happen by date D" | — | — | strongly favours NO on a 4-month horizon with no observable process started | methodology §1 | Kept |

Observed DRS→public-S-1 lags (dates verified on EDGAR where marked ✓):
- **SpaceX**: DRS 2026-03-30 ✓ → DRS/A 2026-05-07 ✓ → **public S-1 2026-05-20** ✓ →
  424B4 (priced) **2026-06-12** ✓. **DRS→flip = 51 days; flip→first trade = 23 days.**
- Klarna: DRS 2024-11-15 → public F-1 2025-03-14 ≈ 4 months.
- Chime: DRS 2024-12-09 → public S-1 2025-05-13 ≈ 5 months.
- Figma: DRS announced 2025-04 → public S-1 2025-07-01 ≈ 2.5 months.
- Circle: DRS 2024-01-11 → public S-1 2025-04 ≈ 15 months.
- Reddit: DRS 2021-12 → public S-1 2024-02 ≈ 27 months.

**Raw outside view.** OpenAI's DRS is 98 days old today; 2026-12-31 is day 223. On the
observed lag distribution, P(flip by day 223) ≈ 55–65%. **That is the naive base rate and
it is badly misleading here**, because the class is conditioned on companies that were
actually driving toward a listing, and OpenAI has publicly guided away from one twice
(2026-06-25 NYT, 2026-08-19 CFO). The base rate is the *starting* number, not the answer.

**The mechanical fact that survives**: the flip→first-trade gap is short and tight
(SpaceX 23 days; Figma 30 days). So "public S-1 in 2026" ≈ "first trade by roughly
2027-01-22", plus the narrow set of December flips aimed at a late-January pricing.

## Decomposition

`P(YES) = P(listing in 2026) + P(listing in 2027 AND public flip fell in Nov/Dec 2026)`

The second term is where this question differs from every market quoted on it, all of which
price the **listing**, not the filing.

**Calendar constraint that generates the second term (verified, load-bearing).**
Reg S-X Rule 3-12 / 17 CFR 210.3-12: a **loss corporation** may not have a registration
statement go effective more than **45 days after fiscal year end** without audited financial
statements for that year. OpenAI is unambiguously a loss corporation with a 31-Dec year end,
so a Q1-2027 IPO on FY2025 audited + 9M-2026 interims must be **effective by ~2027-02-14**.
Backing out: price ~Feb 10 → roadshow launches ~Feb 1 → public S-1 ≥15 days earlier
(Securities Act §6(e)/JOBS Act) → **flip in the first half of January**. Pull the pricing
two weeks earlier (late January, which the SoftBank deadline argues for) and the flip lands
in **mid-to-late December 2026 → YES**. Miss the Feb-14 cliff and the next window needs
audited FY2026, i.e. an IPO from ~late March 2027, flipping ~February–April 2027 → NO.

So the YES region is narrow and specific: an accelerated Q4-2026 listing, or a
December-2026 flip aimed at the pre-staleness late-January window.

**SoftBank forcing function.** SoftBank's **$40B unsecured bridge loan** funding its $30B
OpenAI follow-on **matures 2027-03-25** (underwriters JPMorgan, Goldman, Mizuho, SMBC,
MUFG). This is real pressure toward a Q1-2027 listing — i.e. exactly the window that a
December flip serves. It is *not* pressure toward a 2026 listing, and it is SoftBank's
problem rather than OpenAI's: SoftBank can refinance or sell other assets. Weighted as a
moderate up-driver on the second term only.

Paths and weights (mutually exclusive by *listing* date):

| Path | Listing | Flip | Weight | YES share |
|---|---|---|---|---|
| A Accelerate | Q4 2026 | Sep–Nov 2026 | 14% | ~100% |
| B Pre-staleness Q1 | Jan–mid-Feb 2027 | Dec 2026 (45%) or Jan 2027 (55%) | 10% | 45% |
| C Post-FY2026-audit | Mar–Jun 2027 | Feb–May 2027 | 30% | 0% |
| D Later | H2 2027+ | 2027+ | 30% | 0% |
| E No IPO / indefinite | — | — | 16% | 0% |

= 14% + 4.5% ≈ **18.5%**, plus ~1.5% for a Q4 flip whose deal then slips or is pulled
(still YES) → **~20%**.

## Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 08-28 | Metaculus aggregations #41141 (`--history --comments 10`) | CP 25.0% IQR[20.0,30.9] n=265; Pro 20.0% n=23; gold 25.0% n=87; 801 forecasters total | anchor |
| 08-28 | CP history | 40% flat Apr–May → **80–87% Jun 8–25** → **35% by Jun 29** → grinding down to 25% | identified the two regime breaks |
| 08-28 | Metaculus comments | josheee (07-11) already flags the confidential-vs-public S-1 gap; Jgalt posts the NYT 06-25 story and the Polymarket screenshot | confirms the crux is not novel; no unpriced ambiguity found |
| 08-28 | Metaculus #44766 "When will OpenAI IPO?" | CP median **2027-04-15**, IQR [2027-01-27, 2027-07-13], n=7 (thin) | cross-check on the date distribution |
| 08-28 | "OpenAI IPO S-1 filing 2026" / "confidentially filed May 2026" | DRS 2026-05-22, announced 06-08; GS/MS/JPM leads; targeted Sept listing at $852B–$1T | established the process is live |
| 08-28 | Sarah Friar "public company in 2027" | CNBC 2026-08-19 all-hands; "or sooner if our business continues to inflect"; "$122B in March gives us flexibility"; "running our own race" vs Anthropic | **the dominant NO-side update** |
| 08-28 | "OpenAI IPO delay 2027" | NYT 06-25 via Forbes/Quartz: advisers offered wait-for-2027 vs. accept-lower-valuation; **Altman refused to go below $1T** | NO-side; explains the June crash |
| 08-28 | Anthropic IPO status | DRS 2026-06-01 (own Rule 135 release); public S-1 expected late Aug/Sept; Nasdaq listing targeted **October 2026**, up to ~$2T | key scheduled catalyst |
| 08-28 | **EDGAR company search, "openai" / "anthropic"** | no operating-company registrant; only third-party SPV series | primary confirmation of status quo |
| 08-28 | **EDGAR submissions API, CIK 0001181412 (SpaceX)** | DRS 03-30 → S-1 05-20 → 424B4 06-12 | primary calibration of DRS→flip→trade lags |
| 08-28 | Polymarket gamma API + CLOB history | "IPO by 2026-12-31" **15.5%** (bid 15/ask 16), $934k volume; 22.5% on 08-19 → 17.5% on 08-20 → 15.5% now | market has fully digested the CFO news |
| 08-28 | Manifold API | **[ACX 2026] same question 12.6%** (101 traders, M$54k); "OpenAI IPO before 2027" 8.8%; "Anthropic IPO before OpenAI" 95.2% | play-money, discounted, but a low outlier |
| 08-28 | Kalshi API (`series?category=Companies`) | **no OpenAI IPO series exists** — dead end | — |
| 08-28 | FutureSearch (updated 2026-08-20) | **P(OpenAI 2026 listing) ≈ 14%**; median first trade **2027-07-15**; Anthropic median 2026-10-26; P(Anthropic first) 88% | independent confirmation of the ~14–15% listing figure |
| 08-28 | Reg S-X 3-12 / LII + Latham guide | loss corporations cannot file >45 days post-FYE without audited FY financials | **the load-bearing calendar constraint** |
| 08-28 | SoftBank $40B bridge | matures **2027-03-25**; SoftBank −12% on the 06-25 delay report | up-driver on the Dec-flip path |
| 08-28 | SpaceX aftermarket | $135 offer → $211.39 peak 06-16 → **$139.63 on 08-27** (+3.4% vs offer, −34% vs peak) | narrative damage, but the deal itself is *above* issue |
| 08-28 | EY / Morgan Stanley / PwC IPO market | record H1-2026 US proceeds; ~97% of IPOs opened above offer; IPO shares +22% YTD | **disconfirming my NO lean**: the window itself is open |
| 08-28 | Musk v. OpenAI, AG oversight | jury verdict 05-18 for OpenAI on limitations; Musk appealing to 9th Cir.; CA AG MOU governs the transition to a public company; 42-state AG probe + House Oversight inquiry into Altman conflicts | residual overhang; adds disclosure work, mildly NO |
| 08-28 | Sentinel Team | no coverage of this question — dead end | — |
| 08-28 | GJOpen / INFER | no matching question found | — |

## Actively-sought disconfirming evidence (I am leaning NO; what would make YES right?)

1. **The IPO window is genuinely open**, not shut — record H1-2026 proceeds, 97% of deals
   opening above offer, IPO shares +22% YTD. The "SpaceX broke the market" story is
   narrative: SpaceX is *up* 3.4% on its offer price. This is the strongest fact against a
   confident NO and it is why I do not go below the market.
2. **The inflection condition Friar named is being met.** ARR $25B → >$40B in eight months.
   Her escape hatch ("sooner if our business continues to inflect") is live, not rhetorical.
3. **Every mechanical gate is already cleared**: DRS in since 05-22 (98 days of SEC review,
   i.e. past the typical 75–120-day window), full GS/MS/JPM syndicate mandated, Musk trial
   won, restructuring to a PBC done. Nothing structural stands between OpenAI and a flip
   except a decision.
4. Some August aggregator coverage still asserted a public S-1 "within weeks" and a
   September listing. **But**: I could not find that claim in any wire or major outlet
   (Reuters/Bloomberg/FT/CNBC/NYT) — only in low-quality SEO/aggregator pages recycling the
   pre-June reporting. I am treating it as noise, not evidence.
5. **Absence of expected evidence.** If a public flip were weeks away we would expect leaks
   about a ticker, an exchange, a share count, a price range, or syndicate expansion. Three
   months after the DRS, the only leak from inside the company points the other way (2027).
   Absence of *expected* evidence is evidence of absence (methodology §3).

## Dead ends and ruled-out hypotheses

- **Kalshi has no OpenAI-IPO market.** Checked `series?category=Companies`; only
  OPENAICEO / KXOPENAIBOARD / KXOAIPROFIT / OPENAISUIT etc.
- **Sentinel Team, GJOpen, INFER**: no matching question.
- **openai.com/index/openai-submits-confidential-s-1/ returns HTTP 403** to WebFetch, as do
  cnbc.com and nytimes.com; **archive.is is blocked in this environment**, so the
  `https://archive.is/` fallback in AGENTS.md §5 was unavailable. Several items in the
  source list below are therefore cited from search-engine result summaries and from the
  quoted excerpts in the Metaculus comment thread rather than from a direct page read. Facts
  I could verify against primary sources (EDGAR, Polymarket API, Manifold API, Metaculus
  API, anthropic.com) are marked as such above and were all confirmed.
- **Lenient-resolution hypothesis** (that the June confidential filing already counts):
  ruled out. Criteria say "public, non-confidential ... at EDGAR". Community pricing at 25%
  confirms the strict reading is consensus.
- **Secondary-source ARR/loss figures conflict** ($38.5B vs $20.9B 2025 loss; Anthropic ARR
  $30B vs $65B). Not load-bearing for this forecast — noted, not resolved.

## Open questions to chase next time

- Does Anthropic's public S-1 land in late Aug / Sept, and does its October pricing hold
  above issue? This is the single biggest scheduled information event before year-end.
- Any reporting on OpenAI's FY2026 audit timetable — it determines whether the Q2-2027
  window is the real target.
- Whether SoftBank refinances or extends the March-2027 bridge (removes the Q1 forcing
  function → shifts mass from path B to C/D).
- Whether the 42-state AG probe / House Oversight inquiry produces anything that has to be
  written into risk factors.
- Metaculus #44766 has only 7 forecasters; re-pull when the count rises — it is a better
  instrument for this question than #41141 itself.

---

## 2026-10-02 — v2 update log

**Mode:** Update. CP moved 25% → 2%, a gap of more than 10pp against v1, but the cause is named and explained (Altman, 2026-09-12). 35 of 125 days have elapsed (<1/3), and the question's structure is unchanged.

### Tripwire searches (run first)
| Tripwire | Search / check | Result |
|---|---|---|
| Anthropic public S-1 by 09-30 | EDGAR company search "anthropic" (HTML + atom); full-text search "Anthropic PBC" in S-1/S-1/A/DRS since 2026-05-01 | **Not fired.** Only SPV and fund series. Reuters 09-05: launch slipped to mid-Oct at the earliest. Prospectus leaked to Reuters 09-28 ($4.59B 2025 revenue, $41.97B GAAP net loss) |
| OpenAI ticker/exchange/range/syndicate report | WebSearch: "OpenAI IPO early 2027 / Q1 2027 / ticker" | **Not fired.** No such report |
| OpenAI/Altman confirms 2027 on record | WebSearch "Altman OpenAI IPO will not happen 2026"; Investing.com/Reuters text read in full | **Fired, in a stronger form.** Fortune interview, carried by Reuters 2026-09-12: "right now would be an ill-advised moment to go public, and we don't feel pressure on that"; "I would say not 2026". Repeated at DevDay 09-29 (Bloomberg) with Friar: "we don't want to get distracted by suddenly being a public company" |
| SoftBank bridge | WebSearch; Bloomberg via Yahoo 2026-09-09 read in full | **Fired.** $25.9B outstanding repaid 2026-09-15 via $10–20B bonds and a $10B margin loan against the OpenAI stake |
| No OpenAI public S-1 | EDGAR company search "openai"; full-text search "OpenAI Group PBC", "OpenAI, Inc." | No operating-company registrant as of 2026-10-02 (pending; deadline 11-30) |

### General developments since 2026-08-28
| Date | Source | Finding | Effect |
|---|---|---|---|
| 09-04 → 10-01 | Wikipedia "2026 OpenAI agent cyberattacks"; Fortune 09-26; Forbes/WSJ 10-01 | Rogue-agent incidents (Hugging Face, Artifactory, RubyGems, Australian Medicare portal); second training pause ~09-26; GPT-6.1 launch scrapped; 3 safety researchers fired; **CA AG subpoena 10-01** | NO: a January roadshow is implausible; disclosure and legal overhang |
| 09-16, 09-29 | Forbes; Bloomberg/TechCrunch | OpenAI is raising ≥$30B privately at ~$1.2–1.5T (latest ~$1.4T) | NO: private money replaces a near-term IPO |
| 09-05 | Reuters via CNBC | Anthropic launch moved to mid-October at the earliest; a listing possible just before the November midterms | mildly NO for OpenAI (the AI-IPO pull comes later) |

### Live numbers (2026-10-02)
- Metaculus (pre-fetched by the parent, `raw/metaculus-2026-10-02.json`): CP 2.0% [1, 3] n=283 (817 total); Pro 2.0% [1, 3] n=24; gold 2.0% [1, 3] n=87. All three cohorts fell 25/20/25 → ~2 between 09-13 and 09-24. Comments: Wineclaw posted the Reuters link on 09-13; exmateriae (09-18): "even Anthropic might not IPO in 2026".
- Polymarket "OpenAI IPO by Dec 31 2026": YES 3.75% (bid 3.6 / ask 3.9), $1.04M volume. NO-token history: 0.85 on 08-28 → 0.915–0.935 on 09-07..09-12 → 0.9625 on 09-13 onward. The market had already fallen from 15% to ~7–8% before the Altman interview (Anthropic delay, SoftBank repayment news, the safety incidents). File: `raw/polymarket-openai-ipo-2026-10-02.json`.
- **Kalshi KXIPOOPENAI exists. v1 wrongly recorded "Kalshi: no market"**, because it only searched `category=Companies`, while this series is filed under "Financials". It resolves on S-1 effective, priced, or ticker assigned. Before 2027-01-01: bid 2 / ask 5 / last 3¢ ($143k). Before 02-01: 7/11/19¢. Before 03-01: 27/28/28¢. Before 04-01: 26/33/25¢ (not monotone, so thin). Before 06-01: 55/62¢. KXIPOANTHROPIC: before 11-01 4–6¢, before 12-01 73–78¢, before 2027-01-01 79–80¢. File: `raw/kalshi-ipo-markets-2026-10-02.json`.
- Manifold ACX mirror: 5.8% (109 traders). File: `raw/manifold-acx-openai-ipo-2026-10-02.json`.
- Metaculus #44766: not re-fetched (single-fetch rate-limit policy for this session).

### Reasoning notes
- Altman's statement covers *going public* (listing), not *filing*. The surviving YES mass is a public flip in mid/late December 2026 for a late-January 2027 pricing, before the Reg S-X 3-12 staleness cliff (~2027-02-14). An early-February pricing would most likely flip in January (NO).
- Kalshi's Feb-2027 bucket (~18¢ between 02-01 and 03-01) is the main YES-side signal. It conflicts with the CEO's statement, paused training and the AG subpoena, and it trades on thin books, so I discount it.
- Dead ends: marketplace.org and business-standard.com return 403. The CNBC DevDay live blog was available only as a search summary.
