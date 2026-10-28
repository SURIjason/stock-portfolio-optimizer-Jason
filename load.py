#%%

import sqlite3
import os

def save_to_sqlite(df, db_path="data/cac40_prices.sqlite", table_name="stock_prices"):
    """
    Saves the cleaned data to a SQLite database
    """
    if df.empty:
        print("DataFrame is empty. Nothing to save.")
        return

    dir_path = os.path.dirname(db_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"📁 Created directory: {dir_path}")

    # Connect and write to database
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

    print(f"Data saved to '{db_path}' (table: '{table_name}', rows: {len(df)})")
