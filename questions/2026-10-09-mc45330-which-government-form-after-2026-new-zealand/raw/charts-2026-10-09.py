"""Charts for the two 2026-10-09 forecasts."""
import datetime as dt
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

u_dir, n_dir = sys.argv[1], sys.argv[2]

pts = [("2025-01-22", 476), ("2025-06-25", 501), ("2025-11-26", 512), ("2025-12-10", 514),
       ("2026-03-11", 523), ("2026-05-13", 527), ("2026-07-29", 545), ("2026-09-23", 560),
       ("2026-09-29", 563)]
d = [dt.date.fromisoformat(a) for a, _ in pts]
v = [b for _, b in pts]
fig, ax = plt.subplots(figsize=(8, 4.2))
ax.plot(d, v, "o-", color="#3b6ea5", label="UNESCO verified total (as-of date)")
end = dt.date(2026, 12, 10)
ax.fill_between([d[-1], end], [563, 569], [563, 582], color="#e3a33b", alpha=0.35, label="Forecast IQR 569–582")
ax.plot([d[-1], end], [563, 575], "--", color="#c67a00", label="Forecast median 575")
ax.errorbar([end], [575], yerr=[[12], [24]], fmt="none", ecolor="#c67a00", alpha=0.6, capsize=4)
ax.set_ylabel("Cultural sites confirmed damaged")
ax.set_title("UNESCO Ukraine damaged-sites tracker: history and end-2026 forecast")
ax.grid(alpha=0.3)
ax.legend(loc="upper left", fontsize=8)
fig.tight_layout()
fig.savefig(f"{u_dir}/charts/unesco-trend-v1.png", dpi=130)

opts = ["Other", "None before January", "Labour-led", "National-led"]
me = [1.0, 8.0, 44.5, 46.5]
poly = [None, None, 46.4, 44.9]
fig, ax = plt.subplots(figsize=(8, 3.2))
y = range(len(opts))
ax.barh([i + 0.18 for i in y], me, height=0.36, color="#3b6ea5", label="This forecast (v1)")
ax.barh([i - 0.18 for i in y], [p or 0 for p in poly], height=0.36, color="#999999",
        label="Polymarket coalition mkt (approx. bloc sums)")
for i, val in enumerate(me):
    ax.text(val + 0.6, i + 0.18, f"{val:.1f}%", va="center", fontsize=8)
ax.set_yticks(list(y), opts)
ax.set_xlabel("Probability (%)")
ax.set_title("NZ 2026: which government forms (before 1 Jan 2027)")
ax.legend(fontsize=8, loc="lower right")
ax.set_xlim(0, 60)
fig.tight_layout()
fig.savefig(f"{n_dir}/charts/outcomes-v1.png", dpi=130)
