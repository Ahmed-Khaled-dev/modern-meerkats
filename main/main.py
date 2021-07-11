import tui
from blessed import Terminal

term = Terminal()

# Setting the width and height for the whole layout
WIDTH = 100
HEIGHT = 100


def main() -> None:
    """The main function of the project."""
    print(term.clear)
    table = tui.create_layout(WIDTH, HEIGHT)

    # To print the title Modern Meerkats and centre it as much as i can.
    print(term.move_right(WIDTH//2 - 5) + f"{term.cyan}Modern Meerkats{term.normal}")

    # Creating the line that seperates the code user input area from the history/command box area.
    input_area_dashes = ""
    for i in range(WIDTH//2):
        input_area_dashes = input_area_dashes + "─"

    print(table)

    # Printing line that seperates the code user input area from the history/command box area.
    print(term.move_right(WIDTH//2 + 2) + term.move_up(WIDTH//8) + f"{term.cyan}{input_area_dashes}{term.normal}")

    # Printing the input text in the user input area.
    # Then storing the input and printing it in the history/command box area.

    print(term.move_right(WIDTH//2 + WIDTH//30), end='')

    print(term.bold('Enter code here: '))
    print(term.move_right(WIDTH//2+WIDTH//30), end='')
    curr_loc = term.get_location()

    # this variable can be the number of commands that can be give at a time
    count = 0

    # taking the keystroke from the user and performing necessary operations
    with term.cbreak():
        val = ''
        ans = ""

    # the number of iterations can be modified later
        while count != 3:
            val = term.inkey(timeout=3)
            if not val:
                continue
            # if the ENTER key is detected, the current string will be printed to the command box and count updated
            # clear the user input area without losing the current cursor positon
            elif val.is_sequence and val.code == 343:
                with term.location():
                    print(term.clear_eol)

            # printing the current user input to the command area
                with term.location():
                    print(term.move_xy(WIDTH//2+4, HEIGHT//40+count)+term.bold(ans))
                    ans = ""
                count += 1

            # if a backspace sequence is detected, the last character is erased
            elif val.is_sequence and val.code == 263:
                ans = ans[:-1]
                with term.location():
                    print(term.clear_eol)
                with term.location():
                    print(term.bold(ans))
                continue

            # if any other keystroke is detected, the user input area ignores the input
            elif val.is_sequence:
                continue
            # if the current user input exceeds the width of the terminal:
            # The function throws a warning
            # it breaks out of the loop
            elif val:
                if(curr_loc[1]+len(ans) >= WIDTH):
                    with term.location():
                        print(term.move_xy(WIDTH//2+4, HEIGHT//50+count)+term.bold("Your input is too long"))
                    ans = ""
                    break

            # if the keystroke detected is an alphabet, it is appended to the ans string and printed on the
            # user input area

                ans += "{0}".format(val)
                with term.location():
                    print(term.bold(ans))

    # Set the cursor away from the layout.
    # So after the program is ended it doesn't print on top of the layout.
    print(term.move_xy(0, HEIGHT))


if __name__ == "__main__":
    main()
