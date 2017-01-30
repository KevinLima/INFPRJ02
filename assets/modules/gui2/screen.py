# Import PyGame module
import pygame
from pygame.locals import *

# Initialize PyGame
pygame.init()

class Screen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.surface = pygame.display.set_mode((self.width, self.height))
        # self.surface = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)
        self.caption = pygame.display.set_caption("INFPRJ02")

    def set_background(self, color):
        self.background = pygame.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(color)
        self.surface.blit(self.background, (0, 0))
        pygame.display.update()

    def set_background_color(self, color):
        self.background = pygame.Surface(self.surface.get_size())
        self.background = self.background.convert()
        self.background.fill(color)
        self.surface.blit(self.background, (0, 0))
        pygame.display.update()

    def set_background_image(self, image):
        self.background = pygame.image.load(image)
        screen.surface.blit(self.background, (0, 0))

    def set_caption(self, caption):
        self.caption = pygame.display.set_caption(caption)

screen = Screen()

