from time import time

import utilities
from dice import Dice

from .animations import animations

update_time = time() + utilities.fade_time


def callback_fun():
    pass


is_dice_rolling = False
callback_function = callback_fun


def roll_dice_animation(callback):
    """
    Start dice roll animation. When animation is done call callback function.

    :param callback: Function that will be called when dice roll animation is done.
    :return: None
    """

    global is_dice_rolling, callback_function
    is_dice_rolling = True
    callback_function = callback


def update():
    """
    Update animations in proper time schedule.

    :return: None
    """
    global update_time, is_dice_rolling, callback_function

    # Update in proper time schedule
    if update_time <= time():
        update_time = time() + utilities.fade_time

        # Fade or illuminate global object
        if utilities.fade_direction:
            utilities.fade_alfa += utilities.fade_rate
        else:
            utilities.fade_alfa -= utilities.fade_rate

        # Decide whether global object should be faded or illuminated
        if utilities.fade_alfa >= utilities.fade_max_limit:
            utilities.fade_alfa = utilities.fade_max_limit
            utilities.fade_direction = False
        elif utilities.fade_alfa <= utilities.fade_min_limit:
            utilities.fade_alfa = utilities.fade_min_limit
            utilities.fade_direction = True

        # Update all animations that are active
        for a in animations:
            a.update()

    # Do dice animation if it is enabled
    if is_dice_rolling:
        utilities.dice_animation_change_counter += 1

        # Check if counter is filled
        if utilities.dice_animation_counter == utilities.dice_animation_change_counter:
            # Set new threshold
            utilities.dice_animation_counter += utilities.dice_animation_increment
            utilities.dice_animation_change_counter = 0

            # Change dice number
            Dice.increment_number()
            Dice.set_dice_number()

            if utilities.dice_animation_counter >= utilities.dice_animation_threshold:
                # Set default values for roll animation
                is_dice_rolling = False
                utilities.dice_animation_counter = 1
                utilities.dice_animation_change_counter = 0

                callback_function()
