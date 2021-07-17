from blessed import Terminal

from app.entities import MovingWall


def test_moving_wall_moving_wall_generates_correct_hitboxes():
    term = Terminal()
    wall = MovingWall(
        start_x=1,
        start_y=1,
        loop_interval=2,
        orientation="v",
    )
    box_0 = wall.get_hitbox_at(0, term)
    assert (box_0.pos_x, box_0.pos_y) == (1, 1)
    box_1 = wall.get_hitbox_at(1, term)
    assert (box_1.pos_x, box_1.pos_y) == (1, 2)
    box_2 = wall.get_hitbox_at(2, term)
    assert (box_2.pos_x, box_2.pos_y) == (1, 3)
    box_3 = wall.get_hitbox_at(3, term)
    assert (box_3.pos_x, box_3.pos_y) == (1, 2)
