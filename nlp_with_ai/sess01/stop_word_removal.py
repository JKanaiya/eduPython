# Code for Stopword Removal using NLTK
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text
text = "Natural language processing is a fascinating field of study, and it involves the analysis of textual data."

# Tokenize into words
words = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Output: Stopword Removal
print("After Stopword Removal:")
print(filtered_words)
