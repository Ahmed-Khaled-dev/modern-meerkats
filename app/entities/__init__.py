from typing import Union

from .exit import Exit
from .moving_wall import MovingWall
from .patrol import Patrol, PatrolVision
from .player import Player
from .wall import Wall

Entity = Union[Exit, Player, Wall, MovingWall, Patrol, PatrolVision]
ActionableEntity = Union[Player, MovingWall, Patrol]
