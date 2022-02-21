from mapElements.field import Field
from settings import diceOffset
import random


class Dice:
    fields = []
    numbers = [[0],
               [3, 4],
               [0, 3, 4],
               [1, 3, 4, 6],
               [0, 1, 3, 4, 6],
               [1, 2, 3, 4, 5, 6]]

    number = 0

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
    def roll(color):
        for field in Dice.numbers[Dice.number - 1]:
            Dice.fields[field].turnOff()

        Dice.number = random.randint(1, 6)

        for field in Dice.numbers[Dice.number - 1]:
            Dice.fields[field].setColor(color)
