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

    @property
    def moves(self) -> list[tuple[int, int]]:
        """List of coordinates traversed"""
        moves = []
        for i in range(1, self.length + 1):
            if self.orientation == "up":
                moves.append((self.pos_x, self.pos_y - i))
            elif self.orientation == "down":
                moves.append((self.pos_x, self.pos_y + i))
            elif self.orientation == "left":
                moves.append((self.pos_x - i, self.pos_y))
            elif self.orientation == "right":
                moves.append((self.pos_x + i, self.pos_y))
        return moves

    @property
    def hitboxes(self) -> list[HitBox]:
        """List of time hitboxes derived from the move"""
        return [
            HitBox(pos_x=x, pos_y=y, content=self.content, time=i, parent=self.parent)
            for i, (x, y) in enumerate(self.moves, start=self.time_start)
        ]

    @property
    def time_end(self) -> int:
        """The end time for the given action"""
        return self.time_start + self.length
