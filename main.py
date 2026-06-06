import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_all():
    files = DATA_DIR.glob("*.csv")
    dfs = {f.name: pd.read_csv(f) for f in files}
    return dfs


def main():
    dfs = load_all()
    for name, df in dfs.items():
        print(f"Loaded {name}: {len(df)} rows")


if __name__ == "__main__":
    main()
