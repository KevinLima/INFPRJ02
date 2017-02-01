from assets.modules.gui2.position import *

class Player:
    def __init__(self, name, color, title, x, z):
        self.name = name
        self.title = title
        self.color = color
        self.coordinates = Position(x, z)

    def update(self):
        if self.coordinates.y <= 0:
            print(self.name + " won!")
            self.coordinates.y = 550

    def relocate(self, position):
        self.coordinates = position

    def __repr__(self):
        return "Player Obj\n Name: {}\n Color: {}\n Coordinates: {}\n".format(self.name, self.color, self.coordinates)

