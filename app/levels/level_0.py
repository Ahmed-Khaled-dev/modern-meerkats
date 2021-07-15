import itertools

from app.entities import Exit, Player, Wall
from app.types.commands import Command as Cmd

from . import Level


def Level0() -> Level:
    """Generate Level0 instance"""
    return Level(
        title="Test Level",
        number=0,
        max_commands=7,
        description="yolo",
        player=Player(start_x=7, start_y=7),
        entities=list(
            itertools.chain(
                Wall.create_line(5, 5, 15, "h"),
                Wall.create_line(5, 5, 5, "v"),
                Wall.create_line(20, 5, 5, "v"),
                Wall.create_line(5, 10, 7, "h"),
                [Exit(pos_x=16, pos_y=7)],
            )
        ),
        allowed_commands=[Cmd.Move],
    )
