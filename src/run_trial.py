from __future__ import annotations

from functools import partial
from typing import Any

from psyflow import StimUnit, next_trial_id, set_trial_context

from .utils import TrialPlan


def _context(
    *,
    trial_id: int,
    block_id: str,
    condition_id: str,
    phase: str,
    deadline_s: float,
    valid_keys: list[str],
    task_factors: dict[str, Any],
    stim_id: str,
) -> dict[str, Any]:
    return {
        "trial_id": trial_id,
        "phase": phase,
        "deadline_s": deadline_s,
        "valid_keys": valid_keys,
        "block_id": block_id,
        "condition_id": condition_id,
        "task_factors": task_factors,
        "stim_id": stim_id,
    }


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime,
    block_id=None,
    block_idx=None,
):
    """Run one preplanned visual lexical decision trial."""
    if not isinstance(condition, TrialPlan):
        raise TypeError("Lexical decision trials require a preplanned TrialPlan")
    plan = condition.to_dict()
    trial_id = next_trial_id()
    block_id_value = str(block_id or "block_0")
    block_idx_value = int(block_idx or 0)
    word_key = str(settings.word_key)
    nonword_key = str(settings.nonword_key)
    correct_key = word_key if plan["lexicality"] == "word" else nonword_key
    key_list = [word_key, nonword_key]
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)
    common_factors = {
        "condition": plan["condition"],
        "item_id": plan["item_id"],
        "letter_string": plan["letter_string"],
        "lexicality": plan["lexicality"],
        "frequency_class": plan["frequency_class"],
        "is_practice": plan["is_practice"],
        "correct_key": correct_key,
    }
    trial_data: dict[str, Any] = {
        "trial_id": int(trial_id),
        "block_id": block_id_value,
        "block_idx": block_idx_value,
        "trial_index_in_block": int(plan["trial_index_in_block"]),
        "condition": str(plan["condition"]),
        "condition_id": str(plan["condition_id"]),
        **common_factors,
    }

    fixation_duration = float(settings.fixation_duration)
    fixation = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        fixation,
        **_context(
            trial_id=trial_id,
            block_id=block_id_value,
            condition_id=plan["condition_id"],
            phase="fixation",
            deadline_s=fixation_duration,
            valid_keys=[],
            task_factors={**common_factors, "stage": "fixation"},
            stim_id="fixation",
        ),
    )
    fixation.show(duration=fixation_duration, onset_trigger=settings.triggers.get("fixation")).to_dict(trial_data)

    response_window = float(settings.response_window)
    display_text = str(plan["letter_string"]).upper() if str(settings.display_case).lower() == "upper" else str(plan["letter_string"])
    stimulus = make_unit(unit_label="lexical_decision").add_stim(
        stim_bank.get_and_format("letter_string", letter_string=display_text)
    )
    set_trial_context(
        stimulus,
        **_context(
            trial_id=trial_id,
            block_id=block_id_value,
            condition_id=plan["condition_id"],
            phase="lexical_decision",
            deadline_s=response_window,
            valid_keys=key_list,
            task_factors={**common_factors, "stage": "lexical_decision"},
            stim_id=plan["item_id"],
        ),
    )
    stimulus.capture_response(
        keys=key_list,
        correct_keys=[correct_key],
        duration=response_window,
        onset_trigger=settings.triggers.get(f"stimulus_{plan['condition']}"),
        response_trigger={word_key: settings.triggers.get("word_response"), nonword_key: settings.triggers.get("nonword_response")},
        timeout_trigger=settings.triggers.get("response_timeout"),
        terminate_on_response=True,
    ).to_dict(trial_data)
    response = stimulus.get_state("response", None)
    response_rt = stimulus.get_state("rt", None)
    correct = bool(response == correct_key)
    outcome = "timeout" if response is None else "correct" if correct else "error"
    trial_data.update(
        response_key=str(response) if response is not None else "",
        response_rt=float(response_rt) if isinstance(response_rt, (int, float)) else None,
        correct=correct,
        response_correct=correct,
        outcome=outcome,
    )

    if response is not None and not correct:
        feedback_duration = float(settings.error_feedback_duration)
        feedback = make_unit(unit_label="error_feedback").add_stim(stim_bank.get("feedback_error"))
        set_trial_context(
            feedback,
            **_context(
                trial_id=trial_id,
                block_id=block_id_value,
                condition_id=plan["condition_id"],
                phase="error_feedback",
                deadline_s=feedback_duration,
                valid_keys=[],
                task_factors={**common_factors, "stage": "error_feedback", "correct": False},
                stim_id="feedback_error",
            ),
        )
        feedback.show(duration=feedback_duration, onset_trigger=settings.triggers.get("error_feedback")).to_dict(trial_data)

    iti_duration = float(settings.iti_duration)
    iti = make_unit(unit_label="iti").add_stim(stim_bank.get("blank"))
    set_trial_context(
        iti,
        **_context(
            trial_id=trial_id,
            block_id=block_id_value,
            condition_id=plan["condition_id"],
            phase="iti",
            deadline_s=iti_duration,
            valid_keys=[],
            task_factors={**common_factors, "stage": "iti", "outcome": outcome},
            stim_id="blank",
        ),
    )
    iti.show(duration=iti_duration, onset_trigger=settings.triggers.get("iti")).to_dict(trial_data)
    return trial_data
