class Figure:
    def __init__(self, player, figureOrder):
        self.player = player
        self.figureOrder = figureOrder
        self.field = player.getHouse().getField(figureOrder)

        self.field.setColor(player.getColor())

    def move(self, field):
        self.field.setColor((0, 0, 0))
        self.field = field
        self.field.setColor(())

    def changeColor(self, color=None):
        if color is None:
            self.field.setColor(self.player.getColor())
        else:
            self.field.setColor(color)

    @staticmethod
    def createPlayerFigures(player):
        return [Figure(player, 0), Figure(player, 1), Figure(player, 2), Figure(player, 3)]
