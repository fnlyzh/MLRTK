from src.api import MLRTKHandler

def main() -> None:
    mlrtk = MLRTKHandler()
    # mlrtk.create_directories()
    # mlrtk.delete_directories()
    mlrtk.reset_directories()


if __name__ == "__main__":
    main()