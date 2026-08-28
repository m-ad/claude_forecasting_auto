@AGENTS.md

## Claude Code specifics

- Project skills live in `.claude/skills/`; slash commands in `.claude/commands/`.
  `SKILLS.md` is the index — read it if you are unsure which skill applies.
- Slash commands: `/forecast`, `/update`, `/resolve`, `/status`, `/review`.
- Long research runs: spawn subagents for independent evidence streams (e.g. one per
  scenario branch or per data source), then integrate yourself. Do **not** delegate
  the final probability judgement — integration is where calibration lives.
- Use the TodoWrite/task list for any forecast: the workflow has ≥ 6 steps.

## Git

- Never `git commit` unless asked. Committing forecasts is the operator's call.
  (An explicit instruction to commit and push — e.g. from a harness running you on a
  feature branch — supersedes this.)
- **Rebase before every push.** The remote moves under you: other sessions and merged
  PRs land on `main` while a long forecast run is in progress.

  ```bash
  git pull --rebase origin <branch>       # or: git fetch origin && git rebase origin/main
  git push -u origin <branch>
  ```

  Conflicts in `ledger/forecasts.jsonl` are append-only by construction: keep **both**
  sides, in timestamp order. Never resolve a ledger conflict by dropping a line — rule 8
  (never edit or delete a past forecast) applies to conflict resolution too.
- Push failures that look like network errors: retry up to 4 times with exponential
  backoff (2s, 4s, 8s, 16s) before concluding the push is blocked.

### Fallback: push via the GitHub MCP server

If `git push` still fails after those retries — auth failure, 403/407 from the proxy, no
credential helper, remote rejected — do **not** leave the work sitting in the container.
The container is ephemeral; an unpushed forecast is a lost forecast. Fall back to the
GitHub MCP tools (`mcp__github__*`), which authenticate independently of git:

1. `mcp__github__create_branch` — only if the branch does not exist on the remote yet
   (`owner: m-ad`, `repo: claude_forecasting`, `from_branch: main`).
2. `mcp__github__push_files` — all changed files in one commit. Pass each file's full
   post-edit content, not a diff. This is the right tool for a forecast: `meta.yaml`,
   `forecast.md`, `research.md`, `raw/*.json` and the ledger file go in a single call.
   Use `mcp__github__create_or_update_file` only for a genuine one-file change; it needs
   the existing blob SHA (`git rev-parse <branch>:<path>`).
3. Re-sync the local checkout so it does not diverge from what you pushed:
   `git fetch origin <branch> && git reset --hard origin/<branch>`.

Know the limits before relying on it:

- `push_files` **cannot delete or rename files** — it only creates and updates. A change
  that removes a file needs a working `git push`; say so rather than pushing a partial
  state.
- Binary files (chart PNGs under `questions/<slug>/charts/`) cannot be sent as text
  content. If only the MCP path works, push the text files and tell the operator which
  charts are still local-only.
- The commit lands with the GitHub App as committer, not the local git identity.
- `push_files` commits against the remote tip, so a rebase is not a substitute for
  re-reading files another session may have changed — re-fetch before you build the
  payload if the branch moved.

Say which path succeeded — `git push` or the MCP fallback — in the summary you give the
operator, along with anything the fallback could not carry.
