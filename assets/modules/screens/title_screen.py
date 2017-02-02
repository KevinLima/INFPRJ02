# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *
from assets.modules.screens.help_screen import *
from assets.modules.screens.highscores_screen import *
from assets.modules.screens.rules_screen import *

# Initialize PyGame
pygame.init()

# Title screen
def title_screen():
    # Set background image
    screen.set_background_image("assets/images/title_screen_background.png")

    # Initialize buttons
    play_button = Button999("Play")
    highscores_button = Button999("Highscores")
    help_button = Button999("Help")
    quit_button = Button999("Quit")

    # Set PyGame clock
    clock = pygame.time.Clock()

    # Title screen loop
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.obj.collidepoint(mouse):
                    print("Play button clicked")
                    return

                elif highscores_button.obj.collidepoint(mouse):
                    highscores_screen()
                    screen.set_background_image("assets/images/title_screen_background.png")

                elif help_button.obj.collidepoint(mouse):
                    help_screen()
                    screen.set_background_image("assets/images/title_screen_background.png")

                elif quit_button.obj.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        # Draw buttons
        play_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.25,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.1,
                                          screen.height * 0.25))
        highscores_button.draw(screen, mouse, (screen.width * 0.05,
                                               screen.height * 0.35,
                                               screen.width * 0.375,
                                               screen.height * 0.075),
                                               (screen.width * 0.1,
                                                screen.height * 0.35))
        help_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.45,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.1,
                                          screen.height * 0.45))
        quit_button.draw(screen, mouse, (screen.width * 0.8,
                                         screen.height * 0.9,
                                         screen.width * 0.15,
                                         screen.height * 0.075),
                                         (screen.width * 0.85,
                                          screen.height * 0.9))

        play_icon = Text999("", "material-icons-regular", color_pallete.orange500, screen.width * 0.04, screen.width * 0.05, screen.height * 0.25)
        highscores_icon = Text999("", "material-icons-regular", color_pallete.orange500, screen.width * 0.04, screen.width * 0.05, screen.height * 0.35)
        help_icon = Text999("", "material-icons-regular", color_pallete.orange500, screen.width * 0.04, screen.width * 0.05, screen.height * 0.45)
        quit_icon = Text999("", "material-icons-regular", color_pallete.orange500, screen.width * 0.04, screen.width * 0.8, screen.height * 0.9)

        # Update PyGame screen
        pygame.display.update()
        clock.tick(30)

