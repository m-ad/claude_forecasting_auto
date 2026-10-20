"""Log-return model for the BTC-USD Yahoo close of 2026-10-30 (00:00 UTC Oct 31).

Spot 82,800 (CoinGecko / Yahoo, 2026-10-20 21:34 UTC); horizon ~10.1 days;
annualised vol 37% (Deribit DVOL 37.0-38.8 over Oct 14-19, 2026; 10-day realised
~25%, so implied is the conservative choice); Student-t df=4 for fat tails, scaled so
the standard deviation matches the vol assumption.
"""
import numpy as np
from scipy import stats

spot = 82_750.0
days = 10.1
ann_vol = 0.37
sd = ann_vol * np.sqrt(days / 365)
df = 4
scale = sd / np.sqrt(df / (df - 2))
for p in (5, 10, 25, 50, 75, 90, 95):
    q = stats.t.ppf(p / 100, df) * scale
    print(p, round(spot * np.exp(q)))
print("sd", round(sd, 4))
