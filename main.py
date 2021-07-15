from app.levels.level_0 import Level0
from app.menus import start_menu
from app.screens.level import LevelScreen


def main() -> None:
    """Main function of the project"""
    check = start_menu.main_menu()
    if check is True:
        return
    screen = LevelScreen(level=Level0)
    screen.launch()


if __name__ == "__main__":
    main()
