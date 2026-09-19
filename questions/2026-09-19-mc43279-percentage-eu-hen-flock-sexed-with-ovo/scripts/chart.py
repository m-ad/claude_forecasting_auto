"""Charts for the EU in-ovo sexing penetration question (Metaculus 43279).

Two panels:

* top - the Innovate Animal Ag measured series (all on the 2026 rebased
  denominator), my projected band, and IAA's own July-2028 base case. The point
  is that adoption is decelerating in percentage-point terms even though the
  headline compound growth rate sounds explosive.
* bottom - horizontal bars for the resolution-timing scenarios, because in this
  question *when* Innovate Animal Ag next publishes moves the answer about as
  much as what happens in EU hatcheries.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parents[1] / "charts"
OUT.mkdir(exist_ok=True)

# Innovate Animal Ag measured points, 2026 report basis (commercial layers only).
OBS = [(dt.date(2024, 4, 1), 23.0), (dt.date(2025, 4, 1), 34.0), (dt.date(2026, 6, 1), 40.0)]
# IAA base forecast and its stated range.
IAA = (dt.date(2028, 7, 1), 51.0, 47.0, 55.0)

# Resolution-timing scenarios: label, weight, centre, 25th, 75th.
SCEN = [
    ("Jan-2027 yearly recap used\n(restates the 40% June-2026 figure)", 0.25, 40.4, 39.7, 41.1),
    ("Annual report, as-of 1 Apr 2027", 0.25, 43.5, 42.0, 45.0),
    ("Annual report, as-of 1 Jun 2027", 0.35, 44.6, 43.0, 46.2),
    ("Report slips to H2 2027", 0.15, 46.0, 44.1, 47.9),
]

MY = (43.3, 41.0, 45.6)
CP = (41.7, 38.2, 45.1)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8.8), gridspec_kw={"height_ratios": [1.5, 1]})

xs = [d for d, _ in OBS]
ys = [v for _, v in OBS]
ax1.plot(xs, ys, "o-", color="#1f4e79", lw=2.2, ms=8, label="IAA measured (2026 rebased basis)")
for d, v in OBS:
    ax1.annotate(f"{v:.0f}%", (d, v), textcoords="offset points", xytext=(-4, 10),
                 fontsize=9, color="#1f4e79")

ax1.errorbar([IAA[0]], [IAA[1]], yerr=[[IAA[1] - IAA[2]], [IAA[3] - IAA[1]]], fmt="s",
             color="#7f8c8d", ms=8, capsize=5, label="IAA base forecast (47-55%)")
ax1.annotate("51%", IAA[:2], textcoords="offset points", xytext=(8, -4), fontsize=9,
             color="#7f8c8d")

# My band, drawn across the plausible resolution window rather than at one date.
lo_d, hi_d = dt.date(2027, 1, 4), dt.date(2027, 10, 1)
ax1.fill_between([lo_d, hi_d], [MY[1]] * 2, [MY[2]] * 2, color="#c0392b", alpha=0.18,
                 label="my IQR [41.0, 45.6] over the resolution window")
ax1.plot([lo_d, hi_d], [MY[0]] * 2, color="#c0392b", lw=2, ls="--", label="my median 43.3%")
ax1.plot([lo_d, hi_d], [CP[0]] * 2, color="#e67e22", lw=1.6, ls=":", label="Metaculus CP 41.7%")

ax1.set_ylabel("share of EU commercial layer hens sexed in-ovo (%)")
ax1.set_ylim(18, 58)
ax1.grid(alpha=0.25)
ax1.legend(fontsize=8.5, loc="upper left")
ax1.set_title("EU in-ovo sexing: +11pp in 2024-25, then +5.1pp/yr — Italy carries 2027-28")

y = np.arange(len(SCEN))[::-1]
ax2.barh(y, [s[2] for s in SCEN], color="#2980b9", alpha=0.85, height=0.55)
for yi, s in zip(y, SCEN):
    ax2.plot([s[3], s[4]], [yi, yi], color="#1b2631", lw=2.4)
    ax2.annotate(f"{s[2]:.1f}%   w={s[1]:.2f}", (36.2, yi), fontsize=9, va="center",
                 color="white", fontweight="bold")
ax2.axvline(MY[0], color="#c0392b", ls="--", lw=1.8)
ax2.axvline(CP[0], color="#e67e22", ls=":", lw=1.6)
ax2.set_yticks(y)
ax2.set_yticklabels([s[0] for s in SCEN], fontsize=8.5)
ax2.set_xlim(36, 49)
ax2.set_xlabel("resolving value (%), bar = scenario centre, line = its 25th-75th range")
ax2.grid(axis="x", alpha=0.25)
# vline labels are annotated on the axis rather than in a legend box, which would
# sit on top of the top bar.
ax2.annotate("  my median 43.3%", (MY[0], len(SCEN) - 0.45), color="#c0392b", fontsize=8.5,
             ha="left", va="bottom", fontweight="bold")
ax2.annotate("CP 41.7%  ", (CP[0], len(SCEN) - 0.45), color="#e67e22", fontsize=8.5,
             ha="right", va="bottom", fontweight="bold")
ax2.set_ylim(-0.6, len(SCEN) - 0.15)
ax2.set_title("What resolves the question is mostly which 2027 publication is used")

fig.tight_layout()
fig.savefig(OUT / "eu-trajectory-and-timing-scenarios.png", dpi=150)
print("wrote", OUT / "eu-trajectory-and-timing-scenarios.png")
