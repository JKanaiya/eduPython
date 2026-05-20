# Code for Text Normalization using NLTK
import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet

# Sample text
text = "Natural language processing is a fascinating field of studies."

# Tokenize into words
words = nltk.word_tokenize(text)

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Normalize by lemmatization
normalized_words = [lemmatizer.lemmatize(word, wordnet.VERB) for word in words]

# Output: Text Normalization
print("Text Normalization:")
print(normalized_words)
