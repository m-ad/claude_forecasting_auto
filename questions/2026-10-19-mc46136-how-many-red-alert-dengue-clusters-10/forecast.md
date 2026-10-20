# How many 'red alert' dengue clusters (10+ cases) will Singapore's NEA list as active on 29 October 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46136/ |
| **Tournament** | minibench — one shot, window 2026-10-19T11:15:33Z -> 2026-10-19T14:15:33Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | closed |
| **Current forecast** | Median 2.69, IQR [1.9, 3.39] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the number of localities listed at alert level "Red" ("high-risk area with 10 or more cases") on NEA's dengue clusters page [1]. It uses the first snapshot whose "accurate as at" date is on or after Thursday 29 October 2026. NEA's own classification counts; the resolver does not reclassify. If the page is unavailable, the equivalent figure from NEA's weekly dengue update [2] or from credible media is used. Possible outcomes are 0–8, plus an open upper bin above 8.

### Outside view

The relevant history is the recent Red counts on this page in 2026. There were 4 Red clusters at the mid-June peak (119 cases/week) [3]. There were 2 on 5 Oct [4] and 2 on 12 Oct [2]. The 16 Oct snapshot shows 3 [1]. With weekly cases steady at about 70–90 since late August [2], the count has stayed between 2 and 3. A Red cluster stays Red until transmission stops; it then turns Green (no new cases, 21-day surveillance) or closes [5]. The persistence prior over 10 days is therefore strong: the outside view centres on the current count of 3, with roughly ±1 of drift.

### Inside view

The three current Red clusters (snapshot 16 Oct [1]):

| Cluster | Total cases | Onset in last 2 wks | Trend | P(still Red on ~29 Oct) |
|---|---|---|---|---|
| Lentor Gardens / Tung Po Ave | 12 | 9 | new, growing | 0.88 |
| Bishan St 12 | 16 | 5 | 10 (5 Oct) → 14 (12 Oct) → 16 | 0.72 |
| Ho Ching / Kang Ching Rd | 95 | 4 | 88 (5 Oct) → 93 (12 Oct) → 95 | 0.68 |

Ho Ching and Bishan are still adding about 2 cases a week. Neither is likely to go 14 or more days with no new cases before 29 Oct, but either could, given that the season is ending. Four Yellow clusters (2–4 cases each) are unlikely to reach 10 within 10 days. Two of them sit in the Lentor area, where a fast-growing June cluster has been [3]. Any new Red, from a Yellow cluster growing or a fresh cluster, is modelled as Poisson with mean 0.45.

`model.py` treats the three existing clusters as independent and adds the Poisson term. It gives a mean of 2.73 and P(0,1,2,3,4,5) = 0.01, 0.09, 0.31, 0.41, 0.15, 0.03. I widened that for correlated closures (for example, a wet-season dip), for possible merging or splitting of clusters, and for resolver error, such as counting only the "2 Red" figure from the weekly-update text. Final pmf:

| Red clusters | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|---|---|
| P | 0.02 | 0.11 | 0.30 | 0.36 | 0.15 | 0.045 | 0.01 | 0.005 |

Continuous percentiles (bin-interpolated): p5 0.77, p10 1.23, p25 1.9, p50 2.69, p75 3.39, p90 4.23, p95 4.72.

### Evidence

- NEA clusters page, accurate as at 16 Oct 2026: 7 active clusters, 3 at ≥10 cases (Lentor Gardens/Tung Po Ave 12, Bishan St 12 16, Ho Ching Rd 95) and 4 Yellow (2–4 cases) [1]. Accessed 2026-10-19.
- NEA weekly update: E-week 40 (4–10 Oct) had 79 cases, after 71, 82, 74, 73 and 87 in the five weeks before. On 12 Oct there were 9 active clusters and 2 Red (Ho Ching 93, Bishan 14) [2]. Accessed 2026-10-19.
- On 5 Oct there were 12 active clusters and 2 Red (Ho Ching 88, Bishan 10) [4].
- The June peak had 4 Red clusters. The Countryside Rd/Lentor Ave cluster then had 34 cases and was rated a fast transmitter [3].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket / Kalshi / Manifold | no matching market found | 2026-10-19 | — |

### What would change my mind

- Ho Ching or Bishan reporting no new onsets in the next week. Each would close or turn Green by 29 Oct, pushing the count towards 2.
- A Yellow Lentor cluster passing 10 cases, or merging. A merge would not add a Red, but separate growth would push the count towards 4.
- How the resolver reads the page. The question text says "2 Red" as of 15–16 Oct, while the snapshot I fetched shows 3 clusters at ≥10 cases. If the newest cluster's alert colour lags its case count on the page, the realised count could be one lower.

### Sources

1. NEA, Dengue clusters — https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters (accessed 2026-10-19)
2. NEA, Dengue cases — https://www.nea.gov.sg/dengue-zika/dengue/dengue-cases (accessed 2026-10-19)
3. Tabla, "119 dengue cases recorded in second week of June, highest so far this year" — https://www.tabla.com.sg/short-news/119-dengue-cases-recorded-second-week-june-highest-so-far-year (accessed 2026-10-19)
4. Little Big Red Dot, "Dengue cases fall to 71 a week as NEA keeps two red clusters open in peak season" (8 Oct 2026) — https://littlebigreddot.com/?p=28192 (accessed 2026-10-19)
5. Little Big Red Dot, "Dengue Cluster Colours: What Singapore Households Should Do" — https://littlebigreddot.com/?p=21440 (accessed 2026-10-19)
6. data.gov.sg, Dengue clusters dataset — https://data.gov.sg/dataset/dengue-clusters (accessed 2026-10-19)

**Question**: [How many 'red alert' dengue clusters (10+ cases) will Singapore's NEA list as active on 29 October 2026?](https://www.metaculus.com/questions/46136/)
**Date**: 2026-10-19
**Forecast**: Median 2.69 clusters, IQR [1.9, 3.39] clusters
**Thesis**: The 16 Oct NEA snapshot shows 3 clusters with 10 or more cases. These are a new, growing Lentor Gardens cluster plus the long-running Bishan St 12 and Ho Ching Rd clusters, and both of those still add about 2 cases a week. Weekly cases are flat at about 70–90, so persistence dominates. Most mass is on 2–3, with the forecast most sensitive to whether Ho Ching or Bishan stops producing cases before 29 Oct.
