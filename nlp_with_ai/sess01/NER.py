# Code for Named Entity Recognition (NER) using NLTK
import nltk
from nltk import ne_chunk, pos_tag
from nltk.tokenize import word_tokenize

nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

# Sample text
text = "Natural language processing explores applications such as sentiment analysis and named entity recognition."

# Tokenize into words
words = word_tokenize(text)

# Perform Part-of-Speech tagging
pos_tags = pos_tag(words)

# Perform Named Entity Recognition
ner_result = ne_chunk(pos_tags)

# Output: Named Entity Recognition
print("Named Entity Recognition:")
print(ner_result)
