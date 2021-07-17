from typing import Protocol, Union

from app import constants as const

from .move import Move

Action = Union[Move]


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


def action_from_str(user_input: str, entity: ActionableEntity) -> tuple[Action, bool]:
    """Derive an action from a user string"""
    cmd, _, tail = user_input.partition(" ")
    if user_input in const.VALID_COMMANDS:
        length, _, orientation = tail.partition(" ")
        x, y = entity.last_pos
        return Move(
            pos_x=x,
            pos_y=y,
            length=int(length),
            time_start=entity.time_consumed + 1,
            orientation=orientation,
            parent=entity.__class__,
            content=str(entity),
        ), True
    else:
        return None, False
