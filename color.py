import colorsys

from settings import fadeRate, fadeMaxLimit, fadeMinLimit


class Color:
    def __init__(self, hue=0, saturation=0, value=0):
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.fadeUp = False

    def setHue(self, hue):
        self.hue = hue

    def setSaturation(self, saturation):
        self.saturation = saturation

    def setValue(self, value):
        self.value = value

    def fade(self):
        if self.fadeUp:
            self.value += fadeRate
        else:
            self.value -= fadeRate

        if self.value >= fadeMaxLimit:
            self.value = fadeMaxLimit
            self.fadeUp = False
        elif self.value <= fadeMinLimit:
            self.value = fadeMinLimit
            self.fadeUp = True

    def setFullBrightness(self):
        self.value = 255
        self.saturation = 1

    def setColor(self, color):
        color = colorsys.rgb_to_hsv(color[0], color[1], color[2])
        self.hue = color[0]
        self.saturation = color[1]
        self.value = color[2]

    def getHue(self):
        return self.hue

    def print(self):
        print("Hue : " + str(self.hue))
        print("Value : " + str(self.value))
        print("Saturation : " + str(self.saturation))

    def get(self):
        rgbColor = colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
        return rgbColor[0], rgbColor[1], rgbColor[2]
