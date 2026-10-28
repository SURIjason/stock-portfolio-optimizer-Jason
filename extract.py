import pandas as pd
import os

def get_local_stock_data(paths=None):
    """
    Loads and merges stock data from multiple CSV files.
    Prints basic descriptive stats for each file.
    """
    if paths is None:
        paths = [
            "data/cac40_2021.csv",
            "data/cac40_2022.csv",
            "data/cac40_2023.csv"
        ]

    dfs = []

    for path in paths:
        try:
            df = pd.read_csv(path)
            print(f"   Loaded: {path}")
            print(f"   Shape: {df.shape}")
            print(f"   Columns: {list(df.columns)}")
            print(df.head(2))  # Optional: show preview

            dfs.append(df)

        except FileNotFoundError:
            print(f" File not found: {path}")

    if not dfs:
        print("️ No valid data loaded.")
        return pd.DataFrame()

    combined_df = pd.concat(dfs, ignore_index=True)
    print(f" Combined dataset shape: {combined_df.shape}")
    return combined_df
