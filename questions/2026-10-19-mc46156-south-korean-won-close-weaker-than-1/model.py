"""P(USD/KRW > 1340 on 2026-10-29) from realized vol plus an FOMC-hike jump.

Inputs: PoundSterlingLive daily closes Oct 1-19 2026 (scout digest), TE spot 1,331.24 (Oct 19).
"""
import numpy as np

closes = np.array([1358.52, 1343.34, 1341.52, 1337.86, 1339.76, 1341.97, 1340.63,
                   1334.42, 1342.11, 1341.58, 1341.36, 1334.65, 1332.81])
r = np.diff(np.log(closes))
sd_daily = r.std(ddof=1)
sd_ex_oct2 = r[1:].std(ddof=1)  # drop the unexplained 15-won Oct 1->2 drop
print(f"daily sd {sd_daily:.4%} (ex Oct-2 {sd_ex_oct2:.4%}), annualised {sd_daily*np.sqrt(252):.1%}")

rng = np.random.default_rng(0)
n = 400_000
spot, thr, days = 1331.24, 1340.0, 8  # Oct 20-23, 26-29
for sd in (0.0035, 0.0045, 0.0055):
    for drift_total in (-0.003, 0.0):
        # Student-t (df=4) daily shocks scaled to sd: fat tails
        t = rng.standard_t(4, size=(n, days)) / np.sqrt(2.0) * sd
        logret = t.sum(1) + drift_total
        # FOMC Oct 28: 30% hike -> +0.6% USD/KRW, else small dovish relief -0.15%
        hike = rng.random(n) < 0.30
        logret += np.where(hike, 0.006, -0.0015)
        p = (spot * np.exp(logret) > thr).mean()
        print(f"sd {sd:.2%} drift {drift_total:+.1%}: P(>1340) = {p:.3f}")
