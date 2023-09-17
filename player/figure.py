class Figure:
    def __init__(self, start_field, color):
        self.object = start_field
        self.object.color = color

    def set_color(self, color):
        self.object.color = color



    def move(self, field):
        self.object.setColor((0, 0, 0))
        self.object = field
        self.object.setColor(())
