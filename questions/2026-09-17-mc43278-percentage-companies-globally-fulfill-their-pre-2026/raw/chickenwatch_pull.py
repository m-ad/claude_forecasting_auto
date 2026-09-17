"""Pull the Chicken Watch progress tracker — the resolution source for Metaculus 43278.

The tracker page is a Next.js shell; the rows live in an Awesome Table view
(``-NqYH6wXir1Ia4I27P6G``) backed by a public Google Sheet and fetched by the widget through
the GViz (``gviz/tq``) endpoint. Driving the widget's filter UI is fragile, so we load the page
in Chromium, record the GViz payload off the wire, and re-apply the question's filter ourselves.

Run from the repo root::

    uv run questions/<slug>/raw/chickenwatch_pull.py

Writes ``chickenwatch-broiler-<date>.csv`` (the 650-row broiler slice; the full sheet is
~3.7 MB and 82% cage-free rows this question never touches) and
``chickenwatch-summary-<date>.json`` next to this file. Diffing two dated CSVs is how the
next update measures whether the fulfilled count has moved.
"""

from __future__ import annotations

import collections
import csv
import datetime as dt
import json
import os
import pathlib

os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
TRACKER = "https://chickenwatch.org/progress-tracker?filterK=Broiler"
# An honest HeadlessChrome UA is challenged outright, exactly as for the Metaculus skill.
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
# Sheet column label -> the name we keep in the CSV.
KEEP = {
    "Title Hidden": "company",
    "Victory Date NumberRangeFilter - Hidden": "victory_date",
    "Timeline NumberRangeFilter - Hidden": "timeline",
    "Reporting Fulfillment csvFilter - Hidden": "status",
    "Policy Sub-Type Hidden": "policy_version",
    "Continent 2 Hidden": "continent",
    "Country-Specific Policies 2 Hidden": "country",
    "Industry 2 Hidden": "industry",
    "Broiler Reporting Hidden": "criteria_reported",
    "Description Hidden": "description",
}
ISSUE = "Issue csvFilter - Hidden"
STATUS = "Reporting Fulfillment csvFilter - Hidden"
VICTORY = "Victory Date NumberRangeFilter - Hidden"
TIMELINE = "Timeline NumberRangeFilter - Hidden"


def fetch_rows() -> list[dict[str, object]]:
    """Return every row of the tracker's backing sheet as a label-keyed dict."""
    payloads: list[str] = []
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/opt/pw-browsers/chromium",
            # The egress proxy resets Chromium's TLS 1.3 ClientHello; same fix as the
            # metaculus-aggregations skill's METACULUS_FORCE_TLS12 path.
            args=["--ssl-version-max=tls1.2", "--no-sandbox"],
        )
        page = browser.new_context(user_agent=UA).new_page()
        page.on(
            "response",
            lambda r: payloads.append(r.text()) if "gviz" in r.url else None,
        )
        page.goto(TRACKER, wait_until="networkidle", timeout=120_000)
        page.wait_for_timeout(20_000)
        browser.close()

    body = max(payloads, key=len)  # the data response; the other is a 2-row template probe
    table = json.loads(body[body.index("({") + 1 : body.rindex(")")])["table"]
    cols = [c.get("label") or c.get("id") for c in table["cols"]]

    def cell(row: dict, i: int) -> object:
        c = row["c"][i] if i < len(row["c"]) else None
        return None if c is None else c.get("v")

    return [{cols[i]: cell(r, i) for i in range(len(cols))} for r in table["rows"]]


def selected(rows: list[dict[str, object]]) -> list[dict[str, object]]:
    """Apply the fine print's filter: Broiler, Victory Date 1990-2025, Timeline >= 2026."""
    return [
        r
        for r in rows
        if str(r[ISSUE]) == "Broiler"
        and r[VICTORY] is not None
        and 1990 <= r[VICTORY] <= 2025
        and r[TIMELINE] is not None
        and r[TIMELINE] >= 2026
    ]


def main() -> None:
    stamp = dt.date.today().isoformat()
    rows = fetch_rows()
    broiler = [r for r in rows if str(r[ISSUE]) == "Broiler"]
    with (HERE / f"chickenwatch-broiler-{stamp}.csv").open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(KEEP.values()))
        writer.writeheader()
        for r in broiler:
            writer.writerow({v: r[k] for k, v in KEEP.items()})

    sel = selected(rows)
    counts = collections.Counter(str(r[STATUS]) for r in sel)
    summary = {
        "accessed": stamp,
        "source": TRACKER,
        "backing_sheet": (
            "docs.google.com/spreadsheets/d/"
            "1GcOfjaHy0xTPluZKUkxyNH8u0_qE7T6tdUpeUg7GEyI (sheet 'Cleaned')"
        ),
        "rows_total": len(rows),
        "rows_broiler": len(broiler),
        "q43278_filter": "Issue=Broiler, VictoryDate 1990-2025, Timeline >= 2026",
        "denominator": len(sel),
        "status_counts": dict(counts),
        "resolution_value_today_pct": round(
            100 * counts["Reporting Fulfilled"] / len(sel), 4
        ),
        "fulfilled_companies": [
            str(r["Title Hidden"]) for r in sel if r[STATUS] == "Reporting Fulfilled"
        ],
        "by_timeline": {
            int(tl): {
                "n": sum(1 for r in sel if r[TIMELINE] == tl),
                "fulfilled": sum(
                    1
                    for r in sel
                    if r[TIMELINE] == tl and r[STATUS] == "Reporting Fulfilled"
                ),
            }
            for tl in sorted({r[TIMELINE] for r in sel})
        },
    }
    (HERE / f"chickenwatch-summary-{stamp}.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
