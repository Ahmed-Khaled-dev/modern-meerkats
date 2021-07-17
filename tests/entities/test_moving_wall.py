from blessed import Terminal

from app.actions import action_from_str
from app.entities import MovingWall


def test_moving_wall_get_action_returns_correct_value_for_reverse():
    wall = MovingWall(
        start_x=1,
        start_y=1,
    )
    a1 = action_from_str("move 2 down", wall)
    wall.actions.append(a1)
    a2 = action_from_str("move 1 down", wall)
    wall.actions.append(a2)
    assert wall.loop_interval == 3
    assert wall.last_pos == (1, 4)
    get_pos = lambda x: (x.pos_x, x.pos_y)
    get_res = lambda x: get_pos(wall.get_hitbox_at(x))
    assert get_res(1) == (1, 2)
    assert get_res(2) == (1, 3)
    assert get_res(3) == (1, 4)
    assert get_res(4) == (1, 3)
    assert get_res(5) == (1, 2)


def test_moving_wall_moving_wall_generates_correct_hitboxes():
    term = Terminal()

    wall = MovingWall(
        start_x=1,
        start_y=1,
    )
    action = action_from_str("move 2 down", wall)
    wall.actions.append(action)
    box_1 = wall.get_hitbox_at(1, term)
    assert (box_1.pos_x, box_1.pos_y) == (1, 2)
    box_2 = wall.get_hitbox_at(2, term)
    assert (box_2.pos_x, box_2.pos_y) == (1, 3)
    box_3 = wall.get_hitbox_at(3, term)
    assert (box_3.pos_x, box_3.pos_y) == (1, 2)


def test_moving_wall_with_multiple_actions_generates_correct_hitboxes():
    term = Terminal()
    wall = MovingWall(
        start_x=1,
        start_y=1,
    )
    a1 = action_from_str("move 2 down", wall)
    wall.actions.append(a1)
    assert wall.last_pos == (1, 3)
    a2 = action_from_str("move 2 right", wall)
    wall.actions.append(a2)
    assert wall.last_pos == (3, 3)
    get_pos = lambda x: (x.pos_x, x.pos_y)
    get_res = lambda x: get_pos(wall.get_hitbox_at(x, term))
    assert get_res(0) == (1, 1)
    assert get_res(1) == (1, 2)
    assert get_res(2) == (1, 3)
    assert get_res(3) == (2, 3)
    assert get_res(4) == (3, 3)
    assert get_res(5) == (2, 3)
    assert get_res(6) == (1, 3)
    assert get_res(7) == (1, 2)
    assert get_res(8) == (1, 1)
    assert get_res(9) == (1, 2)
