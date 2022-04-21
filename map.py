from color import Color
from mapElements.buttons.diceButton import DiceButton
from mapElements.dice import Dice, center
from mapElements.buttons.arrowButton import ArrowButton
from mapElements.buttons.button import Button
from mapElements.field import Field
from mapElements.path import Path
from mapElements.house import House
from mapElements.safeHouse import SafeHouse
from mapElements.buttons.submitButton import SubmitButton


class Map:
    @staticmethod
    def create():
        Path.create()
        House.create()
        SafeHouse.create()

        offsetFromCenter = 260
        offset = 50

        start1 = center[0] - offsetFromCenter, center[1]
        start2 = center[0], center[1] - offsetFromCenter
        start3 = center[0] + offsetFromCenter, center[1]
        start4 = center[0], center[1] + offsetFromCenter

        ArrowButton((start1[0], start1[1] - offset), 90)
        ArrowButton((start1[0], start1[1] + offset), -90)
        SubmitButton(start1, -90)

        ArrowButton((start2[0] + offset, start2[1]), 0)
        ArrowButton((start2[0] - offset, start2[1]), 180)
        SubmitButton(start2, 180)

        ArrowButton((start3[0], start3[1] - offset), 90)
        ArrowButton((start3[0], start3[1] + offset), -90)
        SubmitButton(start3, -90)

        ArrowButton((start4[0] + offset, start4[1]), 0)
        ArrowButton((start4[0] - offset, start4[1]), 180)
        SubmitButton(start4, 0)

        DiceButton()
        Dice.create()

        for button in Button.buttons:
            if button.buttonNumber != len(Button.buttons) - 1:
                button.enable()
                button.setFade()

    @staticmethod
    def draw(screen):
        Button.drawAll(screen)
        Path.draw(screen)
        House.drawAll(screen)
        SafeHouse.drawAll(screen)
        Field.drawAll(screen)
