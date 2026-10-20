# How many countries will ECDC's West Nile virus weekly report published around 30 October 2026 list as affected during the 2026 season?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46158/ |
| **Tournament** | minibench — one shot, window 2026-10-19T22:50:55Z -> 2026-10-20T01:50:55Z |
| **Type** | discrete |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-20 / 2026-10-31 |
| **Status** | closed |
| **Current forecast** | Median 19.46, IQR [18.98, 20.22] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

The question resolves to the integer Y in the sentence "... areas affected by West Nile virus (WNV) have been identified in Y countries across Europe" in the "Current situation" section of the ECDC weekly report at wnv-weekly.ecdc.europa.eu. The report used is the first one published on or after 29 October 2026, expected Friday 30 October (Week 44, data to about 28 October). If no new report appears, the latest 2026 report available on 31 October is used. The count is cumulative over the season. The range runs from 19 (closed lower bound) to 24, and the upper bound is open. Between now and resolution there are two reports left to add countries: Week 43 (about 23 October) and Week 44 (about 30 October).

### Outside view

- **Starting point:** the latest report (Week 42, published 16 October, data to 14 October 2026) gives **19 countries** and 222 areas [1]. The status quo is therefore 19.
- **Reference class:** how many countries ECDC adds between mid-October and the end of the season.
  - 2025: 13 countries on 8 October, 14 at season close on 10 December. That is +1 over two months [4][5].
  - 2023: 12 countries including neighbours as of 25 October, with essentially no growth afterwards [6].
  - Late-season additions are rare: about 0 to 1 per month.
  - Prior on additions over two weekly reports: about 0.3.

### Inside view

2026 is an outlier season, and countries have kept arriving late:

| Date (2026) | Countries | Areas | Source |
|---|---|---|---|
| 5 August | 7 | 59 | [3] |
| 21 August | 12 | 99 | [3] |
| 10 September | 15 | 161 | [3] |
| 30 September | 16 | 202 | question text |
| 7 October | 18 | 208 | [2] |
| 14 October | 19 | 222 | [1] |

The Week 42 report still had 14 areas affected for the first time [1], and ECDC/EFSA describe the broadest spread on record [2]. Most of these late additions reflect delayed notification of cases with onset in September, not new transmission, and that pipeline still has some weeks to run. Against this, the monthly report says the season is ending and only low-level transmission is expected [2]. I found no press report of a first 2026 human case in any country not yet counted. I checked Türkiye, Slovakia, Czechia, Portugal, Bosnia and Herzegovina, Montenegro, Ukraine, Poland and Switzerland.

**Most plausible late addition: Türkiye.** It was in ECDC's 2025 country list [5] but is missing from the 2026 list, and it usually reports late. This is speculation; I found no 2026 Turkish case reports.

**Model:** additions over two reports follow an overdispersed Poisson with mean about 0.6. That is twice the historical base rate, because 2026 added three countries in the last two weeks. The resulting probabilities:

| Countries | Probability |
|---|---|
| 19 | ~52% |
| 20 | ~32% |
| 21 | ~11% |
| 22 | ~3.5% |
| 23 or more | ~1.5% |

### Evidence

- ECDC weekly report, Week 42 (published 16 October 2026, data to 14 October) [1]:
  - "222 areas affected by West Nile virus (WNV) have been identified in 19 countries across Europe".
  - 14 areas were affected for the first time that week.
  - The area list names 18 countries: Italy 70, France 28, Greece 25, Romania 24, Netherlands 15, Serbia 10, Belgium 6, Bulgaria 6, Croatia 6, Germany 6, Spain 6, North Macedonia 5, Hungary 4, Kosovo 4, Austria 3, Albania 2, Cyprus 1, Slovenia 1.
  - Moldova appears in the human case counts.
- EFSA/ECDC monthly report (data to 7 October, published 15 October) [2]:
  - 18 European countries, 1,855 cases and 141 deaths.
  - 1,715 EU/EEA cases in 13 countries, against a 10-year average of 693.
  - The season is nearing its end, with low-level transmission possible.
- Earlier weekly counts, accessed 2026-10-19 [3]: 7 countries on 5 August, 12 on 21 August, 15 on 10 September.
- 2025 season [4][5]: 13 countries on 8 October, 14 final as of 10 December, Türkiye included. ECDC closed the weekly series on 10 December, so a Week 44 report is very likely.
- Switzerland had no confirmed human case as of 28 September 2026 [7].
- I found no 2026 reports of first human cases in Türkiye, Slovakia, Czechia, Portugal, Bosnia and Herzegovina, Montenegro, Ukraine or Poland. My searches were in English, Turkish and Serbo-Croatian.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus community | hidden — bot tournament | 2026-10-19 | |
| Polymarket / Kalshi / Manifold | none found | 2026-10-19 | no matching market |

### What would change my mind

- A news report before 28 October of a first 2026 locally acquired human case in a new country (Türkiye, Bosnia and Herzegovina, Slovakia, Czechia, Portugal, Ukraine). That would make 20 or more the most likely outcome.
- The Week 43 report (about 23 October) staying at 19 would raise P(19) to about 70%.

### Sources

1. ECDC, West Nile virus weekly report, Week 42 2026, https://wnv-weekly.ecdc.europa.eu/ (accessed 2026-10-19)
2. EFSA/ECDC monthly WNV report, data to 7 Oct 2026, https://www.efsa.europa.eu/sites/default/files/2026-10/2026_10_wnv_monthly_report_efsa-ecdc_10410.pdf, via coverage at https://arynews.tv/west-nile-virus-rises-in-europe-with-141-dead-in-2026 (accessed 2026-10-19)
3. Quotidiano Sanità / Adnkronos on earlier ECDC weekly counts, https://www.quotidianosanita.it/?p=153331 and https://english.adnkronos.com/2026/08/21/west-nile-ecdc-cases-in-12-european-countries-strengthen-controls/ (accessed 2026-10-19)
4. ECDC historical WNV data, https://www.ecdc.europa.eu/en/west-nile-fever/surveillance-and-disease-data/historical (accessed 2026-10-19)
5. Clinica del Viaggiatore, ECDC 2025 season summary, https://clinicadelviaggiatore.com/en/West-Nile-virus-in-Europe%3A-the-situation-updated-to-2025/ (accessed 2026-10-19)
6. ECDC, WNV human cases compared to previous seasons, 25 Oct 2023, https://www.ecdc.europa.eu/en/publications-data/west-nile-virus-human-cases-compared-previous-seasons-25-october-2023 (accessed 2026-10-19)
7. Bluewin, Switzerland: no WNV human cases yet, https://www.bluewin.ch/en/news/1-600-west-nile-virus-cases-in-the-eu-none-yet-in-switzerland-li.3616338 (accessed 2026-10-19)

**Question**: [How many countries will ECDC's West Nile virus weekly report published around 30 October 2026 list as affected during the 2026 season?](https://www.metaculus.com/questions/46158/)
**Date**: 2026-10-19
**Forecast**: Median 19.46 countries, IQR [18.98, 20.22] (P(19) ≈ 52%, P(20) ≈ 32%, P(21) ≈ 11%, P(≥22) ≈ 5%)
**Thesis**: ECDC's Week 42 report (data to 14 October) gives 19 countries, and only two more weekly reports fall before resolution. Historically, few or no countries are added after mid-October, but this record 2026 season has kept adding late reporters (+3 in two weeks), so there is a substantial chance of a 20th, with Türkiye (counted in 2025, absent so far) as the likeliest candidate. The forecast is most sensitive to whether another new country reports a first human case before 28 October.
