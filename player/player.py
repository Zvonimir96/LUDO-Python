from layot import houses, button_sets
from utilities import available_colors, black_color
from .figure import Figure
from animaton import add_animation, remove_animation, AnimationType


class Player:
    def __init__(self, orderNumber):
        # Get first available color
        self.color = available_colors.pop()

        # Get house and buttons layout for player
        self.house = houses[orderNumber]
        self.buttons = button_sets[orderNumber]

        self.figures = []
        for i in range(4):
            self.figures.append(Figure(self.house.fields[i], self.color))

        self._change_color()
        self.enable_buttons()

        # LUDO can be played with two players
        # Not everyone has to play
        self.playable = False

    def change_color_left(self):
        available_colors.insert(0, self.color)
        self.color = available_colors.pop()
        self._change_color()

    def change_color_right(self):
        available_colors.append(self.color)
        self.color = available_colors.pop(0)
        self._change_color()

    def _change_color(self):
        # Change color of all buttons and figures
        for button in self.buttons:
            button.change_color(self.color)

        for figure in self.figures:
            figure.set_color(self.color)

    def disable(self):
        # Hide buttons and disable animation
        for button in self.buttons:
            button.enabled = False
            remove_animation(button)

        self.color = black_color
        self._change_color()

    def enable_buttons(self):
        for button in self.buttons:
            button.enabled = True
            add_animation(button, AnimationType.BUTTON_ENABLE)

    def disable_buttons(self):
        # Hide buttons and disable animation
        for button in self.buttons:
            button.enabled = False
            remove_animation(button)
