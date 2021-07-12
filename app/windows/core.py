from enum import Enum
from typing import Optional

from blessed import Terminal
from pydantic import BaseModel

term = Terminal()


class Border(Enum):
    """Tokens for window borders"""

    TopL = "┌"
    TopR = "┐"
    BotL = "└"
    BotR = "┘"
    JoinTop = "┬"
    JoinBot = "┴"
    Horizontal = "─"
    Vertical = "│"


class Window(BaseModel):
    """A bordered window with content"""

    title: str
    width: int
    height: int
    pos_x: int
    pos_y: int
    content: Optional[str]
    border_color: str = term.tomato

    def _wrap_body_line(self, content: Optional[str]) -> str:
        if not content:
            line = " " * self.width
        else:
            fill_len = self.width - len(content)
            line = content + (" " * fill_len)
        return line

    @property
    def _content_lines(self) -> dict[int, str]:
        if not self.content:
            return {}
        return {
            index: line for index, line in enumerate(self.content.split("\n"), start=1)
        }

    @property
    def _top_border(self) -> str:
        text = term.center(
            self.title, width=self.width, fillchar=Border.Horizontal.value
        )
        wrapped = f"{Border.TopL.value}{text}{Border.TopR.value}"
        return term.move_xy(self.pos_x, self.pos_y) + wrapped

    @property
    def _bot_border(self) -> str:
        text = Border.Horizontal.value * self.width
        wrapped = f"{Border.BotL.value}{text}{Border.BotR.value}"
        return term.move_xy(self.pos_x, self.pos_y + self.height + 1) + wrapped

    @property
    def _left_border(self) -> str:
        border = ""
        for index in range(1, self.height + 1):
            border += (
                term.move_xy(self.pos_x, self.pos_y + index) + Border.Vertical.value
            )
        return border

    @property
    def _right_border(self) -> str:
        border = ""
        for index in range(1, self.height + 1):
            border += (
                term.move_xy(self.pos_x + self.width + 1, self.pos_y + index)
                + Border.Vertical.value
            )
        return border

    @property
    def _body(self) -> str:
        lines = self._content_lines
        res = []
        for index in range(1, self.height + 1):
            wrapped = self._wrap_body_line(lines.get(index))
            line = f"{term.move_xy(self.pos_x + 1, self.pos_y + index)}{wrapped}"
            res.append(line)
        return "".join(res)

    @property
    def _border(self) -> str:
        return "".join(
            [
                self.border_color,
                self._bot_border,
                self._top_border,
                self._left_border,
                self._right_border,
                term.normal,
            ]
        )

    def __str__(self) -> str:
        return self._border + self._body
