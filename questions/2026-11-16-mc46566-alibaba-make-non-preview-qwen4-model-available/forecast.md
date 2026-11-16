# Will Alibaba make a non-preview Qwen4 model available on a pay-as-you-go API basis before November 28, 2026?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46566/ |
| **Tournament** | minibench — one shot, window 2026-11-16T02:22:39Z -> 2026-11-16T05:22:39Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-11-16 / 2026-11-16 / 2026-11-28 |
| **Status** | closed |
| **Current forecast** | Median 95.0%, IQR [92.0%, 97.0%] (v1, 2026-11-16) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-11-16

### What resolves YES

YES if, as of 23:59 UTC on 27 Nov 2026, either Model Studio pricing page (international alibabacloud.com or China help.aliyun.com) lists at least one Qwen4-series model whose ID does not contain "preview" with standard pay-as-you-go input and output prices. Credible reports of such pay-as-you-go availability before 28 Nov also resolve YES. The listing has to be present at the check, so the question is no longer whether a release lands in the ~2-day gap between the preview's end (16:00 UTC, 25 Nov) and the deadline. **When I fetched both pages on 16 Nov 2026, each already had a `qwen4-max` row with input and output prices** [1][2]. If that holds, the criteria are met 11 days early. The question therefore turns on two things: whether the listing persists, and whether the resolver reads it.

### Outside view

Before the listing, the base rate was preview-to-GA gaps for Qwen Max models, measured from preview launch to the non-preview listing:

| Model | Gap |
|---|---|
| Qwen3-Max | 19 days |
| Qwen3.8-Max | about 15 days |
| Qwen3.7-Max | 1 day |
| Qwen3.6-Max | never GA'd (skipped) |

Sources: [4][5]. A gap of 15–19 days from the 11 Nov preview puts GA around 26–30 Nov, so a listing by 27 Nov would have been roughly 35–45%. In the reference class, pricing pages that list a model with published prices almost never pull the row within two weeks.

### Inside view

The listing itself moves the forecast. Both pricing pages show a non-preview `qwen4-max`:

- **International page:** under "Qwen-Max", Singapore (International) at $1.5 input / $4.5 output per 1M tokens, plus a 1M-token free quota. Global regions are $1.413 / $4.24. The row directly below is qwen3.8-max at $2 / $6, which matches the question's own description of that page. "Last Updated: Nov 16, 2026" [1].
- **China page:** CNY 10 / 30 [2].
- **Model Studio release log:** an entry for `qwen4-max` dated 2026-11-16 [4].
- **Explicit-cache docs:** a Qwen4-specific page uses `qwen4-max` in its examples [3].

This is three or four Alibaba pages that agree, read through two independent fetches with different numbers and currencies. That makes a summariser hallucination unlikely.

What still leaves room for NO:
- Alibaba pulls the row before 27 Nov (pre-published docs for a later launch), about 3%.
- The fetch was misread, about 1–2%.
- The resolver errs, e.g. rules the model "not available" or still Token-Plan-only despite the listing, about 1–2%.

Forecast: 95%.

### Evidence

- 2026-11-16: International pricing page lists `qwen4-max` at $1.5/$4.5 (Singapore) and $1.413/$4.24 (Global regions) [1].
- 2026-11-16: China pricing page lists `qwen4-max` at CNY 10/30 [2].
- 2026-11-16: The qwen4-max-preview page still says Token Plan only, no pay-as-you-go, and retirement after 25 Nov [6]. That rule concerns the preview ID only.
- News coverage as of 16 Nov has not yet reported the listing [7]. Secondary trackers up to about 13 Nov said there was no GA date.

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus | hidden — bot tournament | 2026-11-16 | |
| Polymarket / Kalshi | none found | 2026-11-16 | |
| Manifold "Qwen 4 release date" | resolved on the 11 Nov preview | 2026-11-16 | its criteria counted previews, so not informative here [8] |

### What would change my mind

- The `qwen4-max` row disappears from both pricing pages before 27 Nov.
- Alibaba states that `qwen4-max` is Token-Plan-only, with no pay-as-you-go.

### Sources

1. Alibaba Cloud Model Studio, Model inference pricing (international): https://www.alibabacloud.com/help/en/model-studio/model-pricing (accessed 2026-11-16)
2. Alibaba Cloud Model Studio, Model inference pricing (China): https://help.aliyun.com/en/model-studio/model-pricing (accessed 2026-11-16)
3. Explicit cache, Qwen4: https://www.alibabacloud.com/help/en/model-studio/explicit-cache-qwen4 (accessed 2026-11-16)
4. Model Studio newly released models: https://www.alibabacloud.com/help/en/model-studio/newly-released-models (accessed 2026-11-16)
5. Qwen3.8-Max preview coverage (Fonearena): https://www.fonearena.com/blog/487749/alibaba-qwen3-8-max-preview-features.html/amp (accessed 2026-11-16)
6. Qwen4-Max-Preview documentation: https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview (accessed 2026-11-16)
7. Magica, "Alibaba opens Qwen4-Max preview with a November 25 API deadline": https://magica.com/news/alibaba-qwen4-max-preview-token-plan (accessed 2026-11-16)
8. Manifold, "When will Alibaba release Qwen 4": https://manifold.markets/Bayesian/when-will-alibaba-release-qwen-4 (accessed 2026-11-16)

**Question**: [Will Alibaba make a non-preview Qwen4 model available on a pay-as-you-go API basis before November 28, 2026?](https://www.metaculus.com/questions/46566/)
**Date**: 2026-11-16
**Forecast**: Median 95.0%, IQR [92.0%, 97.0%]
**Thesis**: Both Model Studio pricing pages already list a non-preview `qwen4-max` with pay-as-you-go prices as of 16 Nov 2026: $1.5/$4.5 per 1M tokens internationally, CNY 10/30 on the China page. That already meets the resolution criteria. The residual risk is Alibaba pulling the row before 27 Nov or the resolver misreading it.
