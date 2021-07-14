from pydantic import BaseModel

from app import constants as const
from app.types.hitbox import HitBox
from app.windows.core import Window


class MapWindow(BaseModel):
    """The area in which the current level map is drawn"""

    level_name: str
    level_number: int
    boxes: list[HitBox]
    width: int = const.MAP_WIDTH
    height: int = const.MAP_HEIGHT
    pos_x: int = const.MAP_X
    pos_y: int = const.MAP_Y

    @property
    def window(self) -> Window:
        """Return the window entity for map"""
        title = f"Level {self.level_number} - {self.level_name}"
        return Window(
            title=title,
            width=self.width,
            height=self.height,
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=None,
        )

    @property
    def content(self) -> str:
        """Return the inner content area of a map"""
        return "".join([str(b) for b in self.boxes])
