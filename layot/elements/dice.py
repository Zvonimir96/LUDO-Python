from utilities import positions_path, dice_field_representation

from ..field import Field

# Dice contains 9 fields
# This array is used by dice controller to show number
dice_fields = []

# Map fields of dice that should be activated to represent each number on dice
# Number on dice is saved in key
# Value is array of fields
# Key 0 selects all fields on dice
dice_numbers = {
    0: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    1: [8],
    2: [2, 6],
    3: [2, 6, 8],
    4: [0, 2, 4, 6],
    5: [0, 2, 4, 6, 8],
    6: [0, 1, 2, 4, 5, 6]
}

# Location of dice fields positions on screen
file_object = open(f'{positions_path}/dice.txt', 'r')


def create_dice():
    for i, line in enumerate(file_object):
        # Read one position
        position_string = line.split()

        position = float(position_string[0]), float(position_string[1])

        # Create new field and save it in dice fields variable
        dice_fields.append(Field(position, dice_field_representation))


def draw_dice(screen):
    for field in dice_fields:
        field.draw(screen)
