from assets.modules.gui.button import *
from assets.modules.gui.color_pallete import *
from assets.modules.gui.screen import *

# TODO: Remove
from assets.modules.events_helper import *
'''
from assets.modules.screens.highscore_screen import *
from assets.modules.screens.rules_screen import *
from assets.modules.screens.win_screen import *

# TODO: Remove
from assets.modules.game import *
'''

def main():
    # Uncomment te following line to demo the win screen
    #win_screen("John Doe")
    screen.set_background(color_pallete.indigo500)
    # title_screen()
    # gameplay()

# Set fps
    fps = 60  # frames per second setting
    fps_clock = pygame.time.Clock()


    # Initialize buttons
    start_button = Button("Play", screen.width * 0.5, screen.height * 0.5,
                          "large")
    rules_button = Button("Help", screen.width * 0.5,
                          screen.height * 0.5 + screen.height * 0.125,
                          "large")
    highscore_button = Button("Highscores", screen.width * 0.5,
                              screen.height * 0.5 + screen.height * 0.25,
                              "large")
    exit_button = Button("Quit", screen.width * 0.5,
                         screen.height * 0.5 + screen.height * 0.375,
                         "large")

    # Initialize background
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    font = pygame.font.Font(None, int((screen.width * 0.2)))
    text = font.render("EUROMAST", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (screen.height * 0.25)
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
        screen.surface.blit(background, (0, 0))

        # Update menu buttons
        start_button.track_mouse()
        rules_button.track_mouse()
        highscore_button.track_mouse()
        exit_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(screen.surface, start_button.color, ((start_button.position.x - start_button.width * 0.5),
                                                             (start_button.position.y - start_button.height * 0.5),
                                                             start_button.width, start_button.height))
        screen.surface.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # rules_button.display()
        pygame.draw.rect(screen.surface, rules_button.color,
                         (rules_button.position.x - rules_button.width * 0.5,
                          rules_button.position.y - rules_button.height * 0.5,
                          rules_button.width, rules_button.height))
        screen.surface.blit(rules_button.textSurfaceObj, rules_button.textRectObj)

        # highscore_button.display()
        pygame.draw.rect(screen.surface, highscore_button.color,
                         (highscore_button.position.x - highscore_button.width * 0.5,
                          highscore_button.position.y - highscore_button.height * 0.5,
                          highscore_button.width, highscore_button.height))
        screen.surface.blit(highscore_button.textSurfaceObj, highscore_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(screen.surface, exit_button.color, (exit_button.position.x - exit_button.width * 0.5,
                                                            exit_button.position.y - exit_button.height * 0.5,
                                                            exit_button.width, exit_button.height))
        screen.surface.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)

main()

