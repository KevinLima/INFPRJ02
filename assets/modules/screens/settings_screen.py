# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *
from assets.modules.screens.help_screen import *
from assets.modules.questions import *
from assets.modules.mechanics2.background_music import *

# Initialize PyGame
pygame.init()

# Title screen
def settings_screen():
    # Set background image
    screen.set_background_image("assets/images/background.png")

    # Draw question on screen
    background_music_text = Text999("Background music:",
                           "roboto-mono-regular", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.2)

    # Initialize buttons
    sound_on_button = Button999("On")
    sound_off_button = Button999("Off")
    back_button = Button999("Back")

    # Set PyGame clock
    clock = pygame.time.Clock()

    # Title screen loop
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Manually quit program")
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if sound_on_button.obj.collidepoint(mouse):
                    background_music("On")

                elif sound_off_button.obj.collidepoint(mouse):
                    background_music("Off")

                elif back_button.obj.collidepoint(mouse):
                    return

        # Draw buttons
        sound_on_button.draw(screen, mouse, (screen.width * 0.05,
                                             screen.height * 0.3,
                                             screen.width * 0.075,
                                             screen.height * 0.075),
                                             (screen.width * 0.05,
                                              screen.height * 0.3))
        sound_off_button.draw(screen, mouse, (screen.width * 0.15,
                                             screen.height * 0.3,
                                             screen.width * 0.075,
                                             screen.height * 0.075),
                                             (screen.width * 0.15,
                                              screen.height * 0.3))
        back_button.draw(screen, mouse, (screen.width * 0.8,
                                         screen.height * 0.9,
                                         screen.width * 0.15,
                                         screen.height * 0.075),
                                         (screen.width * 0.8,
                                          screen.height * 0.9))
        # Update PyGame screen
        pygame.display.update()
        clock.tick(30)

