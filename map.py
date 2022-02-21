from dice import Dice
from mapElements.button import Button
from mapElements.field import Field
from mapElements.path import Path
from mapElements.house import House
from mapElements.safeHouse import SafeHouse


class Map:
    @staticmethod
    def create():
        Path.create()
        House.create()
        SafeHouse.create()
        Button.create()
        Dice.create()

    @staticmethod
    def draw(screen):
        Path.draw(screen)
        House.drawAll(screen)
        SafeHouse.drawAll(screen)
        Field.drawAll(screen)
        Button.drawAll(screen)
