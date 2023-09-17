import pygame

from utilities import positions_path, safe_house_field_representation, safe_house_entrance_index, path_line_width, \
    white_color, path_length
from .field import Field
from .path import path_fields

safe_houses = []


class SafeHouse:
    def __init__(self, fields, entrance_field):
        self.fields = fields

        # Field from where figures enter house
        self.entrance_field = entrance_field

    def draw(self, screen):
        # Draw lines between field elements in safe house
        pygame.draw.line(screen, white_color, self.entrance_field.get_position(), self.fields[0].get_position(),
                         path_line_width)
        pygame.draw.line(screen, white_color, self.fields[0].get_position(), self.fields[1].get_position(),
                         path_line_width)
        pygame.draw.line(screen, white_color, self.fields[1].get_position(), self.fields[2].get_position(),
                         path_line_width)
        pygame.draw.line(screen, white_color, self.fields[2].get_position(), self.fields[3].get_position(),
                         path_line_width)

        for field in self.fields:
            field.draw(screen)

    def get_entrance_field(self):
        return self.entrance_field

    def get_field(self, index):
        return self.fields[index]


# Create houses to be drawn
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
            position_string = line.split(', ')
            position_string[1].replace('\n', ' ')

            position = float(position_string[0]), float(position_string[1])
            house_fields.append(Field(position, safe_house_field_representation))
        else:
            # Create new safe house and save it in safe houses variable, so we can access them later
            safe_houses.append(SafeHouse(house_fields, path_fields[safe_house_entrance_index + path_length * i]))


# Draw all houses
def draw_safe_houses(screen):
    for safe_house in safe_houses:
        safe_house.draw(screen)
