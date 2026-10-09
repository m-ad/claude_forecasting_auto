"""Monte Carlo of NZ 2026 seat blocs from the Sep-Oct 2026 polling average."""
import numpy as np

rng = np.random.default_rng(1)
parties = ["NAT", "LAB", "GRN", "ACT", "NZF", "TPM", "TOP", "OTH"]
mean = np.array([28.55, 27.93, 14.5, 9.59, 10.4, 1.65, 5.91 - 0.3, 1.5])
# poll-to-result error + one month of campaign drift
sd = np.array([2.8, 2.8, 1.8, 1.5, 1.6, 0.6, 1.3, 0.6])


def sainte_lague(votes: np.ndarray, seats: int) -> np.ndarray:
    alloc = np.zeros(len(votes), dtype=int)
    for _ in range(seats):
        q = votes / (2 * alloc + 1)
        alloc[np.argmax(q)] += 1
    return alloc


N = 20000
res = {"right": 0, "left": 0, "hung_top_pivot": 0, "hung_other": 0}
top_in = 0
for _ in range(N):
    v = np.clip(rng.normal(mean, sd), 0.1, None)
    v = v / v.sum() * 100
    tpm_elec = rng.integers(2, 7)  # 2..6 Māori electorates
    top_elec = rng.random() < 0.05
    act_elec = True
    elig = (v >= 5)
    elig[parties.index("TPM")] = True
    elig[parties.index("ACT")] |= act_elec
    elig[parties.index("TOP")] |= top_elec
    elig[parties.index("OTH")] = False
    top_in += elig[parties.index("TOP")]
    vv = np.where(elig, v, 0)
    s = sainte_lague(vv, 120)
    ti = parties.index("TPM")
    over = max(0, tpm_elec - s[ti])
    s[ti] = max(s[ti], tpm_elec)
    house = 120 + over
    maj = house // 2 + 1
    right = s[0] + s[3] + s[4]
    left = s[1] + s[2] + s[5]
    top = s[6]
    if right >= maj:
        res["right"] += 1
    elif left + top >= maj and left >= right:
        res["left"] += 1
    elif left + top >= maj:
        res["hung_top_pivot"] += 1
    else:
        res["hung_other"] += 1
print({k: round(v / N, 3) for k, v in res.items()}, "P(TOP in)", round(top_in / N, 3))
