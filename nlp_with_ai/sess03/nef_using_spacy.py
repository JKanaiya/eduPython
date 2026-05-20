"""
====================================================================================================================
Python script  to demonstrate NER (Named Entity Recognition) using the Spacy Library
====================================================================================================================
this script identifies and classifies 'named entities' using spacy's medium english model into predefined categories such as:
    - PERSON    : People's names
    - ORG       : Companies, agencies, institutions
    - LOC       : Non-GPE locations (mountains etc)
    - TIME      : Times smaller than a day
    - MONEY     : Monetary Values
    - FACILITY  : Building's, airports, highways, etc
    - EVENT     : Named Events (elections, battles, etc)
"""

# --------------------------------------------------------------------
# 0. Import
# --------------------------------------------------------------------

import collections
import sys

import rich

# --------------------------------------------------------------------
# 1. Dependency Checks
# --------------------------------------------------------------------


def _check_import(module_name: str, install_hint: str) -> object:
    """
    Attempt to import *module_name* and exit with a helpful message on failure.

    Args:
     module_name  : The Python module to import (e.g. "spacy").
     install_hint : The pip command users should run if the module is absent.

    Returns:
     The imported module object.
    """
    import importlib

    try:
        return importlib.import_module(module_name)
    except ImportError:
        print(f"\n[ERROR] {module_name} is not installed.\n Run: {install_hint}\n")
        sys.exit(
            1
        )  # Stop further script execution to avoid missing module/library errors


spacy = _check_import(
    "spacy", "pip install spacy && python -m spacy download en_core_web_md"
)

# rich module is optional - we degrade gracefull if absent

try:
    from rich import box as rich_box
    from rich.console import Console
    from rich.table import Table

    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

# --------------------------------------------------------------------
# 2. Sample Corpurs (text)
# --------------------------------------------------------------------

SAMPLE_TEXT = """
Ada Lovelace visited London in September 1843 to present her notes on the
analytical engine at a meeting organised by the Royal Society. During the
event, she spoke with engineers from IBM, and researchers from Microsoft
about the future of computing and artificial intelligence. After the
conference, she travelled by train to Manchester and stayed at The Midland
Hotel for three nights before returning home.

Last Friday, David Beckham attended a charity fundraiser at Wembley Stadium
alongside representatives from UNICEF. The organisers announced that more
than £2 million had been raised to support schools in Kenya and India.
Following the ceremony, Beckham shared photographs on Instagram and thanked
supporters from across the United Kingdom for their generosity.
"""

# --------------------------------------------------------------------
# 3. Load spaCy model
# --------------------------------------------------------------------


def load_nlp_model(model_name: str = "en_core_web_md"):
    """
    Load a spaCy language model by name.

    spaCy models bundle a tokeniser, POS tagger, dependency parser, and NER
    pipeline component.  The medium English model (en_core_web_md) is moderate and
    suitable for demonstrations; larger models (en_core_web_lg / trf) are more
    accurate for production use.

    Args:
        model_name : The spaCy model identifier string.

    Returns:
     A spaCy `Language` object (the NLP pipeline).
    """
    try:
        nlp = spacy.load(model_name)
        print(f"[INFO]: Loaded spaCy model: {model_name}")
        return nlp
    except OSError:
        print(
            f"[ERROR]: Could not find spaCy model: {model_name}."
            f"\n'[INFO]: Downloading model now, please wait..."
        )

        # Download the model programatiaclly
        from spacy.cli import download

        try:
            download(model_name)

            # Try loading again after the download
            nlp = spacy.load(model_name)
            print(f"[INFO]: Succeddfully downloaded: {model_name}")
            return nlp
        except Exception as e:
            print(f"[ERROR]: Failed to download: \n{e}.")
            sys.exit(
                1
            )  # Stop further script execution due to failed download of the English medium model


# --------------------------------------------------------------------
# 4. Function to run NER
# --------------------------------------------------------------------
def run_ner(nlp, text: str):
    """
    Run the spaCy NLP pipeline on *text* and return the processed Doc object.

    The Doc object contains:
    - doc.ents  : A tuple of Span objects, one per detected entity.
     - span.text        : The surface string of the entity.
     - span.label_      : The entity type label (e.g. "PERSON").
     - span.start_char  : Character offset (start) in the original text.
     - span.end_char    : Character offset (end) in the original text.
     - doc.sents : Individual sentences (requires the parser component).

    Args:
     nlp  : A loaded spaCy Language pipeline.
     text : The raw input string to analyse.

    Returns:
     A spaCy Doc object.
    """
    doc = nlp(text)
    return doc


# --------------------------------------------------------------------
# 5. Display Helpers
# --------------------------------------------------------------------


def print_entities_flat(doc):
    """
    Print every detected entity on its own line in a flat, sequential list.

    Format:
        <ENTITY TEXT>  →  <LABEL>  (<start>–<end>)

    This mirrors the order in which entities appear in the source text,
    making it easy to verify extraction against the original document.

    Args:
        doc : A processed spaCy Doc object.
    """

    print("\n" + "=" * 70)
    print("ENTITIES (sequential order)")
    print("=" * 70)

    if not doc.ents:
        print("No entities found/detected")
        return  # Stop futher function detection

    for ent in doc.ents:
        description = spacy.explain(ent.label_) or "-"
        print(
            f"{ent.text:<30} -> {ent.label_:<12}"
            f"[{description}]"
            f"chars {ent.start_char} - {ent.end_char}"
        )


def print_entities_grouped(doc) -> None:
    """
    Group entities by their label and print each group alphabetically.

    Useful for quickly seeing *all* organisations or *all* dates together
    without hunting through a flat list.

    Args:
        doc : A processed spaCy Doc object.
    """

    print("\n" + "=" * 70)
    print("ENTITIES (grouped by type)")
    print("=" * 70)

    grouped: dict[str, list[str]] = collections.defaultdict(list)
    for ent in doc.ents:
        grouped[ent.label_].append(ent.text)

    for label in sorted(grouped.keys()):
        description = spacy.explain(label) or "-"
        entities = ", ".join(sorted(set(grouped[label])))  # remove dupes
        print(f"\n {label} ({description})   {entities}")


def print_entities_rich_table(doc) -> None:
    """
    Render a nicely formatted table using the `rich` library (if installed).

    Columns: #  |  Entity Text  |  Type  |  Description  |  Char Span

    Falls back gracefully to a plain-text message if `rich` is not available.

    Args:
        doc : A processed spaCy Doc object.
    """

    print("ENTITIES (rich table)")
    print("\n" + "=" * 70)
    print("=" * 70)

    if not RICH_AVAILABLE:
        print(
            " [rich] not installed - skipping table viewInstall with pip install rich."
        )
        return
    console = Console()
    table = Table(
        title="Named Entities Detected",
        box=rich.box.ROUNDED,
        header_style="bold cyan",
        show_lines=True,
    )

    # Actual Table
    table.add_column("#", style="dim", no_wrap=True, width=4, justify="right")
    table.add_column("Entity", style="bold white", width=28)
    table.add_column("Type", style="bold yellow", width=12)
    table.add_column("Description", style="green", width=30)
    table.add_column("Char Span", style="dim", width=12)

    # colour map: entity label -> row style
    label_colours = {
        "PERSON": "bright_magenta",
        "ORG": "bright_blue",
        "GPE": "bright_cyan",
        "LOC": "cyan",
        "DATE": "bright_green",
        "TIME": "green",
        "MONEY": "bright_yellow",
        "FAC": "orange3",
        "EVENT": "red",
    }

    for n, ent in enumerate(doc.ents, start=1):
        description = spacy.explain(ent.label_) or "_"
        colour = label_colours.get([ent.label_, "white"])
        table.add_row(
            str(n),
            f"[{colour}]{ent.text}[/{colour}]",
            f"[{colour}]{ent.label_}[/{colour}]",
            description,
            f"{ent.start_char} - {ent.end_char}",
        )

    console.print(table)


# generate html doc
def save_displacy_html(doc, output_path: str = "nwr_displacy.html") -> None:
    from spacy import displacy

    html = displacy.render(doc, style="ent", page=True, minify=False)

    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(html)

    print(
        f"\n[INFO] displaCy visualisation saved -> {output_path}"
        f"\n Open it in any browser to see colour-coded entity spans."
    )


# --------------------------------------------------------------------
# 6. Summary Statistics
# --------------------------------------------------------------------


def print_summary(doc) -> None:
    """
    Print high-level statistics about the NER results

    Includes:
        - Total word / token count
        - Total sentence count
        - Total entity count
        - Per-label entity counts (sorted by frequency, descending)
    Args:
        doc: A processed spaCy doc object
    """

    print("\n" + "=" * 70)
    print("Summary Statistics")
    print("=" * 70)

    tokens = [t for t in doc if not t.is_space]
    sentences = list(doc.sents)
    entities = list(doc.ents)

    print(
        f"Tokens: {len(tokens)}"
        f"\n Sentences: {len(sentences)}"
        f"\n Entities: {len(entities)}"
    )

    if entities:
        counter = collections.Counter(ent.label for ent in entites)
        print("\n Breakdown by label:")
        for label, count in counter.most_common():
            description = spacy.explain(ent.label_) or "-"
            bar = "*" * count
            print(f" {label:<12} {count:>3} {bar} ({description})")
