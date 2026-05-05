import torch
import os

def _load_checkpoint(checkpoint_path:str, model, optimizer, device:str) -> int:
    if not os.path.exists(checkpoint_path):
        print(f"No checkpoint found at {checkpoint_path}. Starting from first epoch.")
        return 1
    
    print(f"Loading checkpoint {checkpoint_path}.")
    checkpoint = torch.load(checkpoint_path, map_location=device, weights_only=False)

    model.load_state_dict(checkpoint['model_state_dict'])
    
    if optimizer and 'optimizer_state_dict' in checkpoint:
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    
    return checkpoint['epoch'] + 1        

def _save_checkpoint(checkpoint_path:str, model, optimizer, epoch:int) -> None:
    save_dict = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict()
    }
    torch.save(save_dict, checkpoint_path)

    print(f"Saved checkpoint at {checkpoint_path}.")