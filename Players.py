class Player:
    def __init__(self,col,x,y,w,h):
        self.color = col
        self.posx = x # Center position of rect
        self.posy = y # Center position of rect
        self.sizew = w
        self.sizeh = h

    def update(self):
        if (self.posy < 0):
            self.posy = 550
