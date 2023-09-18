from .arrowButton import ArrowButton
from .submitButton import SubmitButton

from utilities import positions_path

button_sets = []

file_object = open(f'{positions_path}/buttons.txt', 'r')

# Create button sets for each player
for i in range(4):
    buttons = []

    # Each set has three buttons
    for j in range(3):
        # Read line with position coordinates
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
