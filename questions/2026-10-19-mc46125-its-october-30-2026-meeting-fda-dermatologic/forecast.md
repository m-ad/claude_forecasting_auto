# At its October 30, 2026 meeting, will the FDA Dermatologic and Ophthalmic Drugs Advisory Committee vote in favor of SYD-101 (atropine 0.01%) for pediatric progressive myopia?

| | |
|---|---|
| **Source** | metaculus — https://www.metaculus.com/questions/46125/ |
| **Tournament** | minibench — one shot, window 2026-10-19T00:28:46Z -> 2026-10-19T03:28:46Z |
| **Type** | binary |
| **Opened / Closes / Resolves** | 2026-10-19 / 2026-10-19 / 2026-10-30 |
| **Status** | open |
| **Current forecast** | Median 62.0%, IQR [50.0%, 72.0%] (v1, 2026-10-19) |
| **Community** | hidden — bot tournament |
| **Next review** | — |

<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->

---

## v1 — Initial forecast — 2026-10-19

### What resolves YES

YES requires two things at the October 30, 2026 meeting of the FDA's Dermatologic and Ophthalmic Drugs Advisory Committee (DODAC) on NDA 219694 (SYD-101, atropine 0.01%, for slowing myopia progression in children aged 3 and up). First, the committee must hold a formal vote on overall benefit-risk or on support for approval, or on an equivalently worded question. Second, strictly more members must vote Yes than No. The source is the FDA's posted voting results, or credible reporting of them. Abstentions are not counted, and a tie resolves NO. If there are several votes, the one closest to benefit-risk or approval governs, and if there are several of those, the latest one does. If the meeting is cancelled or postponed past October 30, or it is discussion-only with no such vote, the question is **annulled**. That means I only need P(Yes > No | an approval-type vote happens). One interpretive risk: the FDA may phrase the vote as "has substantial evidence of effectiveness been demonstrated?". I treat that as the governing approval-type vote.

### Outside view

FDA advisory committees vote in favour of the sponsor somewhat more often than not; published reviews of adcomm votes put the favourable share at roughly 60–65%. This sub-class is less favourable: the review division has already issued a Complete Response Letter (CRL), so its briefing document will argue against the drug, and panels follow a negative FDA briefing more often than not. Against that, this meeting is unusual. It was convened by the Office of Specialty Medicine during a sponsor's formal dispute of a CRL that found no safety or quality deficiencies. Office-level dispute reviewers usually uphold divisions, so choosing to convene a panel instead suggests genuine openness at the office level. I take a prior of about 50% for "post-CRL, efficacy-only dispute, panel convened" (no clean n is available; this is a judgement).

### Inside view

Factors for YES:
- The pivotal Phase 3 STAR trial (n=847) met its prespecified primary endpoint (p=0.0226) and its key secondary endpoint, annual progression rate (p=0.0002) [1][3].
- There is no safety or quality deficiency [3][4], so the benefit-risk question tilts toward benefit when the risk side is near-benign.
- Clinical consensus and practice already use low-dose atropine, compounded in the US [2][5]. The drug is approved in the EU and UK.
- The sponsor asked for practising pediatric ophthalmologists and optometrists on the panel, and an Open Public Hearing will carry clinician and caregiver voices [1][6].
- The FDA has said the panel will *not* be asked whether the primary endpoint was met [7], so the debate is about clinical meaningfulness, where clinicians lean favourable.
- Trade press since the CRL has framed it as "shifting goalposts" against clinical consensus [8].

Factors for NO:
- The FDA's own conclusion was that the data "did not support effectiveness" [3].
- STAR measured no axial-length endpoint [2], and the 0.01% dose is the weakest one in the literature. LAMP-type data show little axial-length effect at 0.01%, and academic panelists will know this.
- The overall effect looks modest: the primary-endpoint p-value is only 0.02, and the benefit is concentrated in fast progressors [4].
- Current FDA leadership is sceptical about modest-effect approvals, and briefing documents frame panels.

Net: I move up from the ~50% prior to about 62%. A met primary endpoint, a benign safety profile and clinician-heavy pressure usually win benefit-risk votes in ophthalmology. A strongly negative FDA briefing, which comes out about 2 business days before the meeting and after this forecast closes, is the main downside risk. The IQR is wide (50–72%) because the briefing document and the exact vote question are unknown.

### Evidence

- 2025-10-23: The FDA issued a CRL. The primary endpoint was met and no safety or quality deficiencies were found, but the agency said the data did not support effectiveness [3][4].
- Late 2025: Sydnexis filed a Formal Dispute Resolution Request with the Office of Specialty Medicine [1].
- 2026-07-13: The FDA said it intends to convene an advisory committee. The panel "will be asked to discuss various aspects of the application, including findings from the Phase 3 STAR study", and not whether the primary endpoint was hit [1][7].
- A Federal Register notice set the DODAC meeting for October 30, 2026 (docket FDA-2026-N-10606), with briefing materials due no later than 2 business days before it [6].
- 2026-10-07 and 2026-10-14: Pediatric ophthalmologists (Wilson, Fredrick) described the unmet need for an approved, stable product. They noted possible dilution of the effect by older children and the missing axial-length endpoint, and expected the FDA to look past the primary endpoint and possibly reconsider [2].
- 2026-10-13: Ophthalmology Times FAQ: the meeting is confirmed for October 30; no vote question is public yet [5].
- In the fast-progressor subgroup (more than −0.5 D/yr), progression was reduced by more than 50% at month 36 [4].

### Other forecasters

| Source | Value | As of | Note |
|---|---|---|---|
| Metaculus CP | hidden — bot tournament | 2026-10-19 | — |
| Polymarket / Kalshi / Manifold | no market found | 2026-10-19 | — |

### What would change my mind

- **The FDA briefing document** (about October 28). If it argues that the effect is not clinically meaningful, for example a sub-0.1 D/yr difference with no axial-length support, a NO becomes more likely than not. A neutral or mixed briefing pushes toward 70%+.
- **The vote wording.** "Substantial evidence of effectiveness" is a harder bar than "benefits outweigh risks", and a benefit-risk question favours YES because the safety side is clean.

### Sources

1. Sydnexis press release, "Sydnexis Announces FDA Advisory Committee Meeting to Review NDA for SYD-101", Business Wire, 2026-07-13 — https://www.businesswire.com/news/home/20260713332414/en/Sydnexis-Announces-FDA-Advisory-Committee-Meeting-to-Review-NDA-for-SYD-101-for-Pediatric-Progressive-Myopia (accessed 2026-10-19)
2. Healio, "Pediatric experts examine FDA's review of SYD-101", 2026-10-07 — https://www.healio.com/news/ophthalmology/20261014/pediatric-experts-examine-fdas-review-of-syd101-genetic-testing-for-myopia (accessed 2026-10-19)
3. Optometry Times, "FDA sends CRL to Sydnexis for SYD-101", 2025-10-24 — https://www.optometrytimes.com/view/fda-sends-crl-to-sydnexis-for-syd-101-to-slow-myopia-in-children (accessed 2026-10-19)
4. Ophthalmology Times, "FDA issues complete response letter to Sydnexis for SYD-101", 2025-10-24 — https://www.ophthalmologytimes.com/view/fda-issues-complete-response-letter-to-sydnexis-for-syd-101-in-pediatric-myopia (accessed 2026-10-19)
5. Ophthalmology Times, "FAQ: SYD-101 heads to FDA advisory committee", 2026-10-13 — https://www.ophthalmologytimes.com/view/faq-syd-101-heads-to-fda-advisory-committee-what-clinicians-should-know (accessed 2026-10-19)
6. Federal Register public inspection, DODAC meeting notice — https://public-inspection.federalregister.gov/2026-19700.pdf (accessed 2026-10-19)
7. BioCentury, "FDA taking another look at eye therapy rejected under Makary", 2026-07-13 — https://www.biocentury.com/article/660097/fda-taking-another-look-at-eye-therapy-rejected-under-makary (accessed 2026-10-19)
8. BioCentury, "Sydnexis setback highlights FDA's lack of transparency, concerns about shifting goalposts", 2025-11-21 — https://www.biocentury.com/article/657679/sydnexis-setback-highlights-fda-s-lack-of-transparency-concerns-about-shifting-goalposts (accessed 2026-10-19)

**Question**: [At its October 30, 2026 meeting, will the FDA Dermatologic and Ophthalmic Drugs Advisory Committee vote in favor of SYD-101 (atropine 0.01%) for pediatric progressive myopia?](https://www.metaculus.com/questions/46125/)
**Date**: 2026-10-19
**Forecast**: Median 62.0%, IQR [50.0%, 72.0%]
**Thesis**: Advisory committees side with sponsors about 60% of the time, but less often after an FDA rejection. Here the rejection is efficacy-only, the trial met its primary endpoint with a clean safety profile, clinical consensus is pro-atropine, and the panel was convened through the sponsor's formal dispute, which tilts a benefit-risk vote toward YES. The forecast is most sensitive to how harshly the FDA briefing frames the modest 0.01% effect and the missing axial-length data.
