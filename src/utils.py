from __future__ import annotations

import csv
import hashlib
import random
from pathlib import Path
from statistics import median
from typing import Any


CONDITIONS = ("high_frequency_word", "low_frequency_word", "pseudoword")


class TrialPlan(str):
    """String-compatible condition token carrying one lexical item."""

    def __new__(
        cls,
        *,
        item_id: str,
        letter_string: str,
        lexicality: str,
        frequency_class: str,
        donor_word: str,
        is_practice: bool,
        trial_index_in_block: int,
    ) -> "TrialPlan":
        condition_by_class = {
            "high_frequency": "high_frequency_word",
            "low_frequency": "low_frequency_word",
            "pseudoword": "pseudoword",
        }
        condition = f"practice_{lexicality}" if is_practice else condition_by_class[frequency_class]
        obj = str.__new__(cls, condition)
        obj.condition = condition
        obj.item_id = item_id
        obj.letter_string = letter_string
        obj.lexicality = lexicality
        obj.frequency_class = frequency_class
        obj.donor_word = donor_word
        obj.is_practice = bool(is_practice)
        obj.trial_index_in_block = int(trial_index_in_block)
        return obj

    def to_dict(self) -> dict[str, Any]:
        return {
            "condition": self.condition,
            "condition_id": self.item_id,
            "item_id": self.item_id,
            "letter_string": self.letter_string,
            "lexicality": self.lexicality,
            "frequency_class": self.frequency_class,
            "donor_word": self.donor_word,
            "is_practice": self.is_practice,
            "trial_index_in_block": self.trial_index_in_block,
        }


def _stable_seed(base_seed: int, *parts: object) -> int:
    payload = "|".join([str(base_seed), *(str(part) for part in parts)])
    return int.from_bytes(hashlib.blake2b(payload.encode("utf-8"), digest_size=8).digest(), "big")


def load_stimulus_pool(path: str | Path) -> list[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"item_id", "letter_string", "lexicality", "frequency_class", "donor_word", "is_practice"}
    if not rows or not required.issubset(rows[0]):
        raise ValueError("Lexical stimulus CSV is empty or missing required columns")
    if len({row["item_id"] for row in rows}) != len(rows):
        raise ValueError("Lexical stimulus item_id values must be unique")
    if len({row["letter_string"] for row in rows}) != len(rows):
        raise ValueError("Lexical letter strings must be unique")
    lexical_words = {row["letter_string"] for row in rows if row["lexicality"] == "word"}
    donor_words = {row["donor_word"] for row in rows if row["donor_word"]}
    if lexical_words.intersection(donor_words):
        raise ValueError("Presented words and pseudoword donor words must be disjoint")
    for row in rows:
        row["is_practice"] = str(row["is_practice"]).strip().lower() == "true"
    return rows


def _plans_from_rows(rows: list[dict[str, Any]], is_practice: bool) -> list[TrialPlan]:
    return [
        TrialPlan(
            item_id=str(row["item_id"]),
            letter_string=str(row["letter_string"]),
            lexicality=str(row["lexicality"]),
            frequency_class=str(row["frequency_class"]),
            donor_word=str(row.get("donor_word", "")),
            is_practice=is_practice,
            trial_index_in_block=index,
        )
        for index, row in enumerate(rows)
    ]


def generate_trial_blocks(
    *,
    pool: list[dict[str, Any]],
    block_counts: list[dict[str, int]],
    practice_trials: int,
    seed: int,
) -> tuple[list[TrialPlan], list[list[TrialPlan]]]:
    """Build deterministic, exact, no-repeat practice and scored blocks."""
    practice_rows = [row for row in pool if bool(row["is_practice"])]
    practice_words = [row for row in practice_rows if row["lexicality"] == "word"]
    practice_nonwords = [row for row in practice_rows if row["lexicality"] == "nonword"]
    rng = random.Random(_stable_seed(seed, "lexical", "practice"))
    rng.shuffle(practice_words)
    rng.shuffle(practice_nonwords)
    word_count = int(practice_trials) // 2
    nonword_count = int(practice_trials) - word_count
    selected_practice = practice_words[:word_count] + practice_nonwords[:nonword_count]
    rng.shuffle(selected_practice)
    practice = _plans_from_rows(selected_practice, True)

    by_condition = {
        "high_frequency_word": [row for row in pool if not row["is_practice"] and row["frequency_class"] == "high_frequency"],
        "low_frequency_word": [row for row in pool if not row["is_practice"] and row["frequency_class"] == "low_frequency"],
        "pseudoword": [row for row in pool if not row["is_practice"] and row["frequency_class"] == "pseudoword"],
    }
    for condition, rows in by_condition.items():
        random.Random(_stable_seed(seed, "lexical", condition)).shuffle(rows)

    offsets = {condition: 0 for condition in CONDITIONS}
    blocks: list[list[TrialPlan]] = []
    for block_index, configured in enumerate(block_counts):
        selected: list[dict[str, Any]] = []
        for condition in CONDITIONS:
            count = int(configured.get(condition, 0))
            start = offsets[condition]
            end = start + count
            if count < 0 or end > len(by_condition[condition]):
                raise ValueError(f"Insufficient unique stimuli for {condition} in block {block_index + 1}")
            selected.extend(by_condition[condition][start:end])
            offsets[condition] = end
        random.Random(_stable_seed(seed, "lexical", "block", block_index)).shuffle(selected)
        blocks.append(_plans_from_rows(selected, False))
    return practice, blocks


def summarize_trials(rows: list[dict[str, Any]], block_id: str | None = None) -> dict[str, Any]:
    scored = [
        row for row in rows
        if not bool(row.get("is_practice"))
        and row.get("condition") in CONDITIONS
        and (block_id is None or row.get("block_id") == block_id)
    ]

    def median_rt(condition: str) -> float | None:
        values = [
            float(row["response_rt"])
            for row in scored
            if row.get("condition") == condition
            and bool(row.get("correct"))
            and isinstance(row.get("response_rt"), (int, float))
        ]
        return median(values) if values else None

    medians = {condition: median_rt(condition) for condition in CONDITIONS}
    high = medians["high_frequency_word"]
    low = medians["low_frequency_word"]
    return {
        "trials": len(scored),
        "accuracy": sum(bool(row.get("correct")) for row in scored) / len(scored) if scored else 0.0,
        "word_accuracy": sum(bool(row.get("correct")) for row in scored if row.get("lexicality") == "word") / max(1, sum(row.get("lexicality") == "word" for row in scored)),
        "nonword_accuracy": sum(bool(row.get("correct")) for row in scored if row.get("lexicality") == "nonword") / max(1, sum(row.get("lexicality") == "nonword" for row in scored)),
        "median_rt_by_condition": medians,
        "word_frequency_effect": (low - high) if low is not None and high is not None else None,
        "timeouts": sum(row.get("outcome") == "timeout" for row in scored),
    }
