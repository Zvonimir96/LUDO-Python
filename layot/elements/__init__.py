from .path import create_path, draw_path
from .house import create_houses, draw_houses, houses
from .safeHouse import create_safe_houses, draw_safe_houses, safe_houses
from .dice import create_dice, draw_dice, dice_fields, dice_numbers

create_path()
create_houses()
create_safe_houses()
create_dice()


def draw_elements(screen):
    draw_houses(screen)
    draw_safe_houses(screen)
    draw_path(screen)
    draw_dice(screen)
