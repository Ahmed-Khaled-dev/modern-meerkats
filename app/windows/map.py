from typing import Optional

from pydantic import BaseModel

from app import constants as const
from app.windows.core import Window


class MapWindow(BaseModel):
    """The area in which the current level map is drawn"""

    level_name: str
    level_number: int
    width: int = const.MAP_WIDTH
    height: int = const.MAP_HEIGHT
    pos_x: int = const.MAP_X
    pos_y: int = const.MAP_Y
    content: Optional[str]

    def __str__(self) -> str:
        title = f"Level {self.level_number} - {self.level_name}"
        window = Window(
            title=title,
            width=self.width,
            height=self.height,
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self.content,
        )
        return str(window)
