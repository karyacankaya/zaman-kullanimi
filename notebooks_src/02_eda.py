# %% [markdown]
# # 02 - Kesif: insanlar gunlerini nasil geciriyor?

# %%
import sys; sys.path.insert(0, "..")
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from src.config import CATEGORIES
df = pd.read_csv("../data/processed/timeuse.csv")
synthetic = bool(df["synthetic"].iloc[0])
note = " (SENTETIK VERI)" if synthetic else ""

# %%
means = df[CATEGORIES].mean().sort_values()
ax = means.plot.barh(figsize=(7, 4), color="#4C78A8")
ax.set_xlabel("Ortalama saat / gun"); ax.set_title("Ortalama gunluk zaman dagilimi" + note)
plt.tight_layout(); plt.savefig("../figures/01_mean_hours.png", dpi=150); plt.show()

# %%
wk = df.groupby("weekend")[CATEGORIES].mean().T.rename(columns={False: "Hafta ici", True: "Hafta sonu"})
ax = wk.plot.bar(figsize=(8, 4)); ax.set_ylabel("Saat / gun"); ax.set_title("Hafta ici vs hafta sonu" + note)
plt.tight_layout(); plt.savefig("../figures/02_weekday_weekend.png", dpi=150); plt.show()

# %%
plt.figure(figsize=(7, 5))
sns.heatmap(df[CATEGORIES + ["life_sat"]].corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Korelasyon" + note); plt.tight_layout()
plt.savefig("../figures/03_correlation.png", dpi=150); plt.show()
