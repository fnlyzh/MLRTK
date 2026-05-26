from pathlib import Path

DEBUG_NAME: str = "run_create_experiment"

def run_create_experiment(cfg) -> None:
    print(f"[debug] {DEBUG_NAME}: creating new directory for {cfg.MODEL}.")

    if cfg.MODEL_DIR.exists():
        print(f"[debug] {DEBUG_NAME}: {cfg.MODEL_DIR} already exists; skipping.")
        return

    Path.mkdir(cfg.MODEL_DIR)
    Path.touch(cfg.DOCUMENTATION_FILE)
    Path.mkdir(cfg.CHECKPOINTS_DIR)
    Path.mkdir(cfg.RESULTS_DIR)
    Path.mkdir(cfg.CODE_DIR)

    for p in cfg.CODE_FILES:
        Path.touch(p)
    
    print(f"[debug] {DEBUG_NAME}: complete.")