# Python script to demonstrate outlier detection and handling using IQR(Interquartile Range)

# Import the required modules
import pandas as pd
import numpy as np

# 1. Create a sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [5, 35, 32, 39, 45, 120, 28],  # '120' & 5 are outliers
    'Salary': [50000, 2500, 54000, 52000, 110000, 47000, 51000]  # '2500' & '110000' are outliers
}

# 2. Convert the dictionary into a dataframe
df = pd.DataFrame(data)

# 3. Display the original dataframe
print(f"Original Dataframe:\n{df}")

# 4. Detect outliers using IQR method for the 'Age' column
Q1 = df['Age'].quantile(0.25)  # First quartile (Q1)
Q3 = df['Age'].quantile(0.75)  # Third quartile (Q3)
IQR = Q3 - Q1  # Get the interquartile range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# TODO: Detect outliers using the IQR method for 'Salary' column
sQ1 = df['Salary'].quantile(0.25)
sQ3 = df['Salary'].quantile(0.75)
sIQR = sQ3 - sQ1
slower_bound = sQ1 - 1.5 * sIQR
supper_bound = sQ3 + 1.5 * sIQR

# Identify and display the outliers for the 'Age' column
df_no = df[(df['Age'] < lower_bound) | (df['Age'] > upper_bound)]
# Display the dataset after removing the outliers for the 'Age' column
print(f"\nDetected outliers for the 'Age' column:\n{df_no}")

# Identify and display the outliers for the 'Salary' column
df_no_salary = df[(df['Salary'] < slower_bound) | (df['Salary'] > supper_bound)]
# Display the dataset after removing the outliers for the 'Salary' column
print(f"\nDetected outliers outliers for the 'Salary' column:\n{df_no_salary}")

# 5. Handle the outliers -> method i) Remove / rop the outliers
df_no_age_outliers = df[(df['Age'] >= lower_bound) & (df['Age'] <= upper_bound)]
print(f"\nDataset after removing outliers for the 'Salary' column:\n{df_no_age_outliers}")

# 6. Handle the outliers -> method ii) Cap the outliers
df['Age'] = np.where(df['Age'] < lower_bound, lower_bound, np.where(df['Age'] > upper_bound, upper_bound, df['Age']))
print(f"\nDataset after removing outliers for the 'Salary' column:\n{df_no_age_outliers}")
# Display the dataset after capping outliers for the 'Age' column
print(f"\nDataset after capping outliers for the 'Age' column:\n{df}")
