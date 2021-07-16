from typing import Union

from .exit import Exit
from .moving_wall import MovingWall
from .player import Player
from .wall import Wall

Entity = Union[Exit, Player, Wall, MovingWall]
ActionableEntity = Union[Player]
