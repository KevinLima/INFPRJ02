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
def help_screen():
    # Set background image
    screen.set_background_image("assets/images/background.png")

    # Initialize back button
    back_button = Button999("Back", color_pallete.pink300, color_pallete.pink500)

    # Game rules
    game_rules = [
        "Dice:",
        "-numbers 1 and 2 = 1 step in chosen direction",
        "-numbers 3 and 4 = 2 steps in chosen direction",
        "-numbers 5 and 6 = 3 steps in chosen direction",
        "",
        "There is only one player allowed in a hole. If a player ends up on another players hole, the",
        "player who was already on that hole throws a dice.",
        "The number given after throwing the dice (numbers 1 to 6) is the number the player in",
        "the hole has to go down.",
        "",
        "There are four different categories, each with its own color and questions:",
        "Blue = Sports",
        "Green = Geography",
        "Red = Entertainment",
        "Yellow = History",
        "",
        "If a category runs out of questions, move to the category on your right",
        "",
        "If the player gives a wrong answer, doesn’t understand the question or doesn’t give an ",
        "answer within 50 seconds it will be considered wrong and the turn goes to the next player."
    ]

    rules_body_font = pygame.font.Font("assets/fonts/roboto-regular.ttf", int((screen.width * 0.0175)))

    # Generate surfaces
    text_surfaces = [rules_body_font.render(rule, 1, color_pallete.grey50) for rule in game_rules]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        screen.background.blit(surface, ((screen.width * 0.1), (index * surface.get_height()) + (int(screen.height * 0.2))))
    # Display background
    screen.surface.blit(screen.background, (0, 0))

    heading = Heading("GAME RULES", screen.width * 0.125, screen.height * 0.05)

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

