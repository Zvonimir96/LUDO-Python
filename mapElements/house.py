import pygame

from settings import center, whiteColor

from mapElements.field import Field

from settings import lineWidth
from settings import pathLength


class House:
    mode = 1
    fieldMode = 6
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
    def create():
        if House.mode == 0:
            startIndex = 2
            offsetFromCenter = 166
            offset = 30

            start1 = (center[0] - offsetFromCenter, center[1])
            start2 = (center[0], center[1] - offsetFromCenter)
            start3 = (center[0] + offsetFromCenter, center[1])
            start4 = (center[0], center[1] + offsetFromCenter)

            fields = [Field(start1, House.fieldMode),
                      Field((start1[0] - offset, start1[1] - offset), House.fieldMode),
                      Field((start1[0] - offset*2, start1[1]), House.fieldMode),
                      Field((start1[0] - offset, start1[1] + offset), House.fieldMode)]
            House(fields, Field.fields[startIndex])

            fields = [Field(start2, House.fieldMode),
                      Field((start2[0] - offset, start2[1] - offset), House.fieldMode),
                      Field((start2[0], start2[1] - offset * 2), House.fieldMode),
                      Field((start2[0] + offset, start2[1] - offset), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength])

            fields = [Field(start3, House.fieldMode),
                      Field((start3[0] + offset, start3[1] + offset), House.fieldMode),
                      Field((start3[0] + offset * 2, start3[1]), House.fieldMode),
                      Field((start3[0] + offset, start3[1] - offset), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength * 2])

            fields = [Field(start4, House.fieldMode),
                      Field((start4[0] + offset, start4[1] + offset), House.fieldMode),
                      Field((start4[0], start4[1] + offset * 2), House.fieldMode),
                      Field((start4[0] - offset, start4[1] + offset), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength * 3])

        if House.mode == 1:
            startIndex = 2
            offsetFromCenter = 166
            offsetX = 40
            offsetY = 40

            start1 = (center[0] - offsetFromCenter, center[1])
            start2 = (center[0], center[1] - offsetFromCenter)
            start3 = (center[0] + offsetFromCenter, center[1])
            start4 = (center[0], center[1] + offsetFromCenter)

            fields = [Field(start1, House.fieldMode),
                      Field((start1[0] - offsetX, start1[1] - offsetY), House.fieldMode),
                      Field((start1[0] - offsetX, start1[1]), House.fieldMode),
                      Field((start1[0] - offsetX, start1[1] + offsetY), House.fieldMode)]
            House(fields, Field.fields[startIndex])

            fields = [Field(start2, House.fieldMode),
                      Field((start2[0] + offsetX, start2[1] - offsetY), House.fieldMode),
                      Field((start2[0], start2[1] - offsetY), House.fieldMode),
                      Field((start2[0] - offsetX, start2[1] - offsetY), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength])

            fields = [Field(start3, House.fieldMode),
                      Field((start3[0] + offsetX, start3[1] + offsetY), House.fieldMode),
                      Field((start3[0] + offsetX, start3[1]), House.fieldMode),
                      Field((start3[0] + offsetX, start3[1] - offsetY), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength * 2])

            fields = [Field(start4, House.fieldMode),
                      Field((start4[0] - offsetX, start4[1] + offsetY), House.fieldMode),
                      Field((start4[0], start4[1] + offsetY), House.fieldMode),
                      Field((start4[0] + offsetX, start4[1] + offsetY), House.fieldMode)]
            House(fields, Field.fields[startIndex + pathLength * 3])
