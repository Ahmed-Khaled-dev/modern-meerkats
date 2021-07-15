import itertools

from app.entities import Exit, Player, Wall
from app.types.commands import Command as Cmd

from . import Level

Level0 = Level(
    title="Test Level",
    number=0,
    max_commands=7,
    description="yolo",
    player=Player(start_x=7, start_y=3),
    entities=list(
        itertools.chain(
            # Start X Pos, Start Y Pos, Length, Vertical (v) or Horizontal (h)
            # Left coloumn top horizontal line
            Wall.create_line(1, 1, 15, "h"),
            # Left vertical vertical line
            Wall.create_line(1, 1, 38, "v"),
            # Bottom big horizontal line
            Wall.create_line(1, 38, 88, "h"),
            # Right vertical line
            Wall.create_line(88, 1, 38, "v"),
            # Right coloumn top horizontal line
            Wall.create_line(74, 1, 15, "h"),
            # Middle right vertical line
            Wall.create_line(73, 1, 28, "v"),
            # Middle big horizontal line
            Wall.create_line(16, 28, 57, "h"),
            # Middle left vertical line
            Wall.create_line(15, 1, 28, "v"),
            [Exit(pos_x=80, pos_y=3)],
        )
    ),
    allowed_commands=[Cmd.Move],
)
