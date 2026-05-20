from mlrtk.api import MLRTKHandler
from config import get_config

def main() -> None:
    cfg = get_config()
    mlrtk = MLRTKHandler(cfg)
    # mlrtk.create_directories()
    # mlrtk.delete_directories()
    # mlrtk.reset_directories()
    mlrtk.withdraw_archive()


if __name__ == "__main__":
    main()