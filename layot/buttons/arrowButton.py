from project.layout2.buttons.button import Button
from project.utilities.settings import numberOfArrowImages, arrowImageName


class ArrowButton(Button):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, numberOfArrowImages, arrowImageName)

    def setColor(self, color):
        super().setColor(color)
