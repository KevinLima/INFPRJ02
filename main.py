import pygame
from pygame.locals import *
from EventsHelper import EventExist

class Color:
    def __init__(self):
        self.grey50 = (250,250,250)
        self.indigo500 = (63,81,181)

color = Color()

def main():
    # Initialise screen
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('INFPRJ02')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color.indigo500)

    # Display text
    font = pygame.font.Font(None, 72)
    text = font.render('INFPRJ02', 1, color.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (height/4)
    background.blit(text, textpos)

    # Blit to screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while True:
        events = pygame.event.get()
        if EventExist(events, pygame.QUIT):
            pygame.quit()
            exit()

        screen.blit(background, (0, 0))
        pygame.display.flip()

main()
