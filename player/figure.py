from copy import copy


class Figure:
    def __init__(self, start_field, color):
        self.field = start_field
        self.field.primary_color = copy(color)
        self.field.set_primary_color()

        self.move_fields = []

    def set_color(self, color):
        self.field.primary_color = copy(color)
        self.field.set_primary_color()

    def get_color(self):
        return copy(self.field.primary_color)
