from assets.modules.screens.win_screen import *
from assets.modules.screens.help_screen import *
from assets.modules.screens.title_screen import *
from .gui import *
from .mechanics import Dice
from .mechanics2.player import *
from .space import *
from .grid import *

# Import required modules
from assets.modules.gui2.screen import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()

# Initialize screen
pygame.display.set_caption("INFPRJ02")

def gameplay():
    # Initialize buttons
    quit_button = Button("X", screen.width * 0.98, screen.height * 0.05,
                        "small")

    rules_button = Button("?", screen.width * 0.94, screen.height * 0.05,
                          "small")

    dice_button = Button("ROLL DICE", screen.width * 0.925,
                         screen.height * 0.75, "medium")

    next_turn = Button("NEXT TURN", screen.width * 0.925, screen.height * 0.85,
                       "medium")

    direction_button = Button("DIRECTION", screen.width * 0.925,
                              screen.height * 0.95, "medium")

    # Initialize whose turn
    turn = 0 #player 1

    # Initialize direction
    direction = 1 #UP

    # Has the player already trown the dice this turn?
    player_trew_dice = False

    # Initialize Players
    player_1 = Player("Player 1",
                      color_pallete.green500,
                      "P1",
                      0,15)

    player_2 = Player("Player 2",
                      color_pallete.blue500,
                      "P2",
                      2, 15)


    # GAME
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    grid = Grid(player_1, player_2)

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
            help_screen()

        # Get mouse values
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        mouse_pressed_1, mouse_pressed_2, mouse_pressed_3 = pygame.mouse.get_pressed()

        screen.surface.blit(background, (0, 0))

        # Set background image
        screen.set_background_image("assets/images/background.png")

        # button update
        quit_button.track_mouse()

        # quit_button.display()
        pygame.draw.rect(screen.surface, quit_button.color, (quit_button.position.x - quit_button.size.width * 0.5,
                                                            quit_button.position.y - quit_button.size.height * 0.5,
                                                            quit_button.size.width, quit_button.size.height))
        screen.surface.blit(quit_button.textSurfaceObj, quit_button.textRectObj)

        # button update
        rules_button.track_mouse()
        # rules_button.display()
        pygame.draw.rect(screen.surface, rules_button.color, (rules_button.position.x - rules_button.size.width * 0.5,
                                                             rules_button.position.y - rules_button.size.height * 0.5,
                                                             rules_button.size.width, rules_button.size.height))
        screen.surface.blit(rules_button.textSurfaceObj, rules_button.textRectObj)

        # Dice button
        # button update
        dice_button.track_mouse()
        pygame.draw.rect(screen.surface, dice_button.color, (
            dice_button.position.x - dice_button.size.width * 0.5, dice_button.position.y - dice_button.size.height * 0.5,
            dice_button.size.width, dice_button.size.height))
        screen.surface.blit(dice_button.textSurfaceObj, dice_button.textRectObj)

        next_turn.track_mouse()
        pygame.draw.rect(screen.surface, next_turn.color, (
            next_turn.position.x - next_turn.size.width * 0.5, next_turn.position.y - next_turn.size.height * 0.5,
            next_turn.size.width, next_turn.size.height))
        screen.surface.blit(next_turn.textSurfaceObj, next_turn.textRectObj)

        direction_button.track_mouse()
        pygame.draw.rect(screen.surface, direction_button.color, (
            direction_button.position.x - direction_button.size.width * 0.5,
            direction_button.position.y - direction_button.size.height * 0.5,
            direction_button.size.width, direction_button.size.height))
        screen.surface.blit(direction_button.textSurfaceObj, direction_button.textRectObj)

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
            if player_trew_dice == False:
                pygame.time.wait(100)
                dice = Dice()
                dice_number = dice.number()
                dice_button.text = str(dice_number)
                dice_button.update_text()
                dice_button.action = False
                player_trew_dice = True

                amount_of_steps = 0

                if dice_number == 1 or dice_number == 2:
                    amount_of_steps = 1
                if dice_number == 3 or dice_number == 4:
                    amount_of_steps = 2
                if dice_number == 5 or dice_number == 6:
                    amount_of_steps = 3

                if direction == 0: #LEFT
                    if turn == 0:
                        player_1.relocate(grid.move_player(player_1, (amount_of_steps * -1), 0))
                    if turn == 1:
                        player_2.relocate(grid.move_player(player_2, (amount_of_steps * -1), 0))


                if direction == 1: #UP
                    if turn == 0:
                        player_1.relocate(grid.move_player(player_1, 0, (amount_of_steps * -1)))

                    if turn == 1:
                        player_2.relocate(grid.move_player(player_2, 0, (amount_of_steps * -1)))


                if direction == 2:  #RIGHT
                    if turn == 0:
                        player_1.relocate(grid.move_player(player_1, amount_of_steps, 0))

                    if turn == 1:
                        player_2.relocate(grid.move_player(player_2, amount_of_steps, 0))


                if direction == 3:  #DOWN
                    if turn == 0:
                        player_1.relocate(grid.move_player(player_1, 0, amount_of_steps))

                    if turn == 1:
                        player_2.relocate(grid.move_player(player_2, 0, amount_of_steps))



        if next_turn.action:
            pygame.time.wait(100)
            # Keep switching between the players turn
            if turn == 1:
                # Player 1's turn
                turn = 0
            else:
                # Player 2's turn
                turn = 1
            player_trew_dice = False

            next_turn.text = "Player " + str(turn + 1)
            next_turn.update_text()
            next_turn.action = False

        # Update Players
        player_1.update()
        player_2.update()
        grid.create_grid()

        # Display screen.surface, according to framerate
        pygame.display.update()
        fps_clock.tick(fps)

