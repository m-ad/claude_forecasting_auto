# Research log — Will a U.S. federal agency announce new or expanded model evaluation agreements with both OpenAI and Anthropic before September 3, 2026?

Working notes. Rough is fine; **completeness beats polish**. The next update reads this to
learn what was already checked and what was already ruled out.

## Question mechanics

- Resolution source: any U.S. federal agency's official announcement (CAISI/NIST most likely,
  but NSA/CISA/DOD also plausible under EO 14409's framework).
- Window: after Aug 10, before Sept 3 2026 ET (~24 days; question posted 2026-08-27, so ~17 of
  24 days have already elapsed with no qualifying announcement observed).
- Both companies need not be in the same announcement (fine print). Expansion of a
  *pre-existing* arrangement only counts if it names a new model family, access arrangement,
  testing scope, or evaluation domain — a generic renewal or PR restatement does not count.
- Key edge case: CAISI already holds MOUs with both OpenAI and Anthropic (since Aug 2024,
  renegotiated ~May 2026). A pure continuation of that relationship does NOT resolve YES;
  only a genuinely new/expanded element does.
- Key edge case 2: reporting/leaks about a framework are not an "official announcement" by an
  agency. Congressional testimony revealing details might or might not count depending on
  framing — treated as a weak, partial path to YES.

## Reference classes considered

| Class | n | Window | Base rate | Source | Kept? |
|---|---|---|---|---|---|
| CAISI "wave" announcements of new/expanded developer eval agreements (Aug 2024 OpenAI+Anthropic MOUs; May 2026 DeepMind/Microsoft/xAI + renegotiated OpenAI/Anthropic MOUs) | 2 events / ~21 months | scaled to 24-day window | ≈ 24/319 ≈ 7.5% | NIST/CAISI press history (search) | Yes — primary outside-view anchor |
| Any US federal-agency AI-policy "official announcement" in a given month during 2026 (EO signings, framework meetings, CAISI evaluations, export-control actions) | high (~1-2/month) | 24 days | high, but most don't touch "both OpenAI+Anthropic new/expanded eval" | search sweep | Kept only to show base activity is high; doesn't map directly to the conjunction required |
| Status-quo prior for "will X specific policy event happen in the next N weeks" absent a hard deadline in-window | — | — | low (short-horizon events default to no-change) | methodology.md §1 | Yes — secondary anchor, reinforced by evidence below |

## Decomposition

P(YES) requires, within Aug 10–Sept 3 2026:
1. A qualifying mechanism exists to test/expand access to OpenAI's and Anthropic's models
   (it does: CAISI MOUs + the EO 14409 "30-day pre-launch access" framework), AND
2. That mechanism reaches a state where there is something *new* to announce for at least one
   of the two companies (and, on a separate or same announcement, the other), AND
3. A federal agency actually issues a public, official announcement naming it (not just press
   leaks/reporting) inside the 24-day window.

Step 1: essentially satisfied (P≈0.9 both channels are live).
Step 2: plausible — EO 14409 framework was reportedly "finalized"/reviewed with labs Aug 3-4,
  just before the window opened, and OpenAI + Anthropic both attended. If the framework moves
  from "reviewed in a closed-door meeting" to "signed/operational," it would very likely count
  as a "previously not-covered access arrangement." P(step 2 becomes true in-window) ≈ 0.25-0.35.
Step 3 is the bottleneck: the White House explicitly stated (as of Aug 4) it will NOT publicly
  release the framework and wants to keep participation confidential; CAISI's own May 2026
  playbook shows agencies CAN do a lighter-weight announcement without disclosing full
  classified test criteria, so an official announcement is not impossible even under secrecy,
  but the administration's revealed preference is against it. P(step 3 | step 2) ≈ 0.15-0.25.

Multiplying the two binding steps: 0.30 × 0.20 ≈ 0.06. Then discount further for the fact that
17 of the ~24 window-days have already elapsed with zero movement toward an announcement (no
news of any kind after Aug 10 signaling imminent disclosure) → final range ≈ 0.03-0.06.

Independent second path (DOD/other agency touches both companies): weak. DOD relationship with
Anthropic is actively adversarial (blacklisted Feb–Jul 2026 over autonomous-weapons/surveillance
red lines; OpenAI won the DOD classified-network deal that Anthropic did not sign). A DOD-led
evaluation-agreement announcement covering *both* companies in the next week is very unlikely
given this history. Adds at most +0.5-1pp to the total.

## Search log

| Date | Query / source | Finding | Effect on forecast |
|---|---|---|---|
| 2026-08-27 | NIST/CAISI official page + HPCwire + CNBC (May 5 2026 announcement) | CAISI's last "wave" announcement (DeepMind, Microsoft, xAI) was May 5 2026; OpenAI/Anthropic MOUs already existed and were renegotiated at that time, not newly created | Anchors outside-view base rate; confirms OpenAI/Anthropic's *existing* relationship predates the window, so pure continuation ≠ YES |
| 2026-08-27 | Federal Register / DLA Piper / Skadden / WilmerHale on EO 14409 (June 2, 2026) | EO ordered NSA/CISA/Treasury/NIST to build a voluntary 30-day pre-launch model-access framework, core deliverables due by Aug 1, 2026 | Establishes the live mechanism that could generate a qualifying announcement |
| 2026-08-27 | KuCoin / TechPolicy.press | US govt **missed** the Aug 1 deadline for the classified benchmarking process; no public confirmation deliverables were completed on time | Downward: shows execution lag, not urgency |
| 2026-08-27 | CNBC (Aug 3), Axios (Aug 3-4), Fortune (Aug 4), Semafor (Aug 4) | White House held a closed-door meeting Aug 3-4 with Meta, Nvidia, Microsoft, OpenAI, Anthropic to review the draft framework; explicitly said it has **no plans to publicly release** the framework, keeping it under wraps for participating companies only | Strong downward signal — the bottleneck step (public official announcement) is disfavored by the administration's own stated position, just before the window opened |
| 2026-08-27 | TechPolicy.press "Five questions..." | No public disclosure requirement; process is informal, no published criteria/timeline; criticized for opacity | Reinforces low probability of a clean, citable "official announcement" |
| 2026-08-27 | Gillibrand/Warner Senate letter (Aug 3 2026, to Rubio/Bessent/Lutnick/Wiles/Kratsios/Cairncross) | Senators pressing for clarity on AI model access policy, calling current approach "chaotic, opaque" | Some upward pressure toward transparency, but Congressional letters rarely force administration announcements within days-to-weeks |
| 2026-08-27 | aigovernance.com | Describes framework as "finalized" Aug 3 with Meta/Anthropic/Google/OpenAI participating, but no confirmation of a public announcement or specific timeline; suggests such voluntary commitments typically precede binding rules by 12-24 months (i.e., not urgency-coded) | Neutral-to-downward; "finalized" internally ≠ "officially announced" externally |
| 2026-08-27 | NPR / TechCrunch (Feb-Mar 2026), ABC News/GVWire (Jul 2026) | DOD blacklisted Anthropic Feb 2026 over autonomous-weapons/surveillance dispute; OpenAI won the DOD classified-network deal instead; Anthropic's export-control-driven model restrictions were separately lifted by Trump admin in July 2026 (unrelated dispute, resolved) | Confirms DOD track is a weak/unlikely path for a joint OpenAI+Anthropic announcement; the export-control episode is closed and not itself a qualifying "evaluation agreement" |
| 2026-08-27 | Metaculus comments (question history) | Question drafters explicitly debated and tightened the resolution criteria to require BOTH OpenAI and Anthropic (not just any two developers), specifically citing EO 14409 §3b as the intended resolution mechanism | Confirms EO 14409's 30-day-access framework is the mechanism the question was designed to track |
| 2026-08-27 | Metaculus CP/Pro/gold history (raw/metaculus-2026-08-27.json) | CP fell from ~25-28% (Aug 12-16) to 3.0% (Aug 27); Pro fell from ~28% to 7.0%; gold fell from ~30% to 3.0%, tracking the "won't publicly release" news breaking Aug 3-4 and then the accumulating silence through most of the window | Confirms the community update direction matches the evidence found independently; my own decomposition (≈3-6%) lands near CP/gold and below Pro |
| 2026-08-27 | Polymarket/Kalshi/Manifold searches | No dedicated market found for this specific question (federal-agency OpenAI+Anthropic eval-agreement expansion); adjacent markets exist only for "best AI model" leaderboard bets, irrelevant here | No market comparison available beyond Metaculus itself |

## Dead ends and ruled-out hypotheses

- DOD/Department of War track as a path to YES: ruled mostly out given the active Anthropic
  blacklist dispute (only partially/informally resolved) and OpenAI's exclusive classified-network
  win.
- Treating the Aug 3-4 White House meeting itself as a qualifying announcement: does not count —
  it is a closed-door review meeting, not an official announcement of a completed agreement, and
  it predates the window's Aug 10 start regardless.
- Treating the May 5 2026 CAISI announcement as a comparable in-window event: it predates the
  window and was mostly about DeepMind/Microsoft/xAI, not a new/expanded OpenAI+Anthropic element,
  though it is the best available "how does an announcement like this actually get made" template.

## Open questions to chase next time

- Has the EO 14409 framework been operationalized (companies actually submitting models) even
  without a public announcement? If so, watch for any subsequent agency communication that
  crosses from "in effect" to "officially announced."
- Watch for Congressional testimony/appropriations hearings in Sept 2026 that might force
  disclosure of participant lists — would only count if framed as an agency "announcement."
- Watch NIST/CAISI's news page directly (nist.gov/caisi) for anything dated after 2026-08-27.
