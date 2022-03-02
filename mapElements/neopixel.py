from color import Color


class Neopixel:
    def __init__(self, position):
        self.color = Color()
        self.position = position

    def setColor(self, color):
        self.color.setColor(color)

    def setFullBrightness(self):
        self.color.setFullBrightness()

    def fade(self):
        self.color.fade()

    def setHue(self, hue):
        self.color.setHue(hue)

    #Prilikom programiranja yc dodati fade