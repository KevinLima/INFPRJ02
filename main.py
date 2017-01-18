import pygame
from assets.modules.gui import *
from pygame.locals import *
from EventsHelper import EventExist

color_pallete = ColorPallete()

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
    background.fill(color_pallete.indigo500)

    # Display text
    font = pygame.font.Font(None, 72)
    text = font.render('INFPRJ02', 1, color_pallete.grey50)
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
