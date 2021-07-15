import string
from typing import Iterable

from blessed import Terminal
from pydantic import BaseModel

from app import constants as const
from app.actions import Action, action_from_str
from app.entities import Exit, Player, Wall
from app.types.commands import Command
from app.types.events import Event
from app.types.hitbox import HitBox
from app.types.state import LevelState
from app.windows.cmd_help import CmdHelpWindow
from app.windows.cmd_list import CmdListwindow
from app.windows.map import MapWindow
from app.windows.user_input import UserInputWindow


class Level(BaseModel):
    """All components needed to track state and render a level"""

    title: str
    number: int
    max_commands: int
    description: str
    player: Player
    entities: list
    allowed_commands: list[Command]
    state: dict[int, LevelState] = {0: LevelState.Planning}
    current_input: str = ""
    current_time: int = 0

    @property
    def current_state(self) -> LevelState:
        """Get current state based on current time"""
        return self.state.get(self.current_time, LevelState.Planning)

    @property
    def map_initial(self) -> MapWindow:
        """Generate the initial map window"""
        entity_boxes = self.get_boxes_at(0)
        return MapWindow(
            level_name=self.title, level_number=self.number, boxes=entity_boxes
        )

    def get_boxes_at(self, time: int) -> list[HitBox]:
        """Get all hitboxes for a given time"""
        return [self.player.get_hitbox_at(time)] + [
            e.get_hitbox_at(time) for e in self.entities
        ]

    def get_collisions_at(self, time: int) -> Iterable[tuple[HitBox, HitBox]]:
        """Identify all collisions at a given time"""
        boxes = self.get_boxes_at(time)
        table = {}
        for box in boxes:
            key = (box.pos_x, box.pos_y)
            if key not in table:
                table[key] = box
            else:
                yield table[key], box

    def handle_collisions_at(self, time: int) -> None:
        """Update level state for all collisions"""
        for col in self.get_collisions_at(time):
            box_1, box_2 = col
            parents = {box_1.parent, box_2.parent}
            if parents == {Player, Exit}:
                self.state[box_1.time] = LevelState.Win
            elif parents == {Player, Wall}:
                action = self.player.get_action_at(box_1.time)
                action.halt_times.append(box_1.time)
            else:
                pass

    @property
    def map_sequence(self) -> Iterable[MapWindow]:
        """Generate a mpawindow sequence"""
        for t in range(0, self.player.time_consumed + 1):
            self.current_time += 1
            boxes = self.get_boxes_at(t)
            if t == self.player.time_consumed:
                self.state[self.current_time] = LevelState.ExitNotReached
            yield MapWindow(
                level_name=self.title,
                level_number=self.number,
                boxes=boxes,
            )
            if self.current_state in LevelState.terminal():
                break

    @property
    def cmd_list(self) -> CmdListwindow:
        """Generate a command list window"""
        return CmdListwindow(
            max_commands=self.max_commands,
            issued_commands=[str(a) for a in self.player.actions],
        )

    @property
    def cmd_help(self) -> CmdHelpWindow:
        """Generate a command help window"""
        return CmdHelpWindow(allowed_commands=self.allowed_commands)

    @property
    def user_input(self) -> UserInputWindow:
        """Generate a user input window"""
        return UserInputWindow(current_input=self.current_input)

    def add_player_action(self, action: Action) -> None:
        """Add action to player and handle all collisions"""
        current_time = self.player.time_consumed
        self.player.actions.append(action)
        for i in range(current_time, self.player.time_consumed + 1):
            self.handle_collisions_at(i)

    def listen(self, term: Terminal) -> list[Event]:
        """Listen and handle keyboard events"""
        if key := term.inkey():
            if key.code == const.BACKSPACE:
                self.current_input = self.current_input[:-1]
                return [Event.UpdateInput]
            elif key.code == const.ENTER:
                action = action_from_str(self.current_input, self.player)
                self.add_player_action(action)
                self.current_input = ""
                return [Event.UpdateCmdList, Event.UpdateInput]
            elif key.code == const.DEBUG_KEY:
                return [Event.StartSequence, Event.EndLevel]
            elif (
                key.lower() in string.ascii_letters
                or key in string.digits
                or key == " "
            ) and len(self.current_input) < const.INPUT_MAX_LENGTH:
                self.current_input += key.lower()
                return [Event.UpdateInput]

        return []
