from time import time

import utilities
from dice import Dice

from .animations import animations

update_time = time() + utilities.fade_time

is_dice_rolling = False
callback_fun = None


def roll_dice_animation(callback):
    global is_dice_rolling, callback_fun
    is_dice_rolling = True
    callback_fun = callback


def update():
    global update_time, is_dice_rolling, callback_fun
    if update_time <= time():
        update_time = time() + utilities.fade_time

        if utilities.fade_direction:
            utilities.fade_alfa += utilities.fade_rate
        else:
            utilities.fade_alfa -= utilities.fade_rate

        if utilities.fade_alfa >= utilities.fade_max_limit:
            utilities.fade_alfa = utilities.fade_max_limit
            utilities.fade_direction = False
        elif utilities.fade_alfa <= utilities.fade_min_limit:
            utilities.fade_alfa = utilities.fade_min_limit
            utilities.fade_direction = True

        for a in animations:
            a.update()

    if is_dice_rolling:
        utilities.dice_animation_change_counter += 1

        if utilities.dice_animation_counter == utilities.dice_animation_change_counter:
            utilities.dice_animation_counter += utilities.dice_animation_increment
            utilities.dice_animation_change_counter = 0

            Dice.increment_number()
            Dice.set_dice_number()

            if utilities.dice_animation_counter >= utilities.dice_animation_threshold:
                # Set default values for roll animation
                is_dice_rolling = False
                utilities.dice_animation_counter = 1
                utilities.dice_animation_change_counter = 0

                callback_fun()
