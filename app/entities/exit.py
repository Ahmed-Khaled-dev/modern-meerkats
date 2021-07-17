from pydantic import BaseModel

from app import constants as const
from app.types.hitbox import HitBox


class Exit(BaseModel):
    """Entity for player exit denoting end of level"""

    pos_x: int
    pos_y: int

    def __str__(self) -> str:
        return const.EXIT

    def get_hitbox_at(self, time: int) -> HitBox:
        """Get hitbox at a given time"""
        return HitBox(
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=str(self) if time > 0 else str(self) + "<-- exit",
            time=time,
            parent=self.__class__,
        )
