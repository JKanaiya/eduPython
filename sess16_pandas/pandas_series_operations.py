# Python script to demonstrate various operatons on Pandas series

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create and display a sample series
print("----1. Create and display a daily sales series ----")
sales = pd.Series([250, 320, 180, 450, 290, 510, 380], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                  name="Daily Sales")
print(sales)
print("*" * 50)

# 2. Basic mathematical operation on the 'Daily Sales' sample series
print("\n----2. Basic mathematical operation on the 'Daily Sales' sample series ----")
print(f"Original Sales:\n {sales}\n")
# Scalar operation to increase by 10%
print("Sales with a '10%' increase:\n")
sales_increase = sales * 1.1
print(f"{sales_increase}\n")
# Element-wise operations
print("Sales minus 50")
sales_adjusted = sales - 50
print(f"{sales_adjusted}\n")
print("*" * 50)

# 3. Series with series operations
print("\n----3. Series with series operations ----")
discounts = pd.Series([20, 30, 15, 40, 25, 50, 35], index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print(f"Discounts\n{discounts}\n")
print("*" * 50)

# 4. Filtering and conditional operations
print("\n----4. Filtering and conditional operations ----")
print("Days with sales > 300")
high_sales = sales[sales > 300]
print(f"{high_sales}\n")
print("Weekend sales (i.e. Sat & Sun)")
weekend_sales = sales[['Sat', 'Sun']]
print(f"{weekend_sales}\n")

# 5. Statistical operations
print("\n----5. Statistical operations ----")
print(f"Total sales Kes. {sales.sum():.2f}")
print("*" * 50)
print(f"Average sales Kes {sales.mean():.2f} on {sales.idxmax()}")
print(f"Highest sales Kes. {sales.max():.2f} on {sales.idxmax()}")
print(f"Lowest sales Kes. {sales.min():.2f}")
print(f"Standard deviation Kes. {sales.std():.2f}")
print("*" * 50)

# 6. Applying functions
print("\n----6. Applying functions ----")
print(f"Applying square root to sales")
sqrt_sales = sales.apply(lambda x: round(np.sqrt(x), 2))
print(f"{sqrt_sales}\n")
print("*" * 50)

# 7. Missing Data operations
print("\n----7. Missing Data operations ----")
sales_with_na = pd.Series([250, None, 180, 450, None, 510, 380],
                          index=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
print(f"Sales series with missing data:\n{sales_with_na}\n")
print("Fill missing data / values with mean:")
filled_sales_series = sales_with_na.fillna(sales_with_na.mean())
print(f"{filled_sales_series}\n")
print("*" * 50)
