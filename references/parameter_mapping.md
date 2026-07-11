# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---:|---|---|---|---|
| `condition_structure` | `task.conditions` | HF word, LF word, pseudoword | `W2020220682` | Experiments 1-6 varied word frequency and pseudoword/random-string type. | direct | Experiment 3-style subset. |
| `block_size` | `task.trial_per_block` | 30 | `W2020220682` | Trials were grouped in blocks of 30. | direct | Preserved. |
| `lexicality_balance` | `task.block_counts` | 15 words / 15 pseudowords | `W2020220682` | Experiment 3 used 8 HF, 7 LF, and 15 pseudowords per block. | direct | Alternate blocks reverse 8/7 to balance frequency overall. |
| `practice_trials` | `task.practice_trials` | 30 | `W2020220682` | The first block was practice and excluded from analysis. | direct | Preserved. |
| `error_feedback_duration` | `timing.error_feedback_duration` | 0.75 s | `W2020220682` | ERROR followed incorrect responses for 750 ms. | direct | Only keyed errors receive feedback. |
| `iti_duration` | `timing.iti_duration` | 0.15 s | `W2020220682` | Intertrial interval was 150 ms. | direct | Preserved. |
| `response_window` | `timing.response_window` | 2.0 s | `W2020220682` | Responses above 2000 ms were excluded. | adapted | Upper analysis cutoff becomes deadline. |
| `fixation_duration` | `timing.fixation_duration` | 0.5 s | local adaptation | Not specified in primary methods. | inferred | Stable pre-stimulus interval. |
| `response_keys` | `task.word_key/nonword_key` | F / J | local adaptation | Source used `/` for word and `z` for nonword. | adapted | Symmetric keys. |
| `scored_blocks` | `task.total_blocks` | 4 | local adaptation | Source used 50 test blocks. | adapted | Compact no-repeat release. |
| `display_case` | `task.display_case` | uppercase | local adaptation | Case not specified in methods excerpt. | inferred | Monospace uppercase strings. |
