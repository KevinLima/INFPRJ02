from assets.modules.events_helper import event_exist
from assets.modules.gui import *

def rules_screen():
    # Initialize buttons
    back_button = Button("BACK", (screen.size.width * 0.5),
                         (screen.size.height - (screen.size.height * 0.1)), "large")

    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    rules_title_font = pygame.font.Font(None, int((screen.size.width * 0.1)))
    rules_title_text = rules_title_font.render("INSTRUCTIONS", 1, color_pallete.grey50)
    rules_title_text_position = rules_title_text.get_rect()
    rules_title_text_position.centerx = background.get_rect().centerx
    rules_title_text_position.centery =  (screen.size.height * 0.1)
    background.blit(rules_title_text, rules_title_text_position)

    # The rules
    rules = [
        "There is only one player allowed in a hole",
        "If a player ends up on another players hole,",
        "the player who was already on that hole throws a dice",
        "The number given after throwing the dice",
        "(numbers 1 to 6) is the number the player has to go down."
    ]
    rules_body_font = pygame.font.Font(None, 30)
    # Generate surfaces
    text_surfaces = [rules_body_font.render(rule, 1, color_pallete.grey50) for rule in rules]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        background.blit(surface, ((background.get_rect().centerx / 2),
                                  (index * surface.get_height()) + (int(screen.size.height * 0.2))))

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
        screen.screen.blit(background, (0, 0))

        # Update menu buttons
        back_button.track_mouse()

        # Display buttons

        # exit_button.display()
        pygame.draw.rect(screen.screen, back_button.color, (back_button.position.x - back_button.size.width * 0.5,
                                                            back_button.position.y - back_button.size.height * 0.5,
                                                            back_button.size.width, back_button.size.height))
        screen.screen.blit(back_button.textSurfaceObj, back_button.textRectObj)

        pygame.display.update()
