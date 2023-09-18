import time

import utilities
from controller import dice
from layot import dice_numbers, dice_fields
from .animation import Animation
from .animationType import AnimationType

animations = []
update_time = time.time() + utilities.fade_time
is_dice_rolling = False
player_on_turn = None


def dice_enable_animation():
    for index_field in dice_numbers[0]:
        add_animation(dice_fields[index_field], AnimationType.DICE_ENABLE)


def dice_disable_animation():
    for index_field in dice_numbers[0]:
        remove_animation(dice_fields[index_field - 1])


def roll_dice_animation(player):
    global is_dice_rolling, player_on_turn
    player_on_turn = player
    is_dice_rolling = True

    dice.set_dice_number()


def add_animation(obj, animation_type):
    anim = Animation(obj, animation_type)
    anim.update()
    animations.append(anim)


def remove_animation(obj):
    for i, a in enumerate(animations):
        if a.object == obj:
            animations[i].disable()
            del animations[i]
            break


def update():
    global update_time, is_dice_rolling
    if update_time <= time.time():
        update_time = time.time() + utilities.fade_time

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

            dice.increment_number()
            dice.set_dice_number()

            if utilities.dice_animation_counter >= utilities.dice_animation_threshold:
                # Set default values for roll animation
                is_dice_rolling = False
                utilities.dice_animation_counter = 1
                utilities.dice_animation_change_counter = 0

                # Enable player buttons
                player_on_turn.enable_buttons()
