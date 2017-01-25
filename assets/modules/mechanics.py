import random

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number

class Player:
    def __init__(self, name, color, x, y, width, height):
        self.color = color
        self.position = Position(x, y)
        self.width = width
        self.height = height
        self.name = name

    def update(self):
        if self.position.y <= 0:
            print(self.name + " won!")
            self.position.y = 550

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height
