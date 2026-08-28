"""Schema and internal consistency of every ``questions/<slug>/meta.yaml``.

``meta.yaml`` is the machine-readable half of a question: ``status.py`` triages
from it, ``log_forecast.py`` reads and rewrites it, and ``INDEX.md`` is generated
from it. Every one of those readers uses ``.get()`` chains that turn a missing or
misspelled key into a silently wrong row rather than an error, so the schema is
only enforced here.
"""

from __future__ import annotations

import datetime as dt
import re

import pytest
import yaml
from conftest import (
    COMMUNITY_KEYS,
    CURRENT_KEYS,
    DATE_KEYS,
    META_KEYS,
    QUESTION_TYPES,
    QUESTIONS,
    RESOLUTION_KEYS,
    SLUG_RE,
    SOURCES,
    SRC_ABBREV,
    STATUSES,
    TEMPLATES,
    TRIPWIRE_KEYS,
    as_date,
    is_number,
    is_probability,
    metas,
    question_dirs,
    require_date,
)

METAS = metas()
IDS = [slug for slug, _ in METAS]
DIRS = question_dirs()
DIR_IDS = [d.name for d in DIRS]

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")


# ------------------------------------------------------------- folder layout
def test_questions_directory_exists():
    assert QUESTIONS.is_dir(), "questions/ is missing"


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_folder_name_follows_the_naming_convention(folder):
    """``<YYYY-MM-DD>-<src><id>-<slug>``; ``find_slug`` and the index rely on it."""
    assert re.match(SLUG_RE, folder.name), (
        f"{folder.name} does not match <YYYY-MM-DD>-<mc|ks|pm|mf|x><id>-<slug>"
    )
    assert as_date(folder.name[:10]) is not None, (
        f"{folder.name}: the date prefix is not a real calendar date"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_scaffolded_files_all_exist(folder):
    for name in ("meta.yaml", "forecast.md", "research.md"):
        assert (folder / name).is_file(), f"{folder.name}/{name} is missing"
    assert (folder / "raw").is_dir(), (
        f"{folder.name}/raw/ is missing - rule 4 wants the snapshot trail kept"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_meta_parses_as_a_yaml_mapping(folder):
    data = yaml.safe_load((folder / "meta.yaml").read_text(encoding="utf-8"))
    assert isinstance(data, dict), f"{folder.name}/meta.yaml is not a YAML mapping"


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_no_unrendered_template_placeholders(folder):
    for name in ("meta.yaml", "forecast.md", "research.md"):
        text = (folder / name).read_text(encoding="utf-8")
        left = PLACEHOLDER_RE.findall(text)
        assert not left, f"{folder.name}/{name} still contains placeholders {left}"


# -------------------------------------------------------------- top-level keys
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_top_level_keys_are_exactly_the_schema(slug, meta):
    assert set(meta) == META_KEYS, (
        f"{slug}: missing={sorted(META_KEYS - set(meta))} "
        f"extra={sorted(set(meta) - META_KEYS)}"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_slug_field_matches_the_folder_name(slug, meta):
    assert meta.get("slug") == slug, (
        f"{slug}: meta.slug is {meta.get('slug')!r} - the ledger keys on the folder name"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_slug_encodes_the_source_and_post_id(slug, meta):
    src = meta.get("source")
    assert src in SOURCES, f"{slug}: unknown source {src!r}"
    m = re.match(r"^\d{4}-\d{2}-\d{2}-([a-z]{1,2})(\d*)-", slug)
    assert m and m.group(1) == SRC_ABBREV[src], (
        f"{slug}: folder abbreviation does not match source {src!r}"
    )
    pid = meta.get("post_id")
    assert pid is None or (isinstance(pid, int) and pid > 0), (
        f"{slug}: post_id must be a positive int or null, got {pid!r}"
    )
    if m.group(2):
        assert pid == int(m.group(2)), (
            f"{slug}: folder says post {m.group(2)} but meta.post_id is {pid}"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_folder_date_prefix_equals_the_created_date(slug, meta):
    created = as_date((meta.get("dates") or {}).get("created"))
    assert created is not None, f"{slug}: dates.created is missing or unparseable"
    assert created.isoformat() == slug[:10], (
        f"{slug}: folder date prefix != dates.created ({created.isoformat()})"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_title_url_type_and_tags(slug, meta):
    title = meta.get("title")
    assert isinstance(title, str) and title.strip(), f"{slug}: empty title"
    url = meta.get("url")
    assert isinstance(url, str) and url.startswith(("http://", "https://")), (
        f"{slug}: url {url!r} is not an absolute URL"
    )
    if meta.get("source") == "metaculus" and meta.get("post_id"):
        assert str(meta["post_id"]) in url, (
            f"{slug}: url does not contain post id {meta['post_id']}"
        )
    assert meta.get("type") in QUESTION_TYPES, (
        f"{slug}: unknown type {meta.get('type')!r}"
    )
    tags = meta.get("tags")
    assert isinstance(tags, list), f"{slug}: tags must be a list"
    for tag in tags:
        assert isinstance(tag, str) and re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*", tag
        ), f"{slug}: tag {tag!r} is not a lowercase kebab-case slug"


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_unit_is_set_iff_the_question_is_not_binary(slug, meta):
    unit = meta.get("unit")
    if meta.get("type") == "binary":
        assert unit is None, f"{slug}: binary questions carry no unit, got {unit!r}"
    else:
        assert unit is None or (isinstance(unit, str) and unit.strip()), (
            f"{slug}: unit must be a non-empty string or null"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_status_is_known(slug, meta):
    assert meta.get("status") in STATUSES, (
        f"{slug}: unknown status {meta.get('status')!r}, expected {sorted(STATUSES)}"
    )


# --------------------------------------------------------------------- dates
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_dates_block_shape(slug, meta):
    dates = meta.get("dates")
    assert isinstance(dates, dict), f"{slug}: dates must be a mapping"
    assert set(dates) == DATE_KEYS, (
        f"{slug}: dates keys {sorted(dates)} != {sorted(DATE_KEYS)}"
    )
    for key, value in dates.items():
        if value is None:
            continue
        assert as_date(value) is not None, (
            f"{slug}: dates.{key}={value!r} is not an ISO YYYY-MM-DD date"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_dates_run_in_the_right_order(slug, meta):
    raw = meta.get("dates") or {}
    d = {
        k: require_date(v, f"{slug}: dates.{k}")
        for k, v in raw.items()
        if v is not None
    }
    opened, closes = d.get("opened"), d.get("closes")
    resolves, created = d.get("resolves"), d.get("created")
    if opened and closes:
        assert opened <= closes, f"{slug}: opened is after closes"
    if closes and resolves:
        assert closes <= resolves, f"{slug}: closes is after resolves"
    if created and opened:
        assert opened <= created, (
            f"{slug}: the question opened after the folder was created"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_next_review_is_a_date_and_consistent_with_status(slug, meta):
    nxt = meta.get("next_review")
    if nxt is not None:
        assert as_date(nxt) is not None, f"{slug}: next_review {nxt!r} is not ISO"
    if meta.get("status") == "resolved":
        assert nxt is None, (
            f"{slug}: a resolved question keeps next_review null (log_forecast clears it)"
        )
    elif (meta.get("current") or {}).get("version"):
        assert nxt is not None, (
            f"{slug}: an open question with a forecast must schedule its next review"
        )


# ------------------------------------------------------------------- current
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_current_block_shape(slug, meta):
    cur = meta.get("current")
    assert isinstance(cur, dict), f"{slug}: current must be a mapping"
    assert set(cur) == CURRENT_KEYS, (
        f"{slug}: current keys {sorted(cur)} != {sorted(CURRENT_KEYS)}"
    )
    version = cur.get("version")
    assert isinstance(version, int) and version >= 0, (
        f"{slug}: current.version must be a non-negative int, got {version!r}"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_current_is_fully_populated_once_a_forecast_exists(slug, meta):
    cur = meta.get("current") or {}
    if not cur.get("version"):
        assert cur.get("median") is None, f"{slug}: v0 must not carry a median"
        return
    assert as_date(cur.get("date")) is not None, f"{slug}: current.date is not a date"
    assert is_number(cur.get("median")), f"{slug}: current.median must be numeric"
    iqr = cur.get("iqr")
    assert isinstance(iqr, list) and len(iqr) == 2 and all(is_number(v) for v in iqr), (
        f"{slug}: current.iqr must be two numbers, got {iqr!r}"
    )
    lo, hi = iqr
    assert lo <= cur["median"] <= hi, (
        f"{slug}: median {cur['median']} outside IQR [{lo}, {hi}]"
    )
    assert lo < hi, f"{slug}: degenerate IQR [{lo}, {hi}]"
    if meta.get("type") == "binary":
        for name, val in (
            ("median", cur["median"]),
            ("iqr lower", lo),
            ("iqr upper", hi),
        ):
            assert is_probability(val), (
                f"{slug}: binary {name} {val!r} is not a probability in [0, 1]"
            )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_current_date_is_not_in_the_future(slug, meta):
    d = as_date((meta.get("current") or {}).get("date"))
    if d is None:
        pytest.skip("no forecast yet")
    assert d <= dt.date.today(), f"{slug}: current.date {d} is in the future"


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_community_snapshot_shape(slug, meta):
    cur = meta.get("current") or {}
    com = cur.get("community")
    assert isinstance(com, dict), f"{slug}: current.community must be a mapping"
    assert set(com) == COMMUNITY_KEYS, (
        f"{slug}: community keys {sorted(com)} != {sorted(COMMUNITY_KEYS)}"
    )
    for key in ("cp", "pro", "gold"):
        val = com[key]
        if val is None:
            continue
        assert is_number(val), f"{slug}: community.{key} must be numeric or null"
        if meta.get("type") == "binary":
            assert is_probability(val), (
                f"{slug}: community.{key}={val} is not a probability in [0, 1]"
            )
    n = com["n_forecasters"]
    assert n is None or (isinstance(n, int) and n > 0), (
        f"{slug}: n_forecasters must be a positive int or null, got {n!r}"
    )
    if com["as_of"] is not None:
        assert as_date(com["as_of"]) is not None, (
            f"{slug}: community.as_of is not a date"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_community_snapshot_is_not_older_than_the_forecast_it_annotates(slug, meta):
    """Rule 4: fresh data only. A snapshot must not predate the forecast by weeks."""
    cur = meta.get("current") or {}
    as_of, date = (
        as_date((cur.get("community") or {}).get("as_of")),
        as_date(cur.get("date")),
    )
    if as_of is None or date is None:
        pytest.skip("no community snapshot")
    assert as_of <= date, (
        f"{slug}: community.as_of {as_of} is after the forecast date {date}"
    )
    assert (date - as_of).days <= 7, (
        f"{slug}: community snapshot is {(date - as_of).days}d older than the forecast"
    )


# ------------------------------------------------------------------ tripwires
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_tripwires_exist_once_a_forecast_does(slug, meta):
    """Rule 3: every forecast carries concrete, dated, observable tripwires."""
    tripwires = meta.get("tripwires")
    assert isinstance(tripwires, list), f"{slug}: tripwires must be a list"
    if (meta.get("current") or {}).get("version"):
        assert tripwires, f"{slug}: a forecast with no tripwires has no way to be wrong"


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_tripwire_entries_are_well_formed(slug, meta):
    for i, tw in enumerate(meta.get("tripwires") or []):
        where = f"{slug}: tripwire[{i}]"
        assert isinstance(tw, dict), f"{where} is not a mapping"
        assert set(tw) == TRIPWIRE_KEYS, (
            f"{where} keys {sorted(tw)} != {sorted(TRIPWIRE_KEYS)}"
        )
        assert isinstance(tw["signal"], str) and len(tw["signal"].strip()) >= 10, (
            f"{where}: signal must be a concrete observable statement"
        )
        assert as_date(tw["by"]) is not None, f"{where}: by={tw['by']!r} is not a date"
        assert tw["direction"] in {"up", "down", "either"}, (
            f"{where}: direction {tw['direction']!r} must be up/down/either"
        )
        mag = tw["magnitude_pp"]
        assert is_number(mag) and 0 <= mag <= 100, (
            f"{where}: magnitude_pp {mag!r} must be a number in [0, 100]"
        )
        if tw["direction"] == "either":
            assert mag == 0, (
                f"{where}: an 'either' tripwire carries no signed magnitude"
            )
        else:
            assert mag > 0, (
                f"{where}: a directional tripwire needs a non-zero magnitude"
            )
        assert (
            tw["fired"] is None
            or isinstance(tw["fired"], bool)
            or as_date(tw["fired"]) is not None
        ), f"{where}: fired must be null, a bool, or the date it fired"


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_tripwire_deadlines_do_not_run_past_resolution(slug, meta):
    resolves = as_date((meta.get("dates") or {}).get("resolves"))
    if resolves is None:
        pytest.skip("no resolution date")
    deadlines = [(tw, as_date(tw.get("by"))) for tw in (meta.get("tripwires") or [])]
    late = [
        str(tw["signal"])[:40]
        for tw, by in deadlines
        if by is not None and by > resolves
    ]
    assert not late, f"{slug}: tripwires expire after the question resolves: {late}"


# ----------------------------------------------------------------- resolution
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_resolution_block_matches_status(slug, meta):
    res = meta.get("resolution")
    assert isinstance(res, dict), f"{slug}: resolution must be a mapping"
    assert set(res) == RESOLUTION_KEYS, (
        f"{slug}: resolution keys {sorted(res)} != {sorted(RESOLUTION_KEYS)}"
    )
    if meta.get("status") == "resolved":
        assert res["outcome"] is not None, f"{slug}: resolved but no outcome recorded"
        assert as_date(res["date"]) is not None, (
            f"{slug}: resolved but no resolution date"
        )
        assert isinstance(res["source"], str) and res["source"].strip(), (
            f"{slug}: resolved but no resolution source cited"
        )
        if meta.get("type") == "binary":
            assert float(res["outcome"]) in (0.0, 1.0), (
                f"{slug}: binary outcome must be 1.0 or 0.0, got {res['outcome']!r}"
            )
    else:
        assert res["outcome"] is None, (
            f"{slug}: status is {meta.get('status')!r} but an outcome is recorded"
        )


# ------------------------------------------------------------------ templates
def test_template_meta_renders_to_the_same_schema():
    """The scaffold template and the schema the readers expect must not drift."""
    text = (TEMPLATES / "meta.yaml").read_text(encoding="utf-8")
    rendered = text
    for key, val in {
        "SLUG": "2026-01-01-x-demo",
        "TITLE": "Demo?",
        "SOURCE": "other",
        "URL": "https://example.org/",
        "POST_ID": "null",
        "TYPE": "binary",
        "TODAY": "2026-01-01",
    }.items():
        rendered = rendered.replace("{{" + key + "}}", val)
    assert not PLACEHOLDER_RE.search(rendered), (
        "template has placeholders the scaffold never fills"
    )
    data = yaml.safe_load(rendered)
    assert set(data) == META_KEYS, (
        f"templates/meta.yaml keys {sorted(data)} != schema {sorted(META_KEYS)}"
    )
    assert set(data["dates"]) == DATE_KEYS
    assert set(data["current"]) == CURRENT_KEYS
    assert set(data["current"]["community"]) == COMMUNITY_KEYS
    assert set(data["resolution"]) == RESOLUTION_KEYS
    assert data["current"]["version"] == 0 and data["status"] == "open"


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_meta_survives_the_save_load_roundtrip_scripts_perform(slug, meta):
    """``log_forecast`` rewrites meta.yaml via ``yaml.safe_dump`` on every log."""
    dumped = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    assert yaml.safe_load(dumped) == meta, (
        f"{slug}: meta.yaml does not round-trip through safe_dump - "
        "logging a forecast would corrupt it"
    )


# ----------------------------------------------------------- raw snapshot trail
@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_raw_snapshots_are_parseable_and_dated(folder):
    """Rule 4/5: the raw/ folder is the evidence trail; unreadable JSON is no trail."""
    import json

    for path in sorted((folder / "raw").glob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            pytest.fail(f"{folder.name}/raw/{path.name} is not valid JSON: {exc}")
        assert re.search(r"\d{4}-\d{2}-\d{2}", path.stem), (
            f"{folder.name}/raw/{path.name} carries no retrieval date in its filename"
        )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_a_forecast_question_has_at_least_one_raw_snapshot(folder):
    meta = dict(METAS).get(folder.name, {})
    if not (meta.get("current") or {}).get("version"):
        pytest.skip("not forecast yet")
    files = [p for p in (folder / "raw").iterdir() if p.is_file()]
    assert files, f"{folder.name}: forecast logged but raw/ is empty"
