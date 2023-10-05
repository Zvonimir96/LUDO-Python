"""
Create data sets that contains all elements positions.
"""

from .dice import create as create_dice
from .path import create as create_path
from .house import create as create_houses
from .safeHouse import create as create_safe_house
from .buttons import create as create_buttons


def create_positions():
    create_dice()
    create_path()
    create_houses()
    create_safe_house()
    create_buttons()
