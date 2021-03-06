from typing import Optional, Protocol, Union

from .move import Move
from .wait import Wait

Action = Union[Move, Wait]


class ActionableEntity(Protocol):
    """Protocol for entities that can perform actions"""

    actions: list[Action]

    @property
    def time_consumed(self) -> int:
        """Amount of time entity has consumed"""
        ...

    @property
    def last_pos(self) -> tuple[int, int]:
        """Last entity position"""
        ...


def action_from_str(
    user_input: str, entity: ActionableEntity
) -> tuple[Optional[Action], bool]:
    """Derive an action from a user string"""
    cmd, _, tail = user_input.partition(" ")
    if cmd == "move":
        length, _, orientation = tail.partition(" ")
        x, y = entity.last_pos
        return (
            Move(
                pos_x=x,
                pos_y=y,
                length=int(length),
                time_start=entity.time_consumed + 1,
                orientation=orientation,
                parent=entity.__class__,
                content=str(entity),
            ),
            True,
        )
    elif cmd == "wait":
        x, y = entity.last_pos
        return (
            Wait(
                pos_x=x,
                pos_y=y,
                length=int(tail),
                parent=entity.__class__,
                time_start=entity.time_consumed + 1,
                content=str(entity),
            ),
            True,
        )
    else:
        return None, False
