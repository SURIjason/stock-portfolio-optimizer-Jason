import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from portfolio import df_pivot, optimize_portfolio

st.set_page_config(page_title="Maximize Your Sharpe!", layout="wide")
st.title("Maximize Your Sharpe!")

# Sidebar 
st.sidebar.title("Portfolio Settings")

# Slider controls
min_assets = st.sidebar.slider("Minimum # of Assets", 1, 20, value=5)
max_assets = st.sidebar.slider("Maximum # of Assets", min_assets, 30, value=12)
max_weight = st.sidebar.slider("Max Weight per Stock", 0.05, 1.0, value=0.20, step=0.05)

show_table = st.sidebar.checkbox("Show Portfolio Table", value=True)

# Optimize 
weights, ret, vol, sharpe, tickers, returns = optimize_portfolio(
    min_assets=min_assets,
    max_assets=max_assets,
    max_weight=max_weight
)

weights_df = pd.Series(weights, index=tickers)
weights_df = weights_df[weights_df > 0.01].sort_values(ascending=False)

#  Plotting backtest
st.subheader("Backtested Portfolio Performance")
aligned_weights = weights_df.reindex(df_pivot.columns, fill_value=0.0)
cum_returns = (returns @ aligned_weights).cumsum()
base = cum_returns.iloc[0]
normalized_returns = (cum_returns - base + 1) * 100

fig, ax = plt.subplots(figsize=(6, 2))
ax.plot(normalized_returns, label="Cumulative Return", color="dodgerblue", linewidth=1.5)
ax.set_ylabel("Portfolio Value (Index)", fontsize=8)
ax.set_xlabel("Date", fontsize=8)
ax.tick_params(labelsize=6)
ax.legend(fontsize=6, loc='upper left')
st.pyplot(fig)

#bar chart of portfolio weights
st.subheader("Portfolio Composition")
st.bar_chart(weights_df)

# stats
col1, col2, col3 = st.columns(3)
col1.metric("Expected Return", f"{ret:.2%}")
col2.metric("Volatility", f"{vol:.2%}")
col3.metric("Sharpe Ratio", f"{sharpe:.2f}")

# weights table
if show_table:
    st.subheader("Portfolio Weights Table")
    st.dataframe(weights_df)