from typing import Optional

from blessed import Terminal
from pydantic import BaseModel

from app.actions import Action
from app.types.hitbox import HitBox


class Player(BaseModel):
    """The player entity model"""

    start_x: int
    start_y: int
    actions: list[Action] = []

    def __str__(self) -> str:
        return "@"

    @property
    def initial(self) -> HitBox:
        """Initial state of the player"""
        return HitBox(
            pos_x=self.start_x,
            pos_y=self.start_y,
            content=str(self),
            time=0,
            parent=self.__class__,
        )

    def get_action_at(self, time: int) -> Action:
        """Get action at a given time"""
        return [x for x in self.actions if x.time_start <= time <= x.time_end][0]

    def get_hitbox_at(self, time: int, term: Optional[Terminal] = None) -> HitBox:
        """Get hitbox at a given time"""
        if time == 0:
            return self.initial
        else:
            return self.get_action_at(time).get_hitbox_at(time)

    @property
    def last_pos(self) -> tuple[int, int]:
        """Get the last known position for player"""
        if not self.actions:
            return (self.start_x, self.start_y)
        else:
            box = self.get_hitbox_at(self.time_consumed)
            return box.pos_x, box.pos_y

    @property
    def time_consumed(self) -> int:
        """How much time the player has consumed with the current actions"""
        if not self.actions:
            return 0
        else:
            return self.actions[-1].time_end
