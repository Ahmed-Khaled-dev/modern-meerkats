def get_loop_time(loop_interval: int, time: int, reverse: bool = False) -> int:
    """Calculate what hitbox to get in a looped entity"""
    loop_time = time % loop_interval
    if time > loop_interval:
        return get_loop_time(loop_interval, time - loop_interval, not reverse)
    elif time == 0 or (reverse and loop_time == 0):
        return 0
    elif reverse:
        return loop_interval - loop_time
    elif time <= loop_interval:
        return time
    else:
        return loop_time
