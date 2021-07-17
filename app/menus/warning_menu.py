from asciimatics.effects import Print
from asciimatics.renderers import SpeechBubble
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def warning_menu() -> None:
    """Function that creates the main menu"""
    screen = Screen.open()
    scenes = []
    effects = []
    effects.append(Print(
        screen,
        SpeechBubble("WARNING"),
        screen.height // 10-2,
        screen.width // 20,
        colour=1,
        transparent=False))

    effects.append(Print(
        screen,
        SpeechBubble("MAKE SURE THE TERMINAL IS IN FULL-SCREEN MODE"),
        screen.height // 10+1,
        screen.width // 20,
        colour=7,
        transparent=False))

    effects.append(Print(
        screen,
        SpeechBubble("PRESS q WHEN THE TERMINAL IS IN FULL-SCREEN"),
        screen.height // 10+4,
        screen.width // 20,
        colour=3,
        transparent=False))

    scenes.append(Scene(effects, -1))
    screen.play(scenes, repeat=True)
