from .config import get_config

from .file_management.create import run_create
from .file_management.delete import run_delete
from .checkpoints.checkpoint import run_save_checkpoint, run_load_checkpoint

cfg = get_config()

class MLRTKHandler:
    def __init__(self) -> None:
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
    
    def save_checkpoint(self, model, optimizer, epoch) -> None:
        run_save_checkpoint(self.cfg, model, optimizer, epoch)
    
    def load_checkpoint(self, model, optimizer=None) -> int:
        epoch = run_load_checkpoint(self.cfg, model, optimizer)
        return epoch