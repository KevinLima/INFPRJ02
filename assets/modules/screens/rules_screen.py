from assets.modules.events_helper import event_exist
from assets.modules.gui import *
# Import required modules
from assets.modules.gui2.screen import *

def rules_screen():
    # Initialize buttons
    back_button = Button("BACK", (screen.width * 0.5),
                         (screen.height - (screen.height * 0.1)), "large")

    # Initialize background
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    rules_title_font = pygame.font.Font(None, int((screen.width * 0.1)))
    rules_title_text = rules_title_font.render("INSTRUCTIONS", 1, color_pallete.grey50)
    rules_title_text_position = rules_title_text.get_rect()
    rules_title_text_position.centerx = background.get_rect().centerx
    rules_title_text_position.centery =  (screen.height * 0.1)
    background.blit(rules_title_text, rules_title_text_position)

    # The rules
    rules = [
        "Dice:",
        "-numbers 1 and 2 = 1 step in chosen direction",
        "-numbers 3 and 4 = 2 steps in chosen direction",
        "-numbers 5 and 6 = 3 steps in chosen direction",
        "                                             ",
        "There is only one player allowed in a hole. If a player ends up on another players hole, the",
        "player who was already on that hole throws a dice.",
        "The number given after throwing the dice (numbers 1 to 6) is the number the player in",
        "the hole has to go down.",
        " ",
        "There are four different categories, each with its own color and questions:",
        "Blue = Sports",
        "Green = Geography",
        "Red = Entertainment",
        "Yellow = History",
        " ",
        "If a category runs out of questions, move to the category on your right",
        " "
    ]
    rules_body_font = pygame.font.Font("assets/fonts/roboto-regular.ttf", int((screen.width * 0.0175)))
    # Generate surfaces
    text_surfaces = [rules_body_font.render(rule, 1, color_pallete.grey50) for rule in rules]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        background.blit(surface, ((background.get_rect().centerx / 2),
                                  (index * surface.get_height()) + (int(screen.height * 0.2))))

    # Run menu loop
    run_rules_screen = True

    while run_rules_screen:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            print("quit button pressed")
            pygame.quit()
            exit()
        if back_button.action:
            print("back button pressed")
            run_rules_screen = False
        # Display background
        screen.surface.blit(background, (0, 0))

        # Update menu buttons
        back_button.track_mouse()

        # Display buttons

        # exit_button.display()
        pygame.draw.rect(screen.surface, back_button.color, (back_button.position.x - back_button.size.width * 0.5,
                                                            back_button.position.y - back_button.size.height * 0.5,
                                                            back_button.size.width, back_button.size.height))
        screen.surface.blit(back_button.textSurfaceObj, back_button.textRectObj)

        pygame.display.update()
