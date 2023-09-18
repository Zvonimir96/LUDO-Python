import pygame
from utilities import white_color, path_line_width, path_field_representation, positions_path
from ..field import Field

path_fields = []


# Create fields to be drawn
def create_path():
    file_object = open(f'{positions_path}/path.txt', 'r')

    for line in file_object:
        # Split coordinates to x and y
        position_string = line.split()

        position = float(position_string[0]), float(position_string[1])

        # Create new field and save it in path fields variable, so we can access them later
        path_fields.append(Field(position, path_field_representation))


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
    first_field_position = path_fields[0].position

    # For drawing first line we need first position and second position
    # Because of formality second position is called last field position
    last_field_position = first_field_position
    for field in path_fields[1:]:
        field_position = field.position
        pygame.draw.line(screen, white_color.to_rgb(), field_position, last_field_position, path_line_width)
        last_field_position = field_position

    # Connect last and first file
    pygame.draw.line(screen, white_color.to_rgb(), last_field_position, first_field_position, path_line_width)
