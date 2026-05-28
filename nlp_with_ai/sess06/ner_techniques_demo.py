# --------------------------------------------------------------------
# Python script to demonstrate various NER techniques
# --------------------------------------------------------------------
"""
script demonstratesx the following NER techniques:
1. Rule-based NER
2. CRF-based NER
3. spaCy Pretrained Transformer/Statistical NER
4. HuggingFace Transformer-based NER

Each technique is evaulated using
- Precision
- Recall
- F1 Score

----------------------------------------------------------------------------------
Required Modules
----------------------------------------------------------------------------------
- spaCy
- sklearn-crfsuite
- Transformers
- torch
- seqeval

download the spaCy medium model
python -m spacy download en_core_web_md

---------------------------------------------------
DATASET FORMAT
---------------------------------------------------

The dataset uses BIO tagging format.

Example:
[
    ("Chuck", "B-PER"),
    ("Missler", "I-PER"),
    ("visited", "O"),
    ("Kenya", "B-LOC")
]

---------------------------------------------------
NOTES
---------------------------------------------------

This script is educational and intentionally simplified.

- Rule-based NER is heuristic only.
- CRF uses handcrafted features.
- spaCy uses pretrained statistical/deep learning.
- Transformers use HuggingFace pipelines.

---------------------------------------------------

"""

import re
import subprocess
import sys
from collections import defaultdict

import spacy
import transformers
from seqeval.metrics import (
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn_crfsuite import CRF
from spacy.util import is_package
from transformers import pipeline

# --------------------------------------------------------------------
# 1. Sample Dataset
# --------------------------------------------------------------------

train_data = [
    [("Chuck", "B-PER"), ("Missler", "I-PER"), ("visited", "O"), ("Kenya", "B-LOC")],
    [
        ("Microsoft", "B-ORG"),
        ("is", "O"),
        ("based", "O"),
        ("in", "O"),
        ("Seattle", "B-LOC"),
    ],
    [("Elon", "B-PER"), ("Musk", "I-PER"), ("founded", "O"), ("SpaceX", "B-ORG")],
]

test_data = [
    [("Jeff", "B-PER"), ("Bezos", "I-PER"), ("owns", "O"), ("Amazon", "B-ORG")],
    [
        ("Google", "B-ORG"),
        ("opened", "O"),
        ("an", "O"),
        ("office", "O"),
        ("in", "O"),
        ("Nairobi", "B-LOC"),
    ],
]

# --------------------------------------------------------------------
# 2. Utility Functions
# --------------------------------------------------------------------


def extract_tokens(dataset):
    return [[token for token, label in sentence] for sentence in dataset]


def extract_labels(dataset):
    return [[label for token, label in sentence] for sentence in dataset]


# --------------------------------------------------------------------
# 3. Evaulation Function
# --------------------------------------------------------------------
def evaluate_model(true_labels, predicted_labels, model_name):
    print("\n" + "=" * 60)
    print(f"Evaluation: {model_name}")
    print("-" * 60)

    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)

    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1 Score: {f1:.3f}")

    print("\n Detailed report")
    print(classification_report(true_labels, predicted_labels))


# --------------------------------------------------------------------
# 4. i) Rule-Baed NER class
# --------------------------------------------------------------------


class RuleBasedNER:
    def __init__(self):
        self.person_titles = {"Mr", "Mrs", "Dr"}

        self.locations = {
            "Kenya",
            "Seattle",
            "Nairobi",
        }

        self.organisations = {"Microsoft", "Google", "Amazon", "SpaceX"}

    def predict(self, sentence_tokens):
        predictions = []

        for token in sentence_tokens:
            if token in self.locations:
                predictions.append("B-LOC")
            elif token in self.organisations:
                predictions.append("B-ORG")
            elif token[0].isupper():
                predictions.append("B-PER")
            else:
                predictions.append("0")


# --------------------------------------------------------------------
# 4. ii) CRF-Baed NER function
# --------------------------------------------------------------------
def word2features(sentence, index):
    word = sentence[index][0]

    features = {
        "bias": 1.0,
        "word.lower()": word.lower(),
        "word[-3]": word[-3:],
        "word[-2]": word[-2:],
        "word.upper()": word.upper(),
        "word.istitle()": word.istitle(),
        "word.isdigit()": word.isdigit(),
    }

    # Previous word
    if index > 0:
        previous_word = sentence[index - 1][0]
        features.update(
            {
                "-1:word.lower()": previous_word.lower(),
                "-1:word.istitle()": previous_word.istitle(),
            }
        )
    else:
        features["BOS"] = True

    # Next word
    if index < len(sentence) - 1:
        next_word = sentence[index + 1][0]
        features.update(
            {
                "-1:word.lower()": next_word.lower(),
                "-1:word.istitle()": next_word.istitle(),
            }
        )
    else:
        features["EOS"] = True
    return features


def sent2features(sentence):
    return [word2features(sentence, n) for n in range(len(sentence))]


def sent2labels(sentence):
    return [label for token, label in sentence]


# --------------------------------------------------------------------
# 4. iii) SpaCy NER class
# --------------------------------------------------------------------


class SpaCyNER:
    def __init__(self):
        self.model_name = "en_core_web_md"

        # Check whether the model exists
        if not is_package(self.model_name):
            print(
                f"{self.model_name} is not installed!"
                f"\nDownloading spaCy medium model..."
            )

            subprocess.check_call(
                [sys.executable, "-m", "spacy", "download", self.model_name]
            )

            # notify of successful download
            print(f"{self.model_name} downloaded successfully")

    def predict(self, tokens):
        text = " ".join(tokens)

        doc = self.nlp(text)

        predictions = ["O"] * len(doc)

        for ent in doc.ents:
            for idx, token in enumerate(ent):
                label = ent.label_

                mapped_label = {"PERSON": "PER", "ORG": "ORG", "GPE": "LOC"}.get(
                    label, None
                )

                if mapped_label:
                    token_index = token.i

                    if idx == 0:
                        predictions[token_index] = f"B-{mapped_label}"
                    else:
                        predictions[token_index] = f"I-{mapped_label}"
        return predictions


# --------------------------------------------------------------------
# 4. iv) Transformer-Based NER class
# ------------------------------------------------------------------


class TransformerNER:
    def __init__(self):
        self.ner_pipeline = pipeline(
            task="ner", aggregation_strategy="simple", model="dslim/bert-base-NER"
        )

    def predict(self, tokens):

        text = " ".join(tokens)

        entities = self.ner_pipeline(text)

        predictions = ["0"] * len(tokens)

        for entity in entities:
            entity_text = entity["word"]
            entity_label = entity["entity_group"]
            entity_tokens = entity_text.split()

            for n, token in enumerate(tokens):
                if token in entity_tokens:
                    if entity_label == "PER":
                        tag = "PER"
                    elif entity_label == "ORG":
                        tag = "ORG"
                    elif entity_label == "LOC":
                        tag = "LOC"
                    else:
                        continue

                    predictions


def main() -> None:
    """
    Train and evaluate all NER techniques/ approaches

    Workflow:
    1. Prepare CRF features
    2. Train CRF Model
    3. Generate predictions from
        i) Rule-based model
        ii) CRF model
        iii) spaCy-based model
        iv) Transformer-based model
    """
    X_train = [sent2features(s) for s in train_data]
    y_train = [sent2labels(s) for s in train_data]

    X_test = [sent2features() for s in test_data]
    y_test = [sent2labels() for s in test_data]

    token_test = extract_tokens(test_data)

    # -------------------------------------------------------------------------
    # I. Rule-based NER
    # -------------------------------------------------------------------------
    rule_ner = RuleBasedNER()

    rule_predictions = [rule_ner.predict(tokens) for tokens in token_test]

    evaluate_model(
        y_test,
        rule_predictions,
        "Rule-based NER",
    )

    # -------------------------------------------------------------------------
    # II. CRF-based NER
    # -------------------------------------------------------------------------
    crf = CRF(algorithms="lbfgs", c1=0.1, c2=0.2, max_iterations=100)

    crf.fit(X_train, y_train)

    crf_predictions = crf.predict(X_test)

    evaluate_model(y_test, crf_predictions, "CRF-BASED NER")

    # -------------------------------------------------------------------------
    # III. SpaCy NER
    # -------------------------------------------------------------------------
    spacy_ner = SpacyNER()

    spacy_predictions = [spacy_ner.predict(tokens) for tokens in token_test]

    evaluate_model(y_test, spacy_predictions, "spaCy NER")

    # -------------------------------------------------------------------------
    # IV. Transformer-based NER
    # -------------------------------------------------------------------------
    transformer_ner = TransformerNER()

    transformer.predictions = [transformer_ner.predict(tokens) for tokens in token_test]

    print("\n[INFO] Done. NER techniques Demo Complete")


# -------------------------------------------------------------------------
# 6. run the script
# -------------------------------------------------------------------------

if __name__ == "__main__":
    main()
