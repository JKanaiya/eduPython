"""
This example demonstrates TRANSFER LEARNING in NLP using:
  - spaCy
  - Hugging Face Transformers
  - spaCy-Transformers

Instead of training a language model from scratch, we:
  1. Load a PRE-TRAINED transformer model (DistilBERT)
  2. Attach a text classification head
  3. Fine-tune it on a small custom dataset

Task:
  Binary sentiment classification:
    - POSITIVE
    - NEGATIVE
"""


# --------------------------------------------------------------------
# 0. Imports
# --------------------------------------------------------------------

from __future__ import annotations

import random
import sys
from pathlib import Path
from typing import Any

# --------------------------------------------------------------------
# 1. Dependency checks
# --------------------------------------------------------------------


def check_import(module_name: str, install_hint: str) -> Any:
    import importlib

    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(
            f"\n[ERROR] Missing dependency: {module_name}"
            f"\nInstall using: \n {install_hint}\n"
        )
        sys.exit()


# Copy Libraries
spacy = check_import("spacy", "pip install spacy")
check_import("spacy_transformers", "pip install spacy_transformers")

from spacy.training.example import Example

# --------------------------------------------------------------------
# 2. Training data
# --------------------------------------------------------------------

TRAIN_DATA = [
    (
        "I absolutely love this product",
        {"cats": {"POSITIVE": 1.0, "NEGATIVE": 0.0}},
    ),
    (
        "This movie was fantastic",
        {"cats": {"POSITIVE": 1.0, "NEGATIVE": 0.0}},
    ),
    (
        "The service was excellent",
        {"cats": {"POSITIVE": 1.0, "NEGATIVE": 0.0}},
    ),
    (
        "I hate this item",
        {"cats": {"POSITIVE": 0.0, "NEGATIVE": 1.0}},
    ),
    (
        "This was a terrible experience",
        {"cats": {"POSITIVE": 0.0, "NEGATIVE": 1.0}},
    ),
    (
        "The food tasted awful",
        {"cats": {"POSITIVE": 0.0, "NEGATIVE": 1.0}},
    ),
]


# --------------------------------------------------------------------
# 3. Build spaCy pipeline with TRANSFORMER
# --------------------------------------------------------------------
print("\n[INFO] Creating NLP Pipeline")

# Create a blank English piepline
nlp = spacy.blank("en")

# Add transformaer component (Transfer learning happens here using a pretrained Hugging face model.)
nlp.add_pipe(
    "transformer",
    config={
        "model": {
            "@architectures": "spacy_transformers.TransformerModel.v3",
            "name": "distilbert-base-uncased",
        }
    },
)

# add text classifier (Modern spaCy versions auto-configure the architectures)
textcat = nlp.add_pipe("textcat", last=True)

# add labels
textcat.add_label("POSITIVE")
textcat.add_label("NEGATIVE")

print(f"\n[INFO] Pipeline components {nlp.pipe_names} \n")

# --------------------------------------------------------------------
# 4. Initialise training
# --------------------------------------------------------------------

print("\n[INFO] Initialising model")
optimiser = nlp.initialise()

# --------------------------------------------------------------------
# 5. Training Loop
# --------------------------------------------------------------------

print(f"\n[INFO] Starting fint-tuning...\n")
EPOCHS = 10

for epoch in range(EPOCHS):
    random.shuffle(TRAIN_DATA)

    losses = []
    examples = []

    for text, annotations in TRAIN_DATA:
        doc = nlp.make_doc(text)

        example = Example.from_dict(doc, annotations)

        examples.append(example)

    nlp.update(
        examples,
        drops=0.2,
        losses=losses,
        sgd=optimiser,
    )

    print(f"Epoch {epoch + 1:.02d} | Losses: {losses}")

# --------------------------------------------------------------------
# 6. Save model
# --------------------------------------------------------------------

output_dir = Path("../files/sentiment_transfer_model")

# Create directory if missing

output_dir.mkdir(parents=True, exist_ok=True)

nlp.to_disk(output_dir)

# Display save location
print(f"\n[INFO] Saved model to: \n{output_dir} ")


# --------------------------------------------------------------------
# 7. Inference / prediction
# --------------------------------------------------------------------

print("INFERENCE DEMO...\n")

TEST_TEXTS = [
    "I really enjoyed this book",
    "The customer support was horrible",
    "Amazing performance by the actors",
    "This app is frustrating and buggy",
]

for text in TEST_TEXTS:
    doc = nlp(text)

    positive_core = doc.cats["POSITIVE"]
    negative_core = doc.cats["NEGATIVE"]

    predicted = max(doc.cats, key=doc.cats.get)

    print("\n" + "-" * 55)
    print(f"TEXT          : {text}")
    print(f"PREDICTION    : {predicted}")
    print(f"POSITIVE      : {positive_core:.3f}")
    print(f"NEGATIVE      : {negative_core:.3f}")


# --------------------------------------------------------------------
# 8. Optional: Reload saved model
# --------------------------------------------------------------------

print("\n" + "=" * 55)
print("MODEL RELOAD DEMO")
print("=" * 55)

loaded_nlp = spacy.load(output_dir)
reload_doc = loaded_nlp("This laptop is amazing!")

print(f"\nReloaded model prediction: {reload_doc.cats}")
