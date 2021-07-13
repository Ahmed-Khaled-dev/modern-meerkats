from blessed import Terminal

from app.menus import start_menu
from app.screens.level import LevelScreen
from app.types.commands import Command as Cmd
from app.windows.cmd_help import CmdHelpWindow
from app.windows.cmd_list import CmdListwindow
from app.windows.map import MapWindow
from app.windows.user_input import UserInputWindow

sample_map = """
###########           ##############
#         #           #            #
#     @   #           #     x      #
#         #           #            #
#         #           #            #
###     ###           #####     ####
  #     #                 #     #
  #     #                 #     #
  #     #                 #     #
  #     ###################     #
  #                             #
  ###############################
"""


def main() -> None:
    """Main function of the project"""
    check = start_menu.main_menu()
    if(check is True):
        return
    Terminal()

    UserInputWindow()
    CmdHelpWindow(allowed_commands=[Cmd.Move])
    level = LevelScreen(
        map=MapWindow(level_name="Noob Garden", level_number=1, content=sample_map),
        user_input=UserInputWindow(),
        cmd_help=CmdHelpWindow(allowed_commands=[Cmd.Move]),
        cmd_list=CmdListwindow(max_commands=4),
    )
    level.launch()


if __name__ == "__main__":
    main()
