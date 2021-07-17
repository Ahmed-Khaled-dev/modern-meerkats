from typing import Literal

from pydantic import BaseModel

from app import constants as const
from app.actions import Action, Wait, action_from_str
from app.entities.utils import get_loop_time, invert_orientation, is_inverted
from app.types import Orientation
from app.types.hitbox import HitBox


class PatrolVision(BaseModel):
    """Vision for a patrol entity"""

    pos_x: int
    pos_y: int
    char: str = const.PATROL_VISION

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
    def create_from_patrol_pos(
        cls, start_x: int, start_y: int, orientation: Orientation
    ) -> list["PatrolVision"]:
        """Create patrolvision from patrol positioning"""
        if orientation == "up":
            create_args = [
                (start_x - 1, start_y - 1, 3, "h"),
                (start_x - 1, start_y - 2, 3, "h"),
                (start_x - 2, start_y - 3, 5, "h"),
                (start_x - 2, start_y - 4, 5, "h"),
                (start_x - 2, start_y - 5, 5, "h"),
            ]
        elif orientation == "down":
            create_args = [
                (start_x - 1, start_y + 1, 3, "h"),
                (start_x - 1, start_y + 2, 3, "h"),
                (start_x - 2, start_y + 3, 5, "h"),
                (start_x - 2, start_y + 4, 5, "h"),
                (start_x - 2, start_y + 5, 5, "h"),
            ]
        elif orientation == "right":
            create_args = [
                (start_x + 1, start_y - 1, 3, "v"),
                (start_x + 2, start_y - 1, 3, "v"),
                (start_x + 3, start_y - 2, 5, "v"),
                (start_x + 4, start_y - 2, 5, "v"),
                (start_x + 5, start_y - 2, 5, "v"),
            ]
        else:
            create_args = [
                (start_x - 1, start_y - 1, 3, "v"),
                (start_x - 2, start_y - 1, 3, "v"),
                (start_x - 3, start_y - 2, 5, "v"),
                (start_x - 4, start_y - 2, 5, "v"),
                (start_x - 5, start_y - 2, 5, "v"),
            ]
        res = []
        for x, y, l, o in create_args:
            res += cls.create_line(x, y, l, o)
        return res

    def get_hitbox_at(self, time: int) -> HitBox:
        """Get hitbox at a given time"""
        return HitBox(
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self.char,
            time=time,
            parent=self.__class__,
        )


class Patrol(BaseModel):
    """A patrol entity that moves between points"""

    start_x: int
    start_y: int
    orientation: Orientation
    actions: list[Action] = []
    char: str = const.PATROL

    def __str__(self) -> str:
        return self.char

    @classmethod
    def create(
        cls, start_x: int, start_y: int, orientation: Orientation, actions: list[str]
    ) -> "Patrol":
        """Create a patrol entity"""
        patrol = cls(start_x=start_x, start_y=start_y, orientation=orientation)
        for a in actions:
            action, _ = action_from_str(a, patrol)
            if action:
                patrol.actions.append(action)
        return patrol

    @property
    def loop_interval(self) -> int:
        """Calculate the loop interval length"""
        return sum([a.length for a in self.actions])

    @property
    def time_consumed(self) -> int:
        """Amount of time the initial loop consumes"""
        return self.loop_interval

    def get_move_at(self, time: int) -> Action:
        """Get action at a given time"""
        return [x for x in self.actions if x.time_start <= time < x.time_end][0]

    def get_current_position(self, time: int) -> tuple[Orientation, tuple[int, int]]:
        """Get current patrol position and orientation"""
        loop_time = get_loop_time(self.loop_interval, time)
        if loop_time == 0:
            return self.orientation, (self.start_x, self.start_y)
        move = self.get_move_at(loop_time)
        box = move.get_hitbox_at(loop_time)
        if isinstance(move, Wait):
            return self.get_current_position(time - 1)
        if is_inverted(self.loop_interval, time):
            return invert_orientation(move.orientation), (box.pos_x, box.pos_y)
        else:
            return move.orientation, (box.pos_x, box.pos_y)

    def get_hitbox_at(self, time: int) -> HitBox:
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

    def get_current_vision(self, time: int) -> list[PatrolVision]:
        """Generate vision hitboxes"""
        orientation, pos = self.get_current_position(time)
        return PatrolVision.create_from_patrol_pos(
            start_x=pos[0], start_y=pos[1], orientation=orientation
        )
