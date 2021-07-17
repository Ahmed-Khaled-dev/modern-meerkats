from typing import Type

from blessed import Terminal
from pydantic import BaseModel

from app import constants as const
from app.actions import Action


class CmdHelpWindow(BaseModel):
    """Window for displaying helpful information to player about commands"""

    allowed_commands: list[Type[Action]]
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
            term.center(c.name(), width=self.width, fillchar=" ")
            for c in self.allowed_commands
        ]
        header = [
            "",
            "",
            term.center(
                f"{term.orangered('SYNTAX')}/{term.yellow('EXAMPLE')}",
                width=self.width,
                fillchar=" ",
            ),
            "",
        ]
        syntax = []

        for c in self.allowed_commands:
            syntax += [
                term.center(x, width=self.width, fillchar=" ") for x in c.usage()
            ] + [""]

        return base + commands + header + syntax
