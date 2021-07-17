from typing import Type

from pydantic import BaseModel

from app.constants import term
from app.types.hitbox import HitBox


class Wait(BaseModel):
    """Wait command"""

    pos_x: int
    pos_y: int
    time_start: int
    length: int
    content: str
    parent: Type

    def __str__(self) -> str:
        return f"wait {self.length}"

    def get_hitbox_at(self, time: int) -> HitBox:
        """Get hitbox at given time"""
        return HitBox(
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self.content,
            time=time,
            parent=self.parent,
        )

    @property
    def time_end(self) -> int:
        """The end time for the given action"""
        return self.time_start + self.length

    @staticmethod
    def name() -> str:
        """Generate command name"""
        return term.yellow("wait")

    @staticmethod
    def usage() -> list[str]:
        """Generate usag strings"""
        return [
            term.orangered("wait [time]"),
            term.yellow("wait 5"),
        ]
