import pygame
from pygame.locals import *

class Button:
    def __init__(self, t, x, y, w, h):

        self.text = t;  # TEXT ON BUTTON
        self.posx = x;  # X-POSITION -- CENTER OF THE RECT
        self.posy = y;  # Y-POSITION -- CENTER OF THE RECT
        self.sizew = w;  # WIDTH
        self.sizeh = h;  # HEIGHT

        self.hover = False
        self.color = (200, 0, 0)
        self.action = False

        self.fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.textSurfaceObj = self.fontObj.render(self.text, True, (255, 255, 255), ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.posx, self.posy)

    # Detect if hover, and if mousepressed
    def trackMouse(self):
        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mousePressed1, mousePressed2, mousePressed3 = pygame.mouse.get_pressed()

        if (
                                mouseX > self.posx - self.sizew / 2 and mouseX < self.posx + self.sizew / 2 and mouseY > self.posy - self.sizeh / 2 and mouseY < self.posy + self.sizeh / 2):
            self.hover = True
            self.color = (150, 0, 0)
            if (mousePressed1):
                self.color = (255, 0, 0)
                self.action = True
                ## ENTER AN ACTION HERE
        else:
            self.hover = False
            self.color = (0, 0, 0)
            self.action = False

    # Display the button
    #def display(self):
    #    pygame.draw.rect(screen, self.color,
    #                     (self.posx - self.sizew / 2, self.posy - self.sizeh / 2, self.sizew, self.sizeh))
    #    screen.blit(self.textSurfaceObj, self.textRectObj)