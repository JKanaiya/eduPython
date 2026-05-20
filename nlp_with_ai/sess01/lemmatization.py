# Code for Lemmatization using NLTK
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("wordnet")

# Sample text
text = "Named Entity Recognition is crucial in natural language processing tasks, identifying entities such as organizations, persons, and locations."

# Tokenize into words
words = word_tokenize(text)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Lemmatize the words
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

# Output: Lemmatization
print("Lemmatization:")
print(lemmatized_words)
