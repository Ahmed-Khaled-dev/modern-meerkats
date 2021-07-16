from blessed import Terminal
from pydantic import BaseModel

from app import constants as const
from app.types.commands import Command as Cmd


class CmdHelpWindow(BaseModel):
    """Window for displaying helpful information to player about commands"""

    allowed_commands: list[Cmd]
    width: int = const.CMDHELP_WIDTH
    height: int = const.CMDHELP_HEIGHT
    pos_x: int = const.CMDHELP_X
    pos_y: int = const.CMDHELP_Y

    def content_lines(self, term: Terminal) -> list[str]:
        """Return content lines to be rendered"""
        base = [
            "",
            term.center(
                "The available commands are:",
                width=self.width,
                fillchar=" ",
            ),
            "",
            "",
        ]
        commands = [
            term.yellow(term.center(c.value, width=self.width, fillchar=" "))
            for c in self.allowed_commands
        ]
        syntax = [
            "",
            "",
            term.center("SYNTAX", width=self.width, fillchar=" "),
            "",
            term.center("move [distance] [direction]", width=self.width, fillchar=" ")
        ]
        return base + commands + syntax
