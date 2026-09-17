# Research log — Metaculus #43277, pre-2026 cage-free commitments fulfilled by 2028-01-01

Working log. Newest section at the bottom. Records searches run, evidence found, and dead
ends, so the next update knows what has already been ruled out.

## Session 2026-09-17 — v1

### The single most important finding: the resolution source is queryable as raw data

Chicken Watch's progress tracker is a Next.js page that mounts an **AwesomeTable** view
(`data-viewid="-NqYH6wXir1Ia4I27P6G"`). Driving it with Playwright and logging network
responses showed the view is backed by a **public Google Sheet**:

```
https://docs.google.com/spreadsheets/d/1GcOfjaHy0xTPluZKUkxyNH8u0_qE7T6tdUpeUg7GEyI
  /gviz/tq?sheet=Cleaned&headers=2&tqx=out:csv
```

That is the exact table the question's filters run against, so the resolution metric can be
computed directly rather than estimated. Snapshot (gzipped to keep `raw/` in line with the
rest of the repo — read it with `pd.read_csv(path)`, pandas handles `.gz` transparently):
`raw/chickenwatch-cleaned-2026-09-17.csv.gz` (3,566 rows, 30 columns). Relevant columns: `Victory Date`, `Timeline`, `Issue csvFilter`,
`Reporting Fulfillment csvFilter`, `Continent`, `Industry`.

**The filter replicates Metaculus's exactly.** Applying `Issue = Cage-Free`,
`Victory Date 1990–2025`, `Timeline >= 2026` gives **12 / 326 = 3.681%** today. Metaculus's
stated `nominal_min` is **3.71517028 = 12/323** and its `nominal_max` is
**30.030959735 = 97/323** — the same numerator over the denominator as it stood when the
question was written. This is a hard confirmation that my filter matches theirs, and it also
reveals that the question's range is simply "today's value" to "97 fulfilled".

Note what it implies: the denominator drifted 323 → 326 in the few weeks since the question
was written. It is not fixed.

### Reproducing the published aggregates (validation)

| Cut | My computation, 2026-09-17 | Published figure | Source |
|---|---|---|---|
| Cage-free, Timeline ≤ 2024 | **94.0%** (1,323/1,407) | 93% as of Feb 2026 | Faunalytics [4] |
| Cage-free, Timeline ≤ 2025 | **67.5%** (1,692/2,505) | 64% as of Feb 2026 | Faunalytics [4] |
| Cage-free, Timeline ≤ 2024 | — | 92% as of Jul 2025 | OWA / THL [5][6] |

Both reproduce with the right sign and a plausible 7½-month drift. The tracker gained roughly
**105 new "Reporting Fulfilled" marks in 7.5 months (~14/month)** across the ≤2025 pool.

### Deriving the 2025 cohort's path (the key analogue)

The 2025-deadline cohort is the closest analogue to the 2026 cohort the question turns on.
Its value at deadline+1.5 months is not published, but it can be backed out:

- ≤2025 pool = 2,505 rows; ≤2024 pool = 1,407 rows; 2025-only cohort = 1,098 rows.
- Feb 2026: 0.64 × 2,505 ≈ 1,603 fulfilled in ≤2025; 0.93 × 1,407 ≈ 1,309 in ≤2024.
- 2025-only at Feb 2026 ≈ (1,603 − 1,309)/1,098 = **26.8%** (deadline + 1.5 months).
- 2025-only today = **33.6%** (deadline + 8.5 months).

So a cohort gains roughly **+6.8pp over 7 post-deadline months (~1pp/month, decelerating)**,
i.e. ≈ **+12 to +13pp over its first 12 post-deadline months**.

### Fulfilment by deadline-year cohort (measured today)

| Deadline | n | Fulfilled | Reporting (partial) | Not Reporting | Europe+NA+Oceania |
|---|---|---|---|---|---|
| 2020 | 187 | 89.8% | | | 79.1% |
| 2021 | 132 | 97.0% | | | 74.2% |
| 2022 | 120 | 82.5% | 5.8% | | 58.3% |
| 2023 | 103 | 77.7% | 4.9% | 17.5% | 46.6% |
| 2024 | 138 | 92.0% | 4.3% | 3.6% | 39.9% |
| **2025** | **1,098** | **33.6%** | 21.6% | 44.8% | 58.5% |
| **2026** | **120** | **5.0%** | 40.8% | 54.2% | 55.0% |
| **2027** | **51** | **2.0%** | 41.2% | 56.9% | 35.3% |
| **2028** | **64** | **4.7%** | 31.2% | 64.1% | 14.1% |
| **2030** | **69** | **2.9%** | 52.2% | 44.9% | 26.1% |

Two facts do all the work:

1. **There is essentially no pre-deadline ramp.** Cohorts sitting 3, 15, 27 and 51 months
   *before* their deadline all read 2–5%. Fulfilment reporting is a post-deadline event.
2. **The 2025 mega-cohort broke the pattern the 2020–24 cohorts set.** Every small cohort
   (n = 103–187) sits at 78–97%; the one cohort 8× larger sits at 33.6%.

### A correction to my own first hypothesis (recorded because it was wrong)

I initially assumed the 2026 cohort was compositionally weaker than the 2025 cohort — more
North America, less Europe — and that this explained its low reading. **It does not.** The
2026 cohort is 55.0% Europe+NA+Oceania against the 2025 cohort's 58.5%; reweighting the 2025
cohort's fulfilment rate to the 2026 cohort's continent mix moves it only 33.6% → 31.2%, and
to its industry mix only 33.6% → 33.1%. Nor does Western share explain the cohort ranking:
the 2024 cohort is the *least* Western of the mature cohorts (39.9%) and the *most* fulfilled
(92.0%). Composition is not the driver; **time since deadline and cohort size are.**

### The Open Wing Alliance reporting cycle (why timing matters)

Read the two OWA primary PDFs [6][7] in full. Every headline figure in every edition is
scoped to "**deadlines of 2024 or earlier**" (2025 edition) — i.e. the annual report
deliberately covers only cohorts whose deadline is in the *prior* calendar year or before.
Figure 1 of the 2025 Fulfillment Report also supplies the status definitions used by the
tracker: completely fulfilled ("Fulfilled"), partially fulfilled ("Reporting"), or no public
report ("Not Reporting"), with "Supporting data is available at chickenwatch.org".

Consequences:

- The **2025 cohort has not yet had its first dedicated sweep** — that is the report due
  ~Jul–Oct 2026 (the 2025 edition landed 2025-10-16). Its 33.6% is a *pre-sweep* reading.
- The **2026 cohort will have had its sweep** (the ~Oct 2027 edition, covering "2026 or
  earlier") roughly 2–3 months before the 2028-01-01 read.

This asymmetry cuts *upward* on the forecast: the measured 2025-cohort velocity was earned
without a sweep, while the 2026 cohort gets one inside the window.

### The competing upside reference class, and why it is not the centre

The 2024 cohort (n=138) reached ~90% by about deadline+14 months (Faunalytics' 93% for ≤2024
in Feb 2026, against mature cohorts at 78–97%). If the 2026 cohort (n=120, similar size,
*more* Western) behaved the same way, the question would resolve above 30%. Against that:

- Chicken Watch's ≤2025 aggregate moved only 64% → 67.5% in 7.5 months. For it to reach the
  ≤2024 level, ~610 more commitments must be marked fulfilled; at the observed ~14/month that
  is ~44 months. The mega-cohort is not about to snap to 90%.
- **Independent confirmation from a second tracker.** CIWF's EggTrack 2026 (2026-07-09, 852
  commitments / 602 companies) finds only **198 of 415 (48%)** commitments due by 2025
  fulfilled [10][11] — on a sample biased *toward* large, actively-reporting companies. Two
  independent trackers agreeing that the 2025 wave stalled is strong evidence.
- The physical constraint is real: the US cage-free layer flock is ~44% (Apr 2025) rising
  toward ~50% (147.3M cage-free layers, May 2026) [20]. A US chain cannot report 100%
  cage-free sourcing that the supply chain cannot deliver.

So the 2024-cohort analogue gets a minority weight (~12%), not the centre.

### Disconfirming evidence actively sought and found

- **Chick-fil-A** (2016 pledge, 2026 deadline, in the cohort) said on 2026-04-08 that meeting
  the deadline is "uncertain due to numerous industry dynamics and the significant impact the
  bird flu has had" [12][13]. A marquee member of the exact cohort publicly wobbling.
- **Unilever withdrew its global cage-free commitment** in 2025/26 after reaching 68%
  worldwide, citing emerging-market supply constraints; OWA is campaigning for reinstatement
  [18][19]. It also dropped the Better Chicken Commitment.
- **EggTrack 2026 counts active retreat**: of 852 commitments, **61 deadlines pushed back, 29
  deadlines removed while keeping the pledge, 50 pledges withdrawn entirely** [10][11].
- **US state law is going backwards**: Nevada suspended its cage-free retail requirement in
  Feb 2025 (expired Jun 2025); Arizona's rule slid 2025 → 2026 → 2027 → on hold to 2034;
  Michigan has seen repeal bills [14][15][16].
- **OWA's own naming-and-shaming** (2026-01-13) lists Le Pain Quotidien, Illy, McDonald's
  Korea, Krispy Kreme, CKE, Au Bon Pain, Shake Shack, Inspire Brands and Alsea as having
  missed 2025 deadlines, and flags GoTo Foods, Panda Express, Darden, JDE Peets and Papa
  John's as behind on *later* deadlines [8].
- **Peer-reviewed**: Animal Welfare 35:e39 (2026) on China finds 106 commitments, only 16
  fully fulfilled, with cost premia of 20–25% (some estimates 150–300%), supply-chain
  traceability limits and absent government support as barriers [23].

### Evidence that cuts the other way

- The 2026 cohort already has **40.8% "Reporting" (partial progress)** — a large, live feeder
  pool. The 2025 cohort's own Reporting share drained into Fulfilled as its deadline passed.
- Large, credible European names sit in the 2026 cohort: Kesko, Jerónimo Martins, Eroski,
  Metro Inc., Rimi, Publix, Compass Group, Lactalis, Greencore, Bidfood, Gordon Food Service.
- CIWF EggTrack 2026: global average transition **85%, up from 75% in 2023**; UK average 97%
  across 71 reporting commitments [10][11]. The direction of travel is still up.
- US cage-free supply is expanding, not contracting: 147.3M cage-free layers (May 2026) [20].

### Dead ends (do not repeat these)

- **Wayback Machine**: the CDX API was returning "Internet Archive: Temporarily Offline" on
  2026-09-17. Only one snapshot of `chickenwatch.org/progress-tracker` (2026-09-05) is
  indexed, and it is a JS shell with no data. The Google Sheet is not archived. **There is no
  way found to get a historical Chicken Watch snapshot** — hence the back-out arithmetic above.
- **AwesomeTable REST API** (`api.awesome-table.com/v2/apps/<viewId>`, `/apps/<viewId>`):
  404. Only `/v2/access` and `/v2/banners` respond. Go via the Google Sheet.
- **OWA annual reports do not publish a current-deadline-year figure.** Searched both PDFs;
  every statistic is scoped "2024 or earlier". No pre-deadline reading for the 2025 cohort
  exists in them.
- `thegrocer.co.uk` and `newfoodmagazine.com` return **HTTP 405** to WebFetch; use
  `poultrynews.co.uk` / `poultry.network` for the same EggTrack 2026 numbers.
- `chickenwatch.org/cage-free` does not carry the status definitions; they are in the OWA
  fulfillment-report PDF, Figure 1 caption.
- Playwright needs `--ssl-version-max=tls1.2`, the explicit proxy config and
  `ignore_https_errors` in this sandbox, or every navigation dies with
  `ERR_CERT_AUTHORITY_INVALID`. Same root cause as `METACULUS_FORCE_TLS12=1`.

### Other forecasters — nothing to anchor on

Metaculus #43277 is **still unopened**: status `upcoming`, `cp_reveal_time` 2026-09-20,
**2 forecasters, 0 comments**, and all three aggregation cohorts (`recency_weighted`,
`metaculus_pros`, `gold_medalists`) return HTTP 200 with zero history points. The
`metaculus-scraper` fallback confirms "Community Prediction: None". No Kalshi, Polymarket,
Manifold, GJOpen or INFER market on corporate cage-free fulfilment was found; Sentinel and
Mantic do not cover animal-welfare corporate accountability. **This forecast has no crowd
anchor at all** — which is exactly why the direct reconstruction of the resolution source was
worth the effort, and why the next update (after 2026-09-20) should re-check the CP.

### Model

`scripts/model.py` — 400k-draw Monte Carlo, per-deadline-cohort, with a shared "sweep
intensity" factor (σ=0.30 lognormal) that moves all cohorts together and sets most of the IQR
width, an idiosyncratic per-cohort factor (σ=0.25), Gamma denominator growth, a 5% re-dating
dilution shock and a 12% "fast-sweep" regime. Output: median **11.9%**, IQR
**[9.6%, 15.3%]**, p05 7.1%, p95 28.3%, P(≥30%) ≈ 4%.

## Addendum 2026-09-17 (post-rebase) — reconciliation with the broiler twin, mc43278

While rebasing onto `main` I found that a sibling session had landed
`questions/2026-09-17-mc43278-…` — **the same question for broiler commitments**, resolving off
the same Chicken Watch tracker with the same filter shape, at **median 3.8%, IQR [2.3%, 6.6%]**.
My cage-free forecast moves today's value 3.7% → 11.9% (3.2×); theirs barely moves. That gap
needs to be either justified or one of us is wrong, so I checked it against the snapshot.

**Our reads of the dataset agree exactly.** Reproducing their reference-class table from
`raw/chickenwatch-cleaned-2026-09-17.csv.gz` (forward-looking = Timeline > Victory Date;
deadline passed = Timeline ≤ 2025):

| Cut | Mine | Theirs |
|---|---|---|
| Cage-free, forward-looking, deadline passed | **488/1285 = 37.98%** | 488/1285 = 37.98% ✓ |
| Broiler, forward-looking, deadline passed | **7/226 = 3.10%** | 7/226 = 3.10% ✓ |
| Broiler, North America, deadline passed | **5/205 = 2.44%** | 5/205 = 2.44% ✓ |
| Broiler pledges logged as already met | **14/15 = 93.3%** | 15 rows, 93.3% ✓ |
| Broiler, Europe, deadline passed | 2/19 = 10.5% | 2/21 = 9.5% (multi-continent handling; immaterial) |

**The forecasts are consistent, and the cleanest demonstration is a like-for-like clock
comparison.** At the *identical* point on the curve — the 2024-deadline cohort, 21 months past
its deadline:

- **Cage-free: 127/138 = 92.0%**
- **Broiler: 5/195 = 2.6%**

A **36× gap on the same tracker, same read date, same elapsed time.** The twin's own causal
story explains it: cage-free is a procurement switch across a supply chain that already exists,
while ECC/BCC compliance needs a slower-growing breed that is not available at scale. Importing
either forecast's rate into the other would be the error.

**Does their strongest argument bite on me?** Their Step 3 — that Chicken Watch *structurally
undercounts* real fulfilment (Norsk Kylling 100% ECC-compliant since Aug 2022, still logged
`Not Reporting`; Waitrose and REMA 1000 likewise) — is well evidenced and, I think, correct.
**But it does not transfer to my number, for a structural reason worth stating:** my forecast is
fit to *logged-status velocity*, never to real-world compliance. The +1pp/month I measured
(26.8% → 33.6% on the 2025 cohort) and the 78–97% mature-cohort band are both Chicken Watch's
own logging output, so whatever lag the tracker has is **already inside the data I calibrated
on**. Deducting for it again would be double-counting. The twin needed the argument because it
was reasoning from real compliance (ChickenTrack's "3 companies at 100%") down to logged status;
I never make that step.

Their argument #1 — OWA **retired the blanket 2026 ECC deadline** in favour of case-by-case
roadmaps, removing the forcing event — is genuinely damaging *and* genuinely broiler-specific.
The cage-free campaign shows the opposite posture: the Jan-2026 naming-and-shaming release [8]
and the 2026 Eggsposé ("Some companies kept their word. Others are out of time.") [21] are both
deadline-enforcing. **No change to the forecast.** If OWA ever softens the cage-free deadline
the same way, that is worth roughly −4pp and should become a tripwire at the next update.
