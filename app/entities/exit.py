from typing import Optional

from blessed import Terminal
from pydantic import BaseModel

from app.types.hitbox import HitBox


class Exit(BaseModel):
    """Entity for player exit denoting end of level"""

    pos_x: int
    pos_y: int

    def __str__(self) -> str:
        return "🚪"

    def get_hitbox_at(self, time: int, term: Optional[Terminal] = None) -> HitBox:
        """Get hitbox at a given time"""
        return HitBox(
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=str(self) if time > 0 else str(self) + "<-- exit",
            time=time,
            parent=self.__class__,
        )
