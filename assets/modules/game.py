from assets.modules.screens.win_screen import *
from assets.modules.screens.rules_screen import *
from assets.modules.screens.highscore_screen import *
from .menu import *
from .gui import *
from .mechanics import Dice, Player

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()

# Initialize screen
pygame.display.set_caption("INFPRJ02")


def gameplay():
    # Initialize buttons
    quit_button = Button("QUIT", screen.size.width * 0.075, screen.size.height * 0.05,
                        "medium")

    rules_button = Button("Rules", screen.size.width * 0.75, screen.size.height * 0.05,
                          "medium")

    dice_button = Button("ROLL DICE", screen.size.width * 0.925,
                         screen.size.height * 0.75, "medium")

    next_turn = Button("NEXT TURN", screen.size.width * 0.925, screen.size.height * 0.85,
                       "medium")

    direction_button = Button("DIRECTION", screen.size.width * 0.925,
                              screen.size.height * 0.95, "medium")

    # Initialize whose turn
    turn = 0
    number_of_players = 2

    # Initialize direction
    direction = 1

    # Initialize Players
    player_1 = Player("Player 1", color_pallete.green500, screen.size.width * 0.25,
                      screen.size.height * 0.75, screen.size.width * 0.0125,
                      screen.size.height * 0.05)
    player_2 = Player("Player 2", color_pallete.blue500, screen.size.width * 0.3,
                      screen.size.height * 0.75, screen.size.width * 0.0125,
                      screen.size.height * 0.05)


    # GAME
    background = pygame.Surface(screen.screen.get_size())
    background = background.convert()
    background.fill(color_pallete.indigo500)

    # MAIN GAME LOOP
    while True:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            pygame.quit()
            exit()

        # IF YOU PRESS OPTIONS, RUN STARTMENU
        if quit_button.action:
            title_screen()

        # Show the rules screen
        if rules_button.action:
            rules_screen()

        # Get mouse values
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        mouse_pressed_1, mouse_pressed_2, mouse_pressed_3 = pygame.mouse.get_pressed()

        screen.screen.blit(background, (0, 0))

        # button update
        quit_button.track_mouse()

        # quit_button.display()
        pygame.draw.rect(screen.screen, quit_button.color, (quit_button.position.x - quit_button.size.width * 0.5,
                                                            quit_button.position.y - quit_button.size.height * 0.5,
                                                            quit_button.size.width, quit_button.size.height))
        screen.screen.blit(quit_button.textSurfaceObj, quit_button.textRectObj)

        # button update
        rules_button.track_mouse()
        # rules_button.display()
        pygame.draw.rect(screen.screen, rules_button.color, (rules_button.position.x - rules_button.size.width * 0.5,
                                                             rules_button.position.y - rules_button.size.height * 0.5,
                                                             rules_button.size.width, rules_button.size.height))
        screen.screen.blit(rules_button.textSurfaceObj, rules_button.textRectObj)

        # Dice button
        # button update
        dice_button.track_mouse()
        pygame.draw.rect(screen.screen, dice_button.color, (
            dice_button.position.x - dice_button.size.width * 0.5, dice_button.position.y - dice_button.size.height * 0.5,
            dice_button.size.width, dice_button.size.height))
        screen.screen.blit(dice_button.textSurfaceObj, dice_button.textRectObj)

        next_turn.track_mouse()
        pygame.draw.rect(screen.screen, next_turn.color, (
            next_turn.position.x - next_turn.size.width * 0.5, next_turn.position.y - next_turn.size.height * 0.5,
            next_turn.size.width, next_turn.size.height))
        screen.screen.blit(next_turn.textSurfaceObj, next_turn.textRectObj)

        direction_button.track_mouse()
        pygame.draw.rect(screen.screen, direction_button.color, (
            direction_button.position.x - direction_button.size.width * 0.5,
            direction_button.position.y - direction_button.size.height * 0.5,
            direction_button.size.width, direction_button.size.height))
        screen.screen.blit(direction_button.textSurfaceObj, direction_button.textRectObj)

        if direction_button.action:
            pygame.time.wait(100)
            direction += 1
            direction %= 4
            if direction == 0:
                direction_button.text = "LEFT"
            elif direction == 1:
                direction_button.text = "UP"
            elif direction == 2:
                direction_button.text = "RIGHT"
            elif direction == 3:
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

            if direction == 0:
                if turn == 0:
                    player_1.position.x -= player_1.height * dice_number
                if turn == 1:
                    player_2.position.x -= player_2.height * dice_number

            if direction == 1:
                if turn == 0:
                    player_1.position.y -= player_1.height * dice_number
                if turn == 1:
                    player_2.position.y -= player_2.height * dice_number

            if direction == 2:
                if turn == 0:
                    player_1.position.x += player_1.height * dice_number
                if turn == 1:
                    player_2.position.x += player_2.height * dice_number

            if direction == 3:
                if turn == 0:
                    player_1.position.y += player_1.height * dice_number
                if turn == 1:
                    player_2.position.y += player_2.height * dice_number

        if next_turn.action:
            pygame.time.wait(100)
            turn += 1
            turn %= number_of_players
            next_turn.text = "Player " + str(turn + 1)
            next_turn.update_text()
            next_turn.action = False

        # Update Players
        player_1.update()
        player_2.update()
        ## draw player_1
        pygame.draw.rect(screen.screen, player_1.color, (
        player_1.position.x - player_1.width * 0.5, player_1.position.y - player_1.height * 0.5, player_1.width, player_1.height))
        pygame.draw.rect(screen.screen, player_2.color, (
        player_2.position.x - player_2.width * 0.5, player_2.position.y - player_2.height * 0.5, player_2.width, player_2.height))
        # pygame.draw.rect(screen.screen, player_1.color, (200, 200, 100, 100))

        # Display screen.screen, according to framerate
        pygame.display.update()
        fps_clock.tick(fps)



