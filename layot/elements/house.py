import pygame

from utilities import positions_path, house_field_representation, path_line_width, white_color, house_exit_index, path_length

from ..position import Position, PositionType
from ..field import Field
from .path import path_fields

# Contains house for each player
# House order is same as player order
houses = []

# Location of houses fields position on screen
file_object = open(f'{positions_path}/house.txt', 'r')


class House:
    def __init__(self, fields, exit_field):
        """
        Data structure that contains fields that represent house, and field where house exit is.

        :param fields: positions that figure can ocupy.
        :param exit_field: position where figures exit house.
        """
        self.fields = fields

        self.exit_field = exit_field

    def draw(self, screen):
        # Draw lines between field elements in house
        pygame.draw.line(screen, white_color.to_rgb(), self.exit_field.draw_position, self.fields[0].draw_position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[0].draw_position, self.fields[1].draw_position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[1].draw_position, self.fields[2].draw_position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[2].draw_position, self.fields[3].draw_position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[3].draw_position, self.fields[0].draw_position, path_line_width)

        # Draw all fields in house
        for field in self.fields:
            field.draw(screen)


def create_houses():
    # Create four houses
    for i in range(4):
        house_fields = []

        # Each house has four fields
        for j in range(4):
            # Read line with field coordinates
            line = file_object.readline()

            # Split coordinates to x and y
            position_string = line.split()

            position = Position(PositionType.HOUSE, j)

            draw_position = float(position_string[0]), float(position_string[1])
            house_fields.append(Field(draw_position, house_field_representation, position))
        else:
            # Create new house and save it in houses variable, so we can access them later
            houses.append(House(house_fields, path_fields[house_exit_index + path_length * i]))


def draw_houses(screen):
    for house in houses:
        house.draw(screen)
