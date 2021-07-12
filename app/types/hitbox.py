from pydantic import BaseModel

from app import constants as const
from app.windows.core import term


class HitBox(BaseModel):
    """A hitbox is any entity that provides some sort of interaction

    TODO: add collision logic
    """

    pos_x: int
    pos_y: int
    content: str
    time: int

    def __str__(self) -> str:
        x = self.pos_x + const.MAP_X + 1
        y = self.pos_y + const.MAP_Y + 1
        return term.move_xy(x, y) + self.content

    def __lt__(self, other: "HitBox") -> bool:
        return self.time < other.time

    def __hash__(self) -> int:
        return hash((self.pos_x, self.pos_y, self.content, self.time))
