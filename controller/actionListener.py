from layot import button_sets, dice_fields
from utilities import images_size, dice_offset
from layot import Position, PositionType
from dice import Dice

from .gameState import GameState
from .stateMachine import StateMachine


def is_button_clicked(mouse_position):
    # Iterate through all buttons
    for set_number, button_set in enumerate(button_sets):
        for button_number, button in enumerate(button_set):
            # If mouse position is inside coordinates of button
            if (button.draw_position[0]) < mouse_position[0] < (button.draw_position[0] + images_size) and \
                    (button.draw_position[1]) < mouse_position[1] < (button.draw_position[1] + images_size) and \
                    button.enabled:
                button_action(set_number, button_number)
                break

    # If mouse position is inside coordinates of dice
    if mouse_position[0] + dice_offset / 2 > dice_fields[0].draw_position[0] > mouse_position[
        0] - dice_offset * 3 + dice_offset / 2 and \
            mouse_position[1] + dice_offset / 2 > dice_fields[0].draw_position[1] > mouse_position[
        1] - dice_offset * 3 + dice_offset / 2 and Dice.enabled:
        dice_action()


def button_action(player_number, button_number):
    # Button number:
    #   0 - button left
    #   1 - button right
    #   2 - button submit

    if StateMachine.game_state == GameState.SELECT_COLOR:
        if button_number == 0:
            StateMachine.players[player_number].change_color_left()

        elif button_number == 1:
            StateMachine.players[player_number].change_color_right()

        elif button_number == 2:
            StateMachine.select_player_color(player_number)

            playable_players = StateMachine.number_of_playable_players()

            # If there are more than 2 players, game can start
            if playable_players >= 2:
                StateMachine.enable_dice(StateMachine.players[player_number].color)

            # If there are more than 4 players, game starts automatically
            if playable_players == 4:
                StateMachine.start_game()

    elif StateMachine.game_state == GameState.CANNOT_PLAY:
        if button_number == 2:
            StateMachine.next_player()

    elif StateMachine.game_state == GameState.REPEAT_ROLL:
        if button_number == 2:
            StateMachine.set_dice_action()

    elif StateMachine.game_state == GameState.PLAYER_ACTION:
        if button_number == 0:
            StateMachine.select_figure_left()

        elif button_number == 1:
            StateMachine.select_figure_right()

        elif button_number == 2:
            StateMachine.move_figure()


def dice_action():
    if StateMachine.game_state == GameState.SELECT_COLOR:
        StateMachine.start_game()
    elif StateMachine.game_state == GameState.DICE_ACTION:
        StateMachine.roll_dice()
