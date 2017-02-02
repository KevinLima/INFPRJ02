from assets.modules.gui2.position import *
from assets.modules.mechanics2.event_log import *

class Player:
    def __init__(self, name, color, title, x, z, score):
        self.name = name
        self.title = title
        self.color = color
        self.coordinates = Position(x, z)
        self.score = score

    def update(self):
        # TODO: rewrite
        if self.coordinates.y <= 0:
            print(self.name + " won!")

    def relocate(self, position):
        self.coordinates = position
        #print(self.coordinates)

    def scored(self):
        self.score += 10
        event_log.add("[{}]:+10 Points".format(self.title))

    def __repr__(self):
        return "Player Obj\n Name: {}\n Color: {}\n Coordinates: {}\n Score: {}\n".format(self.name, self.color,
                                                                                          self.coordinates, self.score)

