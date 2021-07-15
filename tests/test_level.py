import pytest

from app.actions import action_from_str
from app.entities import Player, Wall
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


@pytest.fixture
def level_with_walls():
    return Level(
        title="",
        number=0,
        max_commands=3,
        description="",
        player=Player(start_x=1, start_y=1),
        entities=Wall.create_line(3, 1, 5, "v"),
        allowed_commands=[],
    )


def test_level_can_generate_initial_map_window(level_empty):
    assert level_empty.map_initial


def test_level_handles_collision_adequately_player_action_add(level_with_walls):
    level = level_with_walls
    action = action_from_str("move 5 right", level.player)
    level.add_player_action(action)
    assert level.player.actions[0].halt_times
