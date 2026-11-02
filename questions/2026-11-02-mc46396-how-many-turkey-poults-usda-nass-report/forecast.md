# How many turkey poults will USDA NASS report as net placed in the United States during October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46396/ |
| **Tournament** | minibench — one shot, window 2026-11-02T10:13:36Z -> 2026-11-02T13:13:36Z |
| **Type** | numeric |
| **Opened / Closes / Resolves** | 2026-11-02 / 2026-11-02 / 2026-11-13 |
| **Status** | closed |
| **Current forecast** | Median 21700, IQR [21350, 22050] (v1, 2026-11-02) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-02

### What resolves YES

The question resolves to the US total (all breeds) October 2026 net poult placements, in thousands, as first published in the NASS Turkey Hatchery report due 2026-11-13 (3 pm ET). Later revisions do not count. Latest published period: September 2026 = 19,571 (report of 2026-10-13); the target is the very next month (one period ahead, not two). Arithmetic: Oct 2025 (as revised in the Oct 2026 report) = 21,284. A +2% y/y pace (the Sept 2026 y/y and the Oct-1 eggs y/y) gives 21,710. Sept→Oct step in revised 2025 data = 21,284/19,096 = +11.5%; in revised 2024 data 20,165/18,601 = +8.4%; applied to 19,571 that gives 21,215–21,820. Bounds are open (17,000–25,000 displayed).

### Outside view

Placements track eggs set a month earlier and hatch. Reference class: the same month in recent years and the October/September ratio (n = 2 reliably revised seasons, 2024 and 2025: 1.084 and 1.115). Year-on-year changes in monthly placements over Sept 2025–Sept 2026 are mostly within ±6% and strongly correlated with the y/y change in eggs in incubators on the 1st (+2% for Oct 1, 2026). Base: Oct 2025 × 1.02 ≈ 21,700.

### Inside view

Three estimators: (a) y/y +2%: 21,710; (b) Oct-1 eggs 26,695 × Oct placements/eggs ratio (0.815 in 2025, 0.822 in 2024 revised) = 21,750–21,940; (c) Sept placements × Sept→Oct step 1.084–1.115 = 21,215–21,820. They centre near 21,700. HPAI: the named October detections are 13,500–60,600 birds each, i.e. tens of thousands of birds against ~21 million monthly placements; eggs already set on Oct 1 (+2% y/y) bound the month, so I apply no HPAI adjustment. High turkey prices (WASDE ~165 c/lb) support placements. Wider spread than the pure estimators because (i) NASS's own stated RMSE for placements is 4.2%, (ii) the 2025 revised Oct figure was revised up by ~8% from first publication (19,684 in the Jan 2026 report to 21,284), showing how noisy this series can be around October, and (iii) I could not verify the historical ratios across more years.

### Evidence

- NASS Turkey Hatchery, 2026-10-13 (accessed 2026-11-02): Sept 2026 placements 19,571 (+2% y/y); Sept hatch 21,122; eggs on Oct 1 26,695 (+2%; Oct 1 2025 = 26,122); Oct 2025 hatch 22,981; Oct 2025 placements 21,284 (Nov 2025 18,482) [1].
- Aug 2026 report (accessed 2026-11-02): Oct 2024 placements 20,165, Sep 2024 18,601 (revised basis) [2].
- Jan 2026 report: older basis — Sep 2025 18,179, Oct 2025 19,684 (ratio 1.083), Oct 2024 19,510; the later annual revision raised Sept–Oct 2025 by 5–8% [3].
- HPAI: question text cites APHIS data through Oct 30, 2026, 11 commercial flocks in 30 days (not independently verified) [4]. Scout found no report of placement cuts.
- WASDE (snippets): 2027 turkey production forecast 5,125 million lb, higher on better returns [5].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-11-02 | |
| Kalshi / Polymarket / Manifold | none found | 2026-11-02 | no market on turkey placements |

### What would change my mind

A pattern showing first-published October figures systematically deviating from the y/y trend implied by the Oct-1 egg count (e.g. an NASS revision note about missing hatcheries), or evidence of large-scale placement deferrals in MN/ND/IA from HPAI control zones. Either would widen or shift the distribution by ~2–4%.

### Sources

1. https://esmis.nal.usda.gov/sites/default/release-files/796103/tkha1026.txt (accessed 2026-11-02)
2. https://esmis.nal.usda.gov/sites/default/release-files/796017/tkha0826.txt (accessed 2026-11-02)
3. https://esmis.nal.usda.gov/sites/default/release-files/795729/tkha0126.txt (accessed 2026-11-02)
4. questions/2026-11-02-mc46396-how-many-turkey-poults-usda-nass-report/raw/metaculus-question-2026-11-02.json (APHIS summary of 2026-10-30; accessed 2026-11-02)
5. https://hpj.com/2026/08/14/usda-adjusts-poultry-and-egg-outlooks/ (search snippet, accessed 2026-11-02)
6. https://www.cidrap.umn.edu/avian-influenza-bird-flu/h5n1-avian-flu-returns-midwest-poultry-farms-multiple-turkey-operations (snippet, accessed 2026-11-02)

**Question**: [How many turkey poults will USDA NASS report as net placed in the United States during October 2026?](https://www.metaculus.com/questions/46396/)
**Date**: 2026-11-02
**Forecast**: Median 21,700 thousand poults, IQR [21,350, 22,050]
**Thesis**: Oct 2025 placements (21,284) grown by the +2% y/y pace of Sept placements and Oct-1 eggs in incubators, cross-checked with the Sept→Oct step, gives ~21,700. HPAI losses are tiny against monthly placements; the forecast is most sensitive to the noisy Sept→Oct seasonal step and NASS estimation error.
