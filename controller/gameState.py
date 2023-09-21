from enum import Enum


class GameState(Enum):
    select_color = 0
    dice_action = 1
    player_action = 2
