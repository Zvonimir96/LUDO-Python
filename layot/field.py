import pygame

from settings import circle_line_width, white_color, black_color, large_circle_size, small_circle_size
from .neopixel import Neopixel


# Field is position that figure can take
class Field():
    def __init__(self, position, circle='large'):
        self.color = pygame.Color()
        self.position = position

        # Set circle diameter dependent on required circle size
        if circle == 'large':
            self.circle_diameter = large_circle_size
        else:
            self.circle_diameter = small_circle_size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.get_color(), [self.position[0], self.position[1]], self.circle_diameter)
        pygame.draw.circle(screen, white_color, [self.position[0], self.position[1]], self.circle_diameter, circle_line_width)



    # TODO vidjeti dali ovo sve trebam
    def setColor(self, color):
        super().setColor(color)

    def get_position(self):
        return self.position[0], self.position[1]

    def setFade(self):
        self.__fade = True

    def disableFade(self):
        self.__fade = False

    def fade(self):
        if self.__fade:
            super().fade()