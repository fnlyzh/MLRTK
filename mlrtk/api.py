from .src.file_management.archive import run_deposit_archive, run_withdraw_archive
from .src.checkpoints.checkpoint import run_save_checkpoint, run_load_checkpoint
from .src.file_management.create_experiment import run_create_experiment
from .src.file_management.delete_experiment import run_delete_experiment
from .src.file_management.setup import run_initiate, run_reset

class MLRTKHandler:
    def __init__(self, cfg) -> None:
        print("[debug] MLRTKHandler: initialising...")

        self.cfg = cfg

        print("[debug] MLRTKHandler: created successfully.")
    
    def initiate(self) -> None:
        run_initiate(self.cfg)
    
    def reset(self) -> None:
        run_reset(self.cfg)
    
    def create_experiment(self) -> None:
        run_create_experiment(self.cfg)
    
    def delete_experiment(self) -> None:
        run_delete_experiment(self.cfg)
    
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