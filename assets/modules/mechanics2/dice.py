import random

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number

    def roll(self, player):
        self.number = random.randint(1, 6)
        
