from app.levels.level_0 import Level0
from app.menus import start_menu
from app.screens.level import LevelScreen
from app.types.events import Event

levels = [Level0(), Level0()]


def main() -> None:
    """Main function of the project"""
    while True:
        check = start_menu.main_menu()
        if check is True:
            return
        for level in levels:
            screen = LevelScreen(level=level)
            event = screen.launch()
            if event == Event.ToMainMenu:
                break
            elif event == Event.ToNextLevel:
                pass


if __name__ == "__main__":
    main()
