from assets.modules.events_helper import event_exist
from assets.modules.gui import *
# Import required modules
from assets.modules.gui2.screen import *
def win_screen(winners_name):
    # Initialize buttons

    exit_button = Button("EXIT",(screen.width * 0.5),
                         (screen.height - (screen.height * 0.1)),
                         "large")

    # Initialize background
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    font = pygame.font.Font(None, int((screen.width * 0.2)))
    game_over_text = font.render("Game Over", 1, color_pallete.grey50)
    game_over_text_position = game_over_text.get_rect()
    game_over_text_position.centerx = background.get_rect().centerx
    game_over_text_position.centery = background.get_rect().centery - (screen.height * 0.25)
    background.blit(game_over_text, game_over_text_position)

    winner_font = pygame.font.Font(None, int((screen.width * 0.1)))
    winner_text = winner_font.render("The winner is..... {}".format(winners_name),1, color_pallete.grey50)
    winner_text_position = winner_text.get_rect()
    winner_text_position.centerx = background.get_rect().centerx
    winner_text_position.centery = game_over_text_position.centery + 100
    background.blit(winner_text, winner_text_position)

    # Run menu loop
    run_win_screen = True

    while run_win_screen:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            print("quit button pressed")
            pygame.quit()
            exit()

        if exit_button.action:
            print("exit button pressed")
            pygame.quit()
            exit()

        # Display background
        screen.surface.blit(background, (0, 0))

        # Update menu buttons
        exit_button.track_mouse()

        # Display buttons

        # exit_button.display()
        pygame.draw.rect(screen.surface, exit_button.color, (exit_button.position.x - exit_button.size.width * 0.5,
                                                            exit_button.position.y - exit_button.size.height * 0.5,
                                                            exit_button.size.width, exit_button.size.height))
        screen.surface.blit(exit_button.textSurfaceObj, exit_button.textRectObj)


        pygame.display.update()

