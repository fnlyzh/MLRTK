from pathlib import Path

DEBUG_NAME: str = "run_create"

def run_create(cfg) -> None:
    print(f"[debug] {DEBUG_NAME}: received instructions to create {cfg.MOVING_DIRS}.")
    
    for p_string in cfg.MOVING_DIRS:
        p = Path(p_string)
        Path.mkdir(p, exist_ok=True)
        print(f"[debug] {DEBUG_NAME}: created {p}.")
    
    print(f"[debug] {DEBUG_NAME}: completed successfully.")