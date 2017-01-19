import random

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number

class Player:
    def __init__(self, color, x, y, w, h, name):
        self.color = color
        self.posx = x # Center position of rect
        self.posy = y # Center position of rect
        self.sizew = w
        self.sizeh = h
        self.name = name

    def update(self):
        if (self.posy <= 0):
            print(self.name + " won!")
            self.posy = 550
