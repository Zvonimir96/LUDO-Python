class Figure:
    def __init__(self, start_field, color):
        self.field = start_field
        self.field.color = color

    def set_color(self, color):
        self.field.color = color
