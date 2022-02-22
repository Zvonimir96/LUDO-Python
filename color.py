import colorsys


class Color:
    colors = []
    colorOrder = 0
    changeRate = 0.1
    V = 1
    S = 1

    def __init__(self):
        self.v = 1
        self.fadeDown = True
        self.color = Color.colorOrder * 0.25
        self.colorOrder = Color.colorOrder

        Color.colors.append(self.color)
        Color.colorOrder += 1

    def get(self):
        rgbColor = colorsys.hsv_to_rgb(self.color, Color.S, Color.V)
        return rgbColor[0] * 255, rgbColor[1] * 255, rgbColor[2] * 255

    def changeColorClockwise(self):
        newColor = self.color + Color.changeRate
        if newColor >= 1:
            newColor = 0

        self.color = newColor

        for c in Color.colors:
            if round(c, 2) == round(newColor, 2):
                self.changeColorClockwise()

        Color.colors[self.colorOrder] = self.color

    def changeColorCounterClockwise(self):
        newColor = self.color - Color.changeRate
        if newColor < 0:
            newColor = 1 - Color.changeRate

        self.color = newColor

        for c in Color.colors:
            if round(c, 2) == round(newColor, 2):
                self.changeColorCounterClockwise()

        Color.colors[self.colorOrder] = self.color
