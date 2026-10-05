"""SENTETIK veri uretici. Gercek ATUS verisi yokken pipeline'i denemek icindir.
Buradan cikan sonuclar GERCEK bulgu degildir."""
import numpy as np
import pandas as pd
from .config import CATEGORIES

# kategori sirasi: sleep, work, eating, sport, friends, tv, social_media
PROFILES = {
    "work":   [7.0, 8.5, 1.0, 0.2, 0.4, 1.2, 0.4],
    "social": [8.0, 3.5, 1.3, 0.5, 3.2, 1.2, 0.6],
    "sleep":  [10.0, 3.0, 1.2, 0.3, 0.6, 1.8, 0.5],
    "screen": [7.8, 3.0, 1.0, 0.2, 0.5, 4.0, 2.2],
}
LIFE_SAT_BASE = {"work": 6.6, "social": 7.4, "sleep": 6.8, "screen": 6.0}


def make_synthetic(n=3000, seed=42):
    rng = np.random.default_rng(seed)
    names = rng.choice(list(PROFILES), size=n, p=[0.35, 0.2, 0.2, 0.25])
    rows = [np.clip(np.array(PROFILES[g]) + rng.normal(0, 0.8, 7), 0, None) for g in names]
    df = pd.DataFrame(rows, columns=CATEGORIES)
    df["age"] = rng.integers(18, 80, n)
    df["sex"] = rng.choice([1, 2], n)
    df["weekend"] = rng.random(n) < 0.3
    base = np.array([LIFE_SAT_BASE[g] for g in names])
    df["life_sat"] = np.clip(np.round(base + rng.normal(0, 1.5, n) + 0.01 * (df["age"] - 45)), 0, 10)
    return df
