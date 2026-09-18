"""Bloc-seat shift between the late-August and mid-September 2026 poll averages."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

labels = ["Arab parties\n(Joint List + Ra'am)",
          "Anti-Netanyahu Zionist bloc\n(Yashar+B'Yachad+YB+Democrats)",
          "Netanyahu bloc\n(Likud+RZP+Otzma+Shas+UTJ+Winter)"]
aug = [12.5, 57.0, 49.0]      # v1: Arab 10-15, anti-Bibi 55-59, Netanyahu 43-51 (median ~49)
sep = [12.6, 52.7, 53.7]      # MEF poll-of-polls + JPost 5-poll avg + Channel 13, 16-17 Sep
y = np.arange(len(labels))
h = 0.36

fig, ax = plt.subplots(figsize=(9, 4.2))
ax.barh(y + h/2, aug, h, label="late Aug 2026 (v1)", color="#9db4c0")
ax.barh(y - h/2, sep, h, label="mid-Sep 2026 (v2)", color="#c1666b")
ax.axvline(61, color="#333", ls="--", lw=1.2)
ax.text(61.6, 2.45, "61 = majority", fontsize=9, color="#333")
for yi, (a, s) in enumerate(zip(aug, sep)):
    ax.text(a + 0.6, yi + h/2, f"{a:.0f}", va="center", fontsize=9, color="#4a5b66")
    ax.text(s + 0.6, yi - h/2, f"{s:.0f}", va="center", fontsize=9, color="#8c3f44")
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Knesset seats (mainstream poll average)")
ax.set_xlim(0, 72)
ax.set_title("The 2026 Israeli bloc picture moved ~4 seats toward Netanyahu in three weeks",
             fontsize=11, pad=12)
ax.legend(loc="lower right", fontsize=9, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("questions/2026-08-31-mc40966-benjamin-netanyahu-cease-prime-minister-israel-during/charts/bloc-shift-aug-to-sep.png", dpi=150)
print("ok")
