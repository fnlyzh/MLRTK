from pathlib import Path
import shutil

def run_initiate(cfg) -> None:
    DEBUG_FILE: str = "run_initiate"

    print(f"[debug] {DEBUG_FILE}: initiating workspace.")

    Path.mkdir(cfg.PROJECT_DIR, exist_ok=True)
    Path.mkdir(cfg.ACTIVE_DIR, exist_ok=True)
    Path.mkdir(cfg.ARCHIVE_DIR, exist_ok=True)

    print(f"[debug] {DEBUG_FILE}: complete.")

def run_reset(cfg) -> None:
    DEBUG_FILE: str = "run_reset"
    
    print(f"[debug] {DEBUG_FILE}: resetting workspace.")

    shutil.rmtree(cfg.PROJECT_DIR)
    Path.mkdir(cfg.PROJECT_DIR)

    print(f"[debug] {DEBUG_FILE}: complete.")