from enum import Enum, auto


class Event(Enum):
    """Events that are fired based on user input"""

    UpdateMap = auto()
    UpdateInput = auto()
    UpdateCmdList = auto()
    StartSequence = auto()
    EndLevel = auto()
    ToNextLevel = auto()
    ToMainMenu = auto()
    RetryLevel = auto()
