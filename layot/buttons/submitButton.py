from .button import Button
from utilities import submit_name


class SubmitButton(Button):
    def __init__(self, position, angle):
        super().__init__(position, angle, submit_name)
