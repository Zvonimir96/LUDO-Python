from copy import copy
from random import randint

from animaton import add_animation, AnimationType, remove_animation, roll_dice_animation, add_callback, animations
from dice import Dice
from layot import dice_numbers, dice_fields, PositionType
from player import Player
from utilities import dice_roll_animation_enabled, fade_alfa, fade_max_limit, fade_min_limit, fade_range

from .gameState import GameState


def get_player_on_turn():
    return StateMachine.players[StateMachine.player_on_turn]


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


def enable_figure_animation(figure):
    # Set start animation parameters

    # Set color value to the global fade rate
    value = fade_alfa
    figure.field.color.value = value
    add_animation(figure.field, AnimationType.MOVE)

    # Calculate fade step
    num_fields = len(figure.move_fields)
    step = fade_range / num_fields

    for field in figure.move_fields:
        value -= step

        # If value is lower than minimum fade rate, mirror it
        if value < fade_min_limit:
            value = fade_min_limit + fade_min_limit - value

            # Change fade step sign
            step *= -1

        # Set color value to the fade step
        field.secondary_color = figure.get_color()
        field.set_secondary_color()

        field.color.value = value
        add_animation(field, AnimationType.MOVE)


def disable_figure_animation(figure):
    # Set color value to the global fade rate
    figure.field.set_primary_color()
    remove_animation(figure.field)

    # Set color value to the proportional global fade rate
    for i in range(len(figure.move_fields)):
        # Remove field from array
        field = figure.move_fields.pop()

        # Set field color
        field.secondary_color = None
        field.set_default_color()
        remove_animation(field)


def figure_callback_max(animation):
    figure = get_player_on_turn().selected_figure

    for field in figure.move_fields:
        add_callback(field, figure_callback_min)

    remove_animation(animation.object)

    # TODO doc i provjeriti
    for player in StateMachine.players:
        if player != get_player_on_turn():
            for fig in player.figures:
                if figure.field.position == fig.field.position:
                    fig.set_position(player.get_empty_house_field())
                    break


def figure_callback_min(animation):
    figure = get_player_on_turn().selected_figure

    remove_animation(animation.object)

    if animation.object != figure.move_fields[-1]:
        return

    StateMachine.next_player()
    figure.move_fields.clear()


class StateMachine:
    game_state = GameState.SELECT_COLOR
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
        # Disable dice
        StateMachine.disable_dice()

        # Set random dice number
        Dice.number = randint(1, 6)

        Dice.number = 6

        # Roll animation is disabled only for testing purposes
        if dice_roll_animation_enabled:
            # Enable dice roll animation
            roll_dice_animation(StateMachine.dice_roll_done)

        else:
            # Dice.number = 6
            Dice.set_dice_number()
            StateMachine.dice_roll_done()

    @staticmethod
    def dice_roll_done():
        player = get_player_on_turn()

        # Enable player buttons
        enable_player_buttons(player)

        # Set new game state based on figure that is playable
        figure = player.select_figure()
        if figure is not None:
            # Set default value of reroll
            player.re_rolls = 0

            StateMachine.game_state = GameState.PLAYER_ACTION

            # Set figure animation
            enable_figure_animation(figure)

        else:
            if player.can_reroll():
                StateMachine.game_state = GameState.REPEAT_ROLL
                player.re_rolls += 1

                if player.re_rolls >= 3:
                    # Set default value of reroll
                    player.re_rolls = 0

                    StateMachine.game_state = GameState.CANNOT_PLAY
            else:
                StateMachine.game_state = GameState.CANNOT_PLAY

    @staticmethod
    def select_figure_left():
        player = get_player_on_turn()

        # Disable last figure animation
        disable_figure_animation(player.selected_figure)

        # Select new figure
        player.select_figure_left()

        # Enable new figure animation
        enable_figure_animation(player.selected_figure)

    @staticmethod
    def select_figure_right():
        player = get_player_on_turn()

        # Disable last figure animation
        disable_figure_animation(player.selected_figure)

        # Select new figure
        player.select_figure_right()

        # Enable new figure animation
        enable_figure_animation(player.selected_figure)

    @staticmethod
    def move_figure():
        player = get_player_on_turn()
        figure = player.selected_figure

        # Disable player on turn buttons
        disable_player_buttons(player)

        figure.move()
        add_callback(figure.field, figure_callback_max)

        StateMachine.game_state = GameState.MOVE_ANIMATION

    @staticmethod
    def next_player():
        if StateMachine.game_state == GameState.CANNOT_PLAY:
            disable_player_buttons(get_player_on_turn())

        for i in range(4):
            StateMachine.player_on_turn += 1

            if StateMachine.player_on_turn >= 4:
                StateMachine.player_on_turn = 0

            if StateMachine.players[StateMachine.player_on_turn].playable:
                break

        # Enable dice action
        StateMachine.enable_dice(copy(get_player_on_turn().color))

        # Set new game state
        StateMachine.game_state = GameState.DICE_ACTION

    @staticmethod
    def set_dice_action():
        player = get_player_on_turn()
        disable_player_buttons(player)

        # Disable dice animation
        dice_disable_animation()

        # Set dice color
        StateMachine.enable_dice(player.color)

        # Set new game state
        StateMachine.game_state = GameState.DICE_ACTION

    @staticmethod
    def start_game():
        for player in StateMachine.players:
            # Disable all buttons
            disable_player_buttons(player)

            if not player.playable:
                # Remove disabled players
                player.disable()

        # Select first player
        StateMachine.next_player()

    @staticmethod
    def select_player_color(player_number):
        # Disable player buttons, and set it playable
        disable_player_buttons(StateMachine.players[player_number])
        StateMachine.players[player_number].playable = True

    @staticmethod
    def enable_dice(color):
        # Set dice color and set default number
        Dice.color = copy(copy(color))
        Dice.number = 0
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
