"""Summarise Likud-vs-Yashar seat gaps by pollster house and over time."""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from datetime import date

sys.path.insert(0, "questions/2026-09-20-mc45670-which-party-win-most-seats-2026-israeli/raw")

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# Right-leaning houses: Channel 14 (Shlomo Filber, ex-Netanyahu aide) and
# Direct Polls / i24. Kept separate because their Likud figures run ~10 seats
# above every other house.
RIGHT_HOUSES = {"Channel 14", "i24 News"}


def parse_date(s: str) -> date | None:
    parts = s.split()
    if len(parts) < 3:
        return None
    day = int(parts[-3]) if len(parts) == 4 else int(parts[0])
    mon = MONTHS.get(parts[-2])
    yr = int(parts[-1])
    if mon is None:
        return None
    return date(yr, mon, day)


rows = []
out = subprocess.run([sys.executable, "parse_polls.py"],
                     cwd="questions/2026-09-20-mc45670-which-party-win-most-seats-2026-israeli/raw",
                     capture_output=True, text=True, check=True).stdout
for line in out.splitlines()[1:]:
    if not line.strip() or "poll rows parsed" in line:
        continue
    m = re.match(r"^(.{18})(.{14})(.{18})(.{6})(.{7})(.{8})", line)
    if not m:
        continue
    d = parse_date(m.group(1).strip())
    firm, pub = m.group(2).strip(), m.group(3).strip()
    try:
        likud, yashar = float(m.group(5)), float(m.group(6))
    except ValueError:
        continue
    if d is None or likud > 45 or yashar > 45:   # drop the one rowspan-mangled row
        continue
    rows.append((d, firm, pub, likud, yashar))

rows.sort(key=lambda r: r[0], reverse=True)

print("=== By house, polls since 2026-08-01 ===")
by_house = defaultdict(list)
for d, firm, pub, l, y in rows:
    if d >= date(2026, 8, 1):
        by_house[pub].append((d, l, y))
for pub, v in sorted(by_house.items(), key=lambda kv: -len(kv[1])):
    gaps = [l - y for _, l, y in v]
    print(f"{pub[:20]:<22} n={len(v):<3} mean Likud={sum(l for _,l,_ in v)/len(v):5.1f} "
          f"mean Yashar={sum(y for _,_,y in v)/len(v):5.1f} mean gap={sum(gaps)/len(gaps):+5.1f} "
          f"Likud-leads={sum(g>0 for g in gaps)}/{len(v)}")

print("\n=== Last 12 polls (most recent first) ===")
for d, firm, pub, l, y in rows[:12]:
    tag = "R" if pub in RIGHT_HOUSES else " "
    print(f"{d} {tag} {pub[:18]:<20} Likud {l:4.0f}  Yashar {y:4.0f}  gap {l-y:+4.0f}")

print("\n=== Fortnightly means, mainstream houses only (Ch14 + i24 excluded) ===")
buckets: dict[str, list[tuple[float, float]]] = defaultdict(list)
for d, firm, pub, l, y in rows:
    if pub in RIGHT_HOUSES or d < date(2026, 6, 1):
        continue
    key = f"{d.isoformat()[:7]}-{'a' if d.day <= 15 else 'b'}"
    buckets[key].append((l, y))
for k in sorted(buckets):
    v = buckets[k]
    ml = sum(l for l, _ in v) / len(v)
    my = sum(y for _, y in v) / len(v)
    print(f"{k}  n={len(v):<3} Likud {ml:5.2f}  Yashar {my:5.2f}  gap {ml-my:+5.2f}")

print("\n=== Same, right-leaning houses only ===")
buckets2: dict[str, list[tuple[float, float]]] = defaultdict(list)
for d, firm, pub, l, y in rows:
    if pub not in RIGHT_HOUSES or d < date(2026, 6, 1):
        continue
    key = f"{d.isoformat()[:7]}-{'a' if d.day <= 15 else 'b'}"
    buckets2[key].append((l, y))
for k in sorted(buckets2):
    v = buckets2[k]
    ml = sum(l for l, _ in v) / len(v)
    my = sum(y for _, y in v) / len(v)
    print(f"{k}  n={len(v):<3} Likud {ml:5.2f}  Yashar {my:5.2f}  gap {ml-my:+5.2f}")

print(f"\ntotal usable poll rows: {len(rows)}")
