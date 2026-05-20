from pathlib import Path
import shutil

def run_deposit_archive(cfg) -> None:
    print(f"[debug] run_deposit_archive: starting.")

    dst = Path(cfg.ARCHIVE_DIR).joinpath(f"{cfg.MODEL}")
    dst.mkdir(exist_ok=False)
    for p in cfg.MOVING_DIRS:
        src = Path(p)
        shutil.move(src, dst)
    
    print(f"[debug] run_deposit_archive: finished.")

def run_withdraw_archive(cfg) -> None:
    print(f"[debug] run_withdraw_archive: starting.")

    dst = Path(cfg.WORK_DIR)
    src_dirs = Path(cfg.ARCHIVE_DIR).joinpath(cfg.MODEL)
    for src in src_dirs.iterdir():
        shutil.move(src, dst)
    
    print(f"[debug] run_withdraw_archive: finished.")