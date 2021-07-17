import asyncio
from random import choice, randint
from typing import Literal, Optional

from asciimatics.effects import Mirage, Print, Stars
from asciimatics.particles import (
    PalmFirework, RingFirework, SerpentFirework, StarFirework
)
from asciimatics.renderers import FigletText, Rainbow, SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen

from app.types.events import Event

_victory_key: Optional[Literal["n", "q"]] = None


def update_screen(
    end_time: int, loop: asyncio.AbstractEventLoop, screen: Screen
) -> None:
    """Checks if the user input matches with keys s or q."""
    event = screen.get_event()
    screen.draw_next_frame()
    global _victory_key
    try:
        if event is not None and chr(event.key_code) == "n":
            _victory_key = "n"
            loop.stop()
        elif event is not None and chr(event.key_code) == "q":
            _victory_key = "q"
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


def victory(screen: Screen) -> Event:
    """Displays the victory screen."""
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(
            screen,
            SpeechBubble("Press q to return to main menu."),
            x=screen.width // 2 - 40,
            y=screen.height // 2 + 3,
            start_frame=5,
            transparent=True,
        ),
    ]
    effects.append(
        Print(
            screen,
            SpeechBubble("Press n to move to next level."),
            x=screen.width // 2 + 10,
            y=screen.height // 2 + 3,
            start_frame=5,
            transparent=False,
        )
    )

    # display fireworks
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(
                screen,
                randint(0, screen.width),
                randint(screen.height // 8, screen.height * 3 // 4),
                randint(start, stop),
                start_frame=randint(0, 250),
            ),
        )

    effects.append(
        Mirage(
            screen,
            Rainbow(screen, FigletText("Victory", font="banner3")),
            screen.height // 2 - 17,
            colour=7,
        )
    )
    effects.append(
        Print(
            screen,
            SpeechBubble("Congratulations you have cleared this level!"),
            screen.height // 2 - 8,
            speed=1,
            start_frame=5,
            transparent=False,
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
    if _victory_key == "n":
        return Event.ToNextLevel
    elif _victory_key == "q":
        return Event.ToMainMenu
    else:
        return Event.ToNextLevel
