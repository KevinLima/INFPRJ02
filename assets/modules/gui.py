import pygame
from pygame.locals import *

class Button:
    def __init__(self, text, x, y, width, height):

        self.text = text;  # TEXT ON BUTTON
        self.posx = x;  # X-POSITION -- CENTER OF THE RECT
        self.posy = y;  # Y-POSITION -- CENTER OF THE RECT
        self.sizew = width;  # WIDTH
        self.sizeh = height;  # HEIGHT

        self.hover = False
        self.color = (200, 0, 0)
        self.action = False

        self.fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
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
                self.color = color_pallete.red500
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

class ColorPallete:
    def __init__(self):
        self.grey50 = (250, 250, 250)
        self.indigo500 = (63, 81, 181)
        self.red500 = (244, 67, 54)

color_pallete = ColorPallete()
