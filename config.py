from dataclasses import dataclass
from typing import ClassVar
from pydantic import BaseModel

@dataclass
class MLRTKConfig(BaseModel):
    MODEL: ClassVar[str] = "test_one"

    """ Moving Directories """
    WORK_DIR: ClassVar[str] = "lab/"
    RESULTS_DIR: ClassVar[str] = "lab/results/"
    CHECKPOINTS_DIR: ClassVar[str] = "lab/checkpoints/"
    MOVING_DIRS: ClassVar[tuple[str]] = (RESULTS_DIR, CHECKPOINTS_DIR)
    ARCHIVE_DIR: ClassVar[str] = "archive/"

def get_config():
    return MLRTKConfig()