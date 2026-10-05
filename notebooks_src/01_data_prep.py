# %% [markdown]
# # 01 - Veri hazirlama
# Gercek ATUS dosyalari `data/raw/` icindeyse onlari, yoksa **sentetik** ornek veriyi kullanir.

# %%
import sys; sys.path.insert(0, "..")
from pathlib import Path
from src.load import load_atus
from src.synthetic import make_synthetic

YEAR = 2013
real = Path(f"../data/raw/atussum_{YEAR}.dat").exists()
df = load_atus("../data/raw", YEAR) if real else make_synthetic()
print("Gercek ATUS verisi" if real else "UYARI: SENTETIK veri kullaniliyor")
print(df.shape)
df.head()

# %%
Path("../data/processed").mkdir(exist_ok=True)
df.assign(synthetic=not real).to_csv("../data/processed/timeuse.csv", index=False)
df.describe().round(2)
