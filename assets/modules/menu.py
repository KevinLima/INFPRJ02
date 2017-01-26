from .events_helper import *
from .gui import *
from assets.modules.screens.rules_screen import *
from assets.modules.screens.highscore_screen import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()

def title_screen():
    # Initialize buttons
    start_button = Button(" Play", screen.size.width * 0.5, screen.size.height * 0.5,
                          "large")
    rules_button = Button(" Help", screen.size.width * 0.5,
                          screen.size.height * 0.5 + screen.size.height * 0.125,
                          "large")
    highscore_button = Button("Highscores", screen.size.width * 0.5,
                              screen.size.height * 0.5 + screen.size.height * 0.25,
                              "large")
    exit_button = Button("Quit", screen.size.width * 0.5,
                         screen.size.height * 0.5 + screen.size.height * 0.375,
                         "large")

    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    font = pygame.font.Font(None, int((screen.size.width * 0.2)))
    text = font.render("EUROMAST", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (screen.size.height * 0.25)
    background.blit(text, textpos)

    # Run menu loop
    run_title_screen = True

    while run_title_screen:
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
            run_title_screen = False

        if rules_button.action:
            rules_screen()
        if highscore_button.action:
            highscore_screen()

        # Display background
        screen.screen.blit(background, (0, 0))


        # Update menu buttons
        start_button.track_mouse()
        rules_button.track_mouse()
        highscore_button.track_mouse()
        exit_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(screen.screen, start_button.color, ((start_button.position.x - start_button.size.width * 0.5),
                                                             (start_button.position.y - start_button.size.height * 0.5),
                                                             start_button.size.width, start_button.size.height))
        screen.screen.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # rules_button.display()
        pygame.draw.rect(screen.screen, rules_button.color,
                         (rules_button.position.x - rules_button.size.width * 0.5,
                          rules_button.position.y - rules_button.size.height * 0.5,
                          rules_button.size.width, rules_button.size.height))
        screen.screen.blit(rules_button.textSurfaceObj, rules_button.textRectObj)

        # highscore_button.display()
        pygame.draw.rect(screen.screen, highscore_button.color,
                         (highscore_button.position.x - highscore_button.size.width * 0.5,
                          highscore_button.position.y - highscore_button.size.height * 0.5,
                          highscore_button.size.width, highscore_button.size.height))
        screen.screen.blit(highscore_button.textSurfaceObj, highscore_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(screen.screen, exit_button.color, (exit_button.position.x - exit_button.size.width * 0.5,
                                                            exit_button.position.y - exit_button.size.height * 0.5,
                                                            exit_button.size.width, exit_button.size.height))
        screen.screen.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)

