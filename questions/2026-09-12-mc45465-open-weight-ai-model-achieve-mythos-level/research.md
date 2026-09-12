# Research log — open-weight model reaching Mythos-level cyber capability before 2027-07-01

Question: Metaculus #45465. All numbers fetched **2026-09-12** unless stated.
Model knowledge cutoff is May 2026; Mythos, Project Glasswing, ExploitGym and ExploitBench
are all post-cutoff, so **nothing here is from memory** — every fact has a live source.

---

## 0. Resolution parsing (the most important step here)

Resolves **YES** if, before 2027-07-01, an **open-weight** AI system equals or exceeds
Anthropic's Mythos on **at least one** of three benchmarks:

1. **ExploitBench** — https://exploitbench.ai/
2. **UK AISI** — narrow cyber tasks, cyber ranges, "The Last Ones", or a comparable new AISI
   benchmark
3. **ExploitGym** — https://benchlm.ai/benchmarks/exploitgym

Fine print, all three clauses YES-friendly:
- Methodology changes are immaterial provided a "methodologically similar comparison to Mythos"
  exists; where it does not, Metaculus **may infer** from other similar comparisons.
- The benchmark need not label the model open-weight — other credible sources suffice.
- Resolves YES if an open-weight model **matches any published score by Mythos or Mythos
  Preview**. Only three AISI numbers count: expert CTF **68.6%**, The Last Ones **6/10**,
  Cooling Tower **3/10**.

**Two readings that matter.**
(a) "At least one of the three" — confirmed by RyanBeck (Metaculus admin) in the comments on
    2026-09-09 in reply to @exmateriae, who had initially read it as all three. So the
    **softest** of the three routes governs.
(b) "Any published score" pins the bar to numbers already in print; a later, higher Mythos
    re-run does not raise it.

**Counter-intuitive resolution risk**: the ExploitGym rows are not run under matched budgets
(GLM-5.3 = 130/869 solves at 6 h vs Mythos Preview = 157/898 at 2 h). A strict resolver could
call the leaderboard comparison not "methodologically similar". Also, the ExploitGym answer key
was **exfiltrated from Hugging Face in July 2026** (see §4), so post-July open-model scores may
be contaminated, giving a resolver a second reason to hesitate. Both cut against YES only in
the world where the crossing is narrow.

---

## 1. Outside view — reference classes

| # | Reference class | n / window | Raw rate or lag | Source |
|---|---|---|---|---|
| R1 | Open-weight vs closed frontier, **cyber-specific** | GLM-5.2, DeepSeek V4-Pro vs Opus 4.5/4.6, tested mid-2026 | **4–7 months** lag (down from 6–10 months through 2025) | UK AISI, 2026-07-17 [S2] |
| R2 | Open-weight vs closed frontier, **general capability** (Epoch Capabilities Index) | continuous series to 2026-05-29 | **~4 months** lag, ~8 ECI points | Epoch AI [S7] |
| R3 | Named benchmark threshold ~15% above current open-weight SOTA, 9-month window | benchmark-saturation pattern generally | high (>85%) | qualitative |
| R4 | Expert timeline projections to open-weight "Mythos-level" | 3 published | Qualiteg: benchmark parity **Q4 2026–Q1 2027** [S15]; Booz Allen: "most of the other 17 models within **six months**" (i.e. ~Mar 2027) [S13]; LessWrong: 85% within **24 months** for real-world capability [S16] | — |

**Time-scaling.** Mythos Preview was announced **2026-04-07** [S8]. The deadline is
**2027-07-01** — a **14.8-month** window against a measured lag of 4–7 months, i.e. the window
is ~2× the upper end of the lag. From today, **9.6 months** remain.

For NO, the effective lag must blow out to **>15 months** — a 3× regression on R1/R2 —
*or* the measurement/publication chain must fail.

**Status-quo prior does not help here.** This is not "will X change"; the status quo is a
fast-moving trend whose extrapolation *is* YES. The bearish outside view is instead R5:
"AI-milestone questions resolve later than forecasters expect" — real, but 2023–2026 has more
often gone the other way.

---

## 2. Inside view — where the bar actually sits, benchmark by benchmark

### Route A — ExploitGym (benchlm.ai snapshot, "Data verified September 10, 2026") [S4]

898 containerised real-world vulnerabilities (userspace, V8, Linux kernel); score = solved
fraction. Paper: Wang et al., 2026-05-11 (sunblaze-ucb) [S5].

| # | Model | Score | Weights |
|---|---|---|---|
| 1 | GPT-6 Astra (OpenAI) | **42.4%** | closed |
| 2 | GPT-5.6 Sol (OpenAI) | 33.7% | closed |
| 3 | GPT-5.6 Terra (OpenAI) | 23.2% | closed |
| 4 | **Claude Mythos Preview** | **17.5%** | closed ← **the bar** |
| 5 | **DeepSeek V4.1 Flash** | **15.3%** | **open** |
| 6 | **GLM-5.3 (Z.AI)** | **15.0%** | **open** |
| 7 | GPT-5.5 | 13.4% | closed |
| 8 | GPT-5.6 Luna | 12.4% | closed |
| 9 | GPT-5.4 | 6.0% | closed |
| 10 | Muse Spark 1.1 (Meta) | 0.8% | closed |

Cross-checked against llm-stats.com [S6], which lists the same three top rows and the same
0.153 / 0.150 for DeepSeek V4.1 Flash and GLM-5.3.

**Gap = 2.2 pp (14% relative), with 9.6 months and ~4–8 qualifying open releases to run.**

Three things make this the load-bearing route:
- **The target is frozen at April 2026.** The closed frontier is already **2.4×** past it
  (Astra 42.4%). This is not a chase against a moving frontier.
- **Mythos is not an outlier here.** On ExploitGym's broad task mix its V8-exploitation
  specialisation is diluted; it sits *fourth*, below three OpenAI models.
- **The current open-weight leader is a *Flash*-tier model** — DeepSeek V4.1-Flash, 552B total
  / 8B active, MIT, released 2026-09-10 at $0.15/M input [S17]. DeepSeek has announced a
  **V4.1 Pro** with no date [S17]. A cheap, distilled model already sits 2.2 pp under the bar.

Implied lag on this route: open weights (15.3%) sit between GPT-5.5 (13.4%, Apr 2026) and
Mythos Preview (17.5%, Apr 2026) → **lag ≈ 4–5 months**, consistent with R1/R2.

### Route B — UK AISI (68.6% expert CTF / 6-of-10 The Last Ones / 3-of-10 Cooling Tower) [S2]

AISI's July 2026 report gives the 4–7 month lag and evaluates GLM-5.2 and DeepSeek V4-Pro; it
reports **no open-weight model at or above Mythos**. AISI explicitly caveats that its lag
figure "is not predictive of whether future open weight models will replicate the more recent
jumps delivered by Mythos Preview and GPT-5.5."

The narrow-task number (expert CTF 68.6%) is the reachable one; the agentic range tasks (The
Last Ones, Cooling Tower) are not. Qualiteg projects AISI **real-environment** parity only in
**Q3 2027–Q2 2028** [S15] — after the deadline. Requires AISI to publish a qualifying open-weight
comparison inside the window.

### Route C — ExploitBench (exploitbench.ai, CMU v8-bench v0.1) [S3]

**This is where the Metaculus consensus contains an error.** Commenters cite "GLM-5.3 at 54.4%
on ExploitBench vs Mythos ~68–69%", sourced to a kingy.ai blog post and mirrored by
llm-stats.com — whose own page flags **Verified 0 / Self-reported 6 / Status Unverified** and
does not even list Mythos [S6].

The **authoritative site named in the resolution criteria** shows something different. Top 7 of
20 (model, regime) rows, sorted by capability coverage:

| # | Model | Coverage | Weights |
|---|---|---|---|
| 1 | Claude Mythos Preview (AutoNudge, 5 seeds) | **78%** | closed |
| 2 | GPT-5.5 (Codex, AutoNudge) | 72% | closed |
| 3 | Claude Mythos Preview (5 seeds) | **72%** | closed |
| 4 | GPT-5.5 (AutoNudge) | 47% | closed |
| 5 | GPT-5.5 | 42% | closed |
| 6 | GPT-5.5 (Codex) | 33% | closed |
| 7 | Claude Opus 4.7 (AutoNudge, 5 seeds) | 28% | closed |

The open-weight rows present are **GLM-5.1, Kimi K2.6 and MiniMax M2.7** — all topping out at
**tier T3 (target primitives)**, none reaching T1 (arbitrary code execution on production V8
with the sandbox on). Only Mythos Preview and GPT-5.5 reach 16/16 capabilities. Newer open
models (GLM-5.3, DeepSeek V4.1) are **not on this leaderboard at all**.

So Route C is a **cliff, not a near-miss**, and the crowd partly believes otherwise. This is the
single largest reason to sit at, not above, the community prediction.

### Decomposition

| Route | P(capability crossed in world, by ~May 2027) | P(published & credited by resolver) | P(route) |
|---|---|---|---|
| A ExploitGym | 0.94 | 0.94 | 0.88 |
| B AISI | 0.35 | 0.60 | 0.21 |
| C ExploitBench | 0.14 | 0.85 | 0.12 |

Routes are strongly positively correlated (one underlying driver: open-weight cyber progress),
so the naive complement 1 − (1−.88)(1−.21)(1−.12) = 0.917 overstates. Marginal contribution of
B and C beyond A ≈ **+0.03**, giving **≈ 0.91**. Adjusting up slightly for the unusually
YES-friendly fine print (three "may infer / other credible sources / any published score"
clauses) → **0.92**.

**Conjunction check** (methodology §7): the story needs one open release to gain 2.2 pp *and*
one benchmark row to be published. Both individually ≥ 0.9; the product is below the least
likely of them. ✓

**Scope check**: doubling the window to ~19 months would take this to ~0.97; halving it to
~4.8 months to ~0.75. The forecast responds sensibly to scope. ✓

**Would I take the other side at 92%?** At 8% for NO I would need an ~8% chance of a
publication/adjudication failure or an ecosystem freeze. That feels roughly fair, not free
money either way. ✓

---

## 3. Searches run (and dead ends)

| Search | Result |
|---|---|
| `Metaculus "Mythos" cyber capabilities open weight` | identified Mythos as Anthropic's April-2026 frontier cyber model; Glasswing context |
| `Claude Mythos Anthropic Project Glasswing` | Glasswing = limited release to ~150 orgs in 15 countries, 10,000+ critical vulns found [S1] |
| AISI open-weight cyber blog (direct fetch) | 4–7 month lag; the predictive caveat [S2] |
| exploitbench.ai (curl, WebFetch 403) | authoritative leaderboard; **contradicts the crowd** [S3] |
| benchlm.ai ExploitGym (curl) | the decisive 17.5 / 15.3 / 15.0 rows [S4] |
| llm-stats ExploitGym + ExploitBench (curl) | cross-check; ExploitBench table there is self-reported/unverified [S6] |
| Epoch open-closed ECI gap (direct fetch) | ~4-month general lag, May 2026 [S7] |
| anthropic.com/research/mythos-preview | announcement 2026-04-07; **no benchmark scores published there** — the eligible numbers come from AISI and the two leaderboards [S8] |
| `China crack down open-weight models` | Beijing accepted DeepSeek V4 / GLM-5.2 / Kimi K3; cyber alone unlikely to trigger restriction [S9] |
| `US policy open-weight cyber threshold CAISI` | **White House framework exempts open-weight models** from pre-release cyber review (WSJ/Bloomberg, 2026-08-05) [S10][S11] |
| `GLM-5.3 weights delayed cyber` | Z.ai held weights 14 days over emergent cyber capability, **shipped 2026-08-28** [S12] |
| `Qwen Max open weight closed shift` | Qwen3.8-Max weights opened 2026-08-12 — even Max-tier now opens [S18] |
| Register / Booz Allen Cyber Weapon Index | Mythos 80, best open-weight DeepSeek-V4-Pro **23**, on end-to-end kill chain; Booz Allen still says 6 months to parity [S13] |
| Aisle "jagged frontier" | small open models replicate Mythos's *analysis* on specific bugs; not a benchmark result [S14] |
| Qualiteg timing projection | benchmark parity Q4 2026–Q1 2027; AISI-environment parity Q3 2027–Q2 2028 [S15] |
| LessWrong "Open-Weights Mythos Capabilities Are Coming" | 85% in 24 months for real capability (harder bar than this question) [S16] |
| `ExploitGym contamination answers dataset` | **answer key exfiltrated from Hugging Face, July 2026** [S19][S20] |
| `DeepSeek V4.1 Flash release` | 2026-09-10, MIT open weights, 552B/8B-active; **V4.1 Pro announced, no date** [S17] |
| Manifold `ExploitGym ≥70% by EOY 2026` | 44%, 22 trades / 4 holders — too thin to use, but confirms benchlm as the de-facto source [S21] |
| Wayback for benchlm ExploitGym history | **dead end** — Internet Archive was offline on 2026-09-12; no historical leaderboard snapshot obtained |
| Kalshi / Polymarket for an AI-cyber-capability contract | **dead end** — no matching contract found |
| SC Media "More Mythos-like models are coming" | **dead end** — Cloudflare 403 on both WebFetch and curl |

---

## 4. Evidence weighing (likelihood ratios from the R1/R2 prior of ~0.90)

| Evidence | Direction | LR | Note |
|---|---|---|---|
| ExploitGym gap is only 2.2 pp, and the leader is a *cheap Flash-tier* open model [S4][S17] | ↑ | ~1.6 | the strongest single fact |
| Closed frontier already 2.4× past the frozen bar (Astra 42.4%) [S4] | ↑ | ~1.3 | bar is old, not moving |
| White House exempts open weights from cyber pre-release review [S10][S11] | ↑ | ~1.2 | kills the main US policy NO path |
| Beijing has tolerated every major open release so far [S9] | ↑ | ~1.15 | |
| Qwen Max-tier now opens weights; Z.ai's 14-day hold ended in a release [S12][S18] | ↑ | ~1.15 | withholding is real but not binding |
| ExploitGym answer key is public since July 2026 [S19][S20] | ↑ | ~1.1 | contamination inflates open scores |
| Only "one of three" routes needed (admin-confirmed) [S1 comments] | ↑ | ~1.2 | |
| **Route C is a cliff, not a near-miss — crowd partly mistaken** [S3] | ↓ | ~0.7 | removes a believed second route |
| Mythos is a genuine outlier on agentic/kill-chain measures (Booz Allen 80 vs 23) [S13] | ↓ | ~0.85 | but not on ExploitGym |
| AISI's own caveat that the lag is not predictive of Mythos-class jumps [S2] | ↓ | ~0.9 | |
| Contamination + mismatched turn budgets give a strict resolver room to refuse [S4][S19] | ↓ | ~0.9 | only bites on a narrow crossing |
| Thin evaluation pipeline: only 2 of 10 ExploitGym rows are open-weight after 4 months [S4] | ↓ | ~0.9 | publication risk is the real residual |

**Evidence I expected to find and did not** (absence of expected evidence):
- No open-weight model at or above **any** eligible Mythos number today — checked all three
  leaderboards directly. Consistent with a NO-today, YES-soon world, not with an already-crossed one.
- No Kalshi/Polymarket contract; no Sentinel or Mantic write-up on this specific threshold.
- No government action anywhere restricting open-weight cyber releases. Actively searched; the
  opposite was found.

---

## 5. Sources

- [S1] Metaculus #45465 — https://www.metaculus.com/questions/45465/ (raw JSON in `raw/metaculus-2026-09-12.json`)
- [S2] UK AI Security Institute, "How far behind the frontier are leading open weight models on cyber?", 2026-07-17 — https://www.aisi.gov.uk/blog/how-far-behind-the-frontier-are-leading-open-weight-models-on-cyber
- [S3] ExploitBench (v8-bench v0.1, S. Lee & D. Brumley, CMU) — https://exploitbench.ai/
- [S4] BenchLM, ExploitGym leaderboard, verified 2026-09-10 — https://benchlm.ai/benchmarks/exploitgym
- [S5] Wang et al., "ExploitGym: Can AI Agents Turn Security Vulnerabilities into Real Attacks?", 2026-05-11
- [S6] LLM-Stats ExploitGym / ExploitBench leaderboards — https://llm-stats.com/benchmarks/exploitgym , /exploitbench
- [S7] Epoch AI, open–closed ECI gap, data to 2026-05-29 — https://epoch.ai/data-insights/open-closed-eci-gap
- [S8] Anthropic, "Claude Mythos Preview", 2026-04-07 — https://www.anthropic.com/research/mythos-preview
- [S9] G. Webster, "Will China Crack Down on Open-Weight Models?", Tech Policy Press, 2026-08-17
- [S10] The White House, "Promoting Advanced Artificial Intelligence Innovation and Security", EO 2026-06-02
- [S11] "White House exempts open-weight AI models from security review" (WSJ/Bloomberg reporting, 2026-08-05)
- [S12] MLQ / Kingy AI on Z.ai's 14-day GLM-5.3 weight hold and the 2026-08-28 release
- [S13] The Register, "Claude Mythos only model to complete full cyber kill chain", 2026-09-02 (Booz Allen Cyber Weapon Index)
- [S14] Aisle, "AI Cybersecurity After Mythos: The Jagged Frontier", 2026-04-07
- [S15] Qualiteg, "When Will a Mythos-Level Open Model Arrive?", 2026-05-22
- [S16] LessWrong, "Open-Weights Mythos Capabilities Are Coming. We're Not Ready.", 2026-08-07
- [S17] DeepSeek-V4.1-Flash release coverage, 2026-09-10 (MIT weights; V4.1 Pro announced, undated)
- [S18] Qwen3.8-Max open weights, 2026-08-12
- [S19] ExploitGym / Hugging Face answer-key exfiltration, disclosed 2026-07-21
- [S20] Anthropic, "Investigating incidents in cybersecurity evals", 2026-07-30
- [S21] Manifold, "High score on ExploitGym ≥ 70% by EOY 2026" — 44%, 22 trades
