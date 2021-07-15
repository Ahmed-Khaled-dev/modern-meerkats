from blessed import Terminal
from pydantic import BaseModel

from app import constants as const
from app.types.hitbox import HitBox


class MapWindow(BaseModel):
    """The area in which the current level map is drawn"""

    level_name: str
    level_number: int
    boxes: list[HitBox]
    width: int = const.MAP_WIDTH
    height: int = const.MAP_HEIGHT
    pos_x: int = const.MAP_X
    pos_y: int = const.MAP_Y

    def content(self, term: Terminal) -> str:
        """Return the inner content area of a map"""
        return "".join([b.render_str(term) for b in self.boxes])
