"""Sensitivity of the median/IQR to the load-bearing assumptions."""
import datetime as dt

import numpy as np

RNG = np.random.default_rng(7)
N = 60_000
START, END = dt.date(2026, 9, 4), dt.date(2027, 6, 29)
DAYS = (END - START).days
dates = [START + dt.timedelta(days=i) for i in range(1, DAYS + 1)]
frac = np.linspace(0, 1, DAYS)

BASE_SEASON = {9: 1.00, 10: 0.95, 11: 0.80, 12: 0.55,
               1: 0.40, 2: 0.45, 3: 0.60, 4: 0.75, 5: 0.90, 6: 1.00}
SCEN_W = np.array([0.14, 0.28, 0.32, 0.18, 0.08])
SCEN_T = np.array([0.30, 0.60, 1.00, 1.50, 2.10])


def run(rate=131.0, season=None, w=SCEN_W, t=SCEN_T, cum=40_900):
    season = season or BASE_SEASON
    s = np.array([season[d.month] for d in dates])
    pick = RNG.choice(len(w), size=N, p=w / w.sum())
    term = t[pick] * np.exp(RNG.normal(0, 0.18, N))
    base = RNG.normal(rate, 12, N)
    amp = RNG.normal(1.0, 0.20, N)
    trend = np.exp(np.outer(np.log(term), frac))
    ss = np.clip(1.0 + (s[None, :] - 1.0) * amp[:, None], 0.15, 1.6)
    added = (base[:, None] * ss * trend).sum(axis=1) * np.exp(RNG.normal(0, 0.10, N))
    tot = added + RNG.normal(cum, 400, N)
    return np.percentile(tot, [25, 50, 75])


def show(lab, q):
    print(f"{lab:52s} median {q[1]:7,.0f}   IQR [{q[0]:7,.0f}, {q[2]:7,.0f}]")


show("baseline", run())
show("baseline incidence 110/day (last-10-day rate)", run(rate=110))
show("baseline incidence 155/day (Jul-Aug average)", run(rate=155))
deep = dict(BASE_SEASON); deep.update({12: 0.40, 1: 0.22, 2: 0.28, 3: 0.45})
show("deep winter (Jan index 0.22)", run(season=deep))
mild = dict(BASE_SEASON); mild.update({12: 0.75, 1: 0.60, 2: 0.65, 3: 0.75})
show("mild winter (Jan index 0.60)", run(season=mild))
show("suppression-heavy weights (D+B = 0.70)",
     run(w=np.array([0.30, 0.40, 0.20, 0.08, 0.02])))
show("growth-heavy weights (C+E = 0.50)",
     run(w=np.array([0.06, 0.16, 0.28, 0.34, 0.16])))
