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

def help_screen():
    # Set background
    screen.set_background(color_pallete.red500)

    # Initialize buttons
    back_button = Button("Back")

    # Create & draw Title text
    title_text = Text("Instructions", color_pallete.grey50, screen.width * 0.125,
                      screen.width * 0.05, screen.height * 0.05)

    # TODO: Fix text not blitting
    # The rules
    rules = [
        "There is only one player allowed in a hole",
        "If a player ends up on another players hole,",
        "the player who was already on that hole throws a dice",
        "The number given after throwing the dice",
        "(numbers 1 to 6) is the number the player has to go down."
    ]
    rules_body_font = pygame.font.Font("roboto-regular.ttf", 30)
    # Generate surfaces
    text_surfaces = [rules_body_font.render(rule, 1, color_pallete.grey50) for rule in rules]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        screen.background.blit(surface, ((screen.background.get_rect().centerx / 2), (index * surface.get_height()) + (int(screen.height * 0.2))))
        # Display background
        screen.surface.blit(screen.background, (0, 0))

    clock = pygame.time.Clock()

    # Help screen loop
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.obj.collidepoint(mouse):
                    print("Back button clicked")
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

