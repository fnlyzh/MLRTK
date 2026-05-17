from functools import wraps

from .src.checkpoint import run_load_checkpoint, run_save_checkpoint
from .src.archive import run_delete_archive
from .src.run import run_archive_run, run_reset_run

class WorkspaceHandler:
    def __init__(self, cfg):
        self.cfg = cfg
        print(f"[debug] WorkspaceHandler: created.")
        
    def load_checkpoint(self, checkpoint_path:str, model, optimizer, device:str) -> int:
        start_checkpoint: int = run_load_checkpoint(checkpoint_path, model, optimizer, device)
        return start_checkpoint
    
    def save_checkpoint(self, checkpoint_path:str, model, optimizer, epoch:int) -> None:
        run_save_checkpoint(checkpoint_path, model, optimizer, epoch)
    
    def archive_run(self) -> None:
        """
        Archives logs, checkpoints, and results for a run.
        Creates a timestamped snapshot of the experiment state.
        """
        run_archive_run(self.cfg)
    
    def reset_run(self) -> None:
        """
        Wipes all files from the directories defined in the config.
        Keeps directory structure intact.
        """
        run_reset_run(self.cfg)
    
    def delete_archive(self, archive_name:str) -> None:
        """
        Deletes a specific archived experiment folder.
        Example:
            delete_archive(cfg, "baseline_vae_20260412_145342")
        """
        run_delete_archive(self.cfg, archive_name)