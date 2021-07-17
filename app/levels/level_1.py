import itertools

from app.actions import Move
from app.entities import Exit, MovingWall, Player, Wall

from . import Level


def Level1() -> Level:
    """Render the second level"""
    return Level(
        title="The Moving Terminal",
        number=1,
        max_commands=7,
        description="This is a level that introduces moving walls to the user",
        player=Player(start_x=6, start_y=33),
        entities=list(
            itertools.chain(
                # Start X Pos, Start Y Pos, Length, Orientation
                # Right coloumn
                Wall.create_line(88, 1, 38, "v"),
                # Right row - Top
                Wall.create_line(74, 1, 15, "h"),
                # Left small coloumn
                Wall.create_line(1, 28, 10, "v"),
                # Middle coloumn - Right
                Wall.create_line(73, 1, 28, "v"),
                # Middle row
                Wall.create_line(1, 28, 73, "h"),
                # Bottom row - Big
                Wall.create_line(1, 38, 88, "h"),
                # Vertical moving walls in the bottom
                MovingWall.create_line(
                    start_x=20,
                    start_y=28,
                    actions=["move 6 down", "move 6 up"],
                    length=4,
                    orientation="v"),
                MovingWall.create_line(
                    start_x=35,
                    start_y=35,
                    actions=["move 6 up", "move 6 down"],
                    length=4,
                    orientation="v"
                ),
                MovingWall.create_line(
                    start_x=45,
                    start_y=28,
                    actions=["move 6 down", "move 6 up"],
                    length=4,
                    orientation="v"
                ),
                MovingWall.create_line(
                    start_x=60,
                    start_y=35,
                    actions=["move 6 up", "move 6 down"],
                    length=4,
                    orientation="v"
                ),
                MovingWall.create_line(
                    start_x=70,
                    start_y=28,
                    actions=["move 6 down", "move 6 up"],
                    length=4,
                    orientation="v"
                ),
                # Horizontal moving walls on the right
                MovingWall.create_line(
                    start_x=74,
                    start_y=24,
                    actions=["move 10 right", "move 10 left"],
                    length=4,
                    orientation="h"
                ),
                MovingWall.create_line(
                    start_x=84,
                    start_y=19,
                    actions=["move 10 left", "move 10 right"],
                    length=4,
                    orientation="h"
                ),
                MovingWall.create_line(
                    start_x=74,
                    start_y=14,
                    actions=["move 10 right", "move 10 left"],
                    length=4,
                    orientation="h"
                ),
                MovingWall.create_line(
                    start_x=84,
                    start_y=9,
                    actions=["move 10 left", "move 10 right"],
                    length=4,
                    orientation="h"
                ),
                [Exit(pos_x=80, pos_y=3)],
            )
        ),
        allowed_commands=[Move],
    )
