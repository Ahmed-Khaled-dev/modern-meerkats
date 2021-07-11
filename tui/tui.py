from blessed import Terminal


class TUI(Terminal):
    """A subclass of `blessed.Terminal` implementing custom functionality for the project's TUI."""

    def __init__(self):
        super().__init__()

    def print_table(self, width: int = 111, height: int = 33) -> None:
        """Prints the custom TUI table to the terminal.

        Parameters
        ----------
        width : int, optional
            Inner (i.e. excluding the borders) width of the table
        height : int, optional
            Inner (i.e. excluding the borders) height of the table
        """
        print(self.tomato, self.clear, end="")

        title = self.center("Modern Meerkats", width=width + 2, fillchar=" ")
        top_border = f"┌{self.center('┬', width=width, fillchar='─')}┐"
        regular_row = f"│{self.center('│', width=width, fillchar=' ')}│"
        horizontal_border_row = (
            f"│{self.rjust('├', width=width // 2 + 1, fillchar=' ')}"
            + f"{'─' * (width // 2)}┤"
        )  # Row with the border between input history and user input
        bottom_border = f"└{self.center('┴', width=width, fillchar='─')}┘"

        print(title)
        print(top_border)
        for row_index in range(height):
            if row_index == height - height // 4 - 1:
                print(horizontal_border_row)
            else:
                print(regular_row)
        print(bottom_border, self.normal)
