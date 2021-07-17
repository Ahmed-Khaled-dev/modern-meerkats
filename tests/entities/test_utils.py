from app.entities.utils import get_loop_time


def test_get_loop_time_returns_correct_time_value():
    assert get_loop_time(2, 0) == 0
    assert get_loop_time(2, 1) == 1
    assert get_loop_time(2, 2) == 2
    assert get_loop_time(2, 3) == 1
    assert get_loop_time(2, 4) == 0
    assert get_loop_time(2, 5) == 1
    assert get_loop_time(2, 6) == 2
