from pydantic import BaseModel

from app import constants as const
from app.windows.core import Window, term


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

    @property
    def _content(self) -> str:
        stubs = [
            f"  {i}. {self._cmd_lookup.get(i, '')}"
            for i in range(1, self.max_commands + 1)
        ]
        return "\n".join(
            [
                term.center(
                    f"You may use {self.max_commands} commands",
                    width=self.width,
                    fillchar=" ",
                ),
                term.normal,
                "\n".join(stubs),
            ]
        )

    def __str__(self) -> str:
        window = Window(
            title="Your Plan",
            width=self.width,
            height=self.height,
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self._content,
        )
        return str(window)
