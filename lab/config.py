from dataclasses import dataclass

@dataclass
class WorkspaceConfig:
    """ ID for current workspace """
    # short name (please don't use spacing)
    MODEL_NAME:str = "EPIC_MODEL"
    # nth version for this model
    MODEL_VERSION:int = 1
    
    # short summary of how this version changes from the previous
    MODEL_DESCRIPTION:str = "using lasso instead of ridge"

    
    """ directories """
    _MODEL_DIR = f"{MODEL_NAME}_v{MODEL_VERSION}/"

    # periodic checkpoints across epochs
    CHECKPOINT_DIR:str = _MODEL_DIR + "/checkpoints/"
    # periodic plots & metrics across epochs
    LOGGING_DIR:str = _MODEL_DIR + "/logging/"
    # user-called plots & metrics
    RESULTS_DIR:str = _MODEL_DIR + "/results/"
    # checkpoints + plots + metrics of all previous runs
    ARCHIVES_DIR:str = _MODEL_DIR + "/archive/"

    # documentation for building the model
    # might use this to construct a continuous thought journal
    JOURNAL_FILE:str = _MODEL_DIR + "/journal.txt"

def load_config():
    return WorkspaceConfig()