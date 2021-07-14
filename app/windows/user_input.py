import math

from pydantic import BaseModel

from app import constants as const
from app.windows.core import Window, term

PROMPT_LINE = "  >> "


class UserInputWindow(BaseModel):
    """Window for dealing with user input"""

    width: int = const.INPUT_WIDTH
    height: int = const.INPUT_HEIGHT
    pos_x: int = const.INPUT_X
    pos_y: int = const.INPUT_Y
    current_input: str = ""

    @property
    def _cursor_loc(self) -> tuple[int, int]:
        row = self.pos_y + math.ceil(self.height / 2)
        return self.pos_x, row

    @property
    def prompt(self) -> str:
        """Draw the prompt and move cursor to right location for input"""
        x, y = self._cursor_loc
        return term.move_xy(x + 2, y) + PROMPT_LINE + self.current_input

    @property
    def _content(self) -> str:
        return "\n".join(
            [
                term.center(
                    "What's your next command?", width=self.width, fillchar=" "
                ),
                "\n",
            ]
        )

    @property
    def window(self) -> Window:
        """Return the window user input"""
        return Window(
            title="Input",
            width=self.width,
            height=self.height,
            pos_x=self.pos_x,
            pos_y=self.pos_y,
            content=self._content,
        )
