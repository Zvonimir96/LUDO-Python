from copy import copy
from random import randint

from animaton import add_animation, AnimationType, remove_animation, roll_dice_animation
from dice import Dice
from layot import dice_numbers, dice_fields
from player import Player
from utilities import black_color, dice_roll_animation_enabled
from .gameState import GameState


def enable_player_buttons(player):
    for button in player.buttons:
        button.enabled = True
        add_animation(button, AnimationType.BUTTON_ENABLE)


def disable_player_buttons(player):
    for button in player.buttons:
        button.enabled = False
        remove_animation(button)


def dice_enable_animation():
    for index_field in dice_numbers[0]:
        add_animation(dice_fields[index_field], AnimationType.DICE_ENABLE)


def dice_disable_animation():
    for index_field in dice_numbers[0]:
        remove_animation(dice_fields[index_field - 1])


class StateMachine:
    game_state = GameState.select_color
    player_on_turn = -1
    players = []

    @staticmethod
    def init():
        # Create all players
        for i in range(4):
            player = Player(i)

            enable_player_buttons(player)
            StateMachine.players.append(player)

    @staticmethod
    def roll_dice():
        # Disable dice action animation
        dice_disable_animation()

        Dice.number = randint(1, 6)

        # Roll animation is disabled only for testing purposes
        if dice_roll_animation_enabled:
            # Enable dice roll animation
            roll_dice_animation(StateMachine.dice_roll_done)

        else:
            Dice.set_dice_number()
            StateMachine.dice_roll_done()

    @staticmethod
    def dice_roll_done():
        print('roll dice done')

        enable_player_buttons(StateMachine._get_player_on_turn())

        # Set new game state
        StateMachine.game_state = GameState.player_action

    @staticmethod
    def next_player():
        for i in range(4):
            StateMachine.player_on_turn += 1

            if StateMachine.player_on_turn >= 4:
                StateMachine.player_on_turn = 0

            if StateMachine.players[StateMachine.player_on_turn].playable:
                break

    @staticmethod
    def set_dice_action():
        # Set dice color
        Dice.color = copy(StateMachine._get_player_on_turn().color)

        # Set dice animation
        dice_enable_animation()

        # Set new game state
        StateMachine.game_state = GameState.dice_action

    @staticmethod
    def start_game():
        for player in StateMachine.players:
            # Disable all buttons
            disable_player_buttons(player)

            if not player.playable:
                # Remove disabled players
                player.set_color(black_color)

        # Select first player
        StateMachine.next_player()

        # Enable dice action
        StateMachine.enable_dice(copy(StateMachine._get_player_on_turn().color))

        # Set new game state
        StateMachine.game_state = GameState.dice_action

    @staticmethod
    def select_player_color(player_number):
        # Disable player buttons, and set it playable
        disable_player_buttons(StateMachine.players[player_number])
        StateMachine.players[player_number].playable = True

    @staticmethod
    def enable_dice(color):
        # Set dice color and set default number
        Dice.color = copy(copy(color))
        Dice.set_dice_number()

        if not Dice.enabled:
            # Enable dice and set animation only if dice is not already enabled
            Dice.enable()

            # Enable dice animation
            dice_enable_animation()

    @staticmethod
    def disable_dice():
        if Dice.enabled:
            # Disable dice and dice animation
            Dice.disable()
            dice_disable_animation()

    @staticmethod
    def number_of_playable_players():
        playable_players = 0
        for player in StateMachine.players:
            if player.playable:
                playable_players += 1

        return playable_players

    @staticmethod
    def _get_player_on_turn():
        return StateMachine.players[StateMachine.player_on_turn]
