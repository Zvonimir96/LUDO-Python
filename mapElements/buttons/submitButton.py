from mapElements.buttons.button import Button
from settings import numberOfSubmitImages, submitImageName


class SubmitButton(Button):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, numberOfSubmitImages, submitImageName)

    def setColor(self, color):
        super().setColor(color)
