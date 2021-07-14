from typing import Literal

from pydantic import BaseModel

from app.types.hitbox import HitBox
from app.windows.core import term


class Wall(BaseModel):
    """Entity denoting a unpassable structure"""

    pos_x: int
    pos_y: int
    char: str = "█"

    @classmethod
    def create_line(
        cls, start_x: int, start_y: int, length: int, orientation: Literal["v", "h"]
    ):
        """Creates an array of static assets to make a line"""
        if orientation == "v":
            return [cls(pos_x=start_x, pos_y=start_y + i) for i in range(0, length)]
        else:
            return [cls(pos_x=start_x + i, pos_y=start_y) for i in range(0, length)]

    @classmethod
    def create_box(cls, start_x: int, start_y: int, height: int, width: int):
        """Creates an array of static assets to make a box"""
        res = []
        for y in range(0, height):
            for x in range(0, width):
                res.append(cls(pos_x=start_x + x, pos_y=start_y + y))
        return res

    def to_hitbox(self, time: int) -> list[HitBox]:
        """Transform wall to hitbox"""
        return [
            HitBox(
                pos_x=self.pos_x,
                pos_y=self.pos_y,
                content=term.seashell4(self.char),
                time=t,
                parent=self.__class__,
            )
            for t in range(0, time)
        ]
