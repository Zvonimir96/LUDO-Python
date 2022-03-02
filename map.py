from mapElements.buttons.diceButton import DiceButton
from mapElements.dice import Dice
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
        Dice.create()

        ArrowButton((300, 200), 45)
        ArrowButton((200, 300), 225)
        SubmitButton((250, 250), 0)

        ArrowButton((800, 300), 315)
        ArrowButton((700, 200), 135)
        SubmitButton((750, 250), 0)

        ArrowButton((700, 800), 225)
        ArrowButton((800, 700), 45)
        SubmitButton((750, 750), 0)

        ArrowButton((200, 700), 135)
        ArrowButton((300, 800), 315)
        SubmitButton((250, 750), 0)

        DiceButton()

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
