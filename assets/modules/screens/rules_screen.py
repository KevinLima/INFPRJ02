from assets.modules.events_helper import event_exist
from assets.modules.gui import *

def rules_screen():
    # Initialize buttons
    back_button = Button("BACK", (screen.width * 0.5),
                         (screen.height * 0.5 + screen.height * 0.25),
                         (screen.width * 0.25), (screen.height * 0.1))

    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    rules_title_font = pygame.font.Font(None, int((screen.width * 0.2)))
    rules_title_text = rules_title_font.render("Game Rules", 1, color_pallete.grey50)
    rules_title_text_position = rules_title_text.get_rect()
    rules_title_text_position.centerx = background.get_rect().centerx
    rules_title_text_position.centery = background.get_rect().centery - (screen.height * 0.25)
    background.blit(rules_title_text, rules_title_text_position)

    rules_body_font = pygame.font.Font(None, 30)
    rules_body_text = rules_body_font.render("The winner is..... \n TEst",1, color_pallete.grey50)
    rules_body_text_position = rules_body_text.get_rect()
    rules_body_text_position.centerx = background.get_rect().centerx
    rules_body_text_position.centery = rules_title_text_position.centery + 100
    background.blit(rules_body_text, rules_body_text_position)

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
        pygame.draw.rect(screen.screen, back_button.color, (back_button.position.x - back_button.width * 0.5,
                                                            back_button.position.y - back_button.height * 0.5,
                                                            back_button.width, back_button.height))
        screen.screen.blit(back_button.textSurfaceObj, back_button.textRectObj)

        pygame.display.update()
