"""Parse the 2026 section of the Wikipedia Israeli opinion-polling table.

Extracts, per poll row, the seat projections for Likud and Yashar plus the
fieldwork date, pollster and sample size. Column order is taken from the table
header; ``colspan`` on merged party columns is expanded so positional indexing
stays valid.
"""
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(__file__).with_name("wikipedia-polling-wikitext-2026-09-20.txt")
LINES = SRC.read_text(encoding="utf-8").splitlines()

# 2026 table runs from the "=== 2026 ===" heading to the "=== 2025 ===" heading.
start = next(i for i, l in enumerate(LINES) if l.strip() == "=== 2026 ===")
end = next(i for i, l in enumerate(LINES) if l.strip() == "=== 2025 ===")
block = LINES[start:end]

# Party columns after date/firm/publisher/sample, in header order.
COLS = ["Likud", "Together", "RZP", "Zehut", "Otzma", "BW", "Shas", "UTJ",
        "YB", "Raam", "JointList", "Dems", "Yashar", "Reserv", "NEP",
        "Amcha", "Haredi", "Others", "Gov"]


def clean(cell: str) -> str:
    cell = cell.lstrip("|").strip()
    c = re.sub(r"<ref[^>]*>.*?</ref>", "", cell, flags=re.DOTALL)
    c = re.sub(r"<ref[^>]*/>", "", c)
    c = re.sub(r"\{\{efn.*?\}\}", "", c, flags=re.DOTALL)
    c = re.sub(r"^\s*(style|class|colspan|rowspan)\s*=\s*\S+\s*\|", "", c).strip()
    c = c.replace("'''", "").strip()
    return c


def seats(cell: str) -> float | None:
    """Return the seat count, or None when the party is below threshold/absent."""
    c = clean(cell)
    if "{{small" in c or "N/A" in c or c in ("", "–", "-"):
        return None
    m = re.match(r"^(\d+(?:\.\d+)?)", c)
    return float(m.group(1)) if m else None


rows: list[dict] = []
cur: list[str] = []
for line in block:
    if line.startswith("|-"):
        if cur:
            rows.append(cur)  # type: ignore[arg-type]
        cur = []
    elif line.startswith(("|", "!")):
        cur.append(line)
if cur:
    rows.append(cur)

out = []
for cells in rows:
    if not cells or "Opdrts" not in cells[0]:
        continue
    if any("colspan=\"22\"" in c or "colspan=22" in c for c in cells):
        continue  # event divider row (list deadline etc.)
    datem = re.search(r"\{\{Opdrts\|([^}]*)\}\}", cells[0])
    if not datem:
        continue
    parts = [p for p in datem.group(1).split("|") if p]
    date = " ".join(parts)
    firm = clean(cells[1]) if len(cells) > 1 else ""
    firm = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", firm)
    pub = clean(cells[2]) if len(cells) > 2 else ""
    pub = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", pub)
    pub = re.sub(r"''", "", pub).strip()
    sample = clean(cells[3]) if len(cells) > 3 else ""

    # Expand colspan across the party columns.
    vals: dict[str, float | None] = {}
    idx = 0
    for cell in cells[4:]:
        span_m = re.search(r"colspan\s*=\s*\"?(\d+)", cell)
        span = int(span_m.group(1)) if span_m else 1
        v = seats(cell)
        for _ in range(span):
            if idx < len(COLS):
                vals[COLS[idx]] = v
            idx += 1
    out.append({"date": date, "firm": firm, "pub": pub, "n": sample,
                "likud": vals.get("Likud"), "yashar": vals.get("Yashar"),
                "gov": vals.get("Gov")})

print(f"{'date':<18}{'firm':<14}{'publisher':<18}{'n':>6}{'Likud':>7}{'Yashar':>8}{'Gov':>6}")
for r in out:
    print(f"{r['date']:<18}{r['firm'][:13]:<14}{r['pub'][:17]:<18}{str(r['n'])[:5]:>6}"
          f"{r['likud']!s:>7}{r['yashar']!s:>8}{r['gov']!s:>6}")
print(f"\n{len(out)} poll rows parsed")
