# Python file to analyze and predict the unemploment rate based on GDP
# using polynomial regression

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Get the path to the file with GDP & Unemployment values
file_path = os.path.abspath(os.path.join(os.getcwd(), "..", "files", "gdp_unemployment.csv"))

# Load the data from the csv file
data = pd.read_csv(file_path)

# Get the year and its GDP
year = data['Year'].values.reshape(-1, 1)
gdp = data['GDP'].values.reshape(-1, 1)
unemployment = data['Unemployment Rate'].values.reshape(-1, 1)

# Create the polynomial features
poly = PolynomialFeatures(degree=2)  # You can adjust the degree (squared terms) suit your models need
X_poly = poly.fit_transform(gdp)

# Train / fit the model
model = LinearRegression()
model.fit(X_poly, unemployment)

# Predict the unemployment rate for 2020 given a GDB of $620 billion
gdp_2020 = np.array([[620]])
gdp_2020_poly = poly.transform(gdp_2020)
predicted_unemployment = model.predict(gdp_2020_poly)

# Display the predicted unemployment rate / percentage
print(f"The predicted unemployment rate for 2020 @ GDP $ 620 billion is: {predicted_unemployment[0][0]:.2f}")

# Plot the graph
plt.scatter(gdp, unemployment, color='blue', label="Data points")
gdp_range = np.linspace(290, 630, 100).reshape(-1, 1)
gdp_range_poly = poly.fit_transform(gdp_range)
predicted_rates = model.predict(gdp_range_poly)
plt.plot(gdp_range, predicted_rates, color='red', label='Predicted rates')
plt.scatter(gdp_2020, predicted_unemployment, color='orange', label='2020 Prediction',
            s=100, edgecolor='black')
plt.title("GDP vs Unemployment")
plt.xlabel("GDP in Billion $")
plt.ylabel("Unemployment Rate %")
plt.legend()
plt.show()
