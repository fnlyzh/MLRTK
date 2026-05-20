from .src.file_management.create import run_create
from .src.file_management.delete import run_delete
from .src.file_management.archive import run_deposit_archive, run_withdraw_archive
from .src.checkpoints.checkpoint import run_save_checkpoint, run_load_checkpoint

class MLRTKHandler:
    def __init__(self, cfg) -> None:
        print("[debug] MLRTKHandler: initialising...")

        self.cfg = cfg

        print("[debug] MLRTKHandler: created successfully.")
    
    def create_directories(self) -> None:
        run_create(self.cfg)
    
    def delete_directories(self) -> None:
        run_delete(self.cfg)

    def reset_directories(self) -> None:
        self.delete_directories()
        self.create_directories()
    
    def deposit_archive(self) -> None:
        """
        Collect moving directories into a folder named cfg.MODEL inside cfg.ARCHIVE_DIR.
        NOTE: assumes there currently exists no directory in cfg.ARCHIVE_DIR named cfg.MODEL.
        """
        run_deposit_archive(self.cfg)
    
    def withdraw_archive(self) -> None:
        run_withdraw_archive(self.cfg)
    
    def save_checkpoint(self, model, optimizer, epoch) -> None:
        run_save_checkpoint(self.cfg, model, optimizer, epoch)
    
    def load_checkpoint(self, model, optimizer=None) -> int:
        epoch = run_load_checkpoint(self.cfg, model, optimizer)
        return epoch