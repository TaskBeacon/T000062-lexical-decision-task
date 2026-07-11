from __future__ import annotations

from contextlib import nullcontext
from functools import partial
from pathlib import Path
from typing import Any

import pandas as pd
from psychopy import core

from psyflow import (
    BlockUnit,
    StimBank,
    StimUnit,
    SubInfo,
    TaskRunOptions,
    TaskSettings,
    context_from_config,
    count_down,
    initialize_exp,
    initialize_triggers,
    load_config,
    parse_task_run_options,
    runtime_context,
)

from src import generate_trial_blocks, load_stimulus_pool, run_trial, summarize_trials


MODES = ("human", "qa", "sim")
DEFAULT_CONFIG_BY_MODE = {
    "human": "config/config.yaml",
    "qa": "config/config_qa.yaml",
    "sim": "config/config_scripted_sim.yaml",
}


def _execute_block(
    *,
    block_id: str,
    block_idx: int,
    plans: list[Any],
    settings: TaskSettings,
    win: Any,
    kb: Any,
    stim_bank: StimBank,
    trigger_runtime: Any,
    sink: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    block = (
        BlockUnit(
            block_id=block_id,
            block_idx=block_idx,
            settings=settings,
            window=win,
            keyboard=kb,
        )
        .add_condition(plans)
        .on_start(lambda _: trigger_runtime.send(settings.triggers.get("block_start")))
        .on_end(lambda _: trigger_runtime.send(settings.triggers.get("block_end")))
        .run_trial(
            partial(
                run_trial,
                stim_bank=stim_bank,
                trigger_runtime=trigger_runtime,
                block_id=block_id,
                block_idx=block_idx,
            )
        )
        .to_dict(sink)
    )
    return list(block.get_all_data())


def _ms(value: float | None) -> str:
    return "--" if value is None else f"{1000 * float(value):.0f} ms"


def run(options: TaskRunOptions) -> None:
    task_root = Path(__file__).resolve().parent
    cfg = load_config(str(options.config_path))
    task_cfg = dict(cfg["task_config"])
    output_dir: Path | None = None
    runtime_scope = nullcontext()
    runtime_ctx = None
    if options.mode in ("qa", "sim"):
        runtime_ctx = context_from_config(task_dir=task_root, config=cfg, mode=options.mode)
        output_dir = runtime_ctx.output_dir
        runtime_scope = runtime_context(runtime_ctx)

    with runtime_scope:
        if options.mode == "qa":
            subject_data = {"subject_id": "qa"}
        elif options.mode == "sim":
            participant_id = "sim"
            if runtime_ctx is not None and runtime_ctx.session is not None:
                participant_id = str(runtime_ctx.session.participant_id or "sim")
            subject_data = {"subject_id": participant_id}
        else:
            subject_data = SubInfo(cfg["subform_config"]).collect()

        settings = TaskSettings.from_dict(task_cfg)
        if options.mode in ("qa", "sim") and output_dir is not None:
            settings.save_path = str(output_dir)
        settings.add_subinfo(subject_data)
        if options.mode == "qa" and output_dir is not None:
            output_dir.mkdir(parents=True, exist_ok=True)
            settings.res_file = str(output_dir / "qa_trace.csv")
            settings.log_file = str(output_dir / "qa_psychopy.log")
            settings.json_file = str(output_dir / "qa_settings.json")

        settings.triggers = cfg["trigger_config"]
        trigger_runtime = initialize_triggers(mock=True) if options.mode in ("qa", "sim") else initialize_triggers(cfg)
        win, kb = initialize_exp(settings)
        stim_bank = StimBank(win, cfg["stim_config"]).preload_all()
        settings.save_to_json()

        pool = load_stimulus_pool(task_root / str(settings.stimuli_file))
        practice_plans, scored_blocks = generate_trial_blocks(
            pool=pool,
            block_counts=[dict(counts) for counts in settings.block_counts],
            practice_trials=int(settings.practice_trials),
            seed=int(settings.plan_seed),
        )

        trigger_runtime.send(settings.triggers.get("experiment_start"))
        StimUnit("instruction", win, kb, runtime=trigger_runtime).add_stim(
            stim_bank.get("instruction")
        ).wait_and_continue()

        if practice_plans:
            StimUnit("practice_intro", win, kb, runtime=trigger_runtime).add_stim(
                stim_bank.get("practice_intro")
            ).wait_and_continue()
            practice_data: list[dict[str, Any]] = []
            _execute_block(
                block_id="practice",
                block_idx=-1,
                plans=practice_plans,
                settings=settings,
                win=win,
                kb=kb,
                stim_bank=stim_bank,
                trigger_runtime=trigger_runtime,
                sink=practice_data,
            )

        all_data: list[dict[str, Any]] = []
        for block_idx, plans in enumerate(scored_blocks):
            if options.mode == "human":
                count_down(win, 3, color="white")
            block_id = f"block_{block_idx + 1}"
            block_rows = _execute_block(
                block_id=block_id,
                block_idx=block_idx,
                plans=plans,
                settings=settings,
                win=win,
                kb=kb,
                stim_bank=stim_bank,
                trigger_runtime=trigger_runtime,
                sink=all_data,
            )
            if block_idx < len(scored_blocks) - 1:
                summary = summarize_trials(block_rows, block_id)
                StimUnit("block_summary", win, kb, runtime=trigger_runtime).add_stim(
                    stim_bank.get_and_format(
                        "block_break",
                        block_num=block_idx + 1,
                        total_blocks=len(scored_blocks),
                        accuracy=f"{summary['accuracy']:.1%}",
                        frequency_effect=_ms(summary["word_frequency_effect"]),
                    )
                ).wait_and_continue()

        summary = summarize_trials(all_data)
        StimUnit("good_bye", win, kb, runtime=trigger_runtime).add_stim(
            stim_bank.get_and_format(
                "good_bye",
                accuracy=f"{summary['accuracy']:.1%}",
                word_accuracy=f"{summary['word_accuracy']:.1%}",
                nonword_accuracy=f"{summary['nonword_accuracy']:.1%}",
                frequency_effect=_ms(summary["word_frequency_effect"]),
                timeouts=summary["timeouts"],
            )
        ).wait_and_continue(terminate=True)
        trigger_runtime.send(settings.triggers.get("experiment_end"))

        pd.DataFrame(all_data).to_csv(settings.res_file, index=False)
        trigger_runtime.close()
        core.quit()


def main() -> None:
    task_root = Path(__file__).resolve().parent
    options = parse_task_run_options(
        task_root=task_root,
        description="Run the Lexical Decision task in human, QA, or simulation mode.",
        default_config_by_mode=DEFAULT_CONFIG_BY_MODE,
        modes=MODES,
    )
    run(options)


if __name__ == "__main__":
    main()
