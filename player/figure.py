from copy import copy


class Figure:
    def __init__(self, field, color):
        """
        Handles figure move action.

        :param field: figure start field.
        :param color: field color.
        """

        self.color = copy(color)

        # Set field color
        self.field = field
        self.field.primary_color = self.color
        self.field.set_primary_color()

        # Arrays used for move animation
        self.move_fields = []

    def set_color(self, color):
        self.color = copy(color)
        self.field.primary_color = self.color
        self.field.set_primary_color()

    def get_color(self):
        return self.color

    def move(self):
        """
        Change figure position from start to end move position.

        :return: None
        """

        # Change start and end field
        self.move_fields.insert(0, self.field)
        self.field = self.move_fields.pop()

        # Replace primary color of start and end move fields
        self.move_fields[0].primary_color = None
        self.field.primary_color = self.color

    def set_position(self, field):
        """
        Change figure position to new field.
        Used when figure is eaten.

        :param field: figure destination.
        :return: None
        """

        # Chang color of new field
        self.field = field
        self.field.primary_color = self.color
        self.field.set_primary_color()
