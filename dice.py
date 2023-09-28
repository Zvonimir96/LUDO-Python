from copy import copy

from layot import dice_fields, dice_numbers
from utilities import Color


class Dice:
    enabled = False
    number = 0
    color = Color()

    @staticmethod
    def set_dice_number():
        # Set color of each field that represent the number
        for index_field in dice_numbers[Dice.number]:
            dice_fields[index_field].color = copy(Dice.color)

    @staticmethod
    def increment_number():
        Dice.number += 1

        # If number is higher than 6, start counting from 1
        if Dice.number > 6:
            Dice.number = 1

    @staticmethod
    def disable():
        Dice.enabled = False

    @staticmethod
    def enable():
        Dice.enabled = True

        # Turn on all dice fields
        Dice.number = 0
        Dice.set_dice_number()
