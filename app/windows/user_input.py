import math

from blessed import Terminal
from pydantic import BaseModel

from app import constants as const


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

    def prompt(self, term: Terminal) -> str:
        """Draw the prompt and move cursor to right location for input"""
        x, y = self._cursor_loc
        return term.move_xy(x + 2, y) + const.PROMPT_LINE + self.current_input

    def content_lines(self, term: Terminal) -> list[str]:
        """Return content lines to be drawn"""
        base = [
            term.center(
                term.bold(term.on_yellow("What's your next command?")),
                width=self.width,
                fillchar=" ",
            ),
            "",
        ]
        return base
