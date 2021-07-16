import time

from blessed import Terminal
from pydantic import BaseModel

from app.levels import Level
from app.types.events import Event
from app.types.state import LevelState
from app.windows.utils import (
    clear_cmdhelp_window, clear_cmdlist_window, clear_map_window,
    clear_user_input_window, render_cmdhelp_border, render_cmdlist_border,
    render_map_border, render_positioned_content, render_user_input_border
)

term = Terminal()


class LevelScreen(BaseModel):
    """The screen components for displaying a level"""

    level: Level

    @property
    def term(self) -> Terminal:
        """Initialize and return a terminal to use in other applications"""
        return term

    def _render_user_input(self) -> None:
        print(clear_user_input_window(self.term))
        print(
            render_positioned_content(
                pos_x=self.level.user_input.pos_x + 1,
                pos_y=self.level.user_input.pos_y + 1,
                lines=self.level.user_input.content_lines(self.term),
                term=self.term,
            )
        )

    def _render_cmd_list(self) -> None:
        print(clear_cmdlist_window(self.term))
        print(
            render_positioned_content(
                pos_x=self.level.cmd_list.pos_x + 1,
                pos_y=self.level.cmd_list.pos_y + 1,
                lines=self.level.cmd_list.content_lines(self.term),
                term=self.term,
            )
        )

    def _render_cmd_help(self) -> None:
        print(clear_cmdhelp_window(self.term))
        print(
            render_positioned_content(
                pos_x=self.level.cmd_help.pos_x + 1,
                pos_y=self.level.cmd_help.pos_y + 1,
                lines=self.level.cmd_help.content_lines(self.term),
                term=self.term,
            )
        )

    def _render_map_initial(self) -> None:
        print(clear_map_window(self.term))
        print(self.level.map_initial.content(self.term))

    def _render_initial(self) -> None:
        print(self.term.clear)
        # render borders
        print(render_cmdlist_border(self.term))
        print(render_user_input_border(self.term))
        print(render_cmdhelp_border(self.term))
        print(
            render_map_border(
                self.term, f"Level {self.level.number} - {self.level.title}"
            )
        )
        # render initial content areas
        self._render_cmd_help()
        self._render_cmd_list()
        self._render_user_input()
        self._render_map_initial()

        # print user input and move cursor
        print(self.level.user_input.prompt(self.term), end="", flush=True)

    def _handle_event(self, event: Event) -> None:
        if event == Event.UpdateCmdList:
            self._render_cmd_list()
        elif event == Event.ResolveCollisions:
            self.level.resolve_collisions()
        elif event == Event.UpdateInput:
            self._render_user_input()
        elif event == Event.UpdateMap:
            self._render_map_initial()
        elif event == Event.StartSequence:
            with self.term.hidden_cursor():
                for window in self.level.map_sequence:
                    print(clear_map_window(self.term))
                    print(window.content(self.term))
                    time.sleep(0.2)
        elif event == Event.EndLevel:
            if self.level.current_state == LevelState.Win:
                print("you made it out")
            elif self.level.current_state == LevelState.ExitNotReached:
                print("you failed to reach the exit")
        print(self.level.user_input.prompt(self.term), end="", flush=True)

    def launch(self) -> None:
        """Launches the level in fullscreen mode"""
        self.level.term = self.term
        with self.term.fullscreen(), self.term.cbreak():
            self._render_initial()
            while self.level.current_state not in LevelState.terminal():
                events = self.level.listen(self.term)
                for e in events:
                    self._handle_event(e)
            while True:
                pass
