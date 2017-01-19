import random
from .gui import *

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number

class Player:
    def __init__(self, color, x, y, width, height, name):
        self.color = color
        self.position = Position(x, y)
        self.width = width
        self.height = height
        self.name = name

    def update(self):
        if self.position.y <= 0:
            print(self.name + " won!")
            self.position.y = 550
