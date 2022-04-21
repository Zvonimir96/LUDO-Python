import pygame

from mapElements.field import Field

from settings import center, whiteColor

from settings import lineWidth
from settings import pathLength


class SafeHouse:
    safeHouses = []
    fieldMode = 6

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
    def create():
        startIndex = 1

        offset = 30
        offsetFromCenter = 100

        start1 = (center[0] - offsetFromCenter, center[1] - offsetFromCenter)
        start2 = (center[0] + offsetFromCenter, center[1] - offsetFromCenter)
        start3 = (center[0] + offsetFromCenter, center[1] + offsetFromCenter)
        start4 = (center[0] - offsetFromCenter, center[1] + offsetFromCenter)

        fields = [Field((start1[0], start1[1]), SafeHouse.fieldMode),
                  Field((start1[0] - offset, start1[1] - offset), SafeHouse.fieldMode),
                  Field((start1[0] - offset * 2, start1[1] - offset * 2), SafeHouse.fieldMode),
                  Field((start1[0] - offset * 3, start1[1] - offset * 3), SafeHouse.fieldMode)]
        SafeHouse(fields, Field.fields[startIndex])

        fields = [Field((start2[0], start2[1]), SafeHouse.fieldMode),
                  Field((start2[0] + offset, start2[1] - offset), SafeHouse.fieldMode),
                  Field((start2[0] + offset * 2, start2[1] - offset * 2), SafeHouse.fieldMode),
                  Field((start2[0] + offset * 3, start2[1] - offset * 3), SafeHouse.fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength])

        fields = [Field((start3[0], start3[1]), SafeHouse.fieldMode),
                  Field((start3[0] + offset, start3[1] + offset), SafeHouse.fieldMode),
                  Field((start3[0] + offset * 2, start3[1] + offset * 2), SafeHouse.fieldMode),
                  Field((start3[0] + offset * 3, start3[1] + offset * 3), SafeHouse.fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength * 2])

        fields = [Field((start4[0], start4[1]), SafeHouse.fieldMode),
                  Field((start4[0] - offset, start4[1] + offset), SafeHouse.fieldMode),
                  Field((start4[0] - offset * 2, start4[1] + offset * 2), SafeHouse.fieldMode),
                  Field((start4[0] - offset * 3, start4[1] + offset * 3), SafeHouse.fieldMode)]
        SafeHouse(fields, Field.fields[startIndex + pathLength * 3])
