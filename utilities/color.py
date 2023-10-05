import colorsys


class Color:
    def __init__(self, hue=0, saturation=0, value=0):
        """
        Colors are represented with HSV variables.
        With this approach it is easier to manipulate color light efects.

        :param hue: color wheel 0 - 1
        :param saturation: brightness of color 0 - 1
        :param value: intensity of color 0 - 255.
        """
        self.hue = hue
        self.saturation = saturation
        self.value = value

    def __str__(self):
        return f'Hue: {self.hue}, Saturation: {self.saturation}, Value: {self.value}'

    def __eq__(self, other):
        return self.hue == other.hue

    def to_rgb(self):
        """
        Convert color from HSV to RGB.

        :return: color in RGB.
        """
        rgbColor = colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
        return rgbColor[0], rgbColor[1], rgbColor[2]