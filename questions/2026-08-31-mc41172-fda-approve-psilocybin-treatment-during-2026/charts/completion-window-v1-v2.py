"""Contribution to P(YES) by NDA-completion window, v1 vs v2."""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

wins = ["slips to 2027", "Dec 16–31", "Dec 1–15", "Nov 16–30", "Nov 1–15", "Oct 16–31", "Oct 1–15"]
v1 = [0.0, 0.0, 0.08, 0.54, 1.79, 3.67, 3.60]
v2 = [0.0, 0.0, 0.07, 0.54, 1.79, 3.65, 2.86]
y = np.arange(len(wins)); h = 0.36

fig, ax = plt.subplots(figsize=(9, 4.4))
ax.barh(y + h/2, v1, h, label=f"v1, 2026-08-31 (Σ = {sum(v1):.1f} pp)", color="#9db4c0")
ax.barh(y - h/2, v2, h, label=f"v2, 2026-09-18 (Σ = {sum(v2):.1f} pp)", color="#5b8c85")
for yi, (a, b) in enumerate(zip(v1, v2)):
    if a: ax.text(a + 0.06, yi + h/2, f"{a:.1f}", va="center", fontsize=8, color="#4a5b66")
    if b: ax.text(b + 0.06, yi - h/2, f"{b:.1f}", va="center", fontsize=8, color="#2f5a53")
ax.set_yticks(y); ax.set_yticklabels(wins, fontsize=9)
ax.set_xlabel("Contribution to P(FDA decision inside 2026), percentage points")
ax.set_title("Almost all of the probability lives in an October NDA completion\n"
             "— and the 17 Sep investor update still said only \"Q4\"", fontsize=11, pad=12)
ax.legend(loc="lower right", fontsize=9, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("questions/2026-08-31-mc41172-fda-approve-psilocybin-treatment-during-2026/charts/completion-window-v1-v2.png", dpi=150)
print("ok")
