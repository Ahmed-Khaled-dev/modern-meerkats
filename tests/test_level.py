import pytest
from blessed import Terminal

from app.actions import action_from_str
from app.entities import MovingWall, Player, Wall
from app.levels import Level


@pytest.fixture
def level_empty():
    return Level(
        title="",
        number=0,
        max_commands=3,
        description="",
        player=Player(start_x=1, start_y=1),
        entities=[],
        allowed_commands=[],
    )


def test_level_can_generate_initial_map_window(level_empty):
    assert level_empty.map_initial


def test_level_handles_collision_adequately_player_action_add():
    level = Level(
        title="",
        number=0,
        max_commands=3,
        description="",
        player=Player(start_x=1, start_y=1),
        entities=Wall.create_line(3, 1, 5, "v"),
        allowed_commands=[],
        term=Terminal(),
    )
    action = action_from_str("move 5 right", level.player)
    level.player.actions.append(action)
    level.resolve_collisions()
    assert level.player.actions[0].halt_times


def test_level_handles_collisions_for_moving_walls():
    wall = MovingWall(start_x=2, start_y=1, actions=[])
    wall_move = action_from_str("move 1 down", wall)
    wall.actions.append(wall_move)
    level = Level(
        title="",
        number=0,
        max_commands=3,
        description="",
        player=Player(start_x=1, start_y=2),
        entities=[wall],
        allowed_commands=[],
        term=Terminal(),
    )
    level.player.actions.append(action_from_str("move 1 right", level.player))
    level.resolve_collisions()
    level.player.actions.append(action_from_str("move 1 right", level.player))
    level.resolve_collisions()
    assert level.player.actions[0].halt_times
    assert not level.player.actions[1].halt_times
