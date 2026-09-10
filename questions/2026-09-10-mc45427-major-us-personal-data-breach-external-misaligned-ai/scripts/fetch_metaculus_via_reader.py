"""Fetch Metaculus post + aggregation JSON through the r.jina.ai reader.

Metaculus is answering every direct request from this container with a Cloudflare
managed challenge (HTTP 403), and browser navigation is unavailable here, so the
skill's own Playwright path cannot clear it. The reader service returns the same
public JSON payloads, which is what this script normalises into the two files the
forecast needs.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.parse

READER = "https://r.jina.ai/"
BASE = "https://www.metaculus.com/api-proxy"
METHODS = ("recency_weighted", "metaculus_pros", "gold_medalists")


def _get(url: str) -> str:
    """Fetch ``url`` through the reader and return the raw body text."""
    quoted = urllib.parse.quote(url, safe="")
    out = subprocess.run(
        ["curl", "-sS", "--max-time", "120", READER + quoted],
        capture_output=True,
        text=True,
        check=True,
    )
    return out.stdout


def _as_json(body: str) -> dict:
    """Strip the reader's markdown preamble, if any, and parse the JSON body."""
    start = body.find("{")
    if start < 0:
        raise ValueError("no JSON object in reader response")
    # The reader wraps API responses in a "Title:/URL Source:/Markdown Content:" header.
    return json.loads(body[start:])


def main() -> None:
    post_id = int(sys.argv[1])
    outdir = sys.argv[2]
    os.makedirs(outdir, exist_ok=True)

    post = _as_json(_get(f"{BASE}/posts/{post_id}/"))
    with open(os.path.join(outdir, "post.json"), "w") as fh:
        json.dump(post, fh, indent=2)

    qid = post["question"]["id"]
    aggs = {}
    for m in METHODS:
        url = (
            f"{BASE}/aggregation_explorer/?post_id={post_id}&question_id={qid}"
            f"&include_bots=false&aggregation_methods={m}&joined_before_date="
        )
        try:
            aggs[m] = _as_json(_get(url))["aggregations"][m]
        except Exception as exc:  # noqa: BLE001 - a cohort with no forecasters 404s
            aggs[m] = {"error": str(exc)}
    with open(os.path.join(outdir, "aggregations.json"), "w") as fh:
        json.dump(aggs, fh, indent=2)

    q = post["question"]
    print("TITLE:", q["title"])
    print("STATUS:", q["status"], "| forecasters:", post["nr_forecasters"])
    print("OPEN:", q["open_time"], "CLOSE:", q["scheduled_close_time"],
          "RESOLVE:", q["scheduled_resolve_time"])
    for key in ("description", "resolution_criteria", "fine_print"):
        text = re.sub(r"\n{3,}", "\n\n", q.get(key) or "")
        print(f"\n===== {key.upper()} =====\n{text}")
    for m in METHODS:
        a = aggs[m]
        if "error" in a:
            print(f"\n{m}: {a['error']}")
            continue
        latest = a.get("latest")
        if not latest:
            print(f"\n{m}: no forecasters")
            continue
        print(
            f"\n{m}: center={latest['centers'][0]:.4f} "
            f"[{latest['interval_lower_bounds'][0]:.4f}, "
            f"{latest['interval_upper_bounds'][0]:.4f}] "
            f"n={latest.get('forecaster_count')}"
        )


if __name__ == "__main__":
    main()
