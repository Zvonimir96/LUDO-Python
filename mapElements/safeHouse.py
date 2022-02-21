import pygame

from mapElements.field import Field

from settings import lineWidth
from settings import whiteColor
from settings import pathLength


class SafeHouse:
    safeHouses = []

    def __init__(self, fields, exitField):
        SafeHouse.safeHouses.append(self)
        self.fields = fields
        self.exitField = exitField
        self.test = 1

    def draw(self, screen):
        pygame.draw.line(screen, whiteColor, self.exitField.getPosition(), self.fields[0].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[0].getPosition(), self.fields[1].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[1].getPosition(), self.fields[2].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[2].getPosition(), self.fields[3].getPosition(), lineWidth)

        for field in self.fields:
            field.draw(screen)

    def getExitField(self):
        return self.exitField

    def getField(self, index):
        return self.fields[index]

    def changeMode(self):
        for field in self.fields:
            field.changeMode()

    @staticmethod
    def changeModes():
        for safeHouse in SafeHouse.safeHouses:
            safeHouse.changeMode()

    @staticmethod
    def drawAll(screen):
        for safeHouse in SafeHouse.safeHouses:
            safeHouse.draw(screen)

    @staticmethod
    def create(fieldMode=0):
        startIndex = 1

        offsetX = 150
        offsetY = 150
        offset = 50

        fields = [Field((500, 500 - offsetY), fieldMode),
                  Field((500, 500 - offset - offsetY), fieldMode),
                  Field((500, 500 - offset * 2 - offsetY), fieldMode),
                  Field((500, 500 - offset * 3 - offsetY), fieldMode)]
        SafeHouse(fields, Field.fields[startIndex])

        fields = [Field((500 + offsetX, 500), fieldMode),
                  Field((500 + offset + offsetX, 500), fieldMode),
                  Field((500 + offset * 2 + offsetX, 500), fieldMode),
                  Field((500 + offset * 3 + offsetX, 500), fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength])

        fields = [Field((500, 500 + offsetY), fieldMode),
                  Field((500, 500 + offset + offsetY), fieldMode),
                  Field((500, 500 + offset * 2 + offsetY), fieldMode),
                  Field((500, 500 + offset * 3 + offsetY), fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength * 2])

        fields = [Field((500 - offsetX, 500), fieldMode),
                  Field((500 - offset - offsetX, 500), fieldMode),
                  Field((500 - offset * 2 - offsetX, 500), fieldMode),
                  Field((500 - offset * 3 - offsetX, 500), fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength * 3])
