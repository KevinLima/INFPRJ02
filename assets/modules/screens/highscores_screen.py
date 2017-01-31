# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.heading import *
from assets.modules.gui2.screen import *
from assets.modules.screens.rules_screen import *

# Initialize PyGame
pygame.init()

# Help screen
def highscores_screen():
    # Set background image
    screen.set_background_image("assets/images/help_screen_background.png")

    # Initialize back button
    back_button = Button999("Back", color_pallete.pink300, color_pallete.pink500)

    # Game rules
    dummy_scores =[
        ["kevin", 1],
        ["Kevin", 2],
        ["robert", 999],
        ["carlos", 3],
        ["Donny", 3],
        ["Mo", 3],
        ["Rich", 3],
        ["Frank", 3],
        ["arnold", 3],
        ["MITCHELL", 3]
    ]

    highscore_body_font = pygame.font.Font("assets/fonts/roboto-mono-regular.ttf", int((screen.width * 0.025)))

    # Generate surfaces
    text_surfaces = [highscore_body_font.render("{:>3d}. {:<10} - {:>4d}".format((dummy_scores.index(score)+1),
                                                                                 score[0],
                                                                                 score[1]),
                                                1, color_pallete.grey50) for score in dummy_scores]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        screen.background.blit(surface, ((screen.width * 0.1),
                                  (index * surface.get_height()) + (int(screen.height * 0.2))))

    # Display background
    screen.surface.blit(screen.background, (0, 0))

    heading = Heading("HIGHSCORES", screen.width * 0.125, screen.height * 0.05)

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

