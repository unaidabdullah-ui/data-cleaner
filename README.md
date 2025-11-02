# 🧹 Data Cleaner

**One-line CSV cleaner** – drops rows with missing values.

```bash
python data_cleaner.py --input dirty.csv --output clean.csv
```

Done.

---

## Install

```bash
pip install pandas
```

---

## Run

```bash
python data_cleaner.py --input data.csv --output cleaned.csv
```

**Output**
```
✅ Saved to cleaned.csv
Rows: 1000 → 920 (80 removed)
```

---

## Code (data_cleaner.py)

```python
import pandas as pd, argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
args = parser.parse_args()

df = pd.read_csv(args.input)
before = len(df)
df = df.dropna()
df.to_csv(args.output, index=False)

print(f"✅ Saved to {args.output}")
print(f"Rows: {before} → {len(df)} ({before-len(df)} removed)")
```

---

## Author
@unaidabdullah-ui · Nov 2025

> Clean data, happy life.
