from typing import Literal, Optional

from blessed import Terminal
from pydantic import BaseModel

from app.actions import Move
from app.entities.utils import get_loop_time
from app.types.hitbox import HitBox


class MovingWall(BaseModel):
    """Entity denoting a unpassable structure that moves up/down or left/right"""

    start_x: int
    start_y: int
    actions: list[Move] = []
    char: str = "█"

    def __str__(self) -> str:
        return self.char

    @classmethod
    def create_line(
        cls,
        start_x: int,
        start_y: int,
        length: int,
        loop_interval: int,
        orientation: Literal["v", "h"],
    ):
        """Creates an array of static assets to make a moving line"""
        if orientation == "v":
            return [
                cls(
                    start_x=start_x,
                    start_y=start_y + i,
                    loop_interval=loop_interval,
                    orientation=orientation,
                )
                for i in range(0, length)
            ]
        else:
            return [
                cls(
                    start_x=start_x + i,
                    start_y=start_y,
                    loop_interval=loop_interval,
                    orientation=orientation,
                )
                for i in range(0, length)
            ]

    @property
    def loop_interval(self) -> int:
        """Calculate the loop interval length"""
        return sum([a.length for a in self.actions])

    @property
    def time_consumed(self) -> int:
        """Amount of time the initial loop consumes"""
        return self.loop_interval

    def get_move_at(self, time: int) -> Move:
        """Get action at a given time"""
        return [x for x in self.actions if x.time_start <= time < x.time_end][0]

    def get_hitbox_at(self, time: int, term: Optional[Terminal] = None) -> HitBox:
        """Get hitbox at a given time"""
        loop_time = get_loop_time(self.loop_interval, time)
        if loop_time == 0:
            return HitBox(
                pos_x=self.start_x,
                pos_y=self.start_y,
                parent=self.__class__,
                content=self.char,
                time=time,
            )
        return self.get_move_at(loop_time).get_hitbox_at(loop_time)

    @property
    def last_pos(self) -> tuple[int, int]:
        """Get the last known position for player"""
        if not self.actions:
            return (self.start_x, self.start_y)
        else:
            box = self.get_move_at(self.time_consumed).get_hitbox_at(self.time_consumed)
            return box.pos_x, box.pos_y
