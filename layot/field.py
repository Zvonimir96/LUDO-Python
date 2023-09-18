import pygame
from utilities import circle_line_width, white_color, large_circle_size, small_circle_size, Color


# Field is position that figure can take
class Field:
    def __init__(self, position, circle='large'):
        self.color = Color()
        self.position = position

        # Set circle diameter dependent on required circle size
        if circle == 'large':
            self.circle_diameter = large_circle_size
        else:
            self.circle_diameter = small_circle_size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.to_rgb(), [self.position[0], self.position[1]], self.circle_diameter)
        pygame.draw.circle(screen, white_color.to_rgb(), [self.position[0], self.position[1]], self.circle_diameter, circle_line_width)
