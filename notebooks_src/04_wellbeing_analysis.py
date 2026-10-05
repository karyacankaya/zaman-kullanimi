# %% [markdown]
# # 04 - Kumeler arasi yasam memnuniyeti
# Kruskal-Wallis + yas/cinsiyet kontrollu regresyon. **Korelasyon, nedensellik degil.**

# %%
import sys; sys.path.insert(0, "..")
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
from scipy import stats
from src.stats import ols
df = pd.read_csv("../data/processed/timeuse_clustered.csv")
note = " (SENTETIK VERI)" if df["synthetic"].iloc[0] else ""

# %%
order = df.groupby("cluster")["life_sat"].mean().sort_values().index
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x="cluster", y="life_sat", order=order, color="#9ecae1")
plt.xticks(rotation=20); plt.ylabel("Yasam memnuniyeti (0-10)")
plt.title("Kumelere gore yasam memnuniyeti" + note); plt.tight_layout()
plt.savefig("../figures/06_satisfaction_by_cluster.png", dpi=150); plt.show()
df.groupby("cluster")["life_sat"].agg(["mean", "std", "count"]).round(2).loc[order]

# %%
groups = [g["life_sat"].values for _, g in df.groupby("cluster")]
h, p = stats.kruskal(*groups)
print(f"Kruskal-Wallis: H={h:.1f}, p={p:.2g}")

# %%
# Yas, cinsiyet ve hafta sonu kontrol edilerek kume farki (referans: alfabetik ilk kume)
d = df.copy()
d["sex"] = d["sex"].astype(str)
d["weekend"] = d["weekend"].astype(str)
res, r2 = ols(d, "life_sat", ["cluster", "sex", "weekend", "age"])
print(f"R2 = {r2:.3f}")
res.round(3)
