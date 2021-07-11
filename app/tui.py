from enum import Enum
from typing import Optional

import blessed
from pydantic import BaseModel

term = blessed.Terminal()


class Border(Enum):
    """Tokens for window borders"""

    TopL = "┌"
    TopR = "┐"
    BotL = "└"
    BotR = "┘"
    Horizontal = "─"
    Vertical = "│"

    def __str__(self) -> str:
        return self.value


class Position(BaseModel):
    """A position in the terminal defined by the row (y) and column (x)"""

    x: int
    y: int


class Window(BaseModel):
    """A bordered box with content"""

    title: str
    width: int  # in columns
    height: int  # in rows
    pos: Position
    content: Optional[str] = None

    def _wrap_body_line(self, content: Optional[str]) -> str:
        if not content:
            line = " " * self.width
        else:
            fill_len = self.width - len(content)
            line = content + (" " * fill_len)
        return f"{Border.Vertical.value}{line}{Border.Vertical.value}"

    @property
    def _content_lines(self) -> dict[int, str]:
        if not self.content:
            return {}
        return {
            index: line for index, line in enumerate(self.content.split("\n"), start=1)
        }

    @property
    def _border_top(self) -> str:
        line = term.center(
            term.bold(self.title), width=self.width, fillchar=Border.Horizontal.value
        )
        wrapped = f"{Border.TopL.value}{line}{Border.TopR.value}"
        return f"{term.move_xy(self.pos.x, self.pos.y)}{wrapped}"

    @property
    def _border_bot(self) -> str:
        wrapped = f"{Border.BotL.value}{self.width * str(Border.Horizontal.value)}{Border.BotR.value}"
        return f"{term.move_xy(self.pos.x, self.pos.y + self.height + 1)}{wrapped}"

    @property
    def _body(self) -> str:
        lines = self._content_lines
        res = []
        for index in range(1, self.height + 1):
            wrapped = self._wrap_body_line(lines.get(index))
            line = f"{term.move_xy(self.pos.x, self.pos.y + index)}{wrapped}"
            res.append(line)
        return "".join(res)

    def __str__(self) -> str:
        return "".join([self._border_top, self._border_bot, self._body])


class Screen(BaseModel):
    """Collection of windows that form the game screen"""

    user_input: Window
    commands: Window
    map_area: Window
    available_commands: Window

    def __str__(self) -> str:
        screen = "".join(
            [
                term.clear,
                str(self.map_area),
                str(self.commands),
                str(self.available_commands),
                str(self.user_input),
                "\n",
            ]
        )
        return screen

    def draw(self) -> None:
        """Draw all windows to screen"""
        print(str(self))
