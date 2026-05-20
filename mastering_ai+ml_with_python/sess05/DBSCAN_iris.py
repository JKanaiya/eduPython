import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
X = iris.data[:, :2]  # user use the first two features for visualization purposes

# Applying DBSCAN
eps = 0.5
min_samples = 5
dbscan = DBSCAN(eps=eps, min_samples=min_samples)
dbscan.fit(X)

# Extracting core points, border points, and noise points
core_samples_mask = np.zeros_like(dbscan.labels_, dtype=bool)
core_samples_mask[dbscan.core_sample_indices_] = True
labels = dbscan.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

# Plotting the clusters
plt.figure(figsize=(8, 6))

# Plot all points
plt.scatter(X[:, 0], X[:, 1], c="gray", marker="o", s=30, label="Data Points")

# Plot core points
plt.scatter(
    X[core_samples_mask][:, 0],
    X[core_samples_mask][:, 1],
    c="blue",
    marker="o",
    s=100,
    label="Core Points",
)

# Plot border points
border_points_mask = ~core_samples_mask & (labels != -1)
plt.scatter(
    X[border_points_mask][:, 0],
    X[border_points_mask][:, 1],
    c="orange",
    marker="o",
    s=50,
    label="Border Points",
)

# Plot noise points
plt.scatter(
    X[labels == -1][:, 0],
    X[labels == -1][:, 1],
    c="red",
    marker="x",
    s=50,
    label="Noise Points",
)

plt.title("DBSCAN Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
