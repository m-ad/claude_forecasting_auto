"""v6 chart: Isaias peak-intensity guidance against the operational Cat 3 line.

The point of the picture: the whole question now hinges on whether one storm
gains one more 5-kt step. NHC's official peak (95 kt) sits just below the
100-kt operational threshold, the raw hurricane models straddle it, and the
statistical aids sit well below it.
"""
import gzip

import matplotlib

matplotlib.use("Agg")  # set before any figure exists; this script only writes PNGs
import matplotlib.pyplot as plt

# Raw dynamical runs arrive ~6 h late, so the 18Z cycle is the latest set
# that has all of them; the interpolated/statistical aids use 00Z 8 Oct.
WANT = {
    "2026100718": ["HMON", "CTCX", "HWRF", "GDMN", "HFSA", "HFSB"],
    "2026100800": ["OFCL", "GDMI", "HCCA", "CTCI", "DSHP", "LGEM", "IVCN"],
}
LABEL = {
    "OFCL": "NHC official", "GDMI": "DeepMind (interp.)", "GDMN": "DeepMind ens. mean",
    "HCCA": "HCCA corrected consensus", "CTCI": "COAMPS-TC (interp.)",
    "CTCX": "COAMPS-TC", "DSHP": "SHIPS (statistical)", "LGEM": "LGEM (statistical)",
    "IVCN": "IVCN consensus", "HWRF": "HWRF", "HMON": "HMON", "HFSA": "HAFS-A",
    "HFSB": "HAFS-B",
}

peaks: dict[str, tuple[int, str]] = {}
with gzip.open("raw/nhc-aal092026-2026-10-08.dat.gz", "rt") as fh:
    for line in fh:
        f = [x.strip() for x in line.split(",")]
        cyc, aid, tau, vmax = f[2], f[4], int(f[5]), int(f[8] or 0)
        if aid in WANT.get(cyc, []) and tau <= 72:
            key = f"{aid}"
            if key not in peaks or vmax > peaks[key][0]:
                peaks[key] = (vmax, cyc[-2:] + "Z")

rows = sorted(peaks.items(), key=lambda kv: kv[1][0])
fig, ax = plt.subplots(figsize=(8.5, 4.8))
for i, (aid, (v, cyc)) in enumerate(rows):
    colour = "#2166ac" if aid == "OFCL" else ("#b2182b" if v >= 100 else "#9e9e9e")
    ax.barh(i, v, color=colour, height=0.65)
    ax.text(v + 1, i, f"{v} kt", va="center", fontsize=8.5)
ax.set_yticks(range(len(rows)))
ax.set_yticklabels([f"{LABEL[a]} ({c})" for a, (_, c) in rows], fontsize=8.5)
ax.axvline(100, color="#b2182b", ls="--", lw=1.2)
ax.text(100.5, -0.9, "operational Cat 3 = 100 kt", color="#b2182b", fontsize=8.5)
ax.set_xlim(60, 118)
ax.set_xlabel("Forecast peak sustained wind, Isaias, next 72 h (kt)")
ax.set_title("Isaias: NHC's peak is one 5-kt step short of a major hurricane",
             fontsize=11, loc="left")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="x", alpha=0.25)
fig.tight_layout()
fig.savefig("charts/isaias_guidance_v6.png", dpi=150)
print("written charts/isaias_guidance_v6.png")
