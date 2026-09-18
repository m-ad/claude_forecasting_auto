"""SPR weekly trajectory with the collapsing taper, my three forecasts, and the STEO path."""
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

weeks = ["2026-07-31", "2026-08-07", "2026-08-14", "2026-08-21", "2026-08-28", "2026-09-04", "2026-09-11"]
vals = [304.809, 298.694, 293.426, 289.726, 286.604, 285.360, 284.957]
x = [dt.date.fromisoformat(w) for w in weeks]

fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.4), gridspec_kw={"width_ratios": [1.45, 1]})

ax.plot(x, vals, marker="o", ms=5, lw=2, color="#3f6f8f", label="WCSSTUS1 weekly (actual)")
eom = dt.date(2026, 9, 30)
ax.errorbar([eom], [284.7], yerr=[[0.7], [0.4]], fmt="D", ms=8, capsize=5, lw=2,
            color="#c1666b", label="v3 median + IQR")
ax.plot([eom], [283.4], marker="s", ms=6, color="#9db4c0", label="v2 median (2026-09-12)")
ax.plot([eom], [282.3], marker="^", ms=6, color="#c8cdd2", label="v1 median (2026-09-07)")
ax.plot([eom], [282.052], marker="*", ms=12, color="#d08c3c", label="Sept-2026 STEO (COSQPUS)")
ax.set_ylabel("SPR crude, million barrels")
ax.set_title("End-September print vs the weekly series", fontsize=11)
ax.legend(fontsize=8, frameon=False, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
ax.tick_params(axis="x", labelrotation=35, labelsize=8)

draws = [6.115, 5.268, 3.700, 3.122, 1.244, 0.403]
lbl = ["08-07", "08-14", "08-21", "08-28", "09-04", "09-11"]
y = np.arange(len(draws))
ax2.barh(y, draws, 0.6, color=["#6f93a8"] * 4 + ["#c1666b"] * 2)
for i, d in enumerate(draws):
    ax2.text(d + 0.12, i, f"{d:.3f}", va="center", fontsize=8.5)
ax2.set_yticks(y); ax2.set_yticklabels(lbl, fontsize=9)
ax2.invert_yaxis()
ax2.set_xlabel("weekly draw, million barrels")
ax2.set_xlim(0, 7.4)
ax2.set_title("Two consecutive sub-0.5 Mb weeks\nend the 'contract clears by 30 Sep' branch", fontsize=10)
ax2.spines[["top", "right"]].set_visible(False)

fig.tight_layout()
fig.savefig("questions/2026-09-07-mc15240-spr-crude-barrels-september-2026/charts/spr-trajectory-v3.png", dpi=150)
print("ok")
