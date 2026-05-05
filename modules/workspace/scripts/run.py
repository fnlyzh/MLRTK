import os
import shutil
from datetime import datetime
from dataclasses import asdict

def _archive_run(cfg) -> None:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_root = os.path.join(
        cfg.ARCHIVES_DIR,
        f"{cfg.MODEL_NAME}_{timestamp}"
    )

    target_map = {
        cfg.LOG_DIR: "logs",
        cfg.CHECKPOINT_DIR: "checkpoints",
        cfg.RESULTS_DIR: "results",
    }

    print(f"Saving '{cfg.MODEL_NAME}' to {archive_root}...\n")

    os.makedirs(archive_root, exist_ok=True)

    config_path = os.path.join(archive_root, "experiment_config.md")
    with open(config_path, "w") as f:
        f.write(f"# Experiment: {cfg.MODEL_NAME}\n\n")
        for key, val in asdict(cfg).items():
            f.write(f"| {key} | {val} |\n")
    
    journal_path = os.path.join(archive_root, "journal.md")
    with open(journal_path, "w") as f:
        f.write(f"# Journal Entry: {cfg.MODEL_NAME}\n\n")
        f.write(f"**Version:** v{cfg.MODEL_VERSION}\n\n")
        f.write(f"**Date:** {timestamp}\n\n")
        f.write("## Description\n")
        f.write(f"{cfg.MODEL_DESCRIPTION}\n")

    for src_dir, label in target_map.items():
        if os.path.exists(src_dir) and os.listdir(src_dir):
            dest_dir = os.path.join(archive_root, label)
            try:
                shutil.copytree(src_dir, dest_dir)
                print(f"Copied {label}")
            except Exception as e:
                print(f"Failed copying {src_dir}: {e}")

def _reset_run(cfg):
    """
    Wipes all files from the directories defined in the config.
    Keeps directory structure intact.
    """
    target_dirs = [cfg.CHECKPOINT_DIR, cfg.LOG_DIR, cfg.RESULTS_DIR]

    print(f"Preparing to wipe working directories for '{cfg.MODEL_NAME}'...\n")

    for directory in target_dirs:

        if os.path.exists(directory):
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)

                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)

                except Exception as e:
                    print(f"  [error]: Could not delete {item_path}: {e}")

            print(f"Cleared: {directory}/")

        else:
            os.makedirs(directory, exist_ok=True)
            print(f"Initialized (was missing): {directory}/")