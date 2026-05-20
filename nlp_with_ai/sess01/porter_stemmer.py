# Code for Stemming using NLTK
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Sample text
text = "Named Entity Recognition is crucial in natural language processing tasks, identifying entities such as organizations, persons, and locations."

# Tokenize into words
words = word_tokenize(text)

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# Stem the words
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Output: Stemming
print("Stemming:")
print(stemmed_words)
