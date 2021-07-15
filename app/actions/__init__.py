import itertools
from typing import Protocol, Union

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


def action_from_str(user_input: str, entity: ActionableEntity) -> Action:
    """Derive an action from a user string"""
    cmd, _, tail = user_input.partition(" ")
    if cmd == "move":
        length, _, orientation = tail.partition(" ")
        haltbable_actions = (x for x in entity.actions if hasattr(x, "halt_times"))
        if orientation in ("left", "right"):
            oriented_halts = list(
                itertools.chain(
                    *[
                        x.halt_times
                        for x in haltbable_actions
                        if x.orientation in ("left", "right")
                    ]
                )
            )
        else:
            oriented_halts = list(
                itertools.chain(
                    *[
                        x.halt_times
                        for x in haltbable_actions
                        if x.orientation in ("up", "down")
                    ]
                )
            )
        x, y = entity.last_pos
        return Move(
            pos_x=x,
            pos_y=y,
            length=int(length),
            time_start=entity.time_consumed + 1,
            orientation=orientation,
            parent=entity.__class__,
            content=str(entity),
            halt_times=oriented_halts,
        )
    else:
        raise ValueError
