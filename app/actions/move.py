from typing import Literal, Type

from pydantic import BaseModel

from app.types.hitbox import HitBox


class Move(BaseModel):
    """A move action displacing the player"""

    pos_x: int
    pos_y: int
    length: int
    time_start: int
    orientation: Literal["up", "down", "left", "right"]
    parent: Type
    content: str
    halt_times: list[int] = []

    def __str__(self) -> str:
        return f"move {self.length} {self.orientation}"

    def get_hitbox_at(self, time: int) -> HitBox:
        """Get the relevant hitbox at a given time"""
        halts = len([x for x in self.halt_times if time > x])
        displacement = time - self.time_start - halts
        if time in self.halt_times:
            return self.get_hitbox_at(time=time - 1)
        elif self.orientation == "up":
            x, y = self.pos_x, self.pos_y - displacement
        elif self.orientation == "down":
            x, y = self.pos_x, self.pos_y + displacement
        elif self.orientation == "left":
            x, y = self.pos_x - displacement, self.pos_y
        elif self.orientation == "right":
            x, y = self.pos_x + displacement, self.pos_y
        else:
            x, y = self.pos_x, self.pos_y
        return HitBox(
            pos_x=x, pos_y=y, content=self.content, time=time, parent=self.parent
        )

    @property
    def time_end(self) -> int:
        """The end time for the given action"""
        return self.time_start + self.length
