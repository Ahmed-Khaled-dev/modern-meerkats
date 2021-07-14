from app.collisions import find_collisions, handle_collision
from app.entities.exit import Exit
from app.entities.player import Player
from app.types.hitbox import HitBox
from app.types.state import LevelState


def test_collisions_are_detected() -> None:
    """Test that given a list of hitboxes all collisions are identified correctly"""
    b1 = HitBox(pos_y=0, pos_x=0, content="", parent=str, time=0)
    b2 = HitBox(pos_y=0, pos_x=0, content="", parent=int, time=0)
    b3 = HitBox(pos_y=0, pos_x=1, content="", parent=str, time=0)
    assert find_collisions([b1, b2, b3]) == [(b1, b2)]


def test_collision_player_exit() -> None:
    """Test that the state is set to win when the player reaches a door"""
    b1 = HitBox(pos_y=0, pos_x=0, content="", parent=Player, time=0)
    b2 = HitBox(pos_y=0, pos_x=0, content="", parent=Exit, time=0)
    _, state = handle_collision((b1, b2), [], LevelState.Execution)
    assert state == LevelState.Win
