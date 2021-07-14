import string
import time

from pydantic import BaseModel

from app import constants as const
from app.collisions import find_collisions, handle_collision
from app.entities.player import Player
from app.levels.level_test import TestLevel
from app.types.state import LevelState
from app.windows.cmd_help import CmdHelpWindow
from app.windows.cmd_list import CmdListwindow
from app.windows.core import term
from app.windows.map import MapWindow
from app.windows.user_input import UserInputWindow


class LevelScreen(BaseModel):
    """The screen components for displaying a level"""

    level: TestLevel
    player: Player
    cmd_list: CmdListwindow
    cmd_help: CmdHelpWindow
    user_input: UserInputWindow
    state: LevelState = LevelState.Planning

    @property
    def map(self) -> MapWindow:
        """Return the initial map window"""
        return self.level.initial(self.player)

    def _render_initial(self) -> None:
        print(term.clear)
        print(self.user_input.window.border)
        print(self.user_input.window.body)
        print(self.cmd_help.window.border)
        print(self.cmd_help.window.body)
        print(self.cmd_list.window.border)
        print(self.cmd_list.window.body)
        print(self.map.window.border)
        print(self.map.window.body)
        print(self.map.content)
        print(self.user_input.prompt, end="", flush=True)

    def _execute(self) -> None:
        seq = self.level.sequence(self.player)
        for w in seq:
            collisions = find_collisions(w.boxes)
            for col in collisions:
                new_boxes, new_state = handle_collision(col, w.boxes, self.state)
                w.boxes = new_boxes
                self.state = new_state
            print(w.window.body)
            print(w.content)
            if self.state in (LevelState.Win, LevelState.ExitNotReached):
                break

            time.sleep(0.2)

    def launch(self) -> None:
        """Launches the level in fullscreen mode"""
        with term.fullscreen(), term.cbreak():
            self._render_initial()
            while self.state not in (LevelState.Win, LevelState.ExitNotReached):
                if key := term.inkey():
                    if key.code == const.BACKSPACE:
                        self.user_input.current_input = self.user_input.current_input[
                            :-1
                        ]
                        print(self.user_input.window.body)
                    elif key.code == const.ENTER:
                        self.cmd_list.issued_commands.append(
                            self.user_input.current_input
                        )
                        self.user_input.current_input = ""
                        print(self.cmd_list.window.body)
                        print(self.user_input.window.body)
                    elif key.code == const.DEBUG_KEY:
                        with term.hidden_cursor():
                            self._execute()
                    elif (
                        key.lower() in string.ascii_letters or key in string.digits
                    ) and len(self.user_input.current_input) < const.INPUT_MAX_LENGTH:
                        self.user_input.current_input += key.lower()
                        print(self.user_input.window.body)
                    print(self.user_input.prompt, end="", flush=True)
            if self.state == LevelState.Win:
                print("you win")
            else:
                print("you lose")
            while True:
                pass
