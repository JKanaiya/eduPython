# Python script that uses SVM (Support Vector Machine) to classify a fruit as either
# an apple or an orange based its weight and size

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create a synthetic dataset for classificying fruits (apples & oranges) using
# 'weight' and 'size' as features

np.random.seed(42) # for reproducibility

# Generate the data for apples
weight_apples = np.random.normal(150, 18, 50) # avg weight of apple is 150 grams
size_apples = np.random.normal(7, 1.6, 50) # Size around 7 cm
label_apples = np.ones(50) # Use label 0 for apples

# Generate the data for orangs
weight_oranges = np.random.normal(200, 18, 50) # avg weight of orange is 200 grams
size_oranges = np.random.normal(7, 1.6, 50) # Size around 8.5 cm
label_oranges = np.zeros(50) # Use label 1 for oranges

# Combine the above data into a sigle dataset
weight = np.concatenate((weight_apples, weight_oranges), axis=0)
size = np.concatenate((size_apples, size_oranges), axis=0)
labels = np.concatenate((label_apples, label_oranges), axis=0)

# Feture matrix and target vector
X = np.column_stack((weight, size))
y = labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialse the SVM model with a linear kernel
svm_clf = SVC(kernel='linear', C=1.0)

# Train the model
svm_clf.fit(X_train, y_train)

# Make the predictions
y_pred = svm_clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matric = confusion_matrix(y_test, y_pred)
classf_report = classification_report(y_test, y_pred, target_names=["Apples", "Oranges"])

# Display yhe results
print(f"Accuracy of KNN model:\n {accuracy}")
print("*" * 50)
print(F"Confusion matric of KNN model:\n {conf_matric}")
print("*" * 50)
print(f"Classification report of KNN model:\n {classf_report}")