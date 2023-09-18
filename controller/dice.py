from copy import copy

from layot import dice_fields, dice_numbers

enabled = False
number = 0
color = None


def set_dice_number():
    # Turn off field
    for field in dice_fields:
        field.color.set_black_color()

    # Set color of each field that represent the number
    for index_field in dice_numbers[number]:
        dice_fields[index_field].color = copy(color)


def increment_number():
    global number

    number += 1
    if number > 6:
        number = 1


def disable():
    global enabled
    enabled = False


def enable():
    global enabled
    enabled = True

    # Turn on all dice fields
    global number
    number = 0
    set_dice_number()
