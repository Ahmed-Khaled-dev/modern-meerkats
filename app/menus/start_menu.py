import asyncio

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

# Create a new screen where the asciimatics will be displayed

check = False
# Whenever the user presses s or q, necessary actions are taken


def update_screen(
    end_time: int, loop: asyncio.AbstractEventLoop, screen: Screen
) -> None:
    """Checks if the user input matches with keys s or q."""
    global check
    event = screen.get_event()
    screen.draw_next_frame()

    try:

        if event is not None and chr(event.key_code) == "s":
            loop.stop()
            check = False

            # Call the next function for user input and terminal here
            # User pressed s, hence the flag is true
        elif event is not None and chr(event.key_code) == "q":
            loop.stop()
            check = True
        else:
            if loop.time() < end_time:
                loop.call_later(0.05, update_screen, end_time, loop, screen)
            else:
                loop.stop()

    except:  # noqa: E722
        if loop.time() < end_time:
            loop.call_later(0.05, update_screen, end_time, loop, screen)
        else:
            loop.stop()


# Define the scene that you'd like to play.
# In this case, the text with different colors will be displayed


def main_menu() -> bool:
    """Function that creates the main menu"""
    screen = Screen.open()
    effects = [
        Cycle(screen, FigletText("MEERKAT'S", font="big"), screen.height // 2 - 20),
        Cycle(
            screen,
            FigletText("     INSIDE  THE  BOX  ADVENTURE    ", font="big"),
            screen.height // 2 - 10,
        ),
        Cycle(
            screen,
            FigletText("Press  s   to  start", font="small"),
            screen.height // 2 + 7,
        ),
        Cycle(
            screen,
            FigletText("Press  q  to  quit", font="small"),
            screen.height // 2 + 13,
        ),
        Stars(screen, (screen.width + screen.height)),
    ]

    # Call the above effects to play on the terminal continously
    screen.set_scenes([Scene(effects, 500)])

    loop = asyncio.new_event_loop()
    end_time = loop.time() + 500.0
    global check
    loop.call_soon(update_screen, end_time, loop, screen)

    # Blocking call interrupted by loop.stop()
    loop.run_forever()
    loop.close()
    screen.clear()
    screen.close()
    return check
