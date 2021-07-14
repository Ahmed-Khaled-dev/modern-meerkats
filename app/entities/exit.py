from pydantic import BaseModel

from app.types.hitbox import HitBox


class Exit(BaseModel):
    """Entity for player exit denoting end of level"""

    pos_x: int
    pos_y: int

    def __str__(self) -> str:
        return "🚪"

    def to_hitbox(self, time: int) -> list[HitBox]:
        """Convert entity to list of hitboxes"""
        return [
            HitBox(
                pos_x=self.pos_x,
                pos_y=self.pos_y,
                content=str(self) if t > 0 else str(self) + "<-- exit",
                time=t,
                parent=self.__class__,
            )
            for t in range(0, time)
        ]
