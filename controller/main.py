from copy import copy
from random import randint

from controller import dice
from animaton import dice_disable_animation, dice_enable_animation, roll_dice_animation
from player import Player
from .gameState import GameState

game_state = GameState.select_color

players = []
playable_players = 0


def roll_dice(player):
    # Generate dice number
    dice.number = randint(1, 6)

    dice.disable()
    dice.color = copy(player.color)
    dice_disable_animation()
    roll_dice_animation(player)


def init():
    # Create all players
    for i in range(4):
        players.append(Player(i))


def button_action(player_number, button_number):
    # Button number:
    #   0 - button left
    #   1 - button right
    #   2 - button submit

    if game_state == GameState.select_color:
        if button_number == 0:
            players[player_number].change_color_left()

        elif button_number == 1:
            players[player_number].change_color_right()

        elif button_number == 2:
            players[player_number].disable_buttons()
            players[player_number].playable = True

            global playable_players
            playable_players += 1

            # If there are more than 2 players, game can start
            if playable_players >= 2:
                if not dice.enabled:
                    dice.color = copy(players[player_number].color)
                    dice.enable()
                    dice_enable_animation()

            # If there are more than 4 players, game starts automatically
            if playable_players == 4:
                start_game()

    # Player action based on dice number
    else:
        if button_number == 2:
            # Disable player buttons
            players[game_state.value].disable_buttons()

            next_player()


def dice_action():
    if game_state == GameState.select_color:
        start_game()
    else:
        dice.disable()
        dice_disable_animation()

        roll_dice(players[game_state.value])


def next_player():
    global game_state

    # Select next available player
    new_player = game_state.value + 1
    if new_player >= playable_players:
        new_player = 0

    game_state = GameState(new_player)

    dice.color = copy(players[game_state.value].color)
    dice.enable()
    dice_enable_animation()


def start_game():
    # Disable all players
    disabled_players = 0
    for i in range(len(players)):
        if not players[i-disabled_players].playable:
            # Remove player from list
            player = players.pop(i-disabled_players)

            # Disable player
            player.disable()
            disabled_players += 1

    # Select first player
    next_player()
