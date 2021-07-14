from app.entities.exit import Exit
from app.entities.player import Player
from app.types.hitbox import HitBox
from app.types.state import LevelState


def find_collisions(boxes: list[HitBox]) -> list[tuple[HitBox, HitBox]]:
    """Given a list of timed hitboxes, identify all pairs of collisions"""
    collisions = []
    table = {}
    for box in boxes:
        key = (box.pos_x, box.pos_y)
        if key not in table:
            table[key] = box
        else:
            collisions.append((table[key], box))
    return collisions


def handle_collision(
    collision: tuple[HitBox, HitBox], context: list[HitBox], state: LevelState
) -> tuple[list["HitBox"], LevelState]:
    """Determine what state to emit and how to change the context based on the collision"""
    box_1, box_2 = collision
    if {box_1.parent, box_2.parent} == {Player, Exit}:
        return context, LevelState.Win
    else:
        return context, state
