from pydantic import BaseModel

from app import constants as const
from app.windows.cmd_help import CmdHelpWindow
from app.windows.cmd_list import CmdListwindow
from app.windows.core import term
from app.windows.map import MapWindow
from app.windows.user_input import UserInputWindow


class LevelScreen(BaseModel):
    """The screen components for displaying a level"""

    map: MapWindow
    cmd_list: CmdListwindow
    cmd_help: CmdHelpWindow
    user_input: UserInputWindow

    def _render(self) -> None:
        print(term.clear)
        print(str(self.user_input))
        print(str(self.cmd_help))
        print(str(self.cmd_list))
        print(str(self.map))
        print(self.user_input.prompt, end="", flush=True)

    def launch(self) -> None:
        """Launches the level in fullscreen mode"""
        with term.fullscreen(), term.cbreak():
            self._render()
            while True:
                if key := term.inkey(timeout=1):
                    if key.code == const.BACKSPACE:
                        self.user_input.current_input = self.user_input.current_input[
                            :-1
                        ]
                    elif key.code == const.ENTER:
                        self.cmd_list.issued_commands.append(
                            self.user_input.current_input
                        )
                        self.user_input.current_input = ""
                    else:
                        self.user_input.current_input += key.lower()
                    self._render()
