from copy import copy


class Figure:
    def __init__(self, start_field, color):
        self.color = copy(color)
        self.field = start_field
        self.field.primary_color = self.color
        self.field.set_primary_color()

        self.move_fields = []

    def set_color(self, color):
        self.field.primary_color = copy(color)
        self.field.set_primary_color()

    def get_color(self):
        return copy(self.field.primary_color)

    def move(self):
        # Change start and end field
        self.move_fields.insert(0, self.field)
        self.field = self.move_fields.pop()

        # Exchange primary color of start and end field
        self.move_fields[0].primary_color = None
        self.field.primary_color = self.color
