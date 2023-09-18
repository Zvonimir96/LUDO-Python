from ..field import Field
from utilities import positions_path, dice_field_representation

dice_fields = []

# Map fields that should be activated to represent each number on dice
dice_numbers = {
    0: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    1: [8],
    2: [2, 6],
    3: [2, 6, 8],
    4: [0, 2, 4, 6],
    5: [0, 2, 4, 6, 8],
    6: [0, 1, 2, 4, 5, 6]
}


def create_dice():
    file_object = open(f'{positions_path}/dice.txt', 'r')

    for i, line in enumerate(file_object):
        # Split coordinates to x and y
        position_string = line.split()

        position = float(position_string[0]), float(position_string[1])

        # Create new field and save it in path fields variable, so we can access them later
        dice_fields.append(Field(position, dice_field_representation))


def draw_dice(screen):
    for field in dice_fields:
        field.draw(screen)
