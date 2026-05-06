# Python script to demonstrate how to handle / deal with missing values

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a sample dataset
data = {
    'Name': ['Abigail', 'Mueni', "Eve", "David", "Charlie"],
    'Age': [24, 22, np.nan, 32, np.nan],
    'City': ['New York', 'Makueni', 'Paris', np.nan, 'Toronto']
}

# 2. Convert the dictionary into a pandas dataframe
df = pd.DataFrame(data)

# 3. Display the original dataframe with missing values
print(f"Original Dataset with missing values:\n{df}")

# 4. Handle missing data
# Option 1: Drop rows with missing values
df_dropna = df.dropna()
# Display the dataset after dropping rows with missing values
print(f"Dataset after dropping rows with missing values:\n{df_dropna}")

# Option 2. Impute / fill in the missing values
# (Fill in the mean for the 'age' column)
df.fillna({'Age': df['Age'].mean()}, inplace=True)
# Fill in the missing categorical values (forward fill for the 'City' column)

df['City'] = df['City'].ffill()

# 6. Display the dataset after imputing the missing values
print(f"Dataset after filling missing values:\n{df}")