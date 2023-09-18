import controller.dice
from layot import button_sets, dice_fields
from utilities import images_size, dice_offset
from .main import button_action, dice_action, init


def is_button_clicked(mouse_position):
    # Iterate through all buttons
    for set_number, button_set in enumerate(button_sets):
        for button_number, button in enumerate(button_set):
            # If mouse position is inside coordinates of button
            if (button.position[0]) < mouse_position[0] < (button.position[0] + images_size) and \
                    (button.position[1]) < mouse_position[1] < (button.position[1] + images_size) and \
                    button.enabled:
                button_action(set_number, button_number)
                break

    # If mouse position is inside coordinates of dice
    if mouse_position[0] + dice_offset / 2 > dice_fields[0].position[0] > mouse_position[
        0] - dice_offset * 3 + dice_offset / 2 and \
            mouse_position[1] + dice_offset / 2 > dice_fields[0].position[1] > mouse_position[
        1] - dice_offset * 3 + dice_offset / 2 and dice.enabled:
        dice_action()