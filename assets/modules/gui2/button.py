# Import PyGame module
import pygame
from pygame.locals import *

# Import required modules
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.position import *
from assets.modules.gui2.screen import *

# Initialize PyGame
pygame.init()

class Button999:
    def __init__(self, text, color=color_pallete.pink300, color_hover=color_pallete.pink500):
        self.text = text
        self.is_hover = False
        self.default_color = color
        self.hover_color = color_hover
        self.font_color = color_pallete.grey50
        self.obj = None

    def label(self):
        '''button label font'''
        font = pygame.font.Font("assets/fonts/roboto-bold.ttf", int(screen.width * 0.025))
        return font.render(self.text, 1, self.font_color)

    def color(self):
        '''change color when hovering'''
        if self.is_hover:
            return self.hover_color
        else:
            return self.default_color

    def draw(self, screen, mouse, rectcoord, labelcoord):
        '''create rect obj, draw, and change color based on input'''
        self.obj = pygame.draw.rect(screen.surface, self.color(), rectcoord)
        screen.surface.blit(self.label(), labelcoord)

        #change color if mouse over button
        self.check_hover(mouse)

    def check_hover(self, mouse):
        '''adjust is_hover value based on mouse over button - to change hover color'''
        if self.obj.collidepoint(mouse):
            self.is_hover = True
        else:
            self.is_hover = False

