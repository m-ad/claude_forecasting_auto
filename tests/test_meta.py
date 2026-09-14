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
    CONTINUOUS_TYPES,
    CURRENT_KEYS,
    DATE_KEYS,
    DATE_UNITS,
    META_KEYS,
    NATIVE_UNIT_TYPES,
    PERCENTILE_KEYS,
    PROBABILITY_TYPES,
    PROBABILITY_UNIT,
    QUESTION_TYPES,
    QUESTIONS,
    RESOLUTION_KEYS,
    SLUG_RE,
    SOURCES,
    SRC_ABBREV,
    STATUSES,
    TEMPLATES,
    TOURNAMENT_KEYS,
    TOURNAMENT_MODES,
    TRIPWIRE_KEYS,
    as_date,
    as_utc_datetime,
    is_number,
    is_probability,
    metas,
    question_dirs,
    registry_entries,
    require_date,
)

METAS = metas()
IDS = [slug for slug, _ in METAS]
DIRS = question_dirs()
DIR_IDS = [d.name for d in DIRS]

PLACEHOLDER_RE = re.compile(r"\{\{[A-Z_]+\}\}")

# `question_id` is required for every Metaculus question, because it - not
# `post_id` - is what the submit API addresses. The one legacy folder that
# predated the field covered a whole *question group* (post 45386 holds two
# subquestions, 2027 and 2028) and was carried by a named exemption; step P0.1
# cleared the legacy questions/ tree, so the exemption is gone and the rule is
# now unconditional. The bot scaffolds one folder per subquestion.


def _is_one_shot(meta) -> bool:
    """True for a bot-tournament question that is forecast once and never revisited."""
    return ((meta or {}).get("tournament") or {}).get("mode") == "one_shot"


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
    """``research.md`` is the one optional file, and only on the sweep path.

    A one-shot tournament question is forecast once inside a ~90-minute window
    and never revisited, so the working log has no second reader: the sources go
    straight into ``forecast.md``. Everything else is required everywhere -
    ``raw/`` in particular, because rule 4's snapshot trail is what makes a
    submitted forecast auditable after the fact.
    """
    required = ["meta.yaml", "forecast.md"]
    if not _is_one_shot(dict(METAS).get(folder.name, {})):
        required.append("research.md")
    for name in required:
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
        if not (folder / name).is_file():
            continue  # research.md is optional; its absence is reported elsewhere
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


# ------------------------------------------------- Metaculus question identity
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_question_id_is_an_int_for_metaculus_questions(slug, meta):
    """``post_id`` identifies the page; ``question_id`` is what the API submits to.

    They are different numbers, and a group post has one ``post_id`` and several
    ``question_id``s. Getting this wrong is not a visible error - the submit call
    returns 404 or, worse, writes a forecast onto the wrong subquestion - so the
    field is required up front rather than derived at submit time.
    """
    qid = meta.get("question_id")
    assert qid is None or (isinstance(qid, int) and qid > 0), (
        f"{slug}: question_id must be a positive int or null, got {qid!r}"
    )
    if meta.get("source") != "metaculus":
        assert qid is None, (
            f"{slug}: only Metaculus has the post/question split, got question_id {qid!r}"
        )
        return
    assert isinstance(qid, int), (
        f"{slug}: a Metaculus question needs question_id - post_id {meta.get('post_id')!r} "
        "cannot be submitted against"
    )


# ----------------------------------------------------------------- tournament
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_tournament_block_shape(slug, meta):
    tour = meta.get("tournament")
    if tour is None:
        return  # operator-added question; the whole block is absent by design
    assert isinstance(tour, dict), f"{slug}: tournament must be a mapping or null"
    assert set(tour) == TOURNAMENT_KEYS, (
        f"{slug}: tournament keys missing={sorted(TOURNAMENT_KEYS - set(tour))} "
        f"extra={sorted(set(tour) - TOURNAMENT_KEYS)}"
    )
    assert isinstance(tour["slug"], str) and tour["slug"].strip(), (
        f"{slug}: tournament.slug is empty"
    )
    assert tour["mode"] in TOURNAMENT_MODES, (
        f"{slug}: tournament.mode {tour['mode']!r} not in {sorted(TOURNAMENT_MODES)}"
    )
    assert as_date(tour["registered"]) is not None, (
        f"{slug}: tournament.registered {tour['registered']!r} is not a date"
    )
    for key in ("opened", "closes", "submitted"):
        if tour[key] is None:
            continue
        assert as_utc_datetime(tour[key]) is not None, (
            f"{slug}: tournament.{key}={tour[key]!r} is not a tz-aware ISO-8601 instant"
        )
    opened, closes = as_utc_datetime(tour["opened"]), as_utc_datetime(tour["closes"])
    if opened and closes:
        assert opened < closes, f"{slug}: the tournament window closes before it opens"
    for key in ("comment_posted", "missed_window"):
        assert isinstance(tour[key], bool), (
            f"{slug}: tournament.{key} must be a bool, got {tour[key]!r}"
        )
    score = tour["official_score"]
    assert score is None or is_number(score), (
        f"{slug}: tournament.official_score must be numeric or null, got {score!r}"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_tournament_slug_is_registered(slug, meta):
    """A question may only claim a tournament the registry actually knows about."""
    tour = meta.get("tournament") or {}
    if not tour.get("slug"):
        pytest.skip("not a tournament question")
    known = {s for s, _ in registry_entries()}
    assert tour["slug"] in known, (
        f"{slug}: tournament {tour['slug']!r} is not in tournaments/registry.yaml "
        f"(known: {sorted(known)})"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_one_shot_questions_carry_no_tripwires_and_no_next_review(slug, meta):
    """One shot means one shot: there is no second visit for a tripwire to trigger.

    Rule 3 still holds for every other question - this is the carve-out, and it is
    the *mode* that earns it, not the tournament.
    """
    if not _is_one_shot(meta):
        return
    assert meta.get("tripwires") == [], (
        f"{slug}: a one_shot question is never revisited, so its tripwires "
        f"{meta.get('tripwires')!r} can never fire"
    )
    assert meta.get("next_review") is None, (
        f"{slug}: a one_shot question schedules no review, got "
        f"{meta.get('next_review')!r}"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_a_submitted_one_shot_question_stays_at_version_one(slug, meta):
    """The append-only half of the one-shot rule, enforced on the question side.

    ``ledger/forecasts.jsonl`` refuses a second ``submission`` record; this refuses
    the v2 that would have been sent.
    """
    tour = meta.get("tournament") or {}
    if tour.get("submitted") is None or tour.get("mode") != "one_shot":
        pytest.skip("nothing submitted under a one-shot mode")
    version = (meta.get("current") or {}).get("version")
    assert version == 1, (
        f"{slug}: submitted at {tour['submitted']} but meta is at v{version} - "
        "a one-shot question is forecast exactly once"
    )
    assert tour.get("missed_window") is not True, (
        f"{slug}: a submitted question cannot also have missed its window"
    )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_missed_window_questions_are_closed_out_and_never_submitted(slug, meta):
    """A window the bot missed is a dead question, not an open one.

    Leaving it ``open`` would keep it in triage forever, and every later sweep
    would re-cost it.
    """
    tour = meta.get("tournament") or {}
    if not tour.get("missed_window"):
        return
    assert meta.get("status") in {"dropped", "resolved"}, (
        f"{slug}: missed_window is true but status is {meta.get('status')!r} - "
        "expected dropped (never forecast) or resolved (scored anyway)"
    )
    assert tour.get("submitted") is None, (
        f"{slug}: missed_window is true but a submission is recorded at "
        f"{tour['submitted']!r}"
    )


# ---------------------------------------------------------------- percentiles
@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_percentiles_shape_and_monotonicity(slug, meta):
    """The five-point CDF the continuous-question submit path sends.

    A non-monotone CDF is rejected by Metaculus with a 400 that names no field, so
    it is cheaper to catch here. The 25/50/75 points are the IQR and the median by
    definition: only the 10th and 90th carry information the forecast block does
    not already hold, and letting them drift apart would mean two disagreeing
    records of the same belief.
    """
    pcts = meta.get("percentiles")
    if pcts is None:
        return
    assert isinstance(pcts, dict), f"{slug}: percentiles must be a mapping or null"
    assert set(pcts) == PERCENTILE_KEYS, (
        f"{slug}: percentile keys {sorted(pcts)} != {sorted(PERCENTILE_KEYS)}"
    )
    assert meta.get("type") in CONTINUOUS_TYPES, (
        f"{slug}: percentiles only apply to {sorted(CONTINUOUS_TYPES)} questions, "
        f"not {meta.get('type')!r}"
    )
    values = [pcts[k] for k in sorted(PERCENTILE_KEYS)]
    assert all(is_number(v) for v in values), (
        f"{slug}: every percentile must be numeric, got {values!r}"
    )
    assert values == sorted(values), (
        f"{slug}: percentiles are not monotone non-decreasing: {values!r}"
    )
    cur = meta.get("current") or {}
    lo, hi = (list(cur.get("iqr") or [None, None]) + [None, None])[:2]
    for key, expected, name in (
        (25, lo, "current.iqr[0]"),
        (50, cur.get("median"), "current.median"),
        (75, hi, "current.iqr[1]"),
    ):
        if expected is None:
            continue
        assert pcts[key] == expected, (
            f"{slug}: percentiles[{key}]={pcts[key]!r} != {name}={expected!r}"
        )


@pytest.mark.parametrize("slug,meta", METAS, ids=IDS)
def test_a_submitted_continuous_question_carries_its_percentiles(slug, meta):
    """Rule 8's audit trail for a numeric submission is the CDF that was sent."""
    if (meta.get("tournament") or {}).get("submitted") is None:
        pytest.skip("nothing submitted")
    if meta.get("type") not in CONTINUOUS_TYPES:
        pytest.skip("not a continuous question")
    assert isinstance(meta.get("percentiles"), dict), (
        f"{slug}: a submitted {meta.get('type')} question must record the five-point "
        "CDF it sent, got percentiles=None"
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
    elif _is_one_shot(meta):
        pass  # asserted the other way round in the one-shot test below
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
        mag = tw["magnitude"]
        assert is_number(mag) and mag >= 0, (
            f"{where}: magnitude {mag!r} must be a non-negative number. It is "
            "unsigned - `direction` carries the sign"
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
def test_tripwire_magnitude_units_match_the_question_type(slug, meta):
    """A magnitude is only readable next to the forecast it moves.

    So the unit is not free-form: probability questions move in percentage
    points, date questions in time, and numeric questions in the question's own
    native unit. Enforcing the last one against ``meta["unit"]`` is what stops a
    numeric tripwire from being silently denominated in something else.
    """
    qtype = meta.get("type")
    native = meta.get("unit")
    for i, tw in enumerate(meta.get("tripwires") or []):
        where = f"{slug}: tripwire[{i}]"
        unit = tw.get("magnitude_unit")
        assert isinstance(unit, str) and unit.strip(), (
            f"{where}: magnitude_unit {unit!r} must be a non-empty string"
        )
        if qtype in PROBABILITY_TYPES:
            assert unit == PROBABILITY_UNIT, (
                f"{where}: a {qtype} question moves in {PROBABILITY_UNIT!r}, "
                f"not {unit!r}"
            )
            assert tw["magnitude"] <= 100, (
                f"{where}: magnitude {tw['magnitude']!r} pp exceeds the "
                "0-100 probability scale"
            )
        elif qtype == "date":
            assert unit in DATE_UNITS, (
                f"{where}: a date question moves in {sorted(DATE_UNITS)}, "
                f"not {unit!r}"
            )
        elif qtype in NATIVE_UNIT_TYPES:
            assert native, (
                f"{slug}: a {qtype} question with tripwires must set `unit`, so "
                "magnitudes have something to be denominated in"
            )
            assert unit == native, (
                f"{where}: magnitude_unit {unit!r} must be the question's native "
                f"unit {native!r}"
            )
            # Scale the sanity bound off the median *and* the IQR width: a
            # question centred near zero (a percent-change one, say) has no
            # useful |median|, but its band still says how big a real move is.
            current = meta.get("current") or {}
            median = current.get("median")
            lo, hi = (list(current.get("iqr") or [None, None]) + [None, None])[:2]
            scales = [abs(median)] if is_number(median) else []
            if is_number(lo) and is_number(hi):
                scales.append(abs(hi - lo))
            scale = max(scales, default=0)
            if scale:
                assert tw["magnitude"] <= scale, (
                    f"{where}: magnitude {tw['magnitude']!r} exceeds the whole "
                    f"forecast scale ({scale}, from median {median!r} and IQR "
                    f"{[lo, hi]}) - check the unit, this is usually a "
                    "percent-vs-native mix-up"
                )


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
        "QUESTION_ID": "null",
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
    # The scaffold is the operator path, which has no tournament and no CDF. Both
    # blocks are filled in later - by the sweep, or by log_forecast.py - so the
    # template must render them as explicit nulls rather than leave them out.
    assert data["tournament"] is None and data["percentiles"] is None, (
        "templates/meta.yaml must scaffold tournament and percentiles as null"
    )
    assert data["question_id"] is None, (
        "templates/meta.yaml must scaffold question_id as null - it is not knowable "
        "from the URL the operator pastes"
    )


def test_template_tripwire_examples_match_the_tripwire_schema():
    """The commented tripwire examples are what an author copies, so they have to
    satisfy the same schema the real files are checked against — otherwise the
    template teaches a shape the test suite rejects."""
    text = (TEMPLATES / "meta.yaml").read_text(encoding="utf-8")
    block = text.split("tripwires: []", 1)[1].split("resolution:", 1)[0]
    # Only the commented YAML itself: "# - signal: ..." and its "#   key: ..."
    # continuation lines. The surrounding prose comments are not part of it.
    uncommented = "\n".join(
        line[2:]
        for line in block.splitlines()
        if line.startswith(("# - ", "#   "))
    )
    examples = yaml.safe_load(uncommented) or []
    examples = [e for e in examples if isinstance(e, dict)]
    assert examples, "templates/meta.yaml has no copyable tripwire example"
    for i, tw in enumerate(examples):
        assert set(tw) == TRIPWIRE_KEYS, (
            f"template tripwire example[{i}] keys {sorted(tw)} != "
            f"{sorted(TRIPWIRE_KEYS)}"
        )
        assert as_date(tw["by"]) is not None
        assert tw["direction"] in {"up", "down", "either"}
        assert is_number(tw["magnitude"]) and tw["magnitude"] >= 0
        assert isinstance(tw["magnitude_unit"], str) and tw["magnitude_unit"].strip()
    units = {tw["magnitude_unit"] for tw in examples}
    assert PROBABILITY_UNIT in units and units - {PROBABILITY_UNIT}, (
        "the template should show both a probability example and a native-unit "
        f"one, got units {sorted(units)}"
    )


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
