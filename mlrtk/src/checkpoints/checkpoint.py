"""
References:
- PyTorch official guide: https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html
"""

from pathlib import Path
import torch

def run_save_checkpoint(cfg, model, optimizer, epoch) -> None:
    p = Path(cfg.CHECKPOINTS_DIR).joinpath("model_weights.pth")
    
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }, p)


def run_load_checkpoint(cfg, model, optimizer=None) -> int:
    p = Path(cfg.CHECKPOINTS_DIR).joinpath("model_weights.pth")

    if not p.exists():
        print(f"[debug] run_load_checkpoint: no checkpoint found at {p}. Returning epoch=1.")
        return 1
    
    checkpoint = torch.load(p, weights_only=True)
    
    model.load_state_dict(checkpoint["model_state_dict"])
    
    if optimizer:
        optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    
    epoch = checkpoint["epoch"]
    
    print(f"[debug] run_load_checkpoint: loaded weights, resuming from epoch {epoch}.")

    return epoch