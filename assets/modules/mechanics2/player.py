from assets.modules.gui2.position import *

class Player:
    def __init__(self, name, color, x, y, width, height, title, X, Z):
        self.name = name
        self.title = title
        self.color = color
        self.position = Position(x, y)
        self.coordinates = Position(X, Z)
        self.width = width
        self.height = height

    def update(self):
        if self.position.y <= 0:
            print(self.name + " won!")
            self.position.y = 550

    def relocate(self, position):
        self.coordinates = position

    def __repr__(self):
        return "Player Obj\n Name: {}\n Color: {}\n Coordinates: {}\n".format(self.name, self.color, self.coordinates)

