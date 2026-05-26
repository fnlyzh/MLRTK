from mlrtk.api import MLRTKHandler
from config import get_config

def main() -> None:
    cfg = get_config()
    mlrtk = MLRTKHandler(cfg)
    # mlrtk.withdraw_archive()
    # mlrtk.create_experiment()
    mlrtk.delete_experiment()
    # mlrtk.deposit_archive()


if __name__ == "__main__":
    main()