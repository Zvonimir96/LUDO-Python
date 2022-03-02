import math

from color import Color
from mapElements.field import Field
from settings import diceOffset, rainbowRate, startRollSpeed, stopRollSpeed, iterationConstant, iterationScale
import random


class Dice:
    fields = []
    numbers = [[0],
               [3, 4],
               [0, 3, 4],
               [1, 3, 4, 6],
               [0, 1, 3, 4, 6],
               [1, 2, 3, 4, 5, 6],
               [1, 2, 3, 4, 5, 6, 7]]

    animation = 1
    number = 0
    hue = 0

    iteration = 0
    changeNumberIteration = 0

    rainbow = False
    rolling = False

    @staticmethod
    def create():
        Dice.fields.append(Field((500, 500), 5))

        Dice.fields.append(Field((500 - diceOffset, 500 - diceOffset), 5))
        Dice.fields.append(Field((500 - diceOffset, 500), 5))
        Dice.fields.append(Field((500 - diceOffset, 500 + diceOffset), 5))

        Dice.fields.append(Field((500 + diceOffset, 500 - diceOffset), 5))
        Dice.fields.append(Field((500 + diceOffset, 500), 5))
        Dice.fields.append(Field((500 + diceOffset, 500 + diceOffset), 5))

    @staticmethod
    def setNumber():
        for field in Dice.numbers[6]:
            Dice.fields[field - 1].turnOff()

        for field in Dice.numbers[Dice.number - 1]:
            Dice.fields[field].setHue(Dice.hue)
            Dice.fields[field].setFullBrightness()

    @staticmethod
    def setColor(color):
        Dice.hue = color.getHue()
        for field in Dice.fields:
            field.setColor(color.get())

    @staticmethod
    def setHue(hue):
        for field in Dice.fields:
            field.setHue(hue)

    @staticmethod
    def roll():
        Dice.number = random.randint(1, 6)
        Dice.setNumber()
        Dice.rolling = True
        Dice.changeNumberIteration = startRollSpeed
        Dice.iteration = 0

    @staticmethod
    def setFade():
        for field in Dice.fields:
            field.setFade()

    @staticmethod
    def disableFade():
        for field in Dice.fields:
            field.disableFade()

    @staticmethod
    def doAnimation():
        if Dice.rolling:
            if Dice.animation == 0:
                Dice.iteration += 1
            elif Dice.animation == 1:
                Dice.iteration += iterationScale/(1 + math.exp(iterationConstant *
                                                               (startRollSpeed - (stopRollSpeed - startRollSpeed)/2)))

            if Dice.changeNumberIteration >= stopRollSpeed:
                Dice.rolling = False
            elif Dice.iteration > Dice.changeNumberIteration:
                Dice.iteration = 0
                Dice.changeNumberIteration += 1

                Dice.number += 1
                if Dice.number >= 7:
                    Dice.number = 1

                Dice.setNumber()

    @staticmethod
    def startRainbow():
        Dice.rainbow = True

    @staticmethod
    def stopRainbow():
        Dice.rainbow = False

    @staticmethod
    def doRainbow():
        if Dice.rainbow:
            Dice.hue += rainbowRate

            if Dice.hue >= 1:
                Dice.hue = 0

            Dice.setHue(Dice.hue)
