from color import Color
from enumerator.gameState import GameState, state
from figure import Figure
from mapElements.buttons.button import Button
from mapElements.dice import Dice
from mapElements.house import House
from settings import blackColor, colorChangeRate


class Player:
    players = []
    playablePlayers = []
    playerOnTurn = 0

    def __init__(self, orderNumber):
        Player.players.append(self)

        self.color = Color(colorChangeRate * orderNumber, 1, 255)
        self.playable = False

        self.orderNumber = orderNumber
        self.house = House.getHouse(orderNumber)
        self.figures = Figure.createPlayerFigures(self)

        self.buttons = [Button.buttons[3 * orderNumber], Button.buttons[3 * orderNumber + 1],
                        Button.buttons[3 * orderNumber + 2]]

        for button in self.buttons:
            button.setColor(self.getColor())

    def getOrderNumber(self):
        return self.orderNumber

    def getHue(self):
        return self.color.getHue

    def getHouse(self):
        return self.house

    def getHue(self):
        return self.color

    def getColor(self):
        return self.color.get()

    def changeColorUpScale(self):
        newColor = self.color.getHue() + colorChangeRate
        if newColor >= 1:
            newColor = 0

        for player in Player.players:
            if round(player.color.getHue(), 2) == round(newColor, 2):
                self.color.setHue(newColor)
                self.changeColorUpScale()
                return

        self.color.setHue(newColor)

    def changeColorDownScale(self):
        newColor = self.color.getHue() - colorChangeRate
        if newColor < 0:
            newColor = 1 - colorChangeRate

        for player in Player.players:
            if round(player.color.getHue(), 2) == round(newColor, 2):
                self.color.setHue(newColor)
                self.changeColorDownScale()
                return

        self.color.setHue(newColor)

    def changeColorClockwise(self):
        self.changeColorUpScale()

        for figure in self.figures:
            figure.setColor()

        for button in self.buttons:
            button.setColor(self.getColor())

    def changeColorCounterClockwise(self):
        self.changeColorDownScale()

        for figure in self.figures:
            figure.setColor()

        for button in self.buttons:
            button.setColor(self.getColor())

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
    def create():
        for i in range(4):
            Player(i)

    @staticmethod
    def start():
        for player in Player.players:
            if not player.isPlayable():
                player.setInactive()

        Player.playablePlayers[Player.playerOnTurn].enableButtons()
        Dice.setColor(Player.playablePlayers[Player.playerOnTurn].color.get())
        Dice.setFade()

        global state
        state = Player.playablePlayers[Player.playerOnTurn].orderNumber

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
