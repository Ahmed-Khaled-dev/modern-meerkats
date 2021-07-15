from prompt_toolkit.shortcuts import yes_no_dialog


def game_over() -> None:
    """Game over screen that pops up for the user."""
    dialog = yes_no_dialog(title='Game Name', text='Game Over!\nDo you wish to continue?')
    ans = dialog.run()
    if ans is True:
        # Continue Game
        print("Continuing game...")
    elif ans is False:
        # Quit Game
        print("Quitting Game...")


game_over()
