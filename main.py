from app.tui import Position, Screen, Window

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

commands_text = """
The plan:
  1. Move 5 down
  2. Move 10 right
  3. Move 5 up
"""

available_text = """
For this level you may use:
  1. Move
  2. Wait
"""

map_area = Window(
    title="Map",
    width=80,
    height=30,
    pos=Position(x=0, y=0),
    content=sample_map,
)
commands = Window(
    title="Commands",
    width=30,
    height=23,
    pos=Position(x=82, y=0),
    content=commands_text,
)
user_input = Window(
    title="User Input",
    width=62,
    height=5,
    pos=Position(x=82, y=25),
    content=None,
)
available_commands = Window(
    title="Available Commands",
    width=30,
    height=23,
    pos=Position(x=114, y=0),
    content=available_text,
)
screen = Screen(
    commands=commands,
    user_input=user_input,
    map_area=map_area,
    available_commands=available_commands,
)
screen.draw()
