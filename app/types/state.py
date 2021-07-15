from enum import Enum, auto


class LevelState(Enum):
    """The current state of the level"""

    Win = auto()
    Planning = auto()
    Execution = auto()
    ExitNotReached = auto()

    @classmethod
    def terminal(cls) -> list["LevelState"]:
        """States denoting that rendering has to stop"""
        return [cls.Win, cls.ExitNotReached]
