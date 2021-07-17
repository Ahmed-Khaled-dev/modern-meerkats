import itertools

from app.entities import Exit, Player, Wall
from app.types.commands import Command as Cmd

from . import Level


def Level0() -> Level:
    return Level(
      title="Test Level",
      number=0,
      max_commands=7,
      description="yolo",
      player=Player(start_x=7, start_y=3),
      entities=list(
          itertools.chain(
              # Start X Pos, Start Y Pos, Length, Vertical (v) or Horizontal (h)
              # Left row - Top
              Wall.create_line(1, 1, 15, "h"),
              # Left coloumn
              Wall.create_line(1, 1, 38, "v"),
              # Right coloumn
              Wall.create_line(88, 1, 38, "v"),
              # Right row - Top
              Wall.create_line(74, 1, 15, "h"),
              # Middle coloumn - Right
              Wall.create_line(73, 1, 28, "v"),
              # Middle row
              Wall.create_line(16, 28, 57, "h"),
              # Middle coloumn - Left
              Wall.create_line(15, 1, 28, "v"),
              # Bottom row - Big
              Wall.create_line(1, 38, 88, "h"),
              [Exit(pos_x=80, pos_y=3)],
          )
      ),
      allowed_commands=[Cmd.Move],
  )

