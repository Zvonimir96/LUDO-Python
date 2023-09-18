from .button import Button
from utilities import arrow_image_name


class ArrowButton(Button):
    def __init__(self, position, angle):
        super().__init__(position, angle, arrow_image_name)
