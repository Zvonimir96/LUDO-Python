from buttonListener import ButtonListener
from color import Color
from enumerator.gameState import GameState, state
from figure import Figure
from mapElements.button import Button
from mapElements.house import House
from settings import blackColor


class Player:
    players = []

    def __init__(self, orderNumber):
        self.color = Color()
        self.playable = False

        self.orderNumber = orderNumber
        self.enum = GameState(orderNumber)
        self.house = House.getHouse(orderNumber)
        self.figures = Figure.createPlayerFigures(self)

        self.buttons = [Button.buttons[3 * orderNumber], Button.buttons[3 * orderNumber + 1],
                        Button.buttons[3 * orderNumber + 2]]

        ButtonListener(self.actionLeft, 3 * orderNumber)
        ButtonListener(self.actionRight, 3 * orderNumber + 1)
        ButtonListener(self.actionConfirm, 3 * orderNumber + 2)

        Player.players.append(self)

        for button in self.buttons:
            button.changeColor(self.getColor())

    def actionLeft(self):
        if state is GameState.SelectPlayerColor:
            self.changeColorClockwise()
        elif state is self.enum:
            pass
        else:
            pass

    def actionRight(self):
        if state is GameState.SelectPlayerColor:
            self.changeColorCounterClockwise()
        elif state is self.enum:
            pass
        else:
            pass

    def actionConfirm(self):
        if state is GameState.SelectPlayerColor:
            self.setPlayable()
        elif state is self.enum:
            pass
        else:
            pass

    def getOrderNumber(self):
        return self.orderNumber

    def getHouse(self):
        return self.house

    def getColor(self):
        return self.color.get()

    def changeColorClockwise(self):
        self.color.changeColorClockwise()

        for figure in self.figures:
            figure.changeColor()

        for button in self.buttons:
            button.changeColor(self.getColor())

    def changeColorCounterClockwise(self):
        self.color.changeColorCounterClockwise()

        for figure in self.figures:
            figure.changeColor()

        for button in self.buttons:
            button.changeColor(self.getColor())

    def setPlayable(self):
        self.playable = True
        self.disableButtons()

    def setInactive(self):
        self.disableButtons()
        self.changeColor(blackColor)

    def enableButtons(self):
        for button in self.buttons:
            button.enable()

    def disableButtons(self):
        for button in self.buttons:
            button.disable()

    def changeColor(self, color):
        for figure in self.figures:
            figure.changeColor(color)

    def isPlayable(self):
        return self.playable

    @staticmethod
    def create():
        for i in range(4):
            Player(i)
