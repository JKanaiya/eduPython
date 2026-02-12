# Python script to demonstrate heirachical clustering algorithm

# Import the required module
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# Generate a synthetic customer dataset with income and spending score
data = {
    'Income': np.random.randint(20000, 100000, 50),
    'Spending Score': np.random.randint(1, 50, 50)
}

# Create a Dataframe and display 10 rows
df = pd.DataFrame(data)
print(f"The first 10 rows of the customers income and spending score are: {df.head(10)}")

# Visualise the entire dataset
plt.figure(figsize=(10, 8))
plt.scatter(df['Income'], df['Spending Score'])
plt.title("Synthetic Data: Income vs spending score")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

# Create a dendrogram
plt.figure(figsize=(10, 8))
dendrogram = sch.dendrogram(sch.linkage(df, method='ward'))
plt.title("Dendogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# Apply Agglomerative Clustering
hc = AgglomerativeClustering(n_clusters=3, metric='euclidean', linkage='ward')
df['Cluster'] = hc.fit_predict(df)

# Plot the clusters
plt.figure(figsize=(10, 6))
plt.scatter(df['Income'], df['Spending Score'], c=df['Cluster'], cmap='viridis')
plt.show()