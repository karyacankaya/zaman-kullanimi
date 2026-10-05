"""Percent-format .py dosyalarini .ipynb'ye cevirir (nbformat gerektirmez)."""
import json, re, sys
from pathlib import Path

def convert(src, dst):
    cells, cur, kind = [], [], None
    def flush():
        if cur and any(l.strip() for l in cur):
            text = "\n".join(cur).strip("\n")
            if kind == "md":
                text = "\n".join(re.sub(r"^# ?", "", l) for l in text.split("\n"))
                cells.append({"cell_type": "markdown", "metadata": {}, "source": text.splitlines(True)})
            else:
                cells.append({"cell_type": "code", "metadata": {}, "execution_count": None,
                              "outputs": [], "source": text.splitlines(True)})
    for line in Path(src).read_text().splitlines():
        if line.startswith("# %%"):
            flush(); cur = []; kind = "md" if "[markdown]" in line else "code"
        else:
            cur.append(line)
    flush()
    nb = {"cells": cells, "nbformat": 4, "nbformat_minor": 5,
          "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}}
    Path(dst).write_text(json.dumps(nb, indent=1))

for f in sorted(Path(__file__).parent.glob("0*.py")):
    convert(f, Path(__file__).parent.parent / "notebooks" / (f.stem + ".ipynb"))
    print("built", f.stem)
