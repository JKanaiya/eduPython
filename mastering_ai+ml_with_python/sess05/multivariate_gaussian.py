import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import multivariate_normal

# Sample Data Generation
np.random.seed(42)

# Generate a 2D dataset with correlation
mean = [0, 0]
covariance_matrix = [[1, 0.5], [0.5, 1]]
data = np.random.multivariate_normal(mean, covariance_matrix, 1000)

# Calculate Covariance Matrix
cov_matrix = np.cov(data, rowvar=False)

# Create a Multivariate Gaussian Distribution
multivariate_dist = multivariate_normal(mean=mean, cov=covariance_matrix)

# Visualize Ellipsoidal Contours
x, y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
pos = np.dstack((x, y))
contour_levels = multivariate_dist.pdf(pos)

plt.scatter(data[:, 0], data[:, 1], alpha=0.5, label="Sample Data")
plt.contour(x, y, contour_levels, levels=10, colors="r", linewidths=2)
plt.title("Multivariate Gaussian Distribution")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
