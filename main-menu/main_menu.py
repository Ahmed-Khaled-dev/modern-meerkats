from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Create a new screen where the asciimatics will be displayed
screen = Screen.open()


# Whenever the user presses s or q, necessary actions are taken
def start_game(event: object) -> None:
    """Checks if the user input matches with keys s or q."""
    flag = False
    try:
        event.key_code
    # If s is pressed, the layout must change to the user terminal

        if(event is not None and chr(event.key_code) == 's'):
            screen.clear()
            screen.close()
            # Call the next function for user input and terminal here
            # Func.func()
            # User pressed s, hence the flag is true
            flag = True
            exit()

        elif(event is not None and chr(event.key_code) == 'q'):
            screen.clear()
            screen.close()
            flag = True
            exit()

    except:  # noqa: E722
        if(flag):
            exit()


# Define the scene that you'd like to play.
# In this case, the text with different colors will be displayed
effects = [
    Cycle(
        screen,
        FigletText("MEERKAT'S", font='big'),
        screen.height // 2 - 20),
    Cycle(
        screen,
        FigletText("     INSIDE  THE  BOX  ADVENTURE    ", font='big'),
        screen.height // 2 - 10),
    Cycle(
        screen,
        FigletText("Press  s   to  start", font='small'),
        screen.height // 2 + 7),
    Cycle(
        screen,
        FigletText("Press  q  to  quit", font='small'),
        screen.height // 2 + 13),


    Stars(screen, (screen.width + screen.height))
]

# Call the above effects to play on the terminal continously
screen.play([Scene(effects, 1000)], stop_on_resize=True, unhandled_input=start_game)
