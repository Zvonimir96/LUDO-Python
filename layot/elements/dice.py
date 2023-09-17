from utilities import Color
from .field import Field
from utilities import positions_path, dice_field_representation

# Map fields that should be activated to represent each number on dice
dice_numbers = {
    0: [1, 2, 3, 4, 5, 6, 7, 8, 9],
    1: [8],
    2: [2, 6],
    3: [2, 6, 8],
    4: [0, 2, 4, 6],
    5: [0, 2, 4, 6, 8],
    6: [0, 1, 2, 4, 5, 6]
}

dice_fields = []


class Dice:
    color = Color

    @staticmethod
    def create():
        file_object = open(f'{positions_path}/dice.txt', 'r')

        for line in file_object:
            # Split coordinates to x and y
            position_string = line.split(', ')
            position_string[1].replace('\n', ' ')

            position = float(position_string[0]), float(position_string[1])

            # Create new field and save it in path fields variable, so we can access them later
            dice_fields.append(Field(position, dice_field_representation))

    @staticmethod
    def set_number(number):
        # Set all fields color to black, in real life turn off neopixel
        for field in dice_fields:
            field.color.set_black_color()
            print(field.color)

        for field in dice_numbers[number]:
            dice_fields[field].color = Dice.color
            dice_fields[field].color.set_full_brightness()

    @staticmethod
    def draw_dice(screen):
        for field in dice_fields:
            field.draw(screen)

