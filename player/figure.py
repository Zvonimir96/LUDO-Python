from copy import copy


class Figure:
    def __init__(self, start_field, color):
        self.field = start_field
        self.field.primary_color = copy(color)
        self.field.set_primary_color()

        self.next_field = None

    def set_color(self, color):
        self.field.primary_color = copy(color)
        self.field.set_primary_color()
