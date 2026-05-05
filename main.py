from functools import wraps

from .scripts.archive import _delete_archive
from .scripts.checkpoint import _load_checkpoint, _save_checkpoint
from .scripts.run import _archive_run, _reset_run

def debug_log(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"{prefix} STARTING.")
            try:
                result = func(*args, **kwargs)
                print(f"{prefix} COMPLETE.")
                return result
            except Exception as e:
                print(f"{prefix} FAILED: {e}")
                raise
        return wrapper
    return decorator

class WorkspaceHandler:
    def __init__(self, cfg):
        self.cfg = cfg
        print(f"[WorkspaceHandler]: created class.")
        
    @debug_log("[load_checkpoint]:")
    def load_checkpoint(self, checkpoint_path:str, model, optimizer, device:str) -> int:
        start_checkpoint:int = _load_checkpoint(checkpoint_path, model, optimizer, device)
        return start_checkpoint
    
    @debug_log("[save_checkpoint]")
    def save_checkpoint(self, checkpoint_path:str, model, optimizer, epoch:int) -> None:
        _save_checkpoint(checkpoint_path, model, optimizer, epoch)
    
    @debug_log("[archive_run]:")
    def archive_run(self) -> None:
        """
        Archives logs, checkpoints, and results for a run.
        Creates a timestamped snapshot of the experiment state.
        """
        _archive_run(self.cfg)
    
    @debug_log("[reset_run]:")
    def reset_run(self) -> None:
        """
        Wipes all files from the directories defined in the config.
        Keeps directory structure intact.
        """
        _reset_run(self.cfg)
    
    @debug_log("[delete_archive]:")
    def delete_archive(self, archive_name:str) -> None:
        """
        Deletes a specific archived experiment folder.
        Example:
            delete_archive(cfg, "baseline_vae_20260412_145342")
        """
        _delete_archive(self.cfg, archive_name)