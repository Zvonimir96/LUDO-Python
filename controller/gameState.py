from enum import Enum


class GameState(Enum):
    SELECT_COLOR = 0
    DICE_ACTION = 1
    PLAYER_ACTION = 2
    CANNOT_PLAY = 3
    REPEAT_ROLL = 4
