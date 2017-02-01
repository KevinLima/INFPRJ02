import random
from .gui import Position, Size

class Dice:
    def __init__(self):
        self.name = "Dice"

    def number(self):
        self.number = random.randint(1, 6)
        return self.number