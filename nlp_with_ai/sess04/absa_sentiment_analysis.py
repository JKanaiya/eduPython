# --------------------------------------------------------------------
# Python script to demonstrate ABSA (aspect based sentiment analysis)
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# 0. Import required modules
# --------------------------------------------------------------------

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from tkinter import NE
from typing import Optional

from nltk.translate.bleu_score import sentence_bleu

# --------------------------------------------------------------------
# 1. Check Dependencies
# --------------------------------------------------------------------


def _require(package: str, install_cmd: str) -> None:
    import importlib.util

    if importlib.util.find_spec(package) is None:
        print(
            f"\n[ERROR] Required pacakge {package} not found."
            f"\n        Install it with: {install_cmd}\n"
        )
        sys.exit(1)


_require("vaderSentiment", "pip install vaderSentiment")

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# --------------------------------------------------------------------
# 2. Aspect taxonomy
# --------------------------------------------------------------------
# each key is the canonical aspect name shown in the output
# each value is a list of surface form keywords (singular, plural, synonyms)
# matching is a case-sensitive and whole-word only regext

ASPECT_TAXONOMY: dict[str, list[str]] = {
    "battery life": ["battery life", "battery", "charge", "charging"],
    "screen": ["screen", "display", "monitor", "resolution", "brightness"],
    "camera": ["camera", "cameras", "photo", "photos", "lens", "zoom"],
    "performance": [
        "performance",
        "speed",
        "processor",
        "lag",
        "fast",
        "slow",
        "snappy",
    ],
    "price": ["price", "cost", "expensive", "cheap", "affordable", "value"],
    "service": ["service", "services", "support", "staff", "customer service"],
    "build quality": [
        "build quality",
        "build",
        "design",
        "materials",
        "durability",
        "sturdy",
    ],
    "storage": ["storage", "memory", "space", "capacity"],
    "audio": [
        "audio",
        "sound",
        "speaker",
        "speakers",
        "headphone",
        "headphones",
        "bass",
    ],
}

# VADER compound-score thresholds (industry standard values)
POSITIVE_THRESHOLD = 0.05
NEGATIVE_THRESHOLD = -0.05

# ---------------------------------------------------------------------------
# 3. Data classes
# ---------------------------------------------------------------------------


@dataclass
class AspectResult:
    """Sentiment prediction for one aspect within a sentence."""

    aspect: str
    sentiment: str  # "POSITIVE" | "NEUTRAL" | "NEGATIVE"
    score: float  # VADER compound score in [-1, +1]
    confidence: str  # "HIGH" | "MEDIUM" | "LOW"
    source: str  # the clause that the aspect was found in


@dataclass
class SentenceResult:
    """Full ABSA output for one input sentence."""

    text: str
    aspect: list[AspectResult] = field(default_factory=list)
    overall_label: Optional[str] = None  # overall VADER sentiment
    overall_score: Optional[float] = None


# -------------------------------------------------------------------------
# 4. Core ABSA Engine
# -------------------------------------------------------------------------


class ABSAAnalyser:
    def __init__(
        self,
        taxonomy: dict[str, list[str]] | None = None,
        positive_threshold: float = POSITIVE_THRESHOLD,
        negative_threshold=NEGATIVE_THRESHOLD,
    ) -> None:

        self._vader = SentimentIntensityAnalyzer()
        self._taxonomy = taxonomy or ASPECT_TAXONOMY
        self._pos_thr = positive_threshold
        self._neg_thr = negative_threshold

        # pre compilr patterns: longest keywords first to avoid partial matches. eg battery life must be checked before battery
        self._patterns: dict[str, list[re.Pattern[str]]] = {}
        for aspect, keywords in self._taxonomy.items():
            sorted_kw = sorted(keywords, key=len, reverse=True)
            self._patterns[aspect] = [
                re.compile(r"\b[re.escape(kw)\b]", re.IGNORECASE) for kw in sorted_kw
            ]

    # -------------------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------------------
    def analyze(self, text: str) -> SentenceResult:
        result = SentenceResult(text=text)

        # Overall sentence-level sentiment
        overall_scores = self._vader.polarity_scores(text)
        result.overall_score = overall_scores["compound"]
        result.overall_label = self._label(result.overall_score)

        # Split into classes so sentiments don't bleed across aspects
        clauses = self._split_clauses(text)

        # match aspects to clauses and score match
        seen_aspects: set[str] = set()
        for clause in clauses:
            for aspect, patterns in self._patterns.items():
                if aspect in seen_aspects:
                    continue
                for pattern in patterns:
                    if pattern.search(clause):
                        scores = self._vader.polarity_scores(clause)
                        compound = scores["compound"]
                        sentiment = self._label(compound)
                        confidence = self._confidence(compound)
                        result.aspect.append(
                            AspectResult(
                                aspect=aspect,
                                sentiment=sentiment,
                                score=compound,
                                confidence=confidence,
                                source=clause.strip(),
                            )
                        )
                        seen_aspects.add(aspect)
                        break  # stop checking other keywords for thos aspect
        return result

    def analyze_batch(self, texts: list[str]) -> list[SentenceResult]:
        return [self.analyze(t) for t in texts]

    # ---------------------------------------------------------------------
    # Private Helpers
    # ---------------------------------------------------------------------

    @staticmethod
    def _split_clauses(text: str) -> list[str]:
        # Primary split on contrastive/additive connectors
        parts = re.split(
            r"\s*(?:but|however|although|though|yet|while|;|,)\s*",
            text,
            flags=re.IGNORECASE,
        )
        # Secondary split: "and the/a/an …" — new noun phrase starting
        clauses: list[str] = []
        for part in parts:
            sub = re.split(
                r"\s+and\s+(?=(?:the|a|an|this|its|my|their)\s)",
                part,
                flags=re.IGNORECASE,
            )
            clauses.extend(sub)

        return [c.strip() for c in clauses if c.strip()]

    def _label(self, compound: float) -> str:
        if compound >= self._pos_thr:
            return "POSITIVE"
        if compound <= self._neg_thr:
            return "NEGATIVE"
        return "NEUTRAL"

    @staticmethod
    def _confidence(compound: float) -> str:

        abs_score = abs(compound)
        if abs_score >= 0.5:
            return "HIGH"
        if abs_score <= 0.2:
            return "MEDIUM"
        return "LO"


# -------------------------------------------------------------------------
# 5. Display Helpers
# -------------------------------------------------------------------------

_SENTIMENT_SYMBOLS = {"POSITIVE": "✓", "NEGATIVE": "✗", "NEUTRAL": "~"}
_SENTIMENT_COLORS = {
    "POSITIVE": "\033[32m",  # green
    "NEGATIVE": "\033[31m",  # red
    "NEUTRAL": "\033[33m",  # yellow
}
_RESET = "\033[0m"
_BOLD = "\033[1m"


def _colorize(text: str, color_code: str) -> str:

    return f"{color_code}{text}{_RESET}"


def print_result(result: SentenceResult, show_clause: bool = False) -> None:
    width = 72
    print("\n" + "-" * width)
    print(f"{_BOLD}TEXT:{_RESET}{result.text}")

    if result.overall_label:
        sym = _SENTIMENT_SYMBOLS[result.overall_label]
        color = _SENTIMENT_COLORS[result.overall_label]
        label = _colorize(f"{sym} {result.overall_label}", color)
        print(f"Overall sentiment: {label}(score: {result.overall_score:+.3f})")

    if not result.aspect:
        print("\n No known product aspects detected")
        return

    print(f"\n  {'Aspect':<16}  {'Sentiment':<10}  {'Conf.':<8}  {'Score':>7}")
    print(f"  {'─' * 15}  {'─' * 9}  {'─' * 7}  {'─' * 7}")
    for r in result.aspect:
        sym = _SENTIMENT_SYMBOLS[r.sentiment]
        color = _SENTIMENT_COLORS[r.sentiment]
        label = _colorize(f"{sym} {r.sentiment:<9}", color)
        print(f"  {r.aspect:<16}  {label}  {r.confidence:<8}  {r.score:+.3f}")
        if show_clause:
            wrapped = textwrap.fill(
                f'"{r.source}"',
                width=width - 22,
                subsequent_indent=" " * 22,
            )
            print(f"  {'':16}  ↳ clause: {wrapped}")


def print_summary_table(results: list[SentenceResult]) -> None:

    width = 72
    print("\n" + "-" * width)
    print(f"{_BOLD} BATCH SUMMARY: {_RESET}")
    print("-" * width)
    for n, result in enumerate(results, start=1):
        short = (result.text[:55] + "-") if len(result.text) > 55 else result.text
        print(f"\n [{n}] {short}")
        if result.aspect:
            parts = []
            for r in result.aspect:
                sym = _SENTIMENT_SYMBOLS[r.sentiment]
                color = _SENTIMENT_COLORS[r.sentiment]
                parts.append(_colorize(f"{sym} {r.aspect}", color))
            print("   " + " |  ".join(parts))
        else:
            print("  No aspects found")
    print("-" * width)


# -------------------------------------------------------------------------
# 6. Demo Sentences
# -------------------------------------------------------------------------

DEMO_SENTENCES = [
    # Clear multi-aspect contrasts
    "The battery life is excellent but the screen is disappointing.",
    "Camera quality is stunning and the performance is incredibly fast.",
    "Battery life is awful and the price is way too high.",
    # Mixed service + storage
    "Customer service was amazing, though the storage is far too limited.",
    # Audio vs screen
    "The display is absolutely gorgeous but the audio sounds terrible.",
    # Mild / neutral tones
    "Build quality feels decent and the camera is okay for the price.",
    "The service was acceptable, nothing special.",
    # Edge cases
    "The weather is nice today.",  # no product aspects → graceful output
    "Everything about this phone is perfect.",  # vague, no specific aspect keyword
]

# -------------------------------------------------------------------------
# 7. Main Execution Function
# -------------------------------------------------------------------------


def main() -> None:

    width = 72
    print("\n" + "-" * width)
    print(f"{_BOLD} ASPECT-BASED SENTIMENT ANALYSIS(ABSA) DEMONSTRATION: {_RESET}")
    print(f"Compatible with python 3.12 +  | VADER")
    print("-" * width)

    analyzer = ABSAAnalyser()

    # ---------------------------------------------------------------------
    # Section i. Detailed per-sentence analysis
    # ---------------------------------------------------------------------

    print(f"\n{_BOLD} -- DETAILED ANALYSIS (with source clauses) -- {_RESET}")
    for sentence in DEMO_SENTENCES:
        result = analyzer.analyze(sentence)
        print_result(result, show_clause=True)

    # ---------------------------------------------------------------------
    # Section ii. Batch Summary
    # ---------------------------------------------------------------------

    results = analyzer.analyze_batch(DEMO_SENTENCES)
    print_summary_table(results)

    # ---------------------------------------------------------------------
    # Section iii. Optional Interactice section
    # ---------------------------------------------------------------------

    print(f"\n{_BOLD} -- INTERACTIVE MODE -- {_RESET}")
    print("Type a sentence to analyze it, or press <Enter> to exti")

    while True:
        try:
            user_input = input("Enter text to ba analyzed:").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            print("Exiting interactive mode")
            break
        result = analyzer.analyze(user_input)
        print_result(result, show_clause=True)
    print(f"\n{_BOLD} -- [DONE] : {_RESET} ABSA demo complete.\n")


# -------------------------------------------------------------------------
# 8. run the script
# -------------------------------------------------------------------------

if __name__ == "__main__":
    main()
