class Space:
    def __init__(self, color):
        self.empty = True
        self.player = None
        self.color = color

    def occupy(self, player):
        self.empty = False
        self.player = player
    def vacate(self):
        self.empty = True
        self.player = None

    def __repr__(self):
        return "Space Obj\n Empty: {}\n Color: {}".format(self.empty, self.color)