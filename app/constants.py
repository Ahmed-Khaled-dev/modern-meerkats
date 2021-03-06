from blessed import Terminal

## Assets
term = Terminal()
PATROL_VISION = term.azure4("█")
WALL = term.seashell4("█")
PATROL = term.tomato("!")
PLAYER = term.green("@")
EXIT = term.brown("#")

WINDOW_PADDING = 1
OFFSET_X = 5
OFFSET_Y = 2
COL_WIDTH = 30
ROW_HEIGHT = 40


# Calculated Constants
MAP_WIDTH = COL_WIDTH * 3
MAP_HEIGHT = ROW_HEIGHT
MAP_X = OFFSET_X
MAP_Y = OFFSET_Y

CMDLIST_WIDTH = COL_WIDTH
CMDLIST_HEIGHT = int((ROW_HEIGHT / 8) * 7) - (WINDOW_PADDING * 2)
CMDLIST_X = MAP_X + MAP_WIDTH + (WINDOW_PADDING * 2)
CMDLIST_Y = MAP_Y

INPUT_WIDTH = COL_WIDTH * 2
INPUT_HEIGHT = int(ROW_HEIGHT / 8)
INPUT_X = CMDLIST_X
INPUT_Y = CMDLIST_Y + CMDLIST_HEIGHT + (WINDOW_PADDING * 2)
PROMPT_LINE = "  >> "
INPUT_MAX_LENGTH = INPUT_WIDTH - (WINDOW_PADDING * 4) - len(PROMPT_LINE)

CMDHELP_WIDTH = INPUT_WIDTH - (WINDOW_PADDING * 2) - CMDLIST_WIDTH
CMDHELP_HEIGHT = CMDLIST_HEIGHT
CMDHELP_X = CMDLIST_X + CMDLIST_WIDTH + (WINDOW_PADDING * 2)
CMDHELP_Y = MAP_Y

# Keys
BACKSPACE = 263
ENTER = 343
DEBUG_KEY = 331  # insert

# Commands
VALID_COMMANDS = ["wait", "jump"]
for i in range(MAP_WIDTH):
    num = i
    num = str(num)
    VALID_COMMANDS.append("move " + num + " left")
    VALID_COMMANDS.append("move " + num + " right")

for i in range(MAP_HEIGHT):
    num = i
    num = str(num)
    VALID_COMMANDS.append("move " + num + " up")
    VALID_COMMANDS.append("move " + num + " down")
