# Python script to demonstrate how to create, display, and access data from using pandas series

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a series from a list
print("---1. Create a pandas series from a list")
temperatures = [2, 68, 75, 79, 83, 77, 70]
temp_series = pd.Series(temperatures, name='Daily Temperatures')
print(temp_series)
print(f"Series name: {temp_series.name}")
print(f"Series type: {type(temp_series)}")
print(f"Series Data Type (dtype): {temp_series.dtype}")

print("*" * 50)

# 2. Create a series with a custom index
print("---2. Create a series with a custom index")
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temp_series_indexed = pd.Series(temperatures, index=days, name='Daily Temperature by Day')
print(temp_series_indexed)
print(f"Index values: {temp_series_indexed.index.tolist()}")

print("*" * 50)

# 3. Create a series from a dictionary
print("---3. Create a series from a dictionary")
stock_prices = {"Kakuzi": 175.25, "Sasini": 138.45, "ABSA": 327.85, "Equity": 145.18}
stock_series = pd.Series(stock_prices, name='Stock Prices')
print(stock_prices)
print(stock_series)

print("*" * 50)
