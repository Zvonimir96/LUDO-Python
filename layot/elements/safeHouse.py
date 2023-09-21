import pygame

from utilities import positions_path, safe_house_field_representation, safe_house_entrance_index, path_line_width, \
    white_color, path_length

from ..position import Position, PositionType
from ..field import Field
from .path import path_fields


# Class SafeHouse is data structure that consists with two variables.
# Fields represent positions that figure can ocupy.
# Exit field represents position from where figure can enter safe house.


class SafeHouse:
    def __init__(self, fields, entrance_field):
        self.fields = fields

        # Field from where figures enter house
        self.entrance_field = entrance_field

    def draw(self, screen):
        # Draw lines between field elements in safe house
        pygame.draw.line(screen, white_color.to_rgb(), self.entrance_field.draw_position, self.fields[0].draw_position,
                         path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[0].draw_position, self.fields[1].draw_position,
                         path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[1].draw_position, self.fields[2].draw_position,
                         path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[2].draw_position, self.fields[3].draw_position,
                         path_line_width)

        for field in self.fields:
            field.draw(screen)


# Create houses to be drawn
safe_houses = []


def create_safe_houses():
    file_object = open(f'{positions_path}/safeHouse.txt', 'r')

    # Create four safe houses
    for i in range(4):
        house_fields = []

        # Each house has four fields
        for j in range(4):
            # Read line with field coordinates
            line = file_object.readline()

            # Split coordinates to x and y
            position_string = line.split()

            position = Position(PositionType.SAFE_HOUSE, j)

            draw_position = float(position_string[0]), float(position_string[1])
            house_fields.append(Field(draw_position, safe_house_field_representation, position))
        else:
            # Create new safe house and save it in safe houses variable, so we can access them later
            safe_houses.append(SafeHouse(house_fields, path_fields[safe_house_entrance_index + path_length * i]))


# Draw all houses
def draw_safe_houses(screen):
    for safe_house in safe_houses:
        safe_house.draw(screen)
