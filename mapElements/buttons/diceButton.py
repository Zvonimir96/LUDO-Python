from mapElements.buttons.button import Button


class DiceButton:
    def __init__(self):
        Button.buttons.append(self)
        DiceButton.button = self

        self.buttonNumber = Button.buttonNumber
        Button.buttonNumber = Button.buttonNumber + 1

        self.position = (500, 500)
        self.width = 100
        self.height = 100

        self.enabled = False
        self.fading = False

    def isButtonClicked(self, mousePosition):
        if (self.position[0] - self.width / 2) < mousePosition[0] < (self.position[0] + self.width / 2) and \
                (self.position[1] - self.height / 2) < mousePosition[1] < (self.position[1] + self.height / 2) and \
                self.enabled:
            return self.buttonNumber
        return -1

    def fade(self):
        pass

    def draw(self, screen):
        pass

    @staticmethod
    def setFade():
        DiceButton.button.fade = True

    @staticmethod
    def disableFade():
        DiceButton.button.fade = False

    @staticmethod
    def disable():
        DiceButton.button.enabled = False

    @staticmethod
    def enable():
        DiceButton.button.enabled = True
