# Python script to demonstrate various operations on pandas dataframes
# likely filtering, grouping, merging, and other dataframe operations

# Import the required modules
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# 1. Create a sample employee dataframe
print("----1. Create a sample employee dataframe ----")
employees = pd.DataFrame({
    'EmployeeID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Abigail', 'Kamau', 'Sharlene', 'Diana', 'Mueni'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['Nakuru', 'Limuru', 'Kisumu', 'Homabay', 'Makueni'],
    'Salary': [55000, 65000, 72000, 48000, 60000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'Finance']
})

# Create a sales dataframe
sales = pd.DataFrame({
    'EmployeeID': [1001, 1002, 1003, 1004, 1005],
    'Q1_Sales': [15000, 22000, 18000, 12000, 25000],
    'Q2_Sales': [18000, 22000, 18000, 12000, 25000],
    'Q3_Sales': [22000, 26000, 22500, 15500, 32000],
})

# Display the employee and sales dataframes
print("Employee dataframe".center(55, "-"))
print(employees)
print()
print("Sales dataframe".center(55, "-"))
print(sales)

# 2. Merge 2 dataframes (i.e Employee & Sales on EmployeeId)
print("----2. Merge 2 dataframes (i.e Employee & Sales on EmployeeId) ----")
combined = pd.merge(employees, sales, on='EmployeeID', how='left')
print("Employee & Sales DataFrame".center(100, "-"))
print(combined)

# 3. Adding calculated columns
print("----3. Adding calculated columns ----")
combined['Total_Sales'] = combined['Q1_Sales'] + combined['Q2_Sales'] + combined['Q3_Sales']
combined['Avg_Sales'] = combined['Total_Sales'] / 3.0
combined['Bonus'] = combined['Total_Sales'] * 0.02
print(f"Dataframe with calculated columns:\n{combined}")

# 4. Filtering Employee data
print("----4. Filtering employee data ----")
print("Employees in IT department:")
IT_employees = employees.loc[employees['Department'] == 'IT']
# it_employees = combined[combined['Department'] == 'IT'] # Will give other details from the combined dataframe
print(IT_employees)

print("\nEmployees earning more than 60k")
high_salary = employees.loc[employees['Salary'] > 60000]
print(high_salary)
print()

# 5. Grouping and aggregating employee data
print("----5. Grouping and aggregating employee data ----")
department_stats = combined.groupby(['EmployeeID', 'Department']).agg({
    'Salary': ['mean', 'sum', 'min', 'max']
})
print(department_stats)
