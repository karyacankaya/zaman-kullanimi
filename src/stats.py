"""statsmodels olmadan basit OLS (katsayi, std hata, p-degeri)."""
import numpy as np
import pandas as pd
from scipy import stats


def ols(df, y, X):
    Xm = pd.get_dummies(df[X], drop_first=True).astype(float)
    Xm.insert(0, "const", 1.0)
    A, b = Xm.to_numpy(), df[y].to_numpy(float)
    beta, *_ = np.linalg.lstsq(A, b, rcond=None)
    resid = b - A @ beta
    dof = len(b) - A.shape[1]
    sigma2 = resid @ resid / dof
    se = np.sqrt(np.diag(sigma2 * np.linalg.inv(A.T @ A)))
    p = 2 * stats.t.sf(np.abs(beta / se), dof)
    r2 = 1 - (resid @ resid) / ((b - b.mean()) @ (b - b.mean()))
    return pd.DataFrame({"coef": beta, "se": se, "p": p}, index=Xm.columns), r2
