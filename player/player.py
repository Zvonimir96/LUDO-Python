from layot import houses, button_sets
from utilities import available_colors
from figure import Figure
from animaton import add_animation, remove_animation, AnimationType


class Player:
    def __init__(self, orderNumber):
        # Get first available color
        self.color = available_colors.pop()

        # Get house and buttons layout for player
        self.house = houses[orderNumber]
        self.house.change_color(self.color)
        self.buttons = button_sets[orderNumber]

        self.figures = []
        for i in range(4):
            self.figures.append(Figure(self.house.fields[i], self.color))

        for button in self.buttons:
            button.change_color(self.color)
            add_animation(button, AnimationType.BUTTON_ENABLE)

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

    def select_color(self):
        # Hide buttons and disable animation
        for button in self.buttons:
            button.enabled = False
            remove_animation(button)

    def _change_color(self):
        # Change color of all buttons and figures
        for button in self.buttons:
            button.change_color(self.color)

        for figure in self.figures:
            figure.set_color(self.color)





    def setInactive(self):
        self.disableButtons()
        self.color.setValue(0)
        for figure in self.figures:
            figure.setColor()

    def enableButtons(self):
        for button in self.buttons:
            button.enable()

    def disableButtons(self):
        for button in self.buttons:
            button.disable()

    def setPlayable(self):
        self.disableButtons()
        self.playable = True

    def isPlayable(self):
        return self.playable

    @staticmethod
    def next():
        newPlayer = Player.playerOnTurn + 1

        if newPlayer > len(Player.playablePlayers):
            newPlayer = 0

        Player.playerOnTurn = newPlayer
        Dice.setColor(Player.playerOnTurn.color.get())
        Dice.setFade()

        global state
        state = Player.playablePlayers[Player.playerOnTurn].orderNumber
