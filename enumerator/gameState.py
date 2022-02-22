from enum import Enum


class GameState(Enum):
    Player0 = 0
    Player1 = 1
    Player2 = 2
    Player3 = 3
    SelectPlayerColor = 4


state = GameState.SelectPlayerColor
