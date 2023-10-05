"""
Create and draw all buttons on board.
"""

from utilities import positions_path

from .arrowButton import ArrowButton
from .submitButton import SubmitButton

# On board there are 4 button sets, each for one player
# Button set contains two arrow, and one submit button
button_sets = []

# Location of button positions on screen
file_object = open(f'{positions_path}/buttons.txt', 'r')

# Create button set for each player
for i in range(4):
    buttons = []

    # Each set has three buttons
    for j in range(3):
        # Read one position
        line = file_object.readline()

        # Split coordinates to x, y and angle of image
        position_string = line.split()

        position = float(position_string[0]), float(position_string[1])

        # First two buttons are arrows, and last button is submit
        if j < 2:
            buttons.append(ArrowButton(position, float(position_string[2])))
        else:
            buttons.append(SubmitButton(position, float(position_string[2])))

    button_sets.append(buttons)


# Function to draw all buttons
def draw_buttons(screen):
    for button_set in button_sets:
        for button in button_set:
            if button.enabled:
                button.draw(screen)
