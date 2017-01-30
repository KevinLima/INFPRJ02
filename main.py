# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui.button import *
from assets.modules.gui.color_pallete import *
from assets.modules.gui.screen import *
from assets.modules.gui.text import *
# from assets.modules.screens.game_screen import *
from assets.modules.screens.help_screen import *
from assets.modules.screens.highscores_screen import *

# Initialize PyGame
pygame.init()

# Title screen
def main():
    # Set background
    screen.set_background(color_pallete.indigo500)

    # Create & draw Title text
    title_text = Text("INFPRJ02", color_pallete.grey50, screen.width * 0.25,
                      screen.width * 0.05, screen.height * 0.05)

    # Initialize buttons
    play_button = Button("Play")
    highscores_button = Button("Highscores")
    help_button = Button("Help")
    settings_button = Button("Settings")
    quit_button = Button("Quit")

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
                    # game_screen()

                elif highscores_button.obj.collidepoint(mouse):
                    highscores_screen()

                elif help_button.obj.collidepoint(mouse):
                    help_screen()

                elif settings_button.obj.collidepoint(mouse):
                    print("Settings button clicked")
                    # settings_screen()

                elif quit_button.obj.collidepoint(mouse):
                    print("Quit button clicked")
                    pygame.quit()
                    sys.exit()

        # Draw buttons
        play_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.5,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.5))
        highscores_button.draw(screen, mouse, (screen.width * 0.05,
                                               screen.height * 0.6,
                                               screen.width * 0.375,
                                               screen.height * 0.075),
                                               (screen.width * 0.05,
                                                screen.height * 0.6))
        help_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.7,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.7))
        settings_button.draw(screen, mouse, (screen.width * 0.05,
                                             screen.height * 0.8,
                                             screen.width * 0.375,
                                             screen.height * 0.075),
                                             (screen.width * 0.05,
                                              screen.height * 0.8))
        quit_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.9,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.9))

        pygame.display.update()
        clock.tick(60)

# Initialize title screen
main()

