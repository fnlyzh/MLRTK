"""
References:
- PyTorch official guide: https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html
"""

from pathlib import Path
import torch

MODEL_WEIGHTS_NAME: str = "model_weights.pt"

def run_save_checkpoint(cfg, model, optimizer, epoch) -> None:
    p: Path = cfg.CHECKPOINTS_DIR.joinpath(MODEL_WEIGHTS_NAME)
    
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }, p)


def run_load_checkpoint(cfg, model, optimizer=None) -> int:
    DEBUG_FILE: str = "run_load_checkpoint"
    p: Path = cfg.CHECKPOINTS_DIR.joinpath(MODEL_WEIGHTS_NAME)

    if not p.exists():
        print(f"[debug] {DEBUG_FILE}: no checkpoint found at {p}. Returning epoch=1.")
        return 1
    
    checkpoint = torch.load(p, weights_only=True)
    
    model.load_state_dict(checkpoint["model_state_dict"])
    
    if optimizer:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    
    epoch = checkpoint["epoch"]
    
    print(f"[debug] {DEBUG_FILE}: loaded weights, resuming from epoch {epoch}.")

    return epoch