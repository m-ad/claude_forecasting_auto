"""``forecast.md`` structure, and its agreement with ``meta.yaml``.

``docs/output-format.md`` fixes this format: a header block that is rewritten in
place on every update, then append-only version sections newest-first, each
ending with the same three-line summary. The header is the only part a reader
sees before scrolling, so a header that disagrees with ``meta.yaml`` is a
publishing bug, not a cosmetic one.
"""

from __future__ import annotations

import re

import pytest
from conftest import as_date, metas, question_dirs, require_date

METAS = dict(metas())
DIRS = [d for d in question_dirs() if (d / "forecast.md").is_file()]
DIR_IDS = [d.name for d in DIRS]

VERSION_HEADING_RE = re.compile(
    r"^## v(\d+)\s+[-–—]\s+(.+?)\s+[-–—]\s+(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE
)
HEADER_ROW_RE = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$", re.MULTILINE)
SENTINEL = "<!-- Versions below, newest first. APPEND-ONLY: never edit or delete a past version. -->"

REQUIRED_SECTIONS = [
    "### What resolves YES",
    "### Outside view",
    "### Inside view",
    "### Evidence",
    "### Other forecasters",
    "### Scenarios",
    "### Sensitivity",
    "### What would change my mind",
    "### Sources",
]
REQUIRED_HEADER_ROWS = [
    "Source",
    "Type",
    "Opened / Closes / Resolves",
    "Status",
    "Current forecast",
    "Next review",
]


def _text(folder):
    return (folder / "forecast.md").read_text(encoding="utf-8")


def _header_rows(text):
    """The leading key/value table, up to the append-only sentinel."""
    head = text.split(SENTINEL)[0]
    return {k.strip(): v.strip() for k, v in HEADER_ROW_RE.findall(head)}


def _version_blocks(text):
    """``[(version, kind, date, body)]`` newest-first, as written in the file."""
    marks = list(VERSION_HEADING_RE.finditer(text))
    blocks = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        blocks.append(
            (int(m.group(1)), m.group(2).strip(), m.group(3), text[m.end() : end])
        )
    return blocks


def _source_entries(body):
    """Split a ``### Sources`` body into entries, re-joining wrapped lines."""
    m = re.search(r"^### Sources\s*$(.*?)(?=^## |\Z)", body, re.MULTILINE | re.DOTALL)
    if not m:
        return []
    entries, current = [], None
    for line in m.group(1).splitlines():
        if re.match(r"^\d+\.\s", line):
            if current is not None:
                entries.append(current)
            current = line
        elif current is not None and line.strip():
            current += " " + line.strip()
        elif current is not None and not line.strip() and line != "":
            continue
    if current is not None:
        entries.append(current)
    return entries


# ------------------------------------------------------------------- header
@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_title_heading_matches_the_meta_title(folder):
    first = _text(folder).splitlines()[0]
    assert first.startswith("# "), (
        f"{folder.name}: forecast.md must open with an H1 title"
    )
    assert first[2:].strip() == str(METAS[folder.name].get("title")).strip(), (
        f"{folder.name}: forecast.md title differs from meta.yaml title"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_header_table_has_every_required_row(folder):
    rows = _header_rows(_text(folder))
    missing = [r for r in REQUIRED_HEADER_ROWS if r not in rows]
    assert not missing, f"{folder.name}: header block is missing rows {missing}"
    assert any(k.startswith("Community") for k in rows), (
        f"{folder.name}: header block has no Community row"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_header_current_forecast_matches_meta(folder):
    meta = METAS[folder.name]
    cur = meta.get("current") or {}
    if not cur.get("version"):
        pytest.skip("not forecast yet")
    row = _header_rows(_text(folder))["Current forecast"]
    if meta.get("type") != "binary":
        pytest.skip("percentage parsing only applies to binary questions")
    m = re.search(
        r"Median\s+([\d.]+)%,\s*IQR\s*\[([\d.]+)%,\s*([\d.]+)%\].*?\(v(\d+),\s*"
        r"(\d{4}-\d{2}-\d{2})\)",
        row,
    )
    assert m, f"{folder.name}: cannot parse the Current forecast row: {row!r}"
    med, lo, hi = (float(m.group(i)) for i in (1, 2, 3))
    assert (med, lo, hi) == pytest.approx(
        (
            round(cur["median"] * 100, 1),
            round(cur["iqr"][0] * 100, 1),
            round(cur["iqr"][1] * 100, 1),
        )
    ), (
        f"{folder.name}: header says {med}% [{lo}%, {hi}%] but meta.yaml says "
        f"{cur['median'] * 100}% [{cur['iqr'][0] * 100}%, {cur['iqr'][1] * 100}%]"
    )
    assert int(m.group(4)) == cur["version"], (
        f"{folder.name}: header version != meta version"
    )
    assert m.group(5) == str(as_date(cur["date"])), (
        f"{folder.name}: header forecast date != meta current.date"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_header_status_and_next_review_match_meta(folder):
    """The header is rewritten in place on every update, resolution included."""
    meta = METAS[folder.name]
    rows = _header_rows(_text(folder))
    assert rows["Status"].strip().lower() == str(meta.get("status")).lower(), (
        f"{folder.name}: header Status is {rows['Status']!r} but meta.yaml says "
        f"{meta.get('status')!r}"
    )
    shown, expected = rows["Next review"].strip(), meta.get("next_review")
    if expected is None:
        assert shown in {"-", "—", "", "none", "None"}, (
            f"{folder.name}: header still advertises a next review of {shown!r} "
            "while meta.yaml has none"
        )
    else:
        assert shown.startswith(str(as_date(expected))), (
            f"{folder.name}: header next review {shown!r} != meta {expected!r}"
        )


# ------------------------------------------------------------------ versions
@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_version_sections_are_newest_first_and_complete(folder):
    blocks = _version_blocks(_text(folder))
    assert blocks, f"{folder.name}: no '## vN - ... - DATE' section found"
    numbers = [b[0] for b in blocks]
    assert numbers == sorted(numbers, reverse=True), (
        f"{folder.name}: version sections are ordered {numbers}, expected newest first"
    )
    assert numbers == list(range(len(numbers), 0, -1)), (
        f"{folder.name}: version numbers {numbers} are not a contiguous 1..N set"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_version_count_matches_meta_current_version(folder):
    blocks = _version_blocks(_text(folder))
    expected = (METAS[folder.name].get("current") or {}).get("version") or 0
    assert len(blocks) == expected, (
        f"{folder.name}: forecast.md has {len(blocks)} version sections but "
        f"meta.yaml is at v{expected}"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_every_version_has_the_required_sections(folder):
    for version, _kind, _date, body in _version_blocks(_text(folder)):
        missing = [s for s in REQUIRED_SECTIONS if s not in body]
        assert not missing, f"{folder.name} v{version}: missing sections {missing}"


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_every_version_ends_with_the_fixed_summary_block(folder):
    for version, _kind, date, body in _version_blocks(_text(folder)):
        m = re.search(
            r"\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})\s*\n"
            r"\*\*Forecast\*\*:\s*(.+?)\s*\n"
            r"\*\*Thesis\*\*:\s*(.+)",
            body,
            re.DOTALL,
        )
        assert m, (
            f"{folder.name} v{version}: missing the fixed "
            "**Date** / **Forecast** / **Thesis** summary block"
        )
        assert m.group(1) == date, (
            f"{folder.name} v{version}: summary date {m.group(1)} != heading date {date}"
        )
        assert len(m.group(3).strip()) >= 40, (
            f"{folder.name} v{version}: thesis is too short to name its drivers"
        )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_summary_forecast_line_quotes_percentages_to_one_decimal(folder):
    """``docs/output-format.md``: one decimal place, and never rounded to 5%."""
    if METAS[folder.name].get("type") != "binary":
        pytest.skip("binary formatting only")
    for version, _kind, _date, body in _version_blocks(_text(folder)):
        m = re.search(
            r"\*\*Forecast\*\*:\s*Median\s+([\d.]+)%,\s*IQR\s*"
            r"\[([\d.]+)%,\s*([\d.]+)%\]",
            body,
        )
        assert m, f"{folder.name} v{version}: Forecast line is not in the fixed format"
        for value in m.groups():
            assert re.fullmatch(r"\d+\.\d", value), (
                f"{folder.name} v{version}: {value}% is not quoted to exactly one decimal"
            )
        med, lo, hi = (float(g) for g in m.groups())
        assert lo <= med <= hi, f"{folder.name} v{version}: median outside its own IQR"


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_version_dates_do_not_precede_the_question_folder(folder):
    created = require_date(
        (METAS[folder.name].get("dates") or {}).get("created"),
        f"{folder.name}: dates.created",
    )
    for version, _kind, date, _body in _version_blocks(_text(folder)):
        assert require_date(date, f"{folder.name} v{version} heading") >= created, (
            f"{folder.name} v{version} is dated {date}, before the folder was created"
        )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_update_versions_open_with_a_revision_table(folder):
    """Every update carries prior -> new with one driver per row."""
    for version, kind, _date, body in _version_blocks(_text(folder)):
        if version == 1:
            assert kind.lower().startswith("initial"), (
                f"{folder.name} v1 is labelled {kind!r}, expected 'Initial forecast'"
            )
            continue
        assert "### Revision" in body, f"{folder.name} v{version}: no Revision table"
        assert "### Tripwire check" in body, (
            f"{folder.name} v{version}: no tripwire check - the previous version's "
            "tripwire list is the update's search plan"
        )


# ------------------------------------------------------------------- sources
@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_sources_are_numbered_with_urls_and_access_dates(folder):
    for version, _kind, _date, body in _version_blocks(_text(folder)):
        entries = _source_entries(body)
        if len(entries) == 1 and "unchanged from v" in entries[0].lower():
            continue
        assert len(entries) >= 10, (
            f"{folder.name} v{version}: {len(entries)} numbered sources "
            "(the research policy's rule of thumb is >= 15)"
        )
        for entry in entries:
            if "http" not in entry:
                continue
            assert re.search(r"accessed\s+\d{4}-\d{2}-\d{2}", entry), (
                f"{folder.name} v{version}: source without an access date: {entry[:80]!r}"
            )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_relative_links_and_images_resolve_on_disk(folder):
    """A chart linked but never written is an invisible hole in the deliverable."""
    text = _text(folder)
    broken = []
    for target in re.findall(r"!?\[[^\]]*\]\(([^)\s]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (folder / target).exists():
            broken.append(target)
    assert not broken, f"{folder.name}: forecast.md links to missing files {broken}"


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_resolved_questions_carry_a_post_mortem(folder):
    """``docs/update-protocol.md``: the missing-tripwire line is the highest-value
    line in the repo, and it only exists in the post-mortem."""
    if METAS[folder.name].get("status") != "resolved":
        pytest.skip("not resolved")
    text = _text(folder)
    assert re.search(r"^## Resolution", text, re.MULTILINE), (
        f"{folder.name}: resolved but forecast.md has no '## Resolution' post-mortem"
    )
    assert "tripwire" in text.lower().split("## resolution")[-1], (
        f"{folder.name}: post-mortem does not discuss the tripwire that should have existed"
    )


@pytest.mark.parametrize("folder", DIRS, ids=DIR_IDS)
def test_research_log_is_not_an_empty_stub(folder):
    body = (folder / "research.md").read_text(encoding="utf-8")
    if not (METAS[folder.name].get("current") or {}).get("version"):
        pytest.skip("not forecast yet")
    assert len(body.strip().splitlines()) >= 20, (
        f"{folder.name}: research.md is a stub - the next update reads it to learn "
        "what was already ruled out"
    )
