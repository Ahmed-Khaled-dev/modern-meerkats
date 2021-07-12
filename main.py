from blessed import Terminal

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


term = Terminal()

ui = UserInputWindow()
cmdh = CmdHelpWindow(allowed_commands=[Cmd.Move])
level = LevelScreen(
    map=MapWindow(level_name="Noob Garden", level_number=1, content=sample_map),
    user_input=UserInputWindow(),
    cmd_help=CmdHelpWindow(allowed_commands=[Cmd.Move]),
    cmd_list=CmdListwindow(max_commands=4),
)
level.launch()
