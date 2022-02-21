import pygame

from mapElements.field import Field

from settings import lineWidth
from settings import whiteColor
from settings import pathLength


class House:
    houses = []

    def __init__(self, fields, startField):
        House.houses.append(self)
        self.fields = fields
        self.startField = startField

    def draw(self, screen):
        pygame.draw.line(screen, whiteColor, self.startField.getPosition(), self.fields[0].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[0].getPosition(), self.fields[1].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[1].getPosition(), self.fields[2].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[2].getPosition(), self.fields[3].getPosition(), lineWidth)
        pygame.draw.line(screen, whiteColor, self.fields[3].getPosition(), self.fields[0].getPosition(), lineWidth)

    def getStartField(self):
        return self.startField

    def getField(self, index):
        return self.fields[index]

    def changeMode(self):
        for field in self.fields:
            field.changeMode()

    @staticmethod
    def getHouse(index):
        return House.houses[index]

    @staticmethod
    def changeModes():
        for house in House.houses:
            house.changeMode()

    @staticmethod
    def drawAll(screen):
        for house in House.houses:
            house.draw(screen)

    @staticmethod
    def create(fieldMode=0):
        startIndex = 2

        position1 = (350, 350)
        position2 = (300, 350)
        position3 = (300, 300)
        position4 = (350, 300)

        fields = [Field(position1, fieldMode), Field(position2, fieldMode),
                  Field(position3, fieldMode), Field(position4, fieldMode)]
        House(fields, Field.fields[startIndex])

        fields = [Field((position1[0] + 300, position1[1]), fieldMode),
                  Field((position2[0] + 400, position2[1]), fieldMode),
                  Field((position3[0] + 400, position3[1]), fieldMode),
                  Field((position4[0] + 300, position4[1]), fieldMode)]
        House(fields, Field.fields[startIndex + pathLength])

        fields = [Field((position1[0] + 300, position1[1] + 300), fieldMode),
                  Field((position2[0] + 350, position2[1] + 350), fieldMode),
                  Field((position3[0] + 400, position3[1] + 400), fieldMode),
                  Field((position4[0] + 350, position4[1] + 350), fieldMode)]
        House(fields, Field.fields[startIndex + pathLength * 2])

        fields = [Field((position1[0], position1[1] + 300), fieldMode),
                  Field((position2[0], position2[1] + 300), fieldMode),
                  Field((position3[0], position3[1] + 400), fieldMode),
                  Field((position4[0], position4[1] + 400), fieldMode)]
        House(fields, Field.fields[startIndex + pathLength * 3])
