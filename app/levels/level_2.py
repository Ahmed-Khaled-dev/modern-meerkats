import itertools

from app.actions import Move
from app.entities import Exit, MovingWall, Player, Wall

from . import Level


def Level2() -> Level:
    """Render the second level"""
    return Level(
        title="The Parkour Terminal",
        number=2,
        max_commands=15,
        description="This is another level with moving walls but with some parkour",
        player=Player(start_x=8, start_y=36),
        entities=list(
            itertools.chain(
                # Start X Pos, Start Y Pos, Length, Orientation
                # Left row - Top
                Wall.create_line(1, 1, 88, "h"),
                # Left coloumn
                Wall.create_line(1, 1, 38, "v"),
                # Middle row - Top
                Wall.create_line(15, 8, 74, "h"),
                # Middle coloumn - Left
                Wall.create_line(15, 9, 30, "v"),
                # Right coloumn - Small
                Wall.create_line(88, 1, 8, "v"),
                # Botton row - left
                Wall.create_line(1, 38, 14, "h"),
                # Small top walls
                Wall.create_line(16, 1, 5, "v"),
                Wall.create_line(26, 4, 5, "v"),
                Wall.create_line(36, 1, 5, "v"),
                Wall.create_line(46, 4, 5, "v"),
                Wall.create_line(56, 1, 5, "v"),
                Wall.create_line(66, 4, 5, "v"),
                # First Horizontal moving walls
                MovingWall.create_line(
                    start_x=1,
                    start_y=19,
                    actions=["move 10 right", "move 10 left"],
                    length=5,
                    orientation="h"
                ),
                MovingWall.create_line(
                    start_x=11,
                    start_y=24,
                    actions=["move 10 left", "move 10 right"],
                    length=5,
                    orientation="h"
                ),
                MovingWall.create_line(
                    start_x=1,
                    start_y=29,
                    actions=["move 10 right", "move 10 left"],
                    length=5,
                    orientation="h"
                ),
                [Exit(pos_x=78, pos_y=4)],
            )
        ),
        allowed_commands=[Move],
    )
