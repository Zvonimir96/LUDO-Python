import pygame

from utilities import positions_path, house_field_representation, path_line_width, white_color, house_exit_index, path_length
from .field import Field
from .path import path_fields

houses = []


# House contains four field elements
class House:
    def __init__(self, fields, exit_field):
        self.fields = fields

        # Field where figures exit house
        self.exit_field = exit_field

    def draw(self, screen):
        # Draw lines between field elements in house
        pygame.draw.line(screen, white_color, self.exit_field.get_position(), self.fields[0].get_position(), path_line_width)
        pygame.draw.line(screen, white_color, self.fields[0].get_position(), self.fields[1].get_position(), path_line_width)
        pygame.draw.line(screen, white_color, self.fields[1].get_position(), self.fields[2].get_position(), path_line_width)
        pygame.draw.line(screen, white_color, self.fields[2].get_position(), self.fields[3].get_position(), path_line_width)
        pygame.draw.line(screen, white_color, self.fields[3].get_position(), self.fields[0].get_position(), path_line_width)

        # Draw all fields in house
        for field in self.fields:
            field.draw(screen)

    def get_exit_field(self):
        return self.exit_field

    def get_field(self, index):
        return self.fields[index]


# Create houses to be drawn
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
            position_string = line.split(', ')
            position_string[1].replace('\n', ' ')

            position = float(position_string[0]), float(position_string[1])
            house_fields.append(Field(position, house_field_representation))
        else:
            # Create new house and save it in houses variable, so we can access them later
            houses.append(House(house_fields, path_fields[house_exit_index + path_length * i]))


# Draw all houses
def draw_houses(screen):
    for house in houses:
        house.draw(screen)
