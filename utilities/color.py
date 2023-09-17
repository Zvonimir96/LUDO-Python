import colorsys
from project.utilities.settings import fade_rate, fade_max_limit, fade_min_limit


# Colors are represented with HSV values
# With this design we can manipulate with light effects
# Value 0 - 255
# Saturation 0 - 1
# HUE 0 - 1

class Color:
    def __init__(self, hue=0, saturation=0, value=0):
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.fadeUp = False

    def __str__(self):
        return f'Hue: {self.hue}, Value: {self.value}, Saturation: {self.saturation}'

    # Animation that allowed color to fade in or fad out
    # Fade is created by increasing or decreasing value
    # When color fully fades in then it fades out
    # When color fully fades out then it fades in
    def fade(self):
        if self.fadeUp:
            self.value += fade_rate
        else:
            self.value -= fade_rate

        if self.value >= fade_max_limit:
            self.value = fade_max_limit
            self.fadeUp = False
        elif self.value <= fade_min_limit:
            self.value = fade_min_limit
            self.fadeUp = True

    # Brightness depends on value from HSV
    # Maximum value is 255
    def set_full_brightness(self):
        self.value = 255
        self.saturation = 1

    # Color with saturation 0 is black color TODO
    def set_black_color(self):
        self.value = 0

    # Get color in RGB values
    def get_color(self):
        rgbColor = colorsys.hsv_to_rgb(self.hue, self.saturation, self.value)
        return rgbColor[0], rgbColor[1], rgbColor[2]