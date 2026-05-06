# Python script to introduce Pandas Dataframes by demonstrating how to cerate, display and explore them.

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a Data frame from a dictionary
print("\n----1. Create a Data frame from a dictionary ----")
data = {
    "Name": ["Abigail", "Kamau", "Sharlene", "Diana", "Mueni"],
    "Age": [25, 30, 35, 28, 32],
    "City": ["Nakuru", "Limuru", "Kisumu", "Homabay", "Makueni"],
    "Salary": [55000, 65000, 72000, 48000, 60000],
    "Department": ["HR", "IT", "IT", "Marketing", "Finance"],
}
print("*" * 50)

df = pd.DataFrame(data)
print(f"Employee Details dataframe created from dictionary:\n{df}")

# 2. Create a Dataframe with custom index
print("\n----2. Create a Dataframe with custom index ----")
df_indexed = pd.DataFrame(data, index=["Emp1", "Emp2", "Emp3", "Emp4", "Emp5"])
print(f"{df_indexed}")
print("*" * 50)

# 3. Dataframe attributes and information
print("\n----3. Dataframe attributes and information ----")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")
print(f"Data types: {df.dtypes}")
print("*" * 50)

# 4. Display methods 'head()' & 'tail()'
print("\n----4. Display methods 'head()' & 'tail()' ----")
print(f"First 3 rows of employee details using 'head()'\n{df.head(3)}")
print(f"Last 3 rows of employee details using 'tail()'\n{df.tail(3)}")
print("*" * 50)

# 5. Accessing data from a Dataframe
print("\n----5. Accessing data from a Dataframe ----")
print("Single column (series):\n")
print(f"df['Name']\n")
print(f"Multiple columns:\n{df[['Name', 'Age', 'Department']]}")
print(f"Access by index position (iloc):")
print(f"First row: \n{df.iloc[0]}")
print(f"Specific cell (row 2, column 'Age':\n{df.iloc[1, 1]}")
print(f"Access by label (loc):\nEmployee with index 2:\n{df.loc[2]}")
print("*" * 50)

# 6. Create a Dataframe from a list of lists
print("\n----6. Create a Dataframe from a list of lists ----")
product_data = [
    ["Laptop", 99999.5, "Electronics", 50],
    ["Mouse", 250.0, "Electronics", 200],
    ["Notebook", 599.0, "Stationary", 150],
    ["Pen", 199.0, "Stationary", 150],
]

product_df = pd.DataFrame(
    product_data, columns=["Product", "Price", "Category", "Stock"]
)
print(f"Product dataframe:\n{product_df}")
print("*" * 50)

# 2. Create a Dataframe with custom index
print("\n----2. Create a Dataframe with custom index ----")

print("*" * 50)
