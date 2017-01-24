from .events_helper import *
from .gui import *
from assets.modules.screens.rules_screen import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()


def intro_menu():
    # Initialize buttons
    start_button = Button("START", (screen.width * 0.5), (screen.height * 0.5), (screen.width * 0.25), (screen.height * 0.1))
    rules_button = Button("RULES",  (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.125), (screen.width * 0.25), (screen.height * 0.1))
    exit_button = Button("EXIT", (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.25), (screen.width * 0.25), (screen.height * 0.1))

    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    font = pygame.font.Font(None, int((screen.width * 0.2)))
    text = font.render("INFPRJ02", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (screen.height * 0.25)
    background.blit(text, textpos)

    # Run menu loop
    run_intro_menu = True

    while run_intro_menu:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            print("quit button pressed")
            pygame.quit()
            exit()
        if exit_button.action:
            print("exit button pressed")
            #pygame.quit()
            #exit()

        if start_button.action:
            run_intro_menu = False

        if rules_button.action:
            rules_screen()

        # Display background
        screen.screen.blit(background, (0, 0))

        # Update menu buttons
        start_button.track_mouse()
        rules_button.track_mouse()
        exit_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(screen.screen, start_button.color, ((start_button.position.x - start_button.width * 0.5),
                                                             (start_button.position.y - start_button.height * 0.5),
                                                             start_button.width, start_button.height))
        screen.screen.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # rules_button.display()
        pygame.draw.rect(screen.screen, rules_button.color,
                         (rules_button.position.x - rules_button.width * 0.5,
                          rules_button.position.y - rules_button.height * 0.5,
                          rules_button.width, rules_button.height))
        screen.screen.blit(rules_button.textSurfaceObj, rules_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(screen.screen, exit_button.color, (exit_button.position.x - exit_button.width * 0.5,
                                                            exit_button.position.y - exit_button.height * 0.5,
                                                            exit_button.width, exit_button.height))
        screen.screen.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)

