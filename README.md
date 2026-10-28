# Project Summary: Stock Portfolio Optimizer

The goal of this project is to create a Python-based application that uses historical financial data from CAC 40 companies to optimise portfolios. By combining quantitative finance, data science, and interactive visualisation, the optimiser helps users create investment portfolios that are customised to their number of stock and maximum weight of a single asset.

## Brief description of the Modules:

- extract.py: Loads and merges historical stock data from multiple local CSV files (2021–2023).  
- transform.py: Cleans and standardizes the dataset by renaming columns, parsing dates, and removing missing values.  
- load.py: Saves the cleaned data into a local SQLite database using sqlite3.  
- main.py: Executes the complete ETL pipeline in a single script.  
- portfolio.py: Computes asset returns and covariances, and performs portfolio optimization using scipy.optimize to maximize the Sharpe Ratio.  
- app.py: Contains the interactive Streamlit dashboard for exploring and visualizing the optimized portfolio.  

## Optimization Logic:

- Input: A matrix of historical asset returns from a csv file containing data from CAC 40 index.  
- Constraints:  
  - Minimum and maximum number of assets in the portfolio.  
  - Maximum allowable weight per stock.  
- Solver: scipy.optimize.minimize is used to find the optimal weight vector under these constraints using a penalty term  

The final result is presented via a Streamlit dashboard, which allows users to interactively to adjust portfolio construction constraints such as the minimum and maximum number of assets and the maximum weight per stock. It displays cumulative portfolio returns through a time-series plot and provides visual insights into portfolio composition using bar charts and detailed weight tables. Additionally, the dashboard presents key performance metrics, including expected return, annualized volatility, and the Sharpe ratio.  

## References:

bryanb. (n.d.). CAC40 Stocks Dataset [Data set]. Kaggle. from https://www.kaggle.com/datasets/bryanb/cac40-stocks-dataset (SpringerLink)  
DataCamp. (n.d.-a). Intro to Python for Data Science [Online course]. https://www.datacamp.com/courses/intro-to-python-for-data-science  
Matplotlib Tutorial (n.d). Matplotlib 3.10.3 [Documentation]. https://matplotlib.org/stable/tutorials/index.html  
pixegami. (2023). Learn Python • #12 Final Project • Build an Expense Tracking App! [Video]. YouTube. https://www.youtube.com/watch?v=HTD86h69PtE (YouTube, classcentral.com)  
QuantPy. (2021). Python for Finance: Are stock returns normally distributed? [Video]. YouTube. https://www.youtube.com/watch?v=NNu1DjWcYeY (youtube.com, youtube.com)  
Syal, A. (n.d.). Python Fundamentals for Data Engineering: Create your first ETL Pipeline [Video]. YouTube. https://www.youtube.com/watch?v=uqRRjcsUGgk (youtube.com)  
