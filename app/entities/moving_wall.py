from typing import Literal

from blessed import Terminal
from pydantic import BaseModel

from app.types.hitbox import HitBox


class MovingWall(BaseModel):
    """Entity denoting a unpassable structure that moves up/down or left/right"""

    start_x: int
    start_y: int
    duration: int
    orientation: Literal["v", "h"]
    char: str = "█"

    @classmethod
    def create_line(
        cls,
        start_x: int,
        start_y: int,
        length: int,
        duration: int,
        orientation: Literal["v", "h"],
    ):
        """Creates an array of static assets to make a moving line"""
        if orientation == "v":
            return [
                cls(
                    start_x=start_x,
                    start_y=start_y + i,
                    duration=duration,
                    orientation=orientation,
                )
                for i in range(0, length)
            ]
        else:
            return [
                cls(
                    start_x=start_x + i,
                    start_y=start_y,
                    duration=duration,
                    orientation=orientation,
                )
                for i in range(0, length)
            ]

    def get_displacement(self, time: int, reverse: bool = False) -> int:
        """Calculate displacement form initial position"""
        if time < self.duration:
            if reverse:
                return self.duration - time
            else:
                return time
        else:
            return self.get_displacement(time - self.duration, not reverse)

    def get_hitbox_at(self, time: int, term: Terminal) -> HitBox:
        """Get hitbox at a given time"""
        displacement = self.get_displacement(time)
        if self.orientation == "h":
            x, y = self.start_x + displacement, self.start_y
        else:
            x, y = self.start_x, self.start_y + displacement
        return HitBox(
            pos_x=x,
            pos_y=y,
            content=term.seashell4(self.char),
            time=time,
            parent=self.__class__,
        )
