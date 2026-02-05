# Python script to demonstrate one-hot encoding and label encoding on a sample dataset

# Import the required modules
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Sample dataset of colors, sizes, and cities
data = pd.DataFrame({
    'colour': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
    'size': ['Small', 'Medium', 'Large', 'Small', 'Large'],
    'city': ['London', 'Paris', 'London', 'New York', 'Paris']
})

# display the original dataset
print("Original Dataset")
print("-" * 55)
print(data)
print("-" * 55)

# 1. One-Hot Encoding the 'color' and 'city' columns
data_onehot = pd.get_dummies(data, columns=['colour', 'city'], prefix=["color", "city"])
# display the dataset after one-hot encoding it
print("\nData after One-Hot Encoding")
print("-" * 55)
print(data_onehot)
print("-" * 55)

# 2. Label Encoding the 'size' column as it has an inherent order (small < medium < large)
size_mapping = {'Small': 1, 'Medium': 2, 'Large': 3}  # Define the order for the size
data['size_encoded'] = data['size'].map(size_mapping)  # Map each category to an integer

# Alternatively, LabelEncoder can be used for non-ordinals
label_encoder = LabelEncoder()
data['color_encoded'] = label_encoder.fit_transform(data['colour'])

# 3. Display the data after label encoding it
print("\nData after Label encoding")
print("-" * 55)
print(data[['size', 'size_encoded', 'color_encoded', 'colour']])
print("-" * 55)

# --- Visualising Encoded Data ---
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plot one-hot encoded data for colours
one_hot_encoded = pd.get_dummies(data['colour'])
one_hot_encoded.sum().plot(kind='bar', ax=ax[0], color=['blue', 'green', 'red'])
ax[0].set_title("One-Hot Encoded 'Colour' Distribution")
ax[0].set_xlabel("Colours")
ax[0].set_ylabel("Frequency")

# Plot label encoded data for size
ax[1].hist(data['size_encoded'], bins=3, color='lightcoral', edgecolor='black')
ax[1].set_title("Label Encoded 'Size' Distribution")
ax[1].set_xlabel("Size Encoded Values")
ax[1].set_ylabel("Frequency")

plt.tight_layout()
plt.show()


