# Python script to demonstrate stemming with visualization

# --------------------------------------------------------------------
# 0. Import
# --------------------------------------------------------------------

import re
from collections import Counter

import matplotlib.pyplot as plt
import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# --------------------------------------------------------------------
# 1. Download the required data
# --------------------------------------------------------------------

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab")


# --------------------------------------------------------------------
# 2. Sample text to be stemmed
# --------------------------------------------------------------------

TEXT = """
The researchers were studying the running patterns of various animals.
They observed that faster runners consistently outperformed slower ones.
The studies showed interesting running behaviours.
"""

# Initialize the stemmer
stemmer = SnowballStemmer("english")


# --------------------------------------------------------------------
# 3. Text Preparation Function
# --------------------------------------------------------------------


def preprocess_text(text: str) -> list:
    """
    Tokenise and clean the input text

    This Function converts text to lowercase, removes punctutation, and returns a lost of valid word tokens

    :param: text: Raw input text
    :return: List of cleaned word tokens
    """
    tokens = word_tokenize(text.lower())

    cleaned_tokens = [re.sub(r"[^a-z]", "", token) for token in tokens]

    return [token for token in cleaned_tokens if token]


# --------------------------------------------------------------------
# 4. Stemming Function
# --------------------------------------------------------------------


def apply_stemming(tokens: list) -> list:
    """
    Apply stemming to a list of tokens
    :param tokens : List of word tokens
    :return: list of stemmed word tokens
    """

    return [stemmer.stem(token) for token in tokens]


# --------------------------------------------------------------------
# 5. visualization Function
# --------------------------------------------------------------------


def plot_frequencies(original: list, stemmed: list) -> None:
    """
    Plot frequency comparison between original and stemmed word tokens

    This helps illustrate how stemming groups similar words together

    :param original: List of original word tokens
    :param stemmed: List of stemmed word tokens
    """

    original_counts = Counter(original)
    stemmed_counts = Counter(stemmed)

    # Select top items for clarity
    top_original = dict(original_counts.most_common(5))
    top_stemmed = dict(stemmed_counts.most_common(5))

    # Plot original word frequencies
    plt.figure(figsize=(12, 8))
    plt.bar(top_original.keys(), top_original.values())
    plt.title("Top Original Words")

    # Plot stemmed word frequencies
    plt.figure(figsize=(12, 8))
    plt.bar(top_stemmed.keys(), top_stemmed.values())
    plt.title("Top Stemmed Words")

    plt.show()


# --------------------------------------------------------------------
# 6. Main Execution Function
# --------------------------------------------------------------------


def main():
    """
    Execute the stemming demonstration

    This demonstrates text preprocessing, stemming and visual comparison

    """
    print(f"\nOriginal Text:\n{TEXT}")

    # Preprocess the text
    tokens = preprocess_text(TEXT)
    print(f"\nTokens:\n{tokens}")

    # Apply stemming
    stemmed_tokens = apply_stemming(tokens)
    print(f"\nStemmed Tokens:\n{stemmed_tokens}")

    # Show/display visual comparison
    plot_frequencies(tokens, stemmed_tokens)


# --------------------------------------------------------------------
# 7. Run the script by invoking it's main() function
# --------------------------------------------------------------------
if __name__ == "__main__":
    main()
