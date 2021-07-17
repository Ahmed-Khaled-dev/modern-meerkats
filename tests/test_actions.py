from app.actions import Move


def test_move_get_at_yields_correct_hitbox():
    move_r = Move(
        pos_x=1,
        pos_y=1,
        length=4,
        time_start=1,
        orientation="right",
        parent=str,
        content="blah",
    )
    assert move_r.get_hitbox_at(1).pos_x == 2
    assert move_r.get_hitbox_at(2).pos_x == 3
    move_d = Move(
        pos_x=1,
        pos_y=1,
        length=4,
        time_start=1,
        orientation="down",
        parent=str,
        content="blah",
    )
    assert move_d.get_hitbox_at(0).pos_y == 1
    assert move_d.get_hitbox_at(1).pos_y == 2
    assert move_d.get_hitbox_at(2).pos_y == 3


def test_move_halt_return_correct_position():
    move_r = Move(
        pos_x=1,
        pos_y=1,
        length=5,
        time_start=1,
        orientation="right",
        parent=str,
        content="blah",
        halt_times=[3, 4],
    )
    assert move_r.get_hitbox_at(0).pos_x == 1
    assert move_r.get_hitbox_at(1).pos_x == 2
    assert move_r.get_hitbox_at(2).pos_x == 3
    assert move_r.get_hitbox_at(3).pos_x == 3
    assert move_r.get_hitbox_at(4).pos_x == 3
    assert move_r.get_hitbox_at(5).pos_x == 4
