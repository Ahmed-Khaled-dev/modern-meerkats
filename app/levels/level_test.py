import itertools

from pydantic import BaseModel

from app.entities.player import Player
from app.entities.static import Wall
from app.types.hitbox import HitBox
from app.windows.map import MapWindow


class TestLevel(BaseModel):
    """A stub level for testing new stuff"""

    level_number = 0
    level_name = "Test"

    def entities(self, player: Player) -> dict[int, list[HitBox]]:
        """Entity lookup table of time to hitbox list"""
        walls = itertools.chain(
            Wall.create_line(5, 5, 15, "h"),
            Wall.create_line(5, 5, 5, "v"),
            Wall.create_line(20, 5, 5, "v"),
            Wall.create_line(5, 10, 7, "h"),
        )
        wall_boxes = itertools.chain(*[x.to_hitbox(len(player.moves)) for x in walls])
        entity_table = {}
        for b in wall_boxes:
            if b.time not in entity_table:
                entity_table[b.time] = [b]
            else:
                entity_table[b.time].append(b)
        return entity_table

    def initial(self, player: Player) -> MapWindow:
        """Initial level state"""
        boxes = self.entities(player).get(0, [])
        boxes.append(player.initial)
        return MapWindow(
            level_name=self.level_name, level_number=self.level_number, boxes=boxes
        )

    def sequence(self, player: Player) -> list[MapWindow]:
        """Sequence of animations"""
        entity_table = self.entities(player)
        for box in player.to_hitbox():
            if box.time in entity_table:
                entity_table[box.time].append(box)
            else:
                entity_table[box.time] = [box]
        windows = []
        for i in range(0, max(entity_table.keys())):
            windows.append(
                MapWindow(
                    level_name=self.level_name,
                    level_number=self.level_number,
                    boxes=entity_table.get(i, []),
                )
            )
        return windows
