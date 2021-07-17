from app.levels.level_0 import Level0
from app.levels.level_1 import Level1
from app.levels.level_2 import Level2
from app.levels.level_3 import Level3
from app.menus import start_menu, warning_menu
from app.screens.level import LevelScreen
from app.types.events import Event

levels = [Level0, Level1, Level2, Level3]


def main() -> None:
    """Main function of the project"""
    while True:
        warning_menu.warning_menu()
        check = start_menu.main_menu()
        if check is True:
            return
        for level in levels:
            while True:
                screen = LevelScreen(level=level())
                event = screen.launch()
                if event == Event.ToMainMenu:
                    break
                elif event == Event.RetryLevel:
                    pass
                elif event == Event.ToNextLevel:
                    break
            if event == Event.ToMainMenu:
                break
            elif event == Event.ToNextLevel:
                pass


if __name__ == "__main__":
    main()
