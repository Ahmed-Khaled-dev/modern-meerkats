from blessed import Terminal

term = Terminal()

# Setting the width and height for the whole layout
WIDTH = 100
HEIGHT = 100


def create_layout(width: int, height: int) -> str:
    """A function to create the whole terminal layout."""
    table = ""

    # Setting up the variable that will be used in the top/bottom of the layout.
    table_dashes = ""
    for w in range(width + 1):
        # If we reached the middle of the layout.
        # Change the character that's used, for a better look.
        if w == width/2:
            table_dashes = table_dashes + f"{term.cyan}┬{term.normal}"
        else:
            table_dashes = table_dashes + f"{term.blue}─{term.normal}"

    table_sides = ""
    for h in range(int(height/3)):
        layout_left_side = f"{term.blue}\n│{term.normal}"
        layout_right_side = f"{term.blue}│{term.normal}"
        layout_middle_line = f"{term.cyan}│{term.normal}"
        # Adding spaces after layout_left_side so that we reach the middle of the layout.
        layout_left_side_with_spaces = layout_left_side.ljust(len(layout_left_side) + int(height/2))
        # Adding spaces before layout_right_side so that we reach the end of the layout.
        layout_right_side_with_spaces = layout_right_side.rjust(len(layout_right_side) + int(height/2))
        # Finally adding all together, left side with spaces + middle line + right side with the spaces before it.
        table_sides = table_sides + layout_left_side_with_spaces + layout_middle_line + layout_right_side_with_spaces

    table_beggining = f"{term.cyan}┌{table_dashes}{term.cyan}┐"
    table = table + table_beggining

    table = table + table_sides

    table_end = f"\n{term.cyan}└{table_dashes.replace('┬', '┴')}{term.cyan}┘{term.normal}"
    table = table + table_end

    return table


print(term.clear)

print(term.center(f"{term.cyan}Modern Meerkats{term.normal}", width=WIDTH + 2, fillchar=" "))

# Creating the line that seperates the code user input area from the history/command box area.
input_area_dashes = ""
for i in range(WIDTH//2):
    input_area_dashes = input_area_dashes + "─"

print(create_layout(WIDTH, HEIGHT))

# Printing line that seperates the code user input area from the history/command box area.
print(term.move_right(WIDTH//2 + 2) + term.move_up(WIDTH//8) + f"{term.cyan}{input_area_dashes}{term.normal}")

# Printing the input text in the user input area.
# Then storing the input and printing it in the history/command box area.
code_entered = input(term.move_right(WIDTH//2 + WIDTH//30) + term.bold('Enter code here: '))
print(term.move_right(WIDTH//2 + WIDTH//30) + term.move_up(WIDTH//5) + code_entered)

# Set the cursor away from the layout.
# So after the program is ended it doesn't print on top of the layout.
print(term.move_xy(0, HEIGHT))
