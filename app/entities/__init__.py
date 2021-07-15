from typing import Union

from .exit import Exit
from .player import Player
from .wall import Wall

Entity = Union[Exit, Player, Wall]
ActionableEntity = Union[Player]
