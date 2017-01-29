import random
from .gui2 import Position, Size

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number

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


