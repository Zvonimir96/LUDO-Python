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

    def setColor(self):
        self.field.setColor(self.player.getColor())

    @staticmethod
    def createPlayerFigures(player):
        figures = []

        for i in range(4):
            figures.append(Figure(player, i))

        return figures
