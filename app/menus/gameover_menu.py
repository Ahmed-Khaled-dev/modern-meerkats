from prompt_toolkit.shortcuts import yes_no_dialog

from app.types.events import Event


def game_over(level_title: str, fail_reason: str) -> Event:
    """Game over screen that pops up for the user."""
    dialog = yes_no_dialog(
        title=level_title, text=f"Game Over!\n{fail_reason}\nDo you wish to continue?"
    )
    ans = dialog.run()
    if ans:
        # Continue Game
        print("Continuing game...")
        return Event.RetryLevel
    else:
        # Quit Game
        print("Quitting Game...")
        return Event.ToMainMenu
