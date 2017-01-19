from .events_helper import *
from .gui import *
from .mechanics import *
from .settings import *

# Set fps
FPS = 30  # frames per second setting
fps_clock = pygame.time.Clock()

# Initialize screen
pygame.init()
# Sets game resolution (Changeable)
width, height = resolution(1280, 720)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("INFPRJ02")

# Initialize menu buttons
def startmenu():
    start_button = Button("START", (width * 0.5), (height * 0.5), (width * 0.25), (height * 0.1))
    exit_button = Button("EXIT", (width * 0.5), (height * 0.5 + height * 0.125), (width * 0.25), (height * 0.1))
    options_button = Button("OPTIONS", (width * 0.075), (height * 0.05), (width * 0.125), (height * 0.05))
    dice_button = Button("ROLL DICE", (width * 0.925), (height * 0.75), (width * 0.125), (height * 0.05))
    next_turn = Button("NEXT TURN", (width * 0.925), (height * 0.85), (width * 0.125), (height * 0.05))
    direction_button = Button("DIRECTION", (width * 0.925), (height * 0.95), (width * 0.125), (height * 0.05))
    options_button.action != options_button.action

    # Initialize background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)

    # Initialize text to display
    font = pygame.font.Font(None, int((width * 0.1)))
    text = font.render("INFPRJ02", 1, color_pallete.grey50)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery - (height / 4)
    background.blit(text, textpos)

    # Initialize Players
    player1 = Player(color_pallete.green500, (width * 0.25), (height * 0.75), (width * 0.0125), (height * 0.05), "Player 1")
    player2 = Player(color_pallete.blue500, (width * 0.3), (height * 0.75), (width * 0.0125), (height * 0.05), "Player 2")

    # Initialize whose turn
    turn = 1
    noPlayers = 2 # Number of players

    # Initialize direction
    direction = 1

    # Run menu loop
    runStartmenu = True

    while runStartmenu:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT) or (exit_button.action):
            pygame.quit()
            exit()

        if (start_button.action):
            start_button.action != start_button.action
            runStartmenu = False

        # Display background
        screen.blit(background, (0, 0))

        # Menu buttons
        # Update buttons
        start_button.track_mouse()
        exit_button.track_mouse()
        options_button.track_mouse()

        # Display buttons
        # start_button.display()
        pygame.draw.rect(screen, start_button.color, (
        start_button.posx - start_button.sizew / 2, start_button.posy - start_button.sizeh / 2, start_button.sizew,
        start_button.sizeh))
        screen.blit(start_button.textSurfaceObj, start_button.textRectObj)

        # exit_button.display()
        pygame.draw.rect(screen, exit_button.color, (
        exit_button.posx - exit_button.sizew / 2, exit_button.posy - exit_button.sizeh / 2, exit_button.sizew,
        exit_button.sizeh))
        screen.blit(exit_button.textSurfaceObj, exit_button.textRectObj)

        # optionsButton.display()
        pygame.draw.rect(screen, options_button.color, (
        options_button.posx - options_button.sizew / 2, options_button.posy - options_button.sizeh / 2, options_button.sizew,
        options_button.sizeh))
        screen.blit(options_button.textSurfaceObj, options_button.textRectObj)

        pygame.display.update()
        fps_clock.tick(FPS)

    # GAME
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)

    # MAIN GAME LOOP
    while True:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            pygame.quit()
            exit()

        # IF YOU PRESS OPTIONS, RUN STARTMENU
        if (options_button.action):
            options_button.action != options_button.action
            startmenu()

        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mousePressed1, mousePressed2, mousePressed3 = pygame.mouse.get_pressed()

        screen.blit(background, (0, 0))

        # button update
        options_button.track_mouse()

        # options_button.display()
        pygame.draw.rect(screen, options_button.color, (options_button.posx - options_button.sizew / 2, options_button.posy - options_button.sizeh / 2,options_button.sizew,options_button.sizeh))
        screen.blit(options_button.textSurfaceObj, options_button.textRectObj)

        # Dice button
        # button update
        dice_button.track_mouse()
        pygame.draw.rect(screen, dice_button.color, (
        dice_button.posx - dice_button.sizew / 2, dice_button.posy - dice_button.sizeh / 2, dice_button.sizew,
        dice_button.sizeh))
        screen.blit(dice_button.textSurfaceObj, dice_button.textRectObj)

        next_turn.track_mouse()
        pygame.draw.rect(screen, next_turn.color, (
        next_turn.posx - next_turn.sizew / 2, next_turn.posy - next_turn.sizeh / 2, next_turn.sizew, next_turn.sizeh))
        screen.blit(next_turn.textSurfaceObj, next_turn.textRectObj)

        direction_button.track_mouse()
        pygame.draw.rect(screen, direction_button.color, (
        direction_button.posx - direction_button.sizew / 2, direction_button.posy - direction_button.sizeh / 2,
        direction_button.sizew, direction_button.sizeh))
        screen.blit(direction_button.textSurfaceObj, direction_button.textRectObj)

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
                    player1.posx -= player1.sizeh * dice_number
                if turn == 1:
                    player2.posx -= player2.sizeh * dice_number

            if (direction == 1):
                if turn == 0:
                    player1.posy -= player1.sizeh * dice_number
                if turn == 1:
                    player2.posy -= player2.sizeh * dice_number

            if (direction == 2):
                if turn == 0:
                    player1.posx += player1.sizeh * dice_number
                if turn == 1:
                    player2.posx += player2.sizeh * dice_number

            if (direction == 3):
                if turn == 0:
                    player1.posy += player1.sizeh * dice_number
                if turn == 1:
                    player2.posy += player2.sizeh * dice_number

        if next_turn.action:
            pygame.time.wait(100)
            turn += 1
            turn = turn % noPlayers
            next_turn.text = "Player " + str(turn + 1)
            next_turn.update_text()
            next_turn.action = False

        # Update Players
        player1.update()
        player2.update()
        ## draw Player1
        pygame.draw.rect(screen, player1.color, (
        player1.posx - player1.sizew / 2, player1.posy - player1.sizeh / 2, player1.sizew, player1.sizeh))
        pygame.draw.rect(screen, player2.color, (
        player2.posx - player2.sizew / 2, player2.posy - player2.sizeh / 2, player2.sizew, player2.sizeh))
        # pygame.draw.rect(screen, player1.color, (200, 200, 100, 100))

        # Display screen, according to framerate
        pygame.display.update()
        fps_clock.tick(FPS)
