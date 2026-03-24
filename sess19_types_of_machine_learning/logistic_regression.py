# Python ML script to use Logistic Regression model to determine whether a person / customer buys a product or not

# Import the required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create a sample dataset
# Features: [Age, Estimated Salary]
# Labels: [0 -> not buy, 1 -> buy]
data = {
    "Age": [22, 25, 47, 52, 46, 56, 55, 60, 62, 61, 30, 32, 34, 35, 40],
    "Estimated Salary": [
        15000,
        29000,
        35000,
        43000,
        70000,
        80000,
        20000,
        25000,
        90000,
        110000,
        60000,
        52000,
        78000,
        65000,
        120000,
    ],
    "Buy": [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1],
}

df = pd.DataFrame(data)

# Display the dataset
print(f"Training Dataset:\n{df}")

# Separate the features and the target
X = df[["Age", "Estimated Salary"]]
y = df["Buy"]

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Scale the features for better performance
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialise the logistic regression model
log_reg = LogisticRegression()

# Train the model
log_reg.fit(X_train, y_train)

# Make the prediction
y_pred = log_reg.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=["Not Buy", "Buy"])

# Display the results
print(f"Accuracy of the logistic regerssion model: {accuracy}")
print(f"y train: {y_train}")
print(f"y pred: {y_pred}")
print(f"Confusion matrix of the logistic regression model:\n{conf_matrix}")
print(f"Classification report of the logistic regression model:\n{class_report}")

