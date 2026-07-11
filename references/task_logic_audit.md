# Lexical Decision Task Logic Audit

## 1. Paradigm Intent

- Task: visual single-string lexical decision.
- Construct: lexical access, orthographic wordness, and visual word recognition.
- Factors: lexicality and word frequency.
- Measures: accuracy, correct RT distributions, word/nonword accuracy, and low-minus-high word-frequency effect.
- Primary citation: `W2020220682`; validation: `W2168979204`; historical provenance: `W1990948551`.

## 2. Block/Trial Workflow

### Block Structure

- One 30-trial practice block, excluded from analysis.
- Four scored blocks of 30 trials.
- Every scored block has 15 words and 15 pseudowords.
- HF/LF counts alternate 8/7 and 7/8, totaling 30 of each.
- `src/utils.py` validates and deterministically allocates the CSV pool without repeats.
- Custom preplanning is required because labels cannot encode exact class counts, item identity, donor disjointness, and no-repeat allocation together.

### Trial State Machine

1. `fixation`: central plus, 500 ms, no response.
2. `lexical_decision`: uppercase string, F/J response, 2000 ms maximum, response terminates display.
3. `error_feedback`: wrong keyed response only, red error message for 750 ms.
4. `iti`: blank display for 150 ms.

## 3. Condition Semantics

- `high_frequency_word`: English word, F correct, Zipf 5.24-6.29.
- `low_frequency_word`: English word, F correct, Zipf 2.22-3.85.
- `pseudoword`: pronounceable vowel-replacement nonword, J correct, Zipf 0.
- Practice items use separate `practice_word` and `practice_pseudoword` labels and are excluded from summaries.

## 4. Response and Scoring Rules

- F means word; J means nonword.
- `correct`: key matches lexicality.
- `error`: wrong valid key; followed by ERROR feedback.
- `timeout`: no key within 2000 ms; no invented feedback.
- Frequency effect: median correct low-frequency RT minus high-frequency RT.
- Downstream source-matched analysis may exclude RTs shorter than 350 ms.

## 5. Stimulus Layout Plan

- Fixation and letter string are centered on black.
- Letter strings are white uppercase Courier New at 1.3 degrees.
- The longest scored strings are seven letters, fitting comfortably within the configured 1280 x 800 display.
- Error feedback replaces the string at center and cannot overlap it.

## 6. Trigger Plan

| Event | Code |
|---|---:|
| experiment start/end | 1 / 99 |
| block start/end | 10 / 90 |
| fixation | 20 |
| HF/LF/pseudoword onset | 30 / 31 / 32 |
| practice word/nonword onset | 33 / 34 |
| word/nonword response/timeout | 40 / 41 / 42 |
| error feedback / ITI | 50 / 60 |

## 7. Architecture Decisions (Auditability)

- `main.py` is mode-aware orchestration with one small block helper.
- `src/utils.py` owns structured CSV parsing, validation, deterministic allocation, and summaries.
- `src/run_trial.py` only realizes a supplied plan and reduces its outcome.
- No adaptive controller or legacy compatibility layer is used.
- PsyFlow owns trial IDs, timing, response capture, triggers, context, and persistence.

## 8. Inference Log

- Four scored blocks replace the source experiment's 50 blocks to create a practical release while preserving 30-trial composition and no-repeat semantics.
- The paper's 2000 ms upper analysis cutoff is used as the task deadline because no display deadline was reported.
- F/J replace `/`/`z` for symmetric keyboards and browser portability.
- A 500 ms fixation and uppercase display are used because the source methods excerpt did not specify those details.
- Very-low-frequency words and random letter strings are omitted to keep a focused three-condition baseline.

## Contract Note

Participant-facing text is config-defined. All displayed items are auditable in `assets/stimuli.csv`; no presented word is a pseudoword donor.
