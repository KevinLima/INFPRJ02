from assets.modules.gui.position import *

class Player:
    def __init__(self, name, color, x, y, width, height):
        self.name = name
        self.color = color
        self.position = Position(x, y)
        self.width = width
        self.height = height

    def update(self):
        if self.position.y <= 0:
            print(self.name + " won!")
            self.position.y = 550

