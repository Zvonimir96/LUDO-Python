from pygame import draw
from copy import copy

from utilities import circle_line_width, white_color, large_circle_size, small_circle_size, Color


class Field:
    def __init__(self, draw_position, circle='large', position=None):
        """
        Field is position on board that can change color.

        :param draw_position: position on screen where field will be drawn.
        :param circle: field draw size.
        :param position: logical position in mesh.
        """

        # Color that will be drawn
        self.color = None

        # Color of figure on that field
        self.primary_color = None

        # Color only used for animation
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
        """
        Set field color to default color.

        :return: None
        """

        self.color = copy(self.default_color)

    def set_primary_color(self):
        """
        Set field color to primary color.

        :return: None
        """

        self.color = copy(self.primary_color)

    def set_secondary_color(self):
        """
        Set field color to secondary color.

        :return: None
        """

        self.color = copy(self.secondary_color)

    def draw(self, screen):
        # Draw field color
        draw.circle(screen, self.color.to_rgb(), [self.draw_position[0], self.draw_position[1]],
                    self.circle_diameter)

        # Draw field edge
        draw.circle(screen, white_color.to_rgb(), [self.draw_position[0], self.draw_position[1]],
                    self.circle_diameter, circle_line_width)
