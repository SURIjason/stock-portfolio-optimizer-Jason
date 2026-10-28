import sqlite3
import pandas as pd
import numpy as np
from scipy.optimize import minimize

# Parameters for the optimization
objective_choice = "sharpe"
risk_free_rate = 0.03
max_volatility = 0.15
penalty_strength = 1e5

# Loading the data
conn = sqlite3.connect("data/cac40_prices.sqlite")
df = pd.read_sql("SELECT date, ticker, close FROM stock_prices", conn)
conn.close()

df["date"] = pd.to_datetime(df["date"])
df_pivot = df.pivot(index="date", columns="ticker", values="close").dropna()
returns = df_pivot.pct_change().dropna()
mean_returns = returns.mean()
cov_matrix = returns.cov()
tickers = mean_returns.index.tolist()
num_assets = len(tickers)

def portfolio_performance(weights):
    annual_return = np.dot(weights, mean_returns) * 252
    annual_vol = np.sqrt(weights.T @ cov_matrix @ weights) * np.sqrt(252)
    sharpe_ratio = (annual_return - risk_free_rate) / annual_vol if annual_vol > 1e-6 else 0
    return annual_return, annual_vol, sharpe_ratio

def sum_constraint(weights):
    return np.sum(weights) - 1

def optimize_portfolio(min_assets=1, max_assets=30, max_weight=1.00):
    def min_cardinality_constraint(weights):
        return np.sum(weights > 1e-4) - min_assets

    def max_cardinality_constraint(weights):
        return max_assets - np.sum(weights > 1e-4)

    def objective(weights):
        ret, vol, sharpe = portfolio_performance(weights)
        score = -sharpe if objective_choice == "sharpe" else -ret   #only sharpe now
        risk_penalty = penalty_strength * max(0, vol - max_volatility)**2
        weight_penalty = penalty_strength * np.sum(np.maximum(0, weights - max_weight)**2)
        return score + risk_penalty + weight_penalty

    constraints = [
        {'type': 'eq', 'fun': sum_constraint},
        {'type': 'ineq', 'fun': min_cardinality_constraint},
        {'type': 'ineq', 'fun': max_cardinality_constraint}
    ]

    bounds = [(0, max_weight) for _ in range(num_assets)]
    initial_weights = np.ones(num_assets) / num_assets

    result = minimize(objective, initial_weights, method='SLSQP',
                      bounds=bounds, constraints=constraints,
                      options={'disp': False, 'maxiter': 1000})

    weights = result.x
    ret, vol, sharpe = portfolio_performance(weights)
    return weights, ret, vol, sharpe, tickers, returns
