"""Scenario mixture for hormuz.now commercial crossings on 2026-11-12 (UTC day)."""
import numpy as np

rng = np.random.default_rng(46386)
N = 400_000


def negbin(mean: float, sd: float, n: int) -> np.ndarray:
    """Negative binomial draws with given mean and sd (sd^2 > mean)."""
    var = sd**2
    p = mean / var
    r = mean**2 / (var - mean)
    return rng.negative_binomial(r, p, n)


# Scenario weights (why: see forecast.md Inside view)
w = {"status_quo": 0.70, "escalation": 0.16, "reopening": 0.14}
n = {k: int(v * N) for k, v in w.items()}

# Status quo: late-Oct hormuz.now complete days 20 Oct-1 Nov mean 8.2, last 7 days 9.1, sd ~2.8;
# widen sd for drift over 10 days.
sq = negbin(9.0, 4.0, n["status_quo"])
# Escalation after 3 Nov midterms (renewed US strikes / attacks): traffic falls toward PortWatch-like 2-5.
esc = negbin(4.0, 2.5, n["escalation"])
# Deal implemented / partial reopening by 12 Nov: June MoU gave 25 on day 1, 31-42 on later days
# (Kpler); hormuz.now's method sits between Kpler and PortWatch. Lognormal, median 24, wide.
reo = np.round(rng.lognormal(np.log(24), 0.55, n["reopening"])).astype(int)

x = np.concatenate([sq, esc, reo])
pcts = [5, 10, 25, 50, 75, 90, 95]
print({p: float(np.percentile(x, p)) for p in pcts})
print("P(>=20)", (x >= 20).mean(), "P(<=3)", (x <= 3).mean(), "P(>150)", (x > 150).mean())
