"""Agreement between the three places a forecast is recorded.

``meta.yaml`` (triage), ``ledger/forecasts.jsonl`` (scoring) and ``INDEX.md``
(the human entry point) are written by different code paths at different times.
Nothing keeps them in step except ``log_forecast.py`` being run for every change,
so drift between them is the failure mode this module exists to catch.
"""

from __future__ import annotations

import re

import pytest
from conftest import (
    REPO,
    as_date,
    forecast_records,
    metas,
    question_dirs,
    resolution_records,
)

METAS = metas()
IDS = [slug for slug, _ in METAS]
FORECASTS = [r for _, r in forecast_records()]
RESOLUTIONS = [r for _, r in resolution_records()]


def _ledger_versions(slug):
    return [r for r in FORECASTS if r.get("slug") == slug]


# --------------------------------------------------------- meta <-> ledger
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_every_forecast_in_meta_is_logged_in_the_ledger(slug, meta):
    """Rule 7: an unlogged forecast cannot be scored."""
    version = (meta.get("current") or {}).get("version") or 0
    logged = _ledger_versions(slug)
    if version == 0:
        assert not logged, f"{slug}: ledger has records but meta.yaml is still at v0"
        return
    assert logged, f"{slug}: meta.yaml is at v{version} but the ledger has no record"
    assert max(r["version"] for r in logged) == version, (
        f"{slug}: ledger tops out at v{max(r['version'] for r in logged)} "
        f"but meta.yaml says v{version}"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_meta_current_equals_the_latest_ledger_record(slug, meta):
    cur = meta.get("current") or {}
    logged = _ledger_versions(slug)
    if not cur.get("version") or not logged:
        pytest.skip("nothing logged yet")
    latest = max(logged, key=lambda r: r["version"])
    assert cur["median"] == latest["median"], (
        f"{slug}: meta median {cur['median']} != ledger median {latest['median']}"
    )
    assert list(cur["iqr"]) == list(latest["iqr"]), (
        f"{slug}: meta IQR {cur['iqr']} != ledger IQR {latest['iqr']}"
    )
    for key in ("cp", "pro", "gold", "n_forecasters"):
        assert (cur.get("community") or {}).get(key) == (
            latest.get("community") or {}
        ).get(key), f"{slug}: community.{key} differs between meta.yaml and the ledger"
    assert meta.get("type") == latest.get("type"), (
        f"{slug}: type differs from the ledger"
    )
    assert meta.get("source") == latest.get("source"), (
        f"{slug}: source differs from the ledger"
    )
    assert meta.get("post_id") == latest.get("post_id"), (
        f"{slug}: post_id differs from the ledger"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_resolution_is_recorded_in_both_places_or_neither(slug, meta):
    logged = [r for r in RESOLUTIONS if r.get("slug") == slug]
    resolved = meta.get("status") == "resolved"
    assert resolved == bool(logged), (
        f"{slug}: meta status is {meta.get('status')!r} but the ledger has "
        f"{len(logged)} resolution record(s)"
    )
    if resolved:
        assert meta["resolution"]["outcome"] == logged[0]["outcome"], (
            f"{slug}: outcome {meta['resolution']['outcome']!r} in meta.yaml != "
            f"{logged[0]['outcome']!r} in the ledger"
        )
        assert meta["resolution"]["source"] == logged[0]["resolution_source"], (
            f"{slug}: resolution source text differs between meta.yaml and the ledger"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_resolution_date_is_not_before_the_last_forecast(slug, meta):
    if meta.get("status") != "resolved":
        pytest.skip("not resolved")
    res_date = as_date(meta["resolution"]["date"])
    cur_date = as_date((meta.get("current") or {}).get("date"))
    if res_date is None or cur_date is None:
        pytest.skip("incomplete dates")
    assert res_date >= cur_date, (
        f"{slug}: resolved {res_date} before the current forecast dated {cur_date}"
    )


def test_ledger_has_no_records_for_deleted_questions():
    known = {d.name for d in question_dirs()}
    logged = {str(r.get("slug")) for r in FORECASTS + RESOLUTIONS}
    orphans = sorted(logged - known)
    assert not orphans, (
        f"the ledger scores questions with no folder: {orphans} - "
        "a deleted folder makes its history unauditable"
    )


# --------------------------------------------------------------- INDEX.md
INDEX = REPO / "INDEX.md"


def test_index_exists():
    assert INDEX.is_file(), "INDEX.md is missing - regenerate with status.py --index"


def _index_rows():
    rows = {}
    for line in INDEX.read_text(encoding="utf-8").splitlines():
        m = re.match(
            r"^\|\s*\[.*?\]\(questions/([^/]+)/forecast\.md\)\s*\|(.*)\|\s*$", line
        )
        if m:
            rows[m.group(1)] = [c.strip() for c in m.group(2).split("|")]
    return rows


def test_index_lists_every_question_exactly_once():
    listed, known = set(_index_rows()), {d.name for d in question_dirs()}
    assert listed == known, (
        f"INDEX.md is stale: missing={sorted(known - listed)} "
        f"unknown={sorted(listed - known)} - rerun scripts/status.py --index"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_index_row_agrees_with_meta(slug, meta):
    row = _index_rows().get(slug)
    if row is None:
        pytest.skip(
            "row missing; reported by test_index_lists_every_question_exactly_once"
        )
    qtype, current, version, _cp, _resolves, next_review, status = row[:7]
    cur = meta.get("current") or {}
    assert qtype == str(meta.get("type")), f"{slug}: INDEX.md type is stale"
    assert status == str(meta.get("status")), f"{slug}: INDEX.md status is stale"
    assert version == str(cur.get("version") or 0), f"{slug}: INDEX.md version is stale"
    expected_review = str(as_date(meta.get("next_review")) or "—")
    assert next_review == expected_review, (
        f"{slug}: INDEX.md next review {next_review!r} != meta {expected_review!r}"
    )
    if cur.get("median") is not None and meta.get("type") == "binary":
        assert current.startswith(f"{cur['median']:.1%}"), (
            f"{slug}: INDEX.md shows {current!r} but meta median is {cur['median']:.1%}"
        )
