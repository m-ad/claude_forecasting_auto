"""v2 (2026-10-09) re-run: start 2026-10-06 at 46,345; Sept-equivalent baseline
raised to ~150/day on the realised Aug-Sep rate (USDA 35,402 @ 07-29 -> 45,216 @ 09-30 = 156/day).
Scenario weights shifted slightly away from suppression (Aug deceleration did not persist).

Monte-Carlo projection of cumulative NWS animal cases in Mexico to 2027-06-29.

Structure: daily incidence = baseline_rate * seasonal_index(month) * trend(t).
The seasonal index is anchored on the observed Dec-2025 -> Jan-2026 collapse in
active cases and on the thermal biology of C. hominivorax (development halts
below ~14 C), which now bites harder because the active burden has moved into
temperate-highland and northern states.
"""
from __future__ import annotations

import datetime as dt

import numpy as np

RNG = np.random.default_rng(20261009)
N = 200_000

START = dt.date(2026, 10, 6)
END = dt.date(2027, 6, 29)          # last USDA report before 2027-07-01
DAYS = (END - START).days           # 266

CUM_NOW = 46_345                    # SENASICA cut 2026-10-06 (Tierra Fuerte); USDA 45,216 @ 2026-09-30
CUM_NOW_SD = 300

# Seasonal multipliers relative to September = 1.00
SEASON = {9: 1.00, 10: 0.95, 11: 0.80, 12: 0.55,
          1: 0.40, 2: 0.45, 3: 0.60, 4: 0.75, 5: 0.90, 6: 1.00}

# Scenario: (label, weight, terminal trend multiplier at 2027-06-29)
import sys

BASE = float(sys.argv[1]) if len(sys.argv) > 1 else 150.0
SCEN = [
    ("D  strong suppression",      0.12, 0.30),
    ("B  moderate suppression",    0.26, 0.60),
    ("A  flat plateau",            0.34, 1.00),
    ("C  renewed growth",          0.20, 1.50),
    ("E  autumn/spring surge",     0.08, 2.10),
]

dates = [START + dt.timedelta(days=i) for i in range(1, DAYS + 1)]
season = np.array([SEASON[d.month] for d in dates])
frac = np.linspace(0, 1, DAYS)      # linear interpolation of the trend

labels = [s[0] for s in SCEN]
weights = np.array([s[1] for s in SCEN])
terminal = np.array([s[2] for s in SCEN])

pick = RNG.choice(len(SCEN), size=N, p=weights)
term = terminal[pick] * np.exp(RNG.normal(0, 0.18, N))          # within-scenario spread
base = RNG.normal(BASE, 15, N)                                   # cases/day, Sept-equivalent
season_amp = RNG.normal(1.0, 0.20, N)                           # seasonal depth AND phase uncertainty

# trend(t) = exp(frac * log(terminal))
trend = np.exp(np.outer(np.log(term), frac))                    # N x DAYS  (chunked below)

def run() -> np.ndarray:
    out = np.empty(N)
    step = 20_000
    for i in range(0, N, step):
        sl = slice(i, min(i + step, N))
        # seasonal depth: pull index toward/away from 1 by season_amp
        s = 1.0 + (season[None, :] - 1.0) * season_amp[sl, None]
        s = np.clip(s, 0.15, 1.6)
        daily = base[sl, None] * s * trend[sl]
        out[sl] = daily.sum(axis=1)
    return out

added = run()

# Model error: my seasonal shape and plateau read could simply be wrong.
added *= np.exp(RNG.normal(0, 0.10, N))

# Counting-regime shift short of annulment: detection effort collapses, or
# SENASICA narrows what it counts without USDA calling the series incomparable.
shift = RNG.random(N) < 0.06
added[shift] *= RNG.uniform(0.30, 0.70, shift.sum())

total = added + RNG.normal(CUM_NOW, CUM_NOW_SD, N)
total = np.round(total / 500) * 500                             # question rounds to nearest 500

qs = [1, 5, 10, 25, 50, 75, 90, 95, 99]
print("added cases Sep-2026..Jun-2027:", np.round(np.percentile(added, [25, 50, 75])).astype(int))
print()
for q in qs:
    print(f"p{q:<3d} {np.percentile(total, q):9,.0f}")
print()
print(f"mean {total.mean():,.0f}   sd {total.std():,.0f}")
print()
for i, (lab, w, t) in enumerate(SCEN):
    m = pick == i
    print(f"{lab:28s} w={w:.2f}  median {np.median(total[m]):9,.0f}  "
          f"[{np.percentile(total[m],25):,.0f}, {np.percentile(total[m],75):,.0f}]")
print()
for thr in (30_000, 45_000, 50_000, 55_000, 60_426, 65_000, 70_000, 80_000, 100_000):
    print(f"P(total > {thr:>7,}) = {(total > thr).mean():5.1%}")

