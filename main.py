from app.entities.player import Player
from app.levels.level_test import TestLevel
from app.menus import start_menu
from app.screens.level import LevelScreen
from app.types.commands import Command as Cmd
from app.windows.cmd_help import CmdHelpWindow
from app.windows.cmd_list import CmdListwindow
from app.windows.user_input import UserInputWindow


def main() -> None:
    """Main function of the project"""
    check = start_menu.main_menu()
    if check is True:
        return
    player = Player(
        start_y=7,
        start_x=7,
        moves=[],
    )
    player.add_move(10, "r")
    player.add_move(6, "d")
    player.add_move(10, "r")
    screen = LevelScreen(
        level=TestLevel(),
        player=player,
        user_input=UserInputWindow(),
        cmd_help=CmdHelpWindow(allowed_commands=[Cmd.Move]),
        cmd_list=CmdListwindow(max_commands=4),
    )
    screen.launch()


if __name__ == "__main__":
    main()
