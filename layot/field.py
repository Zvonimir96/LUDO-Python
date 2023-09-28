from pygame import draw
from copy import copy

from utilities import circle_line_width, white_color, large_circle_size, small_circle_size, Color


# Field is position that figure can take
class Field:
    def __init__(self, draw_position, circle='large', position=None):
        self.color = None
        self.primary_color = None
        self.secondary_color = None

        # Default color is black
        self.default_color = Color()
        self.set_default_color()

        self.draw_position = draw_position
        self.position = position

        # Set circle diameter dependent on required circle size
        if circle == 'large':
            self.circle_diameter = large_circle_size
        else:
            self.circle_diameter = small_circle_size

    def set_default_color(self):
        self.color = copy(self.default_color)

    def set_primary_color(self):
        self.color = copy(self.primary_color)

    def set_secondary_color(self):
        self.color = copy(self.secondary_color)

    def draw(self, screen):
        draw.circle(screen, self.color.to_rgb(), [self.draw_position[0], self.draw_position[1]],
                    self.circle_diameter)
        draw.circle(screen, white_color.to_rgb(), [self.draw_position[0], self.draw_position[1]],
                    self.circle_diameter, circle_line_width)
