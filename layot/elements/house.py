import pygame

from utilities import positions_path, house_field_representation, path_line_width, white_color, house_exit_index, path_length
from ..field import Field
from .path import path_fields


# Class House is data structure that consists with two variables.
# Fields represent positions that figure can ocupy.
# Exit field represents position where figures exit house.
class House:
    def __init__(self, fields, exit_field):
        self.fields = fields

        self.exit_field = exit_field

    def draw(self, screen):
        # Draw lines between field elements in house
        pygame.draw.line(screen, white_color.to_rgb(), self.exit_field.position, self.fields[0].position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[0].position, self.fields[1].position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[1].position, self.fields[2].position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[2].position, self.fields[3].position, path_line_width)
        pygame.draw.line(screen, white_color.to_rgb(), self.fields[3].position, self.fields[0].position, path_line_width)

        # Draw all fields in house
        for field in self.fields:
            field.draw(screen)


# Create variable where houses will be saved
houses = []


def create_houses():
    file_object = open(f'{positions_path}/house.txt', 'r')

    # Create four houses
    for i in range(4):
        house_fields = []

        # Each house has four fields
        for j in range(4):
            # Read line with field coordinates
            line = file_object.readline()

            # Split coordinates to x and y
            position_string = line.split()

            position = float(position_string[0]), float(position_string[1])
            house_fields.append(Field(position, house_field_representation))
        else:
            # Create new house and save it in houses variable, so we can access them later
            houses.append(House(house_fields, path_fields[house_exit_index + path_length * i]))


# Draw all houses
def draw_houses(screen):
    for house in houses:
        house.draw(screen)
