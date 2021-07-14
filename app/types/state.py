from enum import Enum, auto


class LevelState(Enum):
    """The current state of the level"""

    Win = auto()
    Planning = auto()
    Execution = auto()
    ExitNotReached = auto()
