# Task Audit Report

Task: `T000062-lexical-decision-task`

Verdict: no critical or serious findings after repair.

## Findings Repaired

- `[Serious]` Added an explicit mapping from CSV frequency classes (`high_frequency`, `low_frequency`) to canonical condition labels (`high_frequency_word`, `low_frequency_word`). The initial implementation exported shortened labels, skipped the condition-specific onset triggers, and excluded those rows from frequency summaries.
- `[Low]` Added the recommended `.venv/` ignore rule.

## PsyFlow Ownership

| Concern | Owner | Audit result |
|---|---|---|
| Trial ID | PsyFlow `next_trial_id()` | Pass |
| Condition schedule | Documented CSV-backed custom preplanner passed through `BlockUnit` | Pass; exact item identity, donor disjointness, class balance, and no-repeat allocation require preplanning |
| Randomness | Stable task/class/block seeds in `src/utils.py` | Pass |
| Response capture | PsyFlow `StimUnit.capture_response()` | Pass |
| Trigger emission | StimUnit trigger runtime and block lifecycle hooks | Pass after condition-label repair |
| Timing/deadline | Config plus StimUnit | Pass |
| Phase data/context | `set_trial_context()` plus `to_dict()` | Pass |
| Stimulus construction | CSV asset plus config-defined StimBank text | Pass |
| Responder integration | Standard runtime responder seam | Pass |

## Checks Run

- `check_task_standard.py`: pass after repair.
- `taps_utils.validate`: 14 pass, 0 warning, 0 fail after repair.
- Full task-build gates: pass after repair.
- QA conditions: 2 high-frequency words, 2 low-frequency words, and 3 pseudowords.
- QA outcomes: 5 correct, 1 error, and 1 timeout.
- Full scheduler check: 30 practice and 120 scored items, exact class counts, exact per-block counts, and no scored item reuse.

## Residual Risk

- The scored release is intentionally shorter than the 50-block source experiment.
- The 2000 ms response deadline is adapted from the source analysis cutoff.
- English proficiency is not assessed inside the task and should be controlled by the study protocol.
