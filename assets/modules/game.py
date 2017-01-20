from .events_helper import *
from .gui import *
from .mechanics import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()

# Initialize screen
# Sets game resolution (Defaults to 800,600)
screen.width, screen.height = resolution(1920, 1080)
window = pygame.display.set_mode((screen.width, screen.height))
pygame.display.set_caption("INFPRJ02")

def gameplay():
    # Initialize buttons
    quit_button = Button("QUIT",  (screen.width * 0.075), (screen.height * 0.05), (screen.width * 0.125), (screen.height * 0.05))
    dice_button = Button("ROLL DICE", (screen.width * 0.925), (screen.height * 0.75), (screen.width * 0.125), (screen.height * 0.05))
    next_turn = Button("NEXT TURN", (screen.width * 0.925), (screen.height * 0.85), (screen.width * 0.125), (screen.height * 0.05))
    direction_button = Button("DIRECTION", (screen.width * 0.925), (screen.height * 0.95), (screen.width * 0.125), (screen.height * 0.05))

    # Initialize whose turn
    turn = 0
    number_of_players = 2 # Number of players

    # Initialize direction
    direction = 1

    # Initialize Players
    player_1 = Player(color_pallete.green500, (screen.width * 0.25), (screen.height * 0.75), (screen.width * 0.0125), (screen.height * 0.05), "Player 1")
    player_2 = Player(color_pallete.blue500, (screen.width * 0.3), (screen.height * 0.75), (screen.width * 0.0125), (screen.height * 0.05), "Player 2")


    # GAME
    background = pygame.Surface(window.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)

    # MAIN GAME LOOP
    while True:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            pygame.quit()
            exit()

        # IF YOU PRESS OPTIONS, RUN STARTMENU
        if (quit_button.action):
            quit_button.action != quit_button.action
            intro_menu()

        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mousePressed1, mousePressed2, mousePressed3 = pygame.mouse.get_pressed()

        window.blit(background, (0, 0))

        # button update
        quit_button.track_mouse()

        # quit_button.display()
        pygame.draw.rect(window, quit_button.color, (quit_button.position.x - quit_button.width * 0.5, quit_button.position.y - quit_button.height * 0.5,quit_button.width,quit_button.height))
        window.blit(quit_button.textSurfaceObj, quit_button.textRectObj)

        # Dice button
        # button update
        dice_button.track_mouse()
        pygame.draw.rect(window, dice_button.color, (
        dice_button.position.x - dice_button.width * 0.5, dice_button.position.y - dice_button.height * 0.5, dice_button.width,
        dice_button.height))
        window.blit(dice_button.textSurfaceObj, dice_button.textRectObj)

        next_turn.track_mouse()
        pygame.draw.rect(window, next_turn.color, (
        next_turn.position.x - next_turn.width * 0.5, next_turn.position.y - next_turn.height * 0.5, next_turn.width, next_turn.height))
        window.blit(next_turn.textSurfaceObj, next_turn.textRectObj)

        direction_button.track_mouse()
        pygame.draw.rect(window, direction_button.color, (
        direction_button.position.x - direction_button.width * 0.5, direction_button.position.y - direction_button.height * 0.5,
        direction_button.width, direction_button.height))
        window.blit(direction_button.textSurfaceObj, direction_button.textRectObj)

        if direction_button.action:
            pygame.time.wait(100)
            direction += 1
            direction = direction % 4
            if (direction == 0):
                direction_button.text = "LEFT"
            elif (direction == 1):
                direction_button.text = "UP"
            elif (direction == 2):
                direction_button.text = "RIGHT"
            elif (direction == 3):
                direction_button.text = "DOWN"

            direction_button.update_text()
            direction_button.action = False

        if dice_button.action:
            pygame.time.wait(100)
            dice = Dice()
            dice_number = dice.number()
            dice_button.text = str(dice_number)
            dice_button.update_text()
            dice_button.action = False

            if (direction == 0):
                if turn == 0:
                    player_1.position.x -= player_1.height * dice_number
                if turn == 1:
                    player_2.position.x -= player_2.height * dice_number

            if (direction == 1):
                if turn == 0:
                    player_1.position.y -= player_1.height * dice_number
                if turn == 1:
                    player_2.position.y -= player_2.height * dice_number

            if (direction == 2):
                if turn == 0:
                    player_1.position.x += player_1.height * dice_number
                if turn == 1:
                    player_2.position.x += player_2.height * dice_number

            if (direction == 3):
                if turn == 0:
                    player_1.position.y += player_1.height * dice_number
                if turn == 1:
                    player_2.position.y += player_2.height * dice_number

        if next_turn.action:
            pygame.time.wait(100)
            turn += 1
            turn = turn % number_of_players
            next_turn.text = "Player " + str(turn + 1)
            next_turn.update_text()
            next_turn.action = False

        # Update Players
        player_1.update()
        player_2.update()
        ## draw player_1
        pygame.draw.rect(window, player_1.color, (
        player_1.position.x - player_1.width * 0.5, player_1.position.y - player_1.height * 0.5, player_1.width, player_1.height))
        pygame.draw.rect(window, player_2.color, (
        player_2.position.x - player_2.width * 0.5, player_2.position.y - player_2.height * 0.5, player_2.width, player_2.height))
        # pygame.draw.rect(window, player_1.color, (200, 200, 100, 100))

        # Display window, according to framerate
        pygame.display.update()
        fps_clock.tick(fps)

def intro_menu():
    # Initialize buttons
    start_button = Button("START", (screen.width * 0.5), (screen.height * 0.5), (screen.width * 0.25), (screen.height * 0.1))
    settings_button = Button("SETTINGS",  (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.125), (screen.width * 0.25), (screen.height * 0.1))
    exit_button = Button("EXIT", (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.25), (screen.width * 0.25), (screen.height * 0.1))

    # Initialize background
    background = pygame.Surface(window.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    # Initialize text to display
    font = pygame.font.Font(None, int((screen.width * 0.2)))
    text = font.render("INFPRJ02", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - ((screen.height * 0.25))
    background.blit(text, textpos)

    # Run menu loop
    run_intro_menu = True

    while run_intro_menu:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT) or (exit_button.action):
            pygame.quit()
            exit()

        if (start_button.action):
            start_button.action != start_button.action
            run_intro_menu = False

        if (settings_button.action):
            settings_button.action != settings_button.action
            settings_menu()

        # Display background
        window.blit(background, (0, 0))

        # Update menu buttons
        start_button.track_mouse()
        settings_button.track_mouse()
        exit_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(window, start_button.color, ((start_button.position.x - start_button.width * 0.5), (start_button.position.y - start_button.height * 0.5), start_button.width, start_button.height))
        window.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # settings_button.display()
        pygame.draw.rect(window, settings_button.color, (settings_button.position.x - settings_button.width * 0.5, settings_button.position.y - settings_button.height * 0.5, settings_button.width, settings_button.height))
        window.blit(settings_button.textSurfaceObj, settings_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(window, exit_button.color, (exit_button.position.x - exit_button.width * 0.5, exit_button.position.y - exit_button.height * 0.5, exit_button.width, exit_button.height))
        window.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)

def settings_menu():
    # Initialize background
    background = pygame.Surface(window.get_size())
    background = background.convert()
    background.fill(color_pallete.grey900)

    font = pygame.font.Font(None, int((screen.width * 0.025)))
    text = font.render("Resolution: ", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx - ((screen.width * 0.425))
    textpos.centery = background.get_rect().centery - ((screen.height * 0.425))
    background.blit(text, textpos)

    # Initialize buttons
    resolution_button = Button("START", (screen.width * 0.25), (screen.height * 0.075), (screen.width * 0.25), (screen.height * 0.1))
    back_button = Button("BACK", (screen.width * 0.5), (screen.height * 0.5 + screen.height * 0.25), (screen.width * 0.25), (screen.height * 0.1))

    # Initialize direction
    resolution = 1

    resolution_button.track_mouse()
    pygame.draw.rect(window, resolution_button.color, (
    resolution_button.position.x - resolution_button.width * 0.5, resolution_button.position.y - resolution_button.height * 0.5,
    resolution_button.width, resolution_button.height))
    window.blit(resolution_button.textSurfaceObj, resolution_button.textRectObj)

    while 1:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT) or (back_button.action):
            pygame.quit()
            exit()
        if resolution_button.action:
            pygame.time.wait(100)
            resolution += 1
            direction = resolution % 4
            if (resolution == 0):
                resolution_button.text = "800 x 600"
            elif (resolution == 1):
                resolution_button.text = "1280 x 720"
            elif (resolution == 2):
                resolution_button.text = "1600 x 1200"
            elif (resolution == 3):
                resolution_button.text = "1920 x 1080"

            resolution_button.update_text()
            resolution_button.action = False

        # Display background
        window.blit(background, (0, 0))

        # Update menu buttons
        resolution_button.track_mouse()
        back_button.track_mouse()

        # Display buttons
        # resolution_button.display()
        pygame.draw.rect(window, resolution_button.color, ((resolution_button.position.x - resolution_button.width * 0.5), (resolution_button.position.y - resolution_button.height * 0.5), resolution_button.width, resolution_button.height))
        window.blit(resolution_button.textSurfaceObj, resolution_button.textRectObj)

        # back_button.display()
        pygame.draw.rect(window, back_button.color, (
        back_button.position.x - back_button.width * 0.5, back_button.position.y - back_button.height * 0.5, back_button.width, back_button.height))
        window.blit(back_button.textSurfaceObj, back_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(fps)

