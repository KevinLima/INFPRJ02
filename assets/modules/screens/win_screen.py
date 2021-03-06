# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.heading import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *
from assets.modules.screens.rules_screen import *
from assets.modules.mechanics2.game_over import *

# Initialize PyGame
pygame.init()

# Win screen
def win_screen(winner_name, winner_score):
    # Set background image
    screen.set_background_image("assets/images/background.png")

    # Initialize back button
    back_button = Button999("Back", color_pallete.pink300, color_pallete.pink500)

    winner = Text999("Winner: {}".format(winner_name), "roboto-regular", color_pallete.grey50, screen.width * 0.1, screen.width * 0.1, screen.height * 0.4)
    score = Text999("Score: {}".format(winner_score), "roboto-regular", color_pallete.grey50, screen.width * 0.1, screen.width * 0.1, screen.height * 0.6)


    heading = Heading("GAME OVER", screen.width * 0.125, screen.height * 0.05)

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
                if back_button.obj.collidepoint(mouse):
                    return
        game_over.clear()

        # Draw back button
        back_button.draw(screen, mouse, (screen.width * 0.8,
                                         screen.height * 0.9,
                                         screen.width * 0.15,
                                         screen.height * 0.075),
                                         (screen.width * 0.8,
                                          screen.height * 0.9))

        # Update PyGame screen
        pygame.display.update()
        clock.tick(30)

