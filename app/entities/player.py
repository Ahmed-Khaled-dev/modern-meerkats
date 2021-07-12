from typing import Literal

from pydantic import BaseModel

from app.types.hitbox import HitBox


class Player(BaseModel):
    """The player entity model"""

    start_x: int
    start_y: int
    moves: list[tuple[int, int]]

    def __str__(self) -> str:
        return "🧛"

    @property
    def _last_pos(self) -> tuple[int, int]:
        if not self.moves:
            return (self.start_x, self.start_y)
        else:
            return self.moves[-1]

    def add_move(self, length: int, orientation: Literal["l", "r", "u", "d"]) -> None:
        """Append a move to the player move list"""
        for _ in range(0, length):
            x, y = self._last_pos
            if orientation == "u":
                self.moves.append((x, y - 1))
            elif orientation == "d":
                self.moves.append((x, y + 1))
            elif orientation == "l":
                self.moves.append((x - 1, y))
            elif orientation == "r":
                self.moves.append((x + 1, y))

    @property
    def initial(self) -> HitBox:
        """Initial state of the player"""
        return HitBox(pos_x=self.start_x, pos_y=self.start_y, content=str(self), time=0)

    def to_hitbox(self) -> list[HitBox]:
        """Convert Entity to hitboxes"""
        steps = [
            HitBox(pos_x=x, pos_y=y, content=str(self), time=i)
            for i, (x, y) in enumerate(self.moves, start=1)
        ]
        return [self.initial] + steps
