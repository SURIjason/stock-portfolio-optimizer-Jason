#%%

import pandas as pd

def clean_stock_data(df):
    """
    Cleans and formats stock to drop missing values,
    standardize columns and ensure date column is datetime
    """
    df = df.dropna()


    df = df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume",
        "Stock": "ticker"
    })

    df['date'] = pd.to_datetime(df['date'])

    return df
