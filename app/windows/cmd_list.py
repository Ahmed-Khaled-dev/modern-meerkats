from blessed import Terminal
from pydantic import BaseModel

from app import constants as const


class CmdListwindow(BaseModel):
    """Window for displaying lal issued commands"""

    max_commands: int
    width: int = const.CMDLIST_WIDTH
    height: int = const.CMDLIST_HEIGHT
    pos_x: int = const.CMDLIST_X
    pos_y: int = const.CMDLIST_Y
    issued_commands: list[str] = []

    @property
    def _cmd_lookup(self) -> dict[int, str]:
        return {index + 1: cmd for index, cmd in enumerate(self.issued_commands)}

    def content_lines(self, term: Terminal) -> list[str]:
        """Return content lines to be rendered"""
        base = [
            term.center(
                f"You may use {self.max_commands} commands",
                width=self.width,
                fillchar=" ",
            ),
            "",
            "",
        ]
        stubs = [
            f"  {i}. {self._cmd_lookup.get(i, '')}"
            for i in range(1, self.max_commands + 1)
        ]
        return base + stubs
