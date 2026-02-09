# Python script to predict sales for a given year (2019) based on advertisement
# and sales data using simple linear regression

# Import the required modules
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression

# Sample dataset
years = np.array([2014, 2015, 2016, 2017, 2018])
advertisement = np.array([90, 120, 150, 100, 130])
sales = np.array([1000, 1300, 1800, 1200, 1380])

# Reshape the data to make it a 2D array
year = years.reshape((-1, 1))
advertisement = advertisement.reshape((-1, 1))

model = LinearRegression()
model.fit(advertisement, sales)  # Fit the model using training data

# Predict the sales for 2019 given an advertisement budget of 200
sales_2019 = model.predict([[200]])  # Use the model to predict the sales for the year 2019

# Print / display the sales prediction for 2019
print(f"Sales prediction for the year 2019 with an advertisement of $200:\n${sales_2019}")

# For plotting purposes, revert the advertiseing data back to a 1D array
advertisement = advertisement.reshape((-1, 1))

# Variables to plot / visualise the sales and advertising data
slope, intercept, r_value, p_value, std_err = stats.linregress(advertisement, sales)

# Define a function to calculate the linear regression model
def simple_regression(advertisement):
    return slope * advertisement + intercept

# Define the simple linear regression model
simple_regression_model = list(map(simple_regression, advertisement))

# Visualise the data
plt.scatter(advertisement, sales)
# plt.plot(advertisement, simple_regression_model)
plt.title("Advertisement VS Sales")
plt.xlabel("Advertisement Budget")
plt.ylabel("Sales")
plt.show()