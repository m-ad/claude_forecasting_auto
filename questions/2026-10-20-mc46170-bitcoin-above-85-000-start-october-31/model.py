"""P(BTC >= 85,000 at 2026-10-31 00:00 UTC) under lognormal and fat-tailed (Student-t) returns."""

import numpy as np
from scipy import stats

spot = 81_324  # CoinGecko API, 2026-10-20 ~09:42 UTC
strike = 85_000
days = 10.6  # 2026-10-20 09:45 UTC -> 2026-10-31 00:00 UTC
x = np.log(strike / spot)

for vol in (0.30, 0.35, 0.40, 0.45, 0.50, 0.55):
    sigma = vol * np.sqrt(days / 365)
    p_norm = 1 - stats.norm.cdf(x / sigma)
    # Student-t with 4 dof scaled to the same standard deviation (fat tails)
    df = 4
    p_t = 1 - stats.t.cdf(x / (sigma * np.sqrt((df - 2) / df)), df)
    print(f"vol {vol:.2f}: sigma {sigma:.4f}, z {x / sigma:.2f}, P_normal {p_norm:.3f}, P_t4 {p_t:.3f}")
