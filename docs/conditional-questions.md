# Conditional questions — not supported yet

**Status (2026-11-14): not supported.** No script here can read a Metaculus conditional post.
Nothing needs it while the bot enters only bot tournaments, whose questions are binary,
numeric, discrete or multiple choice (`docs/tournament-protocol.md`, "Types"). **Implement
this before the bot enters a non-bot tournament** (the Metaculus Cup, say) or takes on an
individual conditional question.

## What a conditional post is

A conditional post asks "if A, then B?". Post 46448 is an example: "US–Iran war before December
2026? → Trump's net approval on 2026-12-31". It has no `question` and no `group_of_questions`.
Its `conditional` block holds:

| Field | What it is |
|---|---|
| `condition` | A, binary, on its own post |
| `condition_child` | B, the outcome question, on its own post |
| `question_yes`, `question_no` | the two forecastable **branches**: B if A resolves Yes / No. Both are on the conditional post, and their criteria are empty |

Metaculus annuls the branch whose condition did not happen. Only the realised branch is
scored, against B's outcome. The branches close with the condition.

## What happens today

Checked against post 46448 on 2026-11-14:

- `metaculus_api.py post 46448`: the snapshot comes back with every question field `null`.
- `new_question.py`: no type is found, so the folder is scaffolded as the `--type` default,
  `binary`. No question text is cached, which leaves a CI session with no criteria at all.
- `submit_metaculus.select_question`: refuses ("has no question to forecast").
- `tournament_poll.py`: `list_posts` asks only for binary, multiple-choice, numeric and
  discrete posts, which probably filters conditionals out (unverified). One that got through
  would be skipped as "group post (not supported)", a mislabel.

## What to implement

Port the workbench implementation: `m-ad/claude_forecasting` commit `44dbafd`, branch
`ccr-959d71bc-oropp4`; read it there before starting. The design is **one folder per branch**,
pinned with `?sub-question=<id>` as group sub-questions already are. Each branch is then an
ordinary question for the ledger, scoring and submission.

1. **Shared helpers** (`_common.py`): `post_subquestions(post)` returns a group's questions,
   or a conditional's two branches labelled "if yes" / "if no". `pinned_subquestion(url)`
   reads the pin.
2. **API snapshot** (`metaculus_api.question_snapshot`): for a branch, cache the branch
   question plus the **condition's and child's** criteria, fine print and background, joined
   and headed with their post ids. Add a `conditional` block naming the condition, the child
   and both branch ids. CI reads question text only from this snapshot.
3. **Scaffolder** (`new_question.py`):
   - take the type from the branches;
   - refuse a bare conditional URL and print the family plan (condition, child, if-yes,
     if-no, each marked as existing or with its scaffold command);
   - for a pinned branch, write the branch title, a `-if-yes` / `-if-no` slug and a
     `conditional:` block in `meta.yaml` (branch, condition and child post and question ids).
4. **Submitter** (`select_question`): resolve the pin against `post_subquestions`. Submission
   and the rationale comment are per branch. The comment goes to the conditional post, so
   check that two private comments on one post are acceptable.
5. **Family check** (`scripts/conditional.py`, from the workbench): every member scaffolded;
   open members forecast on the same day; the child coherent with the branch mixture
   `p * F_yes + (1 - p) * F_no`, p = P(A). Surface problems in `status.py`.
6. **Rules and docs**: forecast and update the whole family (condition, child, both branches)
   in one run. The workbench has this as AGENTS.md rule 9 and `docs/methodology.md` §9. Drop
   the annulled branch (`status: dropped`), and resolve the other with the child's outcome.
7. **Only if a scheduled tournament run should pick conditionals up**, extend
   `tournament_poll.py`:
   - include conditionals in the `list_posts` type filter (check the API's name for them);
   - emit one job per branch, keyed on the branch question id rather than the post id;
   - check "Metaculus already holds the bot's forecast" per branch;
   - scaffold or update the condition and the child in the same session. Under `one_shot`
     that would mean four one-shot questions in one window. An `updatable` tournament fits
     better.
8. **Tests first**, on a trimmed copy of post 46448: snapshot, scaffold (refusal and pinned
   branch), submission to the pinned branch, family check, poll (if item 7 is done). The
   workbench's `tests/test_conditional.py` is the template.
