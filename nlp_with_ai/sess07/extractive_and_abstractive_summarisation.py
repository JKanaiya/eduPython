# --------------------------------------------------------------------
# Python script to demonstrate Text Summarization using extractive methods and Text Generation
# --------------------------------------------------------------------
"""
script demonstrates extractive Summarization, abstractive Summarization, and text generation using lightweight and beginner-friendly NLP tools

Requirements:
1. transformers
2. torch
3. nltk
4. scikit-learn
5. hf-xet

NOTE:
the first execution downloads small pretrained models and will be a bit slow.
subsequent runs will use the cacheed locals and will be faster

"""
# -------------------------------------------------------------------------------------
# 0. Import the required modules
# -------------------------------------------------------------------------------------

import textwrap
import time
import warnings

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import logging as hf_logging
from transformers import pipeline

hf_logging.set_verbosity_error()  # Get only error messages on the output console

# suppress all UserWarnings and FutureWarnings from transformers & other libraries to ensure console output remains clean
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)


# -------------------------------------------------------------------------------------
# 1. Download required NLTK data
# -------------------------------------------------------------------------------------

REQUIRED_NLTK_RESOURCES = [
    "punkt",
    "punkt_tab",
    "stopwords",
]

for resource in REQUIRED_NLTK_RESOURCES:
    try:
        nltk.data.find(resource)

    except LookupError:
        print(f"Downloading NLTK resource: {resource}")
        nltk.download(resource, quiet=True)

# -------------------------------------------------------------------------------------
# 2. Source text to be summarized
# -------------------------------------------------------------------------------------

SOURCE_TEXT = """
In this session, students should take a comprehensive look into machine
translation and language production with neural networks. The learning
objectives are designed to give students a comprehensive understanding
of these issues, beginning with an overview of machine translation and
its numerous kinds. Students study the issues faced by machine
translation systems via illustrative examples and debates. This paves
the way for a more in-depth understanding of the complexities.

The session then delves into the intriguing area of neural language
models, offering insight into their mechanics and applications.
Students should acquire hands-on experience creating and experimenting
with neural language models for language generation challenges through
interactive exercises and code examples.

At the conclusion of this session, students will have a thorough
understanding of machine translation, neural language synthesis, and
how to effectively address real-world language processing difficulties.
"""


# -------------------------------------------------------------------------------------
# 3. Helper Functions
# -------------------------------------------------------------------------------------


def print_heading(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def print_wrapped(text: str) -> None:
    print(textwrap.fill(text.strip(), width=80))


# -------------------------------------------------------------------------------------
# 4. Extractive Summarization
# -------------------------------------------------------------------------------------


class ExtractiveSummarizer:
    def __init__(self, text):
        self.text = text
        self.sentences = sent_tokenize(self.text)

    # -------------------------------------------------------------------------
    # I. Frequency Based Summarization
    # -------------------------------------------------------------------------

    def frequency_summary(self, num_sentences=2):
        stop_words = set(stopwords.words("english"))
        word_frequencies = {}
        words = word_tokenize(self.text.lower())

        # build a word Frequency table
        for word in words:
            if word.isalnum() and word not in stop_words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1

        # Score sentences
        sentence_scores = {}

        for sentence in self.sentences:
            sentence_words = word.tokenize(sentence.lower())
            score = sum(word_frequencies.get(word, 0) for word in sentence_words)
            sentence_scores[sentence] = score

        # select top sentences
        top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[
            :
        ]


# -------------------------------------------------------------------------------------
# 5. Main Extraction Function
# -------------------------------------------------------------------------------------


def main():
    # Source text
    print_heading("ORIGINAL TEXT")
    print_wrapped(SOURCE_TEXT)

    # ---------------------------------------------------------------------------------
    # 1. Extractive Summarization
    # ---------------------------------------------------------------------------------

    # Frequency Based Extraction
    start = time.time()
    freq_summary = extractive.frequency_summary()
    elapsed = time.time() - start

    print("\n1. Frequency-based summary")
    print_wrapped(freq_summary)
    print(f"\nProcessing Time: {elapsed:.4f} seconds")

    # TF-IDF
    start = time.time()
    tfidf_summary = extractive.tfidf_summary()
    elapsed = time.time() - start

    print("\n2. tf-idf summary")
    print_wrapped(tfidf_summary)
    print(f"\nProcessing Time: {elapsed:.4f} seconds")

    # abstractive Summarization

    print_heading("extractive Summarization")

    extractve = ExtractiveSummarizer(SOURCE_TEXT)

    # ---------------------------------------------------------------------------------
    # 2. Abstracive Summarization
    # ---------------------------------------------------------------------------------
    print_heading("Abstracive Summarization")
    abstractive = AbstractSummarizer()

    start = time.time()
    abs_summary = abstractive.summarise(SOURCE_TEXT)
    elapsed = time.time() - start

    print("\nAbstractive Summary")
    print_wrapped(abs_summary)
    print(f"\nProcessing Time: {elapsed:.4f} seconds")

    # ---------------------------------------------------------------------------------
    # 3. Text Generation
    # ---------------------------------------------------------------------------------

    print_heading("Text Generation")

    generator = TextGenerator()

    prompt = "Neural language modles are important because"

    start = time.time()
    generated = generator.generate(SOURCE_TEXT)
    elapsed = time.time() - start

    print("\nGenerated Text")
    print_wrapped(generated)
    print(f"\nProcessing Time: {elapsed:.4f} seconds")

    # ---------------------------------------------------------------------------------
    # 4. Analysis
    # ---------------------------------------------------------------------------------

    print_heading("Analysis")

    print_wrapped(
        "Extractive summarisation selects important sentences directly "
        "from the original text. It is fast and preserves the original "
        "wording. Abstractive summarisation generates entirely new "
        "sentences using transformer neural networks. It produces more "
        "natural summaries but requires more computational power. Text "
        "generation demonstrates how neural language models predict "
        "likely next words based on context and training data."
    )

    # ---------------------------------------------------------------------------------
    # 5. Script completion
    # ---------------------------------------------------------------------------------

    print_heading("Script Completed")

    print(
        "Successfully demonstrated:\n"
        "  - Frequency-based extractive summarisation\n"
        "  - TF-IDF extractive summarisation\n"
        "  - Abstractive summarisation (T5-small)\n"
        "  - Neural text generation (DistilGPT-2)"
    )
