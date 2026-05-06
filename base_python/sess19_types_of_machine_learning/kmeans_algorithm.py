# Python file to demonstrate the k-means algorithm to determine customer segmentation based on income and
# spending score

# Import the required modules
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate a syntehtic dataset
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.5, random_state=42)

# Convert the data to a dataframe
df = pd.DataFrame(X, columns=['Income', 'Spending Score'])

# Display the first 10 rows of the dataframe
# print(f"The first 10 rows of the income & spending dataframe:\n{df[:10]}")
print(f"The first 10 rows of the income & spending dataframe:\n{df.head(10)}")

# Visualise the dataset
plt.scatter(df['Income'], df['Spending Score'])
plt.title("Synthetic Dataset: Income vs Spending Score")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()

# Apply K-means
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

# Adding cluster labels to the Dataframe
df['Cluster'] = kmeans.labels_

# Plot the clusters
plt.scatter(df['Income'], df['Spending Score'], c=df['Cluster'], cmap='viridis', marker='o')
plt.title("K-means Clusters")
plt.xlabel("Income")
plt.ylabel("Spending Score")

# Plot the cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], s=200, color='red', marker='X', alpha=0.75, label="Centroids")
plt.legend()
plt.show()

# Evaluate the omdel
print(f"Inertia: {kmeans.inertia_}")
# Inertia is the sum of squared distances between each point and its assigned cluster center.
# It helps to assess how well the clusters have been formed, with lower values
# indicating tighter clusters.
