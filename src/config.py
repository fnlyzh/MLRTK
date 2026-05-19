from dataclasses import dataclass
from typing import ClassVar
from pydantic import BaseModel

@dataclass
class MLRTKConfig(BaseModel):
    """ Moving Directories """
    RESULTS_DIR: ClassVar[str] = "lab/results"
    CHECKPOINTS_DIR: ClassVar[str] = "lab/checkpoints"
    MOVING_DIRS: ClassVar[tuple[str]] = (RESULTS_DIR, CHECKPOINTS_DIR)

def get_config():
    return MLRTKConfig()