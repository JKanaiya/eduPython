# Python script to demonstrate anomaly detection using Isolation forest

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

# Generate a synthetic dataset for incom and spending score
np.random.seed()  # Leave seed blank for randome values / use a number for same values e.g 42

# Creating normal data point around incom (30k - 70k) and spending score (20 - 80)
income = np.random.normal(50_000, 10000, 300)
spending_score = np.random.normal(50, 15, 300)
X = np.column_stack((income, spending_score))

# Introduce the anomalies with higher or lower income and spending score
anomalies = np.array([[100_000, 10], [20_000, 90], [80_000, 75], [35000, 5], [60000, 95]])
X = np.vstack((X, anomalies))

# Convert the data into a datafram for ease of use
df = pd.DataFrame(X, columns=['Income', 'Spending Score'])

print(f"First five rows:\n{df.head(5)}")

# Apply isolation Forest
iso_forest = IsolationForest(contamination=.02, random_state=42)
df['Anomaly Score'] = iso_forest.fit_predict(df[['Income', 'Spending Score']])

# Seperate the normal points and anomalies
normal = df[df['Anomaly Score'] == 1]
anomaly = df[df['Anomaly Score'] == -1]

# Plot the results
plt.figure(figsize=(10, 6))
plt.scatter(normal['Income'], normal['Spending Score'],
            color='blue', label='Normal', alpha=0.7)

plt.scatter(anomaly['Income'], anomaly['Spending Score'],
            color='red', label='Anomaly', marker='x', s=100)
plt.xlabel('Income')
plt.ylabel('Spending Score')
plt.title("Anomaly Detection Using Isolation Forest")
plt.legend()
plt.grid(True)
plt.show()
