import asyncio
from typing import Literal, Optional

from asciimatics.effects import Print
from asciimatics.renderers import FigletText, Fire, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from app.types.events import Event

_gameover_key: Optional[Literal["m", "r"]] = None


def update_screen(
    end_time: int, loop: asyncio.AbstractEventLoop, screen: Screen
) -> None:
    """Checks if the user input matches with keys m or r."""
    event = screen.get_event()
    screen.draw_next_frame()
    global _gameover_key
    try:
        if event is not None and chr(event.key_code) == "m":
            _gameover_key = "m"
            loop.stop()
        elif event is not None and chr(event.key_code) == "r":
            _gameover_key = "r"
            loop.stop()
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


def gameover(screen: Screen, fail_reason: str) -> Event:
    """Displays the gameover screen."""
    scenes = []
    effects = [
        Print(
            screen,
            SpeechBubble("Press m to return to main menu."),
            x=screen.width // 2 - 40,
            y=screen.height // 2 + 3,
            start_frame=5,
            transparent=True,
            colour=Screen.COLOUR_RED,
        ),
    ]
    effects.append(
        Print(
            screen,
            SpeechBubble("Press r to retry the level."),
            x=screen.width // 2 + 10,
            y=screen.height // 2 + 3,
            start_frame=5,
            transparent=False,
            colour=Screen.COLOUR_RED,
        )
    )

    # Check https://asciimatics.readthedocs.io/en/stable/asciimatics.html?highlight=fire#asciimatics.renderers.Fire
    effects.append(
        Print(
            screen,
            Fire(screen.height // 2 - 10, 80, "!!!!@@@@###", 1, 40, screen.colours),
            speed=1,
            transparent=True,
            x=screen.width // 2 + 30,
            y=screen.height // 2 - 20,
        ),
    )

    # Check https://asciimatics.readthedocs.io/en/stable/asciimatics.html?highlight=fire#asciimatics.renderers.Fire
    effects.append(
        Print(
            screen,
            Fire(screen.height // 2 - 10, 80, "!!!!@@@@###", 1, 40, screen.colours),
            speed=1,
            transparent=True,
            x=screen.width // 2 - 110,
            y=screen.height // 2 - 20,
        ),
    )

    effects.append(
        Print(
            screen,
            SpeechBubble(f"Congratulations! {fail_reason}."),
            screen.height // 2 - 8,
            speed=1,
            start_frame=5,
            transparent=False,
        )
    )
    effects.append(
        Print(
            screen,
            FigletText("GAME OVER!", "banner"),
            screen.height // 2 - 17,
            colour=Screen.COLOUR_RED,
            bg=Screen.COLOUR_BLACK,
            speed=1,
        )
    )

    scenes.append(Scene(effects, -1))
    screen.set_scenes(scenes)
    loop = asyncio.new_event_loop()
    end_time = loop.time() + 500.0
    loop.call_soon(update_screen, end_time, loop, screen)
    loop.run_forever()
    loop.close()
    screen.clear()
    screen.close()
    if _gameover_key == "m":
        return Event.ToMainMenu
    elif _gameover_key == "r":
        return Event.RetryLevel
    else:
        return Event.RetryLevel
