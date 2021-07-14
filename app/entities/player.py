import itertools
from typing import Literal, Union

from pydantic import BaseModel

from app.types.actions import Move
from app.types.hitbox import HitBox

Action = Union[Move]


class Player(BaseModel):
    """The player entity model"""

    start_x: int
    start_y: int
    actions: list[Action]

    def __str__(self) -> str:
        return "🧛"

    @property
    def _last_pos(self) -> tuple[int, int]:
        if not self.actions:
            return (self.start_x, self.start_y)
        else:
            last_move = [x for x in self.actions if isinstance(x, Move)][-1]
            return last_move.moves[-1]

    def add_move(
        self, length: int, orientation: Literal["up", "down", "left", "right"]
    ) -> None:
        """Add a move action for the player"""
        x, y = self._last_pos
        t = self.actions[-1].time_end if self.actions else 0
        action = Move(
            pos_x=x,
            pos_y=y,
            length=length,
            time_start=t,
            orientation=orientation,
            parent=Player,
            content=str(self),
        )
        self.actions.append(action)

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

    @property
    def time_consumed(self) -> int:
        """How much time the player has consumed with the current actions"""
        if not self.actions:
            return 0
        else:
            return self.actions[-1].time_end

    def to_hitbox(self) -> list[HitBox]:
        """Convert Entity to hitboxes"""
        steps = itertools.chain(*[a.hitboxes for a in self.actions])
        return [self.initial] + list(steps)
