from module.controller import WorkspaceHandler
from lab.config import load_config

def run_test() -> None:
    print("[debug] test: initiating ...")
    cfg = load_config()

    mlrkt = WorkspaceHandler(cfg)

    print("[debug] test: complete.")

if __name__ == "__main__":
    run_test()