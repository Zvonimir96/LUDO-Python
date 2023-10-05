"""
Package dedicated for animations that updates independently of game loop.
"""

from .animations import add_animation, remove_animation, animations, add_callback
from .animationType import AnimationType
from .loop import update, roll_dice_animation
