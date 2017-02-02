# Import PyGame module
import pygame
from pygame.locals import *

# Import required modules
from assets.modules.gui2.position import *
from assets.modules.gui2.screen import *

# Initialize PyGame
pygame.init()

class Text999:
    def __init__(self, text, font, color, size, x, y):
        if font == "material-icons-regular":
            self.font = pygame.font.Font("assets/fonts/material-icons-regular.ttf", int(size))

        elif font == "roboto-mono-bold":
            self.font = pygame.font.Font("assets/fonts/roboto-mono-bold.ttf", int(size))

        elif font == "roboto-mono-regular":
            self.font = pygame.font.Font("assets/fonts/roboto-mono-regular.ttf", int(size))

        elif font == "roboto-regular":
            self.font = pygame.font.Font("assets/fonts/roboto-regular.ttf", int(size))

        elif font == "roboto-regular-bold":
            self.font = pygame.font.Font("assets/fonts/roboto-bold.ttf", int(size))

        self.text = self.font.render(text, 1, color)
        self.position = Position(x, y)
        screen.surface.blit(self.text, (self.position.x, self.position.y))
        pygame.display.update()

