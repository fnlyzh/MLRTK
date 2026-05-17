import torch
import os

def run_load_checkpoint(checkpoint_path: str, model, optimizer, device: str) -> int:
    if not os.path.exists(checkpoint_path):
        print(f"[debug] run_load_checkpoint: checkpoint not found at {checkpoint_path}; starting from epoch 1.")
        start_checkpoint = 1
        return start_checkpoint
    
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)
    print(f"[debug] run_load_checkpoint: loaded from {checkpoint_path}.")

    model.load_state_dict(checkpoint['model_state_dict'])
    
    if optimizer and 'optimizer_state_dict' in checkpoint:
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    start_checkpoint = checkpoint['epoch'] + 1
    
    return start_checkpoint

def run_save_checkpoint(checkpoint_path: str, model, optimizer, epoch:int) -> None:
    save_dict = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict()
    }
    torch.save(save_dict, checkpoint_path)

    print(f"[debug] run_save_checkpoint: saved at {checkpoint_path}.")