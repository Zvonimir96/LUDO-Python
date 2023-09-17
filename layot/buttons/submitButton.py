from project.layout2.buttons.button import Button
from project.utilities.settings import numberOfSubmitImages, submitImageName


class SubmitButton(Button):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, numberOfSubmitImages, submitImageName)

    def setColor(self, color):
        super().setColor(color)
