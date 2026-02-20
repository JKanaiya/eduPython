# Python file to demonstrate Naive Bayes algorithm for News article classification
# (20 newsgroups). It demonstrates Multinomial Naive Bayes
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Import the required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline

# 1. Load data (subset of categories for faster demo)
categories = [
    'rec.sport.hockey',
    'rec.sport.baseball',
    'sci.space',
    'sci.med',
    'talk.politics.guns',
    'comp.graphics',
    'comp.os.ms-windows.misc',
]

print("Loading data...")
data = fetch_20newsgroups(subset='all', categories=categories, remove=('headers', 'footers', 'quotes'), random_state=42)

X = data.data
y = data.target

target_names = data.target_names

print(f"Number of documents: {len(y)}")
print(f"Number of classes: {len(target_names)}")
print()

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print(f"Training set size: {len(X_train):,} documents\ntest set size: {len(X_test):,} documents\n")

# 3. Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_df=0.95,  # ignore very common words
        min_df=5,  # ignore very rare words
        stop_words='english',
        ngram_range=(1, 2),
        analyzer='word',  # include bigrams
    )),
    ('clf', MultinomialNB(alpha=0.01)),
])

# 4. Train the mode
print("Training the Naive Bayes model...")
pipeline.fit(X_train, y_train)

# 5. Make predictions and evaluate them
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, target_names=target_names, digits=3)

# 6. Display the evaluation metrics
print(f"Naive Bayes Accuracy: {accuracy:.2f}")
print(f"Naive Bayes Confusion Matrix:\n{cm}")
print(f"Naive Bayes Classification Report:\n{class_report}")

# 7. Visualise the results
plt.figure(figsize=(10, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=target_names)
disp.plot(
    cmap=plt.cm.Blues,
    values_format='d',
    xticks_rotation=45,
    ax=plt.gca()
)

plt.title('Confusion Matrix - Multinomial Naive Bayes\n(20 Newsgroups subset)', fontsize=14, pad=20)
plt.tight_layout()
plt.show()

# Optional: normalised confusion matrix (row-wise = recall per class)
cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

plt.figure(figsize=(10, 8))
sns.heatmap(
    cm_norm,
    annot=True,
    fmt='.2f',
    cmap='Blues',
    xticklabels=target_names,
    yticklabels=target_names,
    cbar_kws={'label': 'Proportion'}
)
plt.title("Normalised Confusion Matrix (rows = true class)", fontsize=14, pad=20)
plt.xlabel("Predicted label", fontsize=12)
plt.ylabel("True label", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()