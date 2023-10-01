from utilities import path_length


class Position:
    def __init__(self, position_type, index):
        self.type = position_type
        self.index = index

    def __eq__(self, other):
        if self.type == other.type and self.index == other.index:
            return True
        else:
            return False

    def __str__(self):
        return f'Type: {self.type}, Index: {self.index}'

    def __add__(self, other):
        index = self.index + other

        if index >= path_length*4:
            index = 0

        return Position(self.type, index)
