"""``VALIDATE_SLUG``: a sweep job validates its own question, not everyone's.

``ci_commit.sh`` runs the data tests after each forecast. Over every folder, one
malformed file (forecast 46586's undated source, 2026-11-16) failed its own job and
then every later job, whose commits were all marked ``[validation failed]``.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
from conftest import REPO, item_slug, question_dirs, scope_items

A, B = "2026-11-16-mc1-a", "2026-11-16-mc2-b"
KNOWN = {A, B}


def _item(**params):
    return SimpleNamespace(callspec=SimpleNamespace(params=params)) if params else SimpleNamespace()


@pytest.mark.parametrize(
    ("params", "slug"),
    [
        ({"folder": Path("questions") / A}, A),
        ({"slug": A, "meta": {}}, A),
        ({"lineno": 3, "rec": {"slug": A}}, A),
        ({"lineno": 3, "raw": json.dumps({"slug": A})}, A),
        ({"lineno": 3, "raw": "{not json"}, None),
        ({"lineno": 3, "rec": {"event": "forecast"}}, None),
        ({"x": 1}, None),
    ],
    ids=["folder", "slug", "rec", "raw", "bad-raw", "rec-no-slug", "unrelated"],
)
def test_item_slug_reads_every_data_test_parameter(params, slug):
    assert item_slug(params) == slug


def test_scope_drops_only_other_questions_cases():
    own, other = _item(slug=A), _item(folder=Path(B))
    unparametrised, unknown = _item(), _item(slug="s")
    bad_line = _item(lineno=1, raw="{not json")
    kept, dropped = scope_items([own, other, unparametrised, unknown, bad_line], A, KNOWN)
    # Cross-question tests and anything not tied to a known question still run.
    assert kept == [own, unparametrised, unknown, bad_line]
    assert dropped == [other]


def test_an_unknown_target_is_an_error_not_an_empty_run():
    # A typo must not deselect every per-question test and pass vacuously.
    with pytest.raises(pytest.UsageError, match="no question folder"):
        scope_items([_item(slug=A)], "2026-11-16-mc9-typo", KNOWN)


@pytest.mark.skipif(not question_dirs(), reason="no question folders")
def test_validate_slug_scopes_a_real_collection():
    target = question_dirs()[0].name
    env = {**os.environ, "VALIDATE_SLUG": target}
    out = subprocess.run(
        [sys.executable, "-m", "pytest", "--collect-only",
         "tests/test_forecast_md.py", "tests/test_consistency.py"],
        cwd=REPO, env=env, capture_output=True, text=True, check=True,
    ).stdout
    ids = [line for line in out.splitlines() if "::" in line]
    assert any(target in i for i in ids)
    others = {d.name for d in question_dirs()} - {target}
    assert not [i for i in ids if any(o in i for o in others)]
    assert any("test_index_lists_every_question_exactly_once" in i for i in ids)
