from pathlib import Path
import shutil

def run_deposit_archive(cfg) -> None:
    DEBUG_FILE: str = "run_deposit_archive"
    print(f"[debug] {DEBUG_FILE}: starting.")

    dst: Path = cfg.ARCHIVE_DIR.joinpath(cfg.MODEL)
    if dst.exists():
        print(f"[debug] {DEBUG_FILE}: {dst} already exists; skipping.")
        return

    shutil.move(cfg.MODEL_DIR, cfg.ARCHIVE_DIR)
    
    print(f"[debug] run_deposit_archive: finished.")

def run_withdraw_archive(cfg) -> None:
    DEBUG_FILE: str = "run_withdraw_archive"
    print(f"[debug] {DEBUG_FILE}: starting.")

    dst: Path = cfg.ACTIVE_DIR.joinpath(cfg.MODEL)
    if dst.exists():
        print(f"[debug] {DEBUG_FILE}: {dst} already exists; skipping.")
        return

    src: Path = cfg.ARCHIVE_DIR.joinpath(cfg.MODEL)

    shutil.move(src, cfg.ACTIVE_DIR)
    
    print(f"[debug] {DEBUG_FILE}: finished.")