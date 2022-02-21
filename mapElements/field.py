import math
import random
import pygame

from math import sin, cos
from settings import lineWidth
from settings import whiteColor
from settings import blackColor
from settings import diceCircleDiameter


class Field:
    fields = []
    overallRotation = 0
    dRotation = 0.05

    def __init__(self, position, boxMode=0):
        Field.fields.append(self)
        self.color = (0, 0, 0)
        self.x = position[0]
        self.y = position[1]
        self.numberOfModes = 5

        self.boxMode = boxMode
        self.circleDiameter = 15
        self.circleWidth = 3

        startDeviation = 10
        deviation = 3

        self.point11 = (self.x + random.randint(startDeviation, startDeviation + deviation),
                        self.y - random.randint(startDeviation, startDeviation + deviation))
        self.point12 = (self.x - random.randint(startDeviation, startDeviation + deviation),
                        self.y - random.randint(startDeviation, startDeviation + deviation))
        self.point13 = (self.x - random.randint(startDeviation, startDeviation + deviation),
                        self.y + random.randint(startDeviation, startDeviation + deviation))
        self.point14 = (self.x + random.randint(startDeviation, startDeviation + deviation),
                        self.y + random.randint(startDeviation, startDeviation + deviation))

        squareLength = 10

        self.point21 = (self.x + squareLength, self.y - squareLength)
        self.point22 = (self.x - squareLength, self.y - squareLength)
        self.point23 = (self.x - squareLength, self.y + squareLength)
        self.point24 = (self.x + squareLength, self.y + squareLength)

        rotation = random.random() * math.pi

        self.point31 = (self.x - squareLength * cos(rotation) - squareLength * sin(rotation),
                        self.y - squareLength * sin(rotation) + squareLength * cos(rotation))
        self.point32 = (self.x - squareLength * cos(rotation) + squareLength * sin(rotation),
                        self.y - squareLength * sin(rotation) - squareLength * cos(rotation))
        self.point33 = (self.x + squareLength * cos(rotation) + squareLength * sin(rotation),
                        self.y + squareLength * sin(rotation) - squareLength * cos(rotation))
        self.point34 = (self.x + squareLength * cos(rotation) - squareLength * sin(rotation),
                        self.y + squareLength * sin(rotation) + squareLength * cos(rotation))

        Field.overallRotation = Field.overallRotation + Field.dRotation
        rotation = Field.overallRotation

        self.point41 = (self.x - squareLength * cos(rotation) - squareLength * sin(rotation),
                        self.y - squareLength * sin(rotation) + squareLength * cos(rotation))
        self.point42 = (self.x - squareLength * cos(rotation) + squareLength * sin(rotation),
                        self.y - squareLength * sin(rotation) - squareLength * cos(rotation))
        self.point43 = (self.x + squareLength * cos(rotation) + squareLength * sin(rotation),
                        self.y + squareLength * sin(rotation) - squareLength * cos(rotation))
        self.point44 = (self.x + squareLength * cos(rotation) - squareLength * sin(rotation),
                        self.y + squareLength * sin(rotation) + squareLength * cos(rotation))

    def setColor(self, color):
        self.color = color

    def draw(self, screen):
        if self.boxMode == 0:
            pygame.draw.circle(screen, self.color, [self.x, self.y], self.circleDiameter)
            pygame.draw.circle(screen, whiteColor, [self.x, self.y], self.circleDiameter, width=self.circleWidth)

        elif self.boxMode == 1:
            pygame.draw.polygon(screen, self.color, [self.point11, self.point12, self.point13, self.point14])
            pygame.draw.line(screen, whiteColor, self.point11, self.point12, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point12, self.point13, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point13, self.point14, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point14, self.point11, width=lineWidth)

        elif self.boxMode == 2:
            pygame.draw.polygon(screen, self.color, [self.point21, self.point22, self.point23, self.point24])
            pygame.draw.line(screen, whiteColor, self.point21, self.point22, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point22, self.point23, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point23, self.point24, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point24, self.point21, width=lineWidth)

        elif self.boxMode == 3:
            pygame.draw.polygon(screen, self.color, [self.point31, self.point32, self.point33, self.point34])
            pygame.draw.line(screen, whiteColor, self.point31, self.point32, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point32, self.point33, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point33, self.point34, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point34, self.point31, width=lineWidth)

        elif self.boxMode == 4:
            pygame.draw.polygon(screen, self.color, [self.point41, self.point42, self.point43, self.point44])
            pygame.draw.line(screen, whiteColor, self.point41, self.point42, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point42, self.point43, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point43, self.point44, width=lineWidth)
            pygame.draw.line(screen, whiteColor, self.point44, self.point41, width=lineWidth)

        if self.boxMode == 5:
            pygame.draw.circle(screen, self.color, [self.x, self.y], diceCircleDiameter)
            pygame.draw.circle(screen, self.color, [self.x, self.y], diceCircleDiameter, width=diceCircleDiameter)

    def getPosition(self):
        return self.x, self.y

    def changeMode(self):
        self.boxMode = self.boxMode + 1

        if self.boxMode > self.numberOfModes - 1:
            self.boxMode = 0

    def turnOff(self):
        self.setColor(blackColor)

    @staticmethod
    def getField(index):
        return Field.fields[index]

    @staticmethod
    def drawAll(screen):
        for field in Field.fields:
            field.draw(screen)
