class Player:
    def __init__(self,col,x,y,w,h,n):
        self.color = col
        self.posx = x # Center position of rect
        self.posy = y # Center position of rect
        self.sizew = w
        self.sizeh = h
        self.name = n

    def update(self):
        if (self.posy < 0):
            print(self.name+" won!")
            self.posy = 550
