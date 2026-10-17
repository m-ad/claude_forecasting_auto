#!/usr/bin/env bash
# Commit the bot's state and push it, surviving concurrent pushes from parallel jobs.
#
#   scripts/ci_commit.sh "<commit message>" [full]
#
# Order: stage bot paths -> regenerate INDEX.md -> validate -> commit -> rebase onto
# the remote -> regenerate INDEX.md again -> push, retrying with exponential backoff
# (CLAUDE.md). The append-only ledgers merge with git's built-in `union` driver
# (.gitattributes), so two jobs appending to the same ledger rebase cleanly. INDEX.md
# is generated, so on a rebase conflict either side will do (`ours` driver, defined
# below): it is regenerated from the merged questions right after.
#
# A failing validation still commits, then fails the job. That is deliberate: by
# the time this runs, a forecast may already be live on Metaculus, and its record
# is what stops a second submission. Losing the record to keep the suite green
# would trade a visible test failure for an invisible rules violation.
set -uo pipefail

msg="${1:?commit message required}"
scope="${2:-fast}"
branch="${BOT_BRANCH:-main}"

git config merge.ours.driver true

reindex() {
  uv run scripts/status.py --index >/dev/null && git add INDEX.md
}

git add -A questions ledger 2>/dev/null
if git diff --cached --quiet; then
  echo "nothing to commit"
  exit 0
fi
reindex

validation=ok
if [ "$scope" = full ]; then
  uv run pytest -q || validation=failed
else
  # The data tests over the bot's own files; the code did not change in this run.
  uv run pytest -q tests/test_meta.py tests/test_ledger.py tests/test_consistency.py \
    tests/test_forecast_md.py || validation=failed
fi
[ "$validation" = ok ] || msg="$msg [validation failed]"

git commit -q -m "$msg" || { echo "::error::git commit failed"; exit 1; }

pushed=""
for wait in 2 4 8 16 0; do
  if git pull --rebase -q origin "$branch"; then
    reindex
    git diff --cached --quiet || git commit -q --amend --no-edit
    if git push -q origin "HEAD:$branch"; then
      pushed=1
      break
    fi
  fi
  git rebase --abort 2>/dev/null || true
  [ "$wait" = 0 ] && break
  echo "push failed; retrying in ${wait}s"
  sleep "$wait"
done
if [ -z "$pushed" ]; then
  echo "::error::could not push to $branch after 5 attempts"
  exit 1
fi
echo "pushed to $branch: $msg"
if [ "$validation" != ok ]; then
  echo "::error::state committed despite failing validation - see the pytest output above"
  exit 1
fi
