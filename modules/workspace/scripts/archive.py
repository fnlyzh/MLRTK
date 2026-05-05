import os
import shutil

def _delete_archive(cfg, archive_name:str) -> None:
    archive_path = os.path.join(cfg.ARCHIVES_DIR, archive_name)

    if not os.path.exists(archive_path):
        print(f"Path not found {archive_name}")
        return

    if not os.path.isdir(archive_path):
        print(f"Path is not a directory {archive_path}")
        return

    try:
        shutil.rmtree(archive_path)
        print(f"Deleted archive '{archive_name}'")
    except Exception as e:
        print(f"Failed to delete archive '{archive_name}' -> {e}")