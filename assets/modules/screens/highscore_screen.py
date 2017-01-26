from assets.modules.events_helper import event_exist
from assets.modules.gui import *

def highscore_screen():
    # Initialize buttons
    back_button = Button("BACK", (screen.width * 0.5),
                         (screen.height - (screen.height * 0.1)),
                         (screen.width * 0.25), (screen.height * 0.1))

    # Initialize background
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    highscore_title_font = pygame.font.Font(None, int((screen.width * 0.1)))
    highscore_title_text = highscore_title_font.render("Highscores", 1, color_pallete.grey50)
    highscore_title_text_position = highscore_title_text.get_rect()
    highscore_title_text_position.centerx = background.get_rect().centerx
    highscore_title_text_position.centery = (screen.height * 0.1)
    background.blit(highscore_title_text, highscore_title_text_position)

    dummy_scores =[
        ["kevin", 1],
        ["Kevin", 2],
        ["robert", 999],
        ["carlos", 3],
        ["Donny", 3],
        ["Mo", 3],
        ["Rich", 3],
        ["Frank", 3],
        ["arnold", 3],
        ["MITCHELL", 3]
    ]

    highscore_body_font = pygame.font.Font('Courier.dfont', 30)

    # Generate surfaces
    text_surfaces = [highscore_body_font.render("{:>3d}. {:<10} - {:>4d}".format((dummy_scores.index(score)+1),
                                                                                 score[0],
                                                                                 score[1]),
                                                1, color_pallete.grey50) for score in dummy_scores]

    # Blit the text surfaces
    for index, surface in enumerate(text_surfaces):
        background.blit(surface, ((background.get_rect().centerx / 2),
                                  (index * surface.get_height()) + (int(screen.height * 0.2))))

    # Run menu loop
    run_highscore_screen = True

    while run_highscore_screen:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            print("quit button pressed")
            pygame.quit()
            exit()
        if back_button.action:
            print("back button pressed")
            run_highscore_screen = False

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
