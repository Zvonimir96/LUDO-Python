import pygame

from utilities import white_color, path_line_width, path_field_representation, positions_path

from ..position import Position, PositionType
from ..field import Field

path_fields = []


# Create fields to be drawn
def create_path():
    file_object = open(f'{positions_path}/path.txt', 'r')

    for i, line in enumerate(file_object):
        # Split coordinates to x and y
        position_string = line.split()

        draw_position = float(position_string[0]), float(position_string[1])

        position = Position(PositionType.PATH, i)

        # Create new field and save it in path fields variable, so we can access them later
        path_fields.append(Field(draw_position, path_field_representation, position))


# Path contains fields and lines between fields
def draw_path(screen):
    draw_path_lines(screen)
    draw_path_fields(screen)


# Draw each field
def draw_path_fields(screen):
    for field in path_fields:
        field.draw(screen)


# Draw lines between fields
def draw_path_lines(screen):
    first_field_position = path_fields[0].draw_position

    # For drawing first line we need first position and second position
    # Because of formality second position is called last field position
    last_field_position = first_field_position
    for field in path_fields[1:]:
        field_position = field.draw_position
        pygame.draw.line(screen, white_color.to_rgb(), field_position, last_field_position, path_line_width)
        last_field_position = field_position

    # Connect last and first file
    pygame.draw.line(screen, white_color.to_rgb(), last_field_position, first_field_position, path_line_width)
