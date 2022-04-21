import math

from enumerator.gameState import GameState, state
from mapElements.buttons.diceButton import DiceButton
from mapElements.dice import Dice
from player import Player


class ButtonListener:
    firstRoll = True

    @staticmethod
    def buttonClicked(buttonNumber):
        playerNumber = math.floor(buttonNumber/3)
        function = buttonNumber % 3

        #None clicked
        if buttonNumber == -1:
            return

        #Dice button click
        if buttonNumber >= 12:
            if state == GameState.SelectPlayerColor:
                ButtonListener.start()
                Dice.disableFade()
                Dice.setRotation(Player.playablePlayers[Player.playerOnTurn].orderNumber)

            elif state == GameState.Game:
                if ButtonListener.firstRoll:
                    Dice.roll()
                    ButtonListener.firstRoll = False

                elif not Dice.rolling:
                    ButtonListener.next()
                    Dice.roll()

        #Left arrow click
        if function == 0:
            if state == GameState.SelectPlayerColor:
                Player.players[playerNumber].changeColorClockwise()

        # Right arrow click
        if function == 1:
            if state == GameState.SelectPlayerColor:
                Player.players[playerNumber].changeColorCounterClockwise()

        # Submit click
        if function == 2:
            if state == GameState.SelectPlayerColor:
                Player.playablePlayers.append(Player.players[playerNumber])
                Player.players[playerNumber].setPlayable()

                if len(Player.playablePlayers) >= 4:
                    ButtonListener.start()
                elif len(Player.playablePlayers) == 2:
                    DiceButton.enable()
                    Dice.setFade()
                    Dice.startRainbow()

                if len(Player.playablePlayers) >= 2:
                    Dice.setColor(Player.players[playerNumber].getHue())

    @staticmethod
    def start():
        for player in Player.players:
            if not player.isPlayable():
                player.setInactive()

        Dice.setColor(Player.playablePlayers[0].getHue())
        Dice.setRotation(Player.playerOnTurn)
        Dice.setFade()
        Dice.stopRainbow()

        global state
        state = GameState.Game

    @staticmethod
    def next():
        nextPlayer = Player.playerOnTurn + 1
        if nextPlayer >= len(Player.playablePlayers):
            nextPlayer = 0

        Player.playerOnTurn = nextPlayer
        Dice.setColor(Player.playablePlayers[Player.playerOnTurn].getHue())
        Dice.setRotation(Player.playablePlayers[Player.playerOnTurn].orderNumber)
