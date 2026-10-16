"""Monte Carlo for 2026 US execution count (mc45255), v3 2026-10-16."""
import numpy as np

rng = np.random.default_rng(45255)
N = 400_000
BASE = 31  # DPIC count as of 2026-10-13 (Robertson executed)

# Scheduled warrants: P(carried out on the scheduled date)
sched = {
    "Reaves FL 10/20": 0.94,
    "Guardado FL 11/5": 0.92,
    "Taylor AL 11/5": 0.87,
    "Weisheit IN 11/5 (or 11/19)": 0.68,
    "Rubio TX 11/12": 0.70,
    "Pavatt OK 11/12": 0.86,  # board denied clemency 3-2 on 10/14
    "Dennes TX 11/19": 0.83,
    "Hasan MIL 12/3": 0.42,  # Trump 10/15: "He will die, as scheduled"; no habeas yet
}


def run(sched: dict[str, float], fl_pmf: list[float], fl_succ: float, other_lam: float,
        shared_sd: float = 0.0) -> np.ndarray:
    """Simulate totals; shared_sd adds a common logit shock (e.g. a drug-supply or
    protocol shock that hits several states at once) so outcomes are not independent."""
    shock = rng.normal(0, shared_sd, N) if shared_sd else np.zeros(N)
    tot = np.full(N, BASE)
    for p in sched.values():
        lp = np.log(p / (1 - p)) + shock
        tot += rng.random(N) < 1 / (1 + np.exp(-lp))
    n_fl = rng.choice(len(fl_pmf), size=N, p=fl_pmf)
    lp = np.log(fl_succ / (1 - fl_succ)) + shock
    tot += rng.binomial(n_fl, 1 / (1 + np.exp(-lp)))
    tot += rng.poisson(other_lam, N)
    return tot


def bins(t: np.ndarray) -> dict[str, float]:
    return {"Fewer than 39": (t < 39).mean(), "39": (t == 39).mean(), "40": (t == 40).mean(),
            "41": (t == 41).mean(), "More than 41": (t > 41).mean()}


# no new FL warrant by 10/16 -> earliest new date ~11/16; window shrinks to ~6.5 weeks
FL = [0.04, 0.10, 0.22, 0.32, 0.22, 0.08, 0.02]
base = run(sched, FL, 0.93, 0.35, shared_sd=0.4)
print("BASE", {k: round(v, 3) for k, v in bins(base).items()},
      "mean", base.mean().round(2), "pct", np.percentile(base, [5, 25, 50, 75, 95]))

# Sensitivities
cases = {
    "FL slower (mean~2)": {"fl_pmf": [0.08, 0.22, 0.35, 0.23, 0.10, 0.02, 0.0]},
    "FL faster (mean~3.6)": {"fl_pmf": [0.02, 0.05, 0.12, 0.25, 0.30, 0.18, 0.08]},
    "Hasan 0.15": {"hasan": 0.15},
    "Hasan 0.70": {"hasan": 0.70},
    "others lam 0.15": {"other": 0.15},
    "others lam 1.0": {"other": 1.0},
}
for name, kw in cases.items():
    s = dict(sched)
    if "hasan" in kw:
        s["Hasan MIL 12/3"] = kw["hasan"]
    t = run(s, kw.get("fl_pmf", FL), 0.93, kw.get("other", 0.35), shared_sd=0.4)
    print(f"{name:22s}", {k: round(v, 3) for k, v in bins(t).items()}, "median", np.median(t))

# pmf for ledger
vals, cnts = np.unique(base, return_counts=True)
print({int(v): round(c / N, 4) for v, c in zip(vals, cnts)})
