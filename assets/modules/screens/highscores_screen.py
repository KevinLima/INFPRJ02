# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui.button import *
from assets.modules.gui.color_pallete import *
from assets.modules.gui.screen import *
from assets.modules.gui.text import *

# Initialize PyGame
pygame.init()

def highscores_screen():
    # Initialize buttons
    back_button = Button("Back")

    # Initialize text to display
    highscore_title_font = pygame.font.Font(None, int((screen.width * 0.1)))
    highscore_title_text = highscore_title_font.render("Highscores", 1, color_pallete.grey50)
    highscore_title_text_position = highscore_title_text.get_rect()
    highscore_title_text_position.centerx = screen.background.get_rect().centerx
    highscore_title_text_position.centery = (screen.height * 0.1)
    screen.background.blit(highscore_title_text, highscore_title_text_position)

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

    highscore_body_font = pygame.font.Font('roboto-mono-regular.ttf', 30)

    # Generate surfaces
    text_surfaces = [highscore_body_font.render("{:>3d}. {:<10} - {:>4d}".format((dummy_scores.index(score)+1),
                                                                                 score[0],
                                                                                 score[1]),
                                                1, color_pallete.grey50) for score in dummy_scores]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        screen.background.blit(surface, ((screen.background.get_rect().centerx / 2),
                                  (index * surface.get_height()) + (int(screen.height * 0.2))))


        # Display background
        screen.surface.blit(screen.background, (0, 0))

    clock = pygame.time.Clock()
    # Highscores screen loop
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.obj.collidepoint(mouse):
                    print("Back button clicked")
                    screen.set_background(color_pallete.indigo500)
                    return

        # Draw buttons
        back_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.9,
                                         screen.width * 0.375,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.9))

        pygame.display.update()
        clock.tick(60)

