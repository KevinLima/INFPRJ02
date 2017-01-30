# Import PyGame module
import pygame
from pygame.locals import *

# Import required modules
from assets.modules.gui2.position import *
from assets.modules.gui2.screen import *

# Initialize PyGame
pygame.init()

class Text:
    def __init__(self, text, color, size, x, y):
        self.font = pygame.font.SysFont("roboto-regular", int(size))
        self.text = self.font.render(text, 1, color)
        self.position = Position(x, y)
        screen.surface.blit(self.text, (self.position.x, self.position.y))
        pygame.display.update()

'''
text = Text("Text", color_pallete.grey50, screen.width * 0.25,
            screen.width * 0.25, screen.height * 0.25)
'''

