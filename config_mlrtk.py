from dataclasses import dataclass
from typing import ClassVar
from pydantic import BaseModel
from pathlib import Path

@dataclass
class MLRTKConfig(BaseModel):
    PROJECT_DIR: ClassVar[Path] = Path("project/")
    ACTIVE_DIR: ClassVar[Path] = PROJECT_DIR.joinpath("lab/")
    ARCHIVE_DIR: ClassVar[str] = PROJECT_DIR.joinpath("archive/")

    """ Directory Setup """
    MODEL: ClassVar[str] = "test_one"    
    MODEL_DIR: ClassVar[Path] = ACTIVE_DIR.joinpath(MODEL)
    
    DOCUMENTATION_FILE: ClassVar[Path] = MODEL_DIR.joinpath("README.md")
    CHECKPOINTS_DIR: ClassVar[Path] =  MODEL_DIR.joinpath("checkpoints/")
    RESULTS_DIR: ClassVar[Path] = MODEL_DIR.joinpath("results/")
    CODE_DIR: ClassVar[Path] = MODEL_DIR.joinpath("src/")

    CODE_FILES: ClassVar[tuple[Path]] = (
        CODE_DIR.joinpath("architecture.py"),
        CODE_DIR.joinpath("config.py"),
        CODE_DIR.joinpath("loss.py"),
        CODE_DIR.joinpath("train.py")
    )

def get_config():
    return MLRTKConfig()