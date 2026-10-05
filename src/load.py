"""Gercek ATUS verisini yukleme + kategorilere cevirme."""
from pathlib import Path
import pandas as pd
from .config import CATEGORY_PREFIXES, LIFE_SAT_COL


def _read(path):
    df = pd.read_csv(path)
    df.columns = [c.lower() for c in df.columns]
    return df


def load_atus(raw_dir="../data/raw", year=2013):
    raw = Path(raw_dir)
    summ = _read(raw / f"atussum_{year}.dat")
    resp = _read(raw / f"atusresp_{year}.dat")
    wb = _read(raw / f"wbresp_{year}.dat")

    out = summ[["tucaseid"]].copy()
    for cat, prefixes in CATEGORY_PREFIXES.items():
        cols = [c for c in summ.columns if any(c.startswith(p) for p in prefixes)]
        out[cat] = summ[cols].sum(axis=1) / 60  # dakika -> saat

    # yas, cinsiyet, gun: hangi dosyada varsa oradan al
    for new, old in {"age": "teage", "sex": "tesex", "day": "tudiaryday"}.items():
        if old in summ.columns:
            src = summ
        elif old in resp.columns:
            src = resp
        else:
            raise KeyError(f"'{old}' ne atussum ne atusresp icinde var. "
                           f"atussum sutunlari: {list(summ.columns[:15])}")
        out[new] = src.set_index("tucaseid")[old].reindex(out["tucaseid"]).values
    out["weekend"] = out["day"].isin([1, 7])

    wb = wb[["tucaseid", LIFE_SAT_COL.lower()]].rename(columns={LIFE_SAT_COL.lower(): "life_sat"})
    out = out.merge(wb, on="tucaseid")
    out = out[out["life_sat"].between(0, 10)]
    return out.drop(columns=["day", "tucaseid"]).reset_index(drop=True)