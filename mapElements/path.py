import pygame
import math

from settings import center, whiteColor

from mapElements.field import Field

from settings import lineWidth
from settings import pathLength


class Path:
    fields = []

    @staticmethod
    def changeModes():
        for field in Path.fields:
            field.changeMode()

    @staticmethod
    def draw(screen):
        lastPosition = -1
        for field in Path.fields:
            if lastPosition != -1:
                pygame.draw.line(screen, whiteColor, field.getPosition(), lastPosition, lineWidth)
            else:
                firstPoint = field.getPosition()

            lastPosition = field.getPosition()

        pygame.draw.line(screen, whiteColor, lastPosition, firstPoint, lineWidth)

    @staticmethod
    def create(fieldMode=0):
        offsetFromCenter = 75
        offsetX = 450
        offsetY = 180

        bezUp = Bezier((center[0] - offsetFromCenter, center[1]),
                       (center[0] - offsetX, center[1] - offsetY),
                       (center[0] - offsetY, center[1] - offsetX),
                       (center[0], center[1] - offsetFromCenter))
        bezLeft = Bezier((center[0], center[1] - offsetFromCenter),
                         (center[0] + offsetY, center[1] - offsetX),
                         (center[0] + offsetX, center[1] - offsetY),
                         (center[0] + offsetFromCenter, center[1]))
        bezDown = Bezier((center[0] + offsetFromCenter, center[1]),
                         (center[0] + offsetX, center[1] + offsetY),
                         (center[0] + offsetY, center[1] + offsetX),
                         (center[0], center[1] + offsetFromCenter))
        bezRight = Bezier((center[0], center[1] + offsetFromCenter),
                          (center[0] - offsetY, center[1] + offsetX),
                          (center[0] - offsetX, center[1] + offsetY),
                          (center[0] - offsetFromCenter, center[1]))

        x1 = 1
        x2 = int(math.ceil(pathLength / 2))
        y1 = 0.5
        y2 = 1.42
        summ = [0] * 1

        for i in range(pathLength):
            if i < pathLength / 2:
                x = i + 1
            else:
                x = pathLength - i

            scale = (y2 - y1) / (x2 - x1) * (x - x1) + y1
            step = 1 / (pathLength - 1) * scale
            summ.append(summ[i] + step)

        for i in range(pathLength):
            Path.fields.append(Field(bezUp.calc(summ[i]), fieldMode))

        for i in range(pathLength):
            Path.fields.append(Field(bezLeft.calc(summ[i]), fieldMode))

        for i in range(pathLength):
            Path.fields.append(Field(bezDown.calc(summ[i]), fieldMode))

        for i in range(pathLength):
            Path.fields.append(Field(bezRight.calc(summ[i]), fieldMode))


class Bezier:
    def __init__(self, P0, P1, P2, P3):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2
        self.P3 = P3

    def calc(self, t):
        return ((1 - t) ** 3 * self.P0[0] + 3 * t * (1 - t) ** 2 * self.P1[0] + 3 * t ** 2 * (1 - t) * self.P2[
            0] + t ** 3 * self.P3[0],
                (1 - t) ** 3 * self.P0[1] + 3 * t * (1 - t) ** 2 * self.P1[1] + 3 * t ** 2 * (1 - t) * self.P2[
                    1] + t ** 3 * self.P3[1])
