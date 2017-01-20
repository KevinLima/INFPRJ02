from .events_helper import *
from .gui import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()


def intro_menu():
    # Initialize buttons
    start_button = Button("START", (screen.width * 0.5), (screen.height * 0.5), (screen.width * 0.25), (screen.height * 0.1))
    settings_button = Button("SETTINGS",  (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.125), (screen.width * 0.25), (screen.height * 0.1))
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
            pygame.quit()
            exit()

        if start_button.action:
            run_intro_menu = False

        if settings_button.action:
            settings_menu()

        # Display background
        screen.screen.blit(background, (0, 0))

        # Update menu buttons
        start_button.track_mouse()
        settings_button.track_mouse()
        exit_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(screen.screen, start_button.color, ((start_button.position.x - start_button.width * 0.5),
                                                             (start_button.position.y - start_button.height * 0.5),
                                                             start_button.width, start_button.height))
        screen.screen.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # settings_button.display()
        pygame.draw.rect(screen.screen, settings_button.color,
                         (settings_button.position.x - settings_button.width * 0.5,
                          settings_button.position.y - settings_button.height * 0.5,
                          settings_button.width, settings_button.height))
        screen.screen.blit(settings_button.textSurfaceObj, settings_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(screen.screen, exit_button.color, (exit_button.position.x - exit_button.width * 0.5,
                                                            exit_button.position.y - exit_button.height * 0.5,
                                                            exit_button.width, exit_button.height))
        screen.screen.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)


def settings_menu():
    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    font = pygame.font.Font(None, int((screen.width * 0.025)))
    text = font.render("Resolution: ", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx - (screen.width * 0.425)
    textpos.centery = background.get_rect().centery - (screen.height * 0.425)
    background.blit(text, textpos)

    # Initialize buttons
    resolution_button = Button("DEFAULT", (screen.width * 0.25), (screen.height * 0.075), (screen.width * 0.25), (screen.height * 0.1))
    back_button = Button("BACK", (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.25), (screen.width * 0.25), (screen.height * 0.1))

    # Initialize direction
    resolution = -1

    resolution_button.track_mouse()
    pygame.draw.rect(screen.screen, resolution_button.color, (
    resolution_button.position.x - resolution_button.width * 0.5, resolution_button.position.y - resolution_button.height * 0.5,
    resolution_button.width, resolution_button.height))
    screen.screen.blit(resolution_button.textSurfaceObj, resolution_button.textRectObj)

    while 1:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            pygame.quit()
            exit()
        if back_button.action:
            break
        if resolution_button.action:
            pygame.time.wait(100)
            resolution += 1
            resolution %= 4
            if resolution == 0:
                resolution_button.text = "800 x 600"
                screen.resolution(800, 600)
            elif resolution == 1:
                resolution_button.text = "1280 x 720"
                screen.resolution(1280, 720)
            elif resolution == 2:
                resolution_button.text = "1600 x 1200"
                screen.resolution(1600, 1200)
            elif resolution == 3:
                resolution_button.text = "1920 x 1080"
                screen.resolution(1920, 1080)

            resolution_button.update_text()

        # Display background
        screen.screen.blit(background, (0, 0))

        # Update menu buttons
        resolution_button.track_mouse()
        back_button.track_mouse()

        # Display buttons
        # resolution_button.display()
        pygame.draw.rect(screen.screen, resolution_button.color, ((resolution_button.position.x - resolution_button.width * 0.5), (resolution_button.position.y - resolution_button.height * 0.5), resolution_button.width, resolution_button.height))
        screen.screen.blit(resolution_button.textSurfaceObj, resolution_button.textRectObj)

        # back_button.display()
        pygame.draw.rect(screen.screen, back_button.color, (
        back_button.position.x - back_button.width * 0.5, back_button.position.y - back_button.height * 0.5, back_button.width, back_button.height))
        screen.screen.blit(back_button.textSurfaceObj, back_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)
