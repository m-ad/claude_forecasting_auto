# Research log — Percentage change in funds raised by GiveWell, 2027 and 2028 vs 2026

Working notes for Metaculus post 45386 (group of two numeric subquestions).

## Question mechanics

- **Resolution source**: GiveWell's annual *metrics report* (https://www.givewell.org/about/impact),
  headline **funds raised** figure. Resolves `100 × (F_i − F_2026) / F_2026`.
- **Metrics year**: February–January. Metrics year 2026 = Feb 2026 – Jan 2027;
  2027 = Feb 2027 – Jan 2028; 2028 = Feb 2028 – Jan 2029.
- **Release schedule**: the metrics report lands roughly 7 months after the metrics year
  closes. Observed publication dates: 2024 report → blog post 2025-08-13; 2025 report →
  blog post 2026-08-31 (PDF marked "Last updated: August 2026").
- **Scheduled resolution**: subquestion 2027 (qid 45575) 2028-09-01; subquestion 2028
  (qid 45576) 2029-09-01. **Edge case**: the 2025 report appeared on 2026-08-31, one day
  before the equivalent cut-off. A report published in September rather than August would
  leave the subquestion unresolvable on its scheduled date. Expect Metaculus to wait
  rather than annul, but flag it.
- **Range**: 0–200, both bounds open, so negative outcomes are representable. The range
  choice reveals the question author expected growth.
- **Definition edge cases**:
  - "Funds raised" includes donations made *directly to recommended charities* that
    GiveWell tracks, and **commitments GiveWell recognises as funds raised in a given
    year** (glossary, 2025 metrics report). It therefore runs well above IRS Form 990
    revenue for The Clear Fund.
  - Restatements of F₂₀₂₆ are used if published (fine print).
  - Nominal USD, no inflation adjustment.
- **Author error to note**: the question background says "Coefficient Giving has committed
  to set aside $175 million in 2026". That figure was superseded on 2026-07-23, when
  Coefficient Giving raised its **2026** allocation to GiveWell's recommendations to
  **$1 billion**. The background does not mention it. The denominator is therefore much
  larger than the framing implies — this is the central insight of the forecast.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| GiveWell own Y/Y change in funds raised | 4 | 2022–2025 | +1.2%, −41.1%, +16.8%, +48.6% | metrics reports 2022/2024/2025 | **yes** — the only directly comparable series |
| GiveWell own 2-year change (t vs t−2) | 3 | 2023–2025 | −40.4%, −31.2%, +73.6% | same | **yes** — matches the 2028 subquestion's horizon |
| GiveWell non-CG (individual) giving Y/Y | 4 | 2022–2025 | −14.4%, +0.9%, +23.4%, +64.0% | same | **yes** — the block that actually compounds |
| "Year after an Open Phil step-down" | 1 | 2022→2023 | −41% total, with non-OP giving flat | 2024 metrics report | **yes** — closest structural analogue to 2026→2027 |
| Large US public charity revenue growth | — | — | typically single-digit % | not used | no — GiveWell's funder concentration makes it uninformative |

Base-rate conclusion: 1-year changes in this series are dispersed on the order of
±40–50 percentage points and 2-year changes ±40–75pp, even without a one-off in the base
year. Any IQR narrower than ~50pp wide would be overconfident.

## Key numbers (all retrieved 2026-09-04, snapshot in `raw/`)

Funds raised, USD m, GiveWell metrics years:

| Year | Total | of which CG / Open Phil | Non-CG |
|---|---|---|---|
| 2021 | 595.5 | 300 | 295.5 |
| 2022 | 602.9 | 350 | 252.9 |
| 2023 | 355.1 | 100 | 255.1 |
| 2024 | 414.9 | 100 | 314.9 |
| 2025 | 616.4 | 100.0 | 516.3 |
| 2026 | **committed 1,000 from CG** | 1,000 | ? |

The 2025 jump is almost entirely the $1m+ donor bucket: donations through GiveWell from
$1m+ donors went $151.3m (26 donors) → $359.7m (39 donors). New-donor money more than
doubled; returning-donor money +77%. This is lumpy, mega-donor-driven growth, not a broad
retail trend — the retail buckets ($100–$9,999) barely moved.

## Decomposition

`F = CG + IND`, forecast separately because they are different processes.

**CG (Coefficient Giving, formerly Open Philanthropy), the institutional block**
- Recognition follows the *commitment year*, not disbursement. Evidence: 2022 report says
  $350m was recognised in 2022 while ~$128m was retained for later grantmaking; the
  Oct-2023 $300m/3-year pledge was recognised $100m in each of 2023, 2024, 2025.
- 2025-12-18: CG allocates **$175m for 2026**. 2026-07-23: CG (with Good Ventures) raises
  the **2026 allocation to $1bn** — its own post is titled "Increasing Our **2026
  Allocation** to GiveWell's Recommendations to $1 Billion".
- CG's own words: *"This substantial increase is a one-off surge rather than a new steady
  state"* and *"Future funding is far from guaranteed; this is a bet on laying the
  groundwork for others to emerge and pick up the baton."* Stated reasons: capacity
  building takes time, costs rise once other donors arrive, and transformative AI may
  compress the window.
- Counterweight: CG's 2025 CEO letter says it aims to scale in 2026 and *"prepare for even
  larger growth in 2027 and 2028"*; Good Ventures is "eager to accelerate"; non-Good-
  Ventures donor funding through CG more than doubled in 2025 to >$200m. So the 2027
  steady state is plausibly well above the pre-surge $175m even if far below $1bn.
- **Residual risk**: GiveWell described it as a *"near-term funding commitment"*, which
  leaves room for recognition split across metrics years 2026 and 2027. Modelled at 25%.

**IND (individuals, family foundations, effective-giving orgs, direct-to-charity)**
- $516.3m in 2025 and growing fast. The forward driver is AI equity becoming liquid.
- Anthropic: confidential S-1 filed 2026-06-01; reports in late Aug / early Sep 2026 point
  to a public prospectus after Labor Day and a first trade in late September / early
  October 2026 near a $965bn valuation (some reports float up to $2tn). The Metaculus CP
  for "When will Anthropic IPO?" is 2026-12-23 — i.e. the news flow is *ahead* of the CP.
  Modal lockup 135–180 days ⇒ employee liquidity ≈ Feb–Apr 2027, at the very start of
  **metrics year 2027**, with the December 2027 giving season inside the same year.
- OpenAI: CP median IPO 2027-05-18, lockup modal 180 days ⇒ liquidity ≈ Nov 2027 – Mar
  2028, i.e. straddling metrics years 2027 and 2028, weighted to **2028**.
- All seven Anthropic co-founders have pledged 80% of their wealth; press estimates put
  each stake near $17bn at recent valuations. Anthropic ran a ~$6bn employee tender in
  February 2026 — inside metrics year 2026, so some of this is already in the denominator.
- Disconfirming: this wealth is "all on paper right now"; much AI-linked giving is
  expected to go to AI safety rather than global health; EA Forum commenters explicitly
  question whether GiveWell captures a large share; new liquid donors typically route
  through donor-advised funds, which delays the grant date that GiveWell counts.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-09-04 | Metaculus post 45386 JSON + aggregations for qids 45575/45576 | Group of two numeric subquestions; **zero forecasters, zero comments, no CP in any cohort**. No anchor available. | none — must forecast cold |
| 2026-09-04 | GiveWell metrics reports 2021/2022/2024/2025 (PDF) | Full funds-raised series and CG split; donor-size tables | built the base rates |
| 2026-09-04 | GiveWell blog "GiveWell's 2025 Metrics and Impact" 2026-08-31 | $616m raised (+49%), $427m directed; "grantmaking likely to approach or even exceed $1bn in 2026" | sets 2026 grantmaking scale |
| 2026-09-04 | GiveWell blog "Scaling Our Impact…" 2026-07-23 | CG raises commitment to $1bn; team 38→79 researchers; cost-effectiveness bar cut 8x→6x | denominator inflated |
| 2026-09-04 | Coefficient Giving "Increasing Our 2026 Allocation…" (via text proxy) | **"one-off surge rather than a new steady state"**; "bet on laying the groundwork" | the single most load-bearing fact |
| 2026-09-04 | CG 2025 Letter from the CEO (via search) | CG total giving +50% in 2025 to >$1bn; aims for "even larger growth in 2027 and 2028" | counterweight; raises CG-2027 median |
| 2026-09-04 | Metaculus 44766/44767/44793/44795 | Anthropic IPO CP 2026-12-23, OpenAI 2027-05-18; lockups modal 135–180d | timing of the AI wave into metrics years |
| 2026-09-04 | News search, Anthropic IPO status | Targeting late-Sep/early-Oct 2026 listing; no delay reported; OpenAI slipped to 2027 | pulled the wave slightly earlier → raised g27 |
| 2026-09-04 | Transformer News, Anthropic employee pledges | 7 co-founders pledge 80% of wealth (~$17bn each); GiveWell named a likely recipient | supports upside tail |
| 2026-09-04 | EA Forum "Front-Load Giving Because of Anthropic Donors?" + comments | Argues for giving now; commenters doubt GiveWell's share; "US-centric giving anticipated" | tempered g27/g28 |
| 2026-09-04 | EA Forum "Coefficient Giving just gave GiveWell $1 billion" | "much of the future funding we're anticipating depends on the valuations of some extremely volatile assets" | widened the tails |
| 2026-09-04 | GiveWell blog 2023-04-10 "expected funds raised through 2025" | GiveWell's own 50% CI for 2025 was $400–800m; actual $616m | GiveWell's projections are decently calibrated but very wide — so should mine be |
| 2026-09-04 | Manifold search "GiveWell", "Coefficient Giving" | Only tangential markets; "CG directs ≥$1.5bn in 2026" at 90.5%; "GiveWell approves ≥$800m in grant year 2026" at 50% on 4 traders, last traded 2026-07-22 (stale, pre-dates the $1bn news) | discounted, not used as an anchor |

## Dead ends and ruled-out hypotheses

- `coefficientgiving.org` is not reachable from this container (connection reset via curl
  and Playwright, 403 via the fetch tool). The CG post was read through a text-extraction
  proxy and cross-checked against two independent search summaries and the GiveWell blog.
  **Next update: try again, and try `philanthropy.com` (403 here) via archive.**
- The funds-raised series exists only inside the metrics-report PDFs, not on any HTML
  page or API. Extract with `uv run --with pypdf python -c "from pypdf import PdfReader;
  print(chr(10).join((p.extract_text() or '') for p in PdfReader('gw_2025.pdf').pages))"` —
  the tables come out as one token per line, so pipe through `tr -s '\n' ' '` to read them.
  `pypdf` is deliberately *not* a project dependency; nothing in the repo imports it.
- ProPublica / Form 990 revenue ($269.5m FY2024) is *not* the resolution basis. The
  question's own background cites it; it is roughly 65% of the metrics-report figure for
  the same period and must not be used.
- `metaculus_aggregations.py` returns HTTP 400 for group posts when called with only a
  post id; the aggregation endpoint needs `question_id` for each subquestion. Worked
  around with a direct probe (`scripts/` in the scratchpad). **Worth fixing in the skill.**
- No Kalshi, Polymarket, GJOpen, INFER, Sentinel or Mantic coverage of philanthropic
  fundraising volumes was found. Searched; none exists.
- Could not verify from a reliable source the size of any Open Philanthropy / Good
  Ventures equity stake in Anthropic. Reports confirm Dustin Moskovitz personally invested
  in Anthropic's May 2021 Series A, and the Chronicle of Philanthropy frames the $1bn as
  "banking on an AI windfall", but the stake size is **not** established here. Not used
  quantitatively.

## Open questions to chase next time

1. Does GiveWell's 2026 metrics report (expected ~Aug 2027) recognise the full $1bn in
   metrics year 2026? This single number moves both subquestions by tens of points.
2. Does CG publish a 2027 allocation to GiveWell recommendations (the 2026 one came on
   2025-12-18)? That is the earliest hard read on the numerator.
3. Did the Anthropic IPO happen in Q4 2026, and what lockup did the prospectus set?
4. Any GiveWell statement quantifying expected funds raised for 2027–2028, in the style of
   the April 2023 "expected funds raised through 2025" post.

## v2 — 2026-09-27 (red-team + re-analysis)

### Metaculus fetch

- `metaculus_aggregations.py` still cannot handle group posts, so the fetch used a scratch
  wrapper that calls the skill's `_Fetcher` with `question_id=45575/45576` pinned. The output is
  cached in `raw/metaculus-2026-09-27.json` (latest quartiles, full CDFs, history, 9 comments).
  **Still worth fixing in the skill:** loop over `group_of_questions.questions[*].id`.
- The history is the key finding. All cohorts sat at ~115–150% (2027 leg) until 2026-09-25
  18:03 UTC, when a Pro commenter (MaxA) posted an analysis of the $1bn base-year effect. Within
  ~36 h: CP 117 → 78, Pros 151 → 37, gold 124 → 51 (the 2027 leg). The first forecaster on 2026-09-04 (a gold
  medalist) was at 10.7% / 37.4%, close to v1.

### Search log

| Date | Query / source | Finding | Effect |
|---|---|---|---|
| 2026-09-27 | "Anthropic IPO delayed" (Motley Fool 09-26, Forbes 09-23 citing WSJ, Bloomberg 09-22) | IPO slips Oct → **Nov 2026**, target ~$2tn, up to $100bn raised | valuation ↑; timing ≈ |
| 2026-09-27 | Motley Fool 09-05 citing The Information | Portion of insider shares sellable **at the IPO**; the rest locked "well over 180 days", free ~**mid-2027** | 2027 numerator ↓; 2026 denominator ↑ |
| 2026-09-27 | Longterm Wiki "Anthropic Pre-IPO DAF Transfers" | DAF holdings $20–40bn at $380bn (matching 3:1 at up to 50% in 2021–24, then 1:1 at 25%); no DAF payout minimum; no cause-split data | the missed fact in v1; AI block sized from it |
| 2026-09-27 | EA Forum "The Anthropic IPO Is Coming…" | Co-founders ~1.8% each (~12.6% combined), 80% pledges | founder pool |
| 2026-09-27 | Transformer News 2026-03-12 | GiveWell named as one of several advisory channels; AI safety expected to dominate | caps the GiveWell share |
| 2026-09-27 | GiveWell blog index and "Scaling Our Impact" | "near-term funding commitment"; >$400m already committed in 2026 by July; latest post 2026-09-03; no 2027 guidance | recognition risk kept; carryover into 2027 |
| 2026-09-27 | "Coefficient Giving GiveWell 2027 allocation" | nothing published | tripwire not due |
| 2026-09-27 | OBBBA charitable deduction (Tax Foundation, Fidelity Charitable) | 0.5%-of-AGI floor and 35% cap from 2026, so gifts were accelerated into 2025 | the 2025 base is flattered; ratio impact ≈ 0 |
| 2026-09-27 | EA Forum (Lewars, 2026-07-24) | Large donors advised to redirect marginal dollars after the $1bn | small ↓ base |
| 2026-09-27 | coefficientgiving.org via WebFetch and archive.is | 403 / archive.is unreachable | not re-verified; v1 wording retained |

### Model v2 (why it differs from v1)

See the module docstring of `scripts/model_v2.py`. In short, the AI-linked money is now its
own additive block with IPO/lockup states, and Coefficient Giving and AI-linked giving are no
longer strongly positively correlated. `scripts/pool_v2.py` adds a 30% linear pool with the
Pro + gold CDF.

### Open questions (next update)

1. The final S-1: lockup schedule, how DAF-held shares are treated, and pricing valuation.
2. Coefficient Giving's 2027 allocation (expect Dec 2026).
3. Any GiveWell statement on how the $1bn is split across metrics years. **Cheapest
   high-value action: ask GiveWell directly.**
4. Whether Metaculus admins rescale the 0–200 range (a commenter asked on 2026-09-25).
