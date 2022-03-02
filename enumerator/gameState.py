from enum import Enum


class GameState(Enum):
    SelectPlayerColor = 0
    Game = 1


state = GameState.SelectPlayerColor
