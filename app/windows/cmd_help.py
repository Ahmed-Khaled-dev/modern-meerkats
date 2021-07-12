from pydantic import BaseModel

from app import constants as const
from app.types.commands import Command as Cmd
from app.windows.core import Window, term


class CmdHelpWindow(BaseModel):
    """Window for displaying helpful information to player about commands"""

    allowed_commands: list[Cmd]
    width: int = const.CMDHELP_WIDTH
    height: int = const.CMDHELP_HEIGHT
    pos_x: int = const.CMDHELP_X
    pos_y: int = const.CMDHELP_Y

    @property
    def _content(self) -> str:
        return "\n".join(
            [
                term.center(
                    "The available commands are:",
                    width=self.width,
                    fillchar=" ",
                ),
                "\n",
                "\n".join(
                    [
                        term.center(c.value, width=self.width, fillchar=" ")
                        for c in self.allowed_commands
                    ]
                ),
            ]
        )

    def __str__(self) -> str:
        window = Window(
            title="Help",
            width=self.width,
            height=self.height,
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self._content,
        )
        return str(window)
