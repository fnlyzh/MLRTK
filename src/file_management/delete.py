from pathlib import Path
import shutil

DEBUG_NAME: str = "run_delete"

def run_delete(cfg) -> None:
    print(f"[debug] {DEBUG_NAME}: received instructions to delete {cfg.MOVING_DIRS}")

    for p_string in cfg.MOVING_DIRS:
        p = Path(p_string)
        if p.exists():
            shutil.rmtree(p)
            print(f"[debug] {DEBUG_NAME}: deleted {p}")
        else:
            print(f"[debug] {DEBUG_NAME}: not found {p}")

    print(f"[debug] {DEBUG_NAME}: completed succesfully.")