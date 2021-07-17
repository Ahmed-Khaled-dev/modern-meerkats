from typing import Type

from blessed import Terminal
from pydantic import BaseModel

from app import constants as const


class HitBox(BaseModel):
    """A hitbox is any entity that provides some sort of interaction"""

    pos_x: int
    pos_y: int
    content: str
    time: int
    parent: Type

    def __lt__(self, other: "HitBox") -> bool:
        return self.time < other.time

    def __hash__(self) -> int:
        return hash((self.pos_x, self.pos_y, self.content, self.time))

    @property
    def in_bounds(self) -> bool:
        """Check if hitbox is within the bounds of the map"""
        return (
            self.pos_x >= const.MAP_X - 1
            and self.pos_x <= const.MAP_X + const.MAP_WIDTH - 2
            and self.pos_y >= const.MAP_Y - 1
            and self.pos_y <= const.MAP_Y + const.MAP_HEIGHT - 2
        )

    def render_str(self, term: Terminal) -> str:
        """Generate a renderable string for a hitbox"""
        x = self.pos_x + const.MAP_X + 1
        y = self.pos_y + const.MAP_Y + 1
        return term.move_xy(x, y) + self.content
