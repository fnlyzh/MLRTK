from pathlib import Path
import shutil

DEBUG_NAME: str = "run_delete_experiment"

def run_delete_experiment(cfg) -> None:
    print(f"[debug] {DEBUG_NAME}: deleting directory for {cfg.MODEL}.")

    if not cfg.MODEL_DIR.exists():
        print(f"[debug]: {DEBUG_NAME}: {cfg.MODEL_DIR} not found; skipping.")
        return

    shutil.rmtree(cfg.MODEL_DIR)
    
    print(f"[debug] {DEBUG_NAME}: complete.")