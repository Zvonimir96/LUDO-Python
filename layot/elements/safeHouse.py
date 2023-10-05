import pygame

from utilities import positions_path, safe_house_field_representation, safe_house_entrance_index, path_line_width, \
    white_color, path_length

from ..position import Position, PositionType
from ..field import Field
from .path import path_fields

# Contains safe house for each player
# Safe house order is same as player order
safe_houses = []

# Location of safe houses fields position on screen
file_object = open(f'{positions_path}/safeHouse.txt', 'r')


class SafeHouse:
    def __init__(self, fields, entrance_field):
        """
        Data structure that contains fields that represent safe house, and field from where safe house is accessible.

        :param fields: positions that figure can ocupy.
        :param entrance_field: position from where safe house is accessible
        """
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

        # Draw all fields in safe house
        for field in self.fields:
            field.draw(screen)


def create_safe_houses():
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
