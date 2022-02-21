from buttonListener import ButtonListener
from color import Color
from figure import Figure
from mapElements.button import Button
from mapElements.house import House
from enumerator.gameState import gameState, gameEnumerator
from settings import blackColor


class Player:
    players = []

    def __init__(self, orderNumber):
        self.color = Color()
        self.playable = False

        self.orderNumber = orderNumber
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
        if gameState == gameEnumerator[0]:
            self.changeColorClockwise()
        elif gameState == "Player" + str(self.orderNumber):
            print(self.orderNumber)
        else:
            pass

    def actionRight(self):
        if gameState == gameEnumerator[0]:
            self.changeColorCounterClockwise()
        elif gameState == "Player" + str(self.orderNumber):
            print(self.orderNumber)
        else:
            pass

    def actionConfirm(self):
        if gameState == gameEnumerator[0]:
            self.setPlayable()
        elif gameState == "Player" + str(self.orderNumber):
            print(self.orderNumber)
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
        gameEnumerator.append("Player" + str(self.orderNumber))

        self.playable = True
        self.disableButtons()

    def enableButtons(self):
        for button in self.buttons:
            button.enable()

    def disableButtons(self):
        for button in self.buttons:
            button.disable()

    def changeColor(self, color):
        for figure in self.figures:
            figure.changeColor(color)

    @staticmethod
    def startGame():
        print("asd")
        for player in Player.players:
            if not player.playable:
                player.changeColor(blackColor)
                player.disableButtons()

    @staticmethod
    def create():
        Player(0)
        Player(1)
        Player(2)
        Player(3)
