from app.actions import Move, action_from_str
from app.entities import Player


def test_get_action_at_returns_correct_action():
    a1 = Move(
        pos_x=1,
        pos_y=1,
        length=3,
        time_start=1,
        orientation="right",
        parent=Player,
        content="a",
    )
    a2 = Move(
        pos_x=1,
        pos_y=1,
        length=3,
        time_start=5,
        orientation="right",
        parent=Player,
        content="a",
    )

    player = Player(start_x=1, start_y=1, actions=[a1, a2])
    assert player.get_action_at(4) == a1
    assert player.get_action_at(5) == a2
