from assets.modules.gui2.subheading import *
from assets.modules.screens.title_screen import *
from .mechanics import Dice
from .mechanics2.player import *
from .grid import *
from .screens.question_screen import *
from assets.modules.gui2.screen import *
from assets.modules.screens.user_input_screen import *
from assets.modules.mechanics2.event_log import *
from assets.modules.mechanics2.game_over import *

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

    # Has the player answered a question this turn
    player_answered_question = False

    # Initialize Players
    player_1 = Player(user_input_screen("Player 1 name?"),
                      color_pallete.green500, "P1", 0, 15, 0)

    player_2 = Player(user_input_screen("Player 2 name?"),
                      color_pallete.blue500, "P2", 2, 15, 0)


    # GAME
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    grid = Grid(player_1, player_2)


    players_scoreboard = [
        player_1.name + " - " + str(player_1.score),
        player_2.name + " - " + str(player_2.score)
    ]

    # MAIN GAME LOOP
    while True:
        events = pygame.event.get()
        if event_exist(events, pygame.QUIT):
            pygame.quit()
            exit()

        # IF YOU PRESS OPTIONS, RUN STARTMENU
        if quit_button.action:
            event_log.clear()
            return
        if game_over.is_it_over == True:
            event_log.clear()
            return

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
                event_log.add("[P{}]:Rolled a {}".format((turn + 1), dice_number))

                if player_answered_question == False:
                    x_index = 0
                    if turn == 0:
                        x_index = player_1.coordinates.x
                    if turn == 1:
                        x_index = player_2.coordinates.x

                category = questions.categories[x_index]

                result = question_screen(category)
                print("Result {}".format(result))
                event_log.add("[P{}]:The answer was {}".format((turn + 1), result))

                # Only move the player if the question was answered correctly
                if result == True:
                    amount_of_steps = 0

                    if dice_number == 1 or dice_number == 2:
                        amount_of_steps = 1
                    if dice_number == 3 or dice_number == 4:
                        amount_of_steps = 2
                    if dice_number == 5 or dice_number == 6:
                        amount_of_steps = 3

                    # Add to score
                    if turn == 0:
                        player_1.scored()
                    else:
                        player_2.scored()


                    if direction == 0: #LEFT
                        if turn == 0:
                            players_positions = grid.move_player(player_1, (amount_of_steps * -1), 0, player_2)
                            player_1.relocate(players_positions[0])
                            player_2.relocate(players_positions[1])
                        if turn == 1:
                            players_positions = grid.move_player(player_2, (amount_of_steps * -1), 0, player_1)
                            player_2.relocate(players_positions[0])
                            player_1.relocate(players_positions[1])


                    if direction == 1: #UP
                        if turn == 0:
                            players_positions = grid.move_player(player_1, 0, (amount_of_steps * -1), player_2)
                            player_1.relocate(players_positions[0])
                            player_2.relocate(players_positions[1])

                        if turn == 1:
                            players_positions = grid.move_player(player_2, 0, (amount_of_steps * -1), player_1)
                            player_2.relocate(players_positions[0])
                            player_1.relocate(players_positions[1])

                        event_log.add("[P{}]:Took {} steps".format((turn + 1), amount_of_steps))


                    if direction == 2:  #RIGHT
                        if turn == 0:
                            players_positions = grid.move_player(player_1, amount_of_steps, 0, player_2)
                            player_1.relocate(players_positions[0])
                            player_2.relocate(players_positions[1])

                        if turn == 1:
                            players_positions = grid.move_player(player_2, amount_of_steps, 0, player_1)
                            player_2.relocate(players_positions[0])
                            player_1.relocate(players_positions[1])


                    if direction == 3:  #DOWN
                        if turn == 0:
                            players_positions = grid.move_player(player_1, 0, amount_of_steps, player_2)
                            player_1.relocate(players_positions[0])
                            player_2.relocate(players_positions[1])

                        if turn == 1:
                            players_positions = grid.move_player(player_2, 0, amount_of_steps, player_1)
                            player_2.relocate(players_positions[0])
                            player_1.relocate(players_positions[1])


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
            event_log.add("[Game]:Turn switched")

            next_turn.text = "Player " + str(turn + 1)
            next_turn.update_text()
            next_turn.action = False



        score_body_font = pygame.font.Font("assets/fonts/roboto-regular.ttf", int((screen.width * 0.0175)))

        players_scoreboard[0] = player_1.name + " [" + player_1.title + "] - " + str(player_1.score)
        players_scoreboard[1] = player_2.name + " [" + player_2.title + "] - " + str(player_2.score)

        # Generate surfaces
        text_surfaces = [score_body_font.render(player, 1, color_pallete.grey50) for player in players_scoreboard]

        if player_1.update() == True:
            game_over.its_over(player_1.name, player_1.score)
        if player_2.update() == True:
            game_over.its_over(player_2.name, player_2.score)

        grid.create_grid()
        event_log.create()



        # Blit the text surfaces
        for index, surface in enumerate(text_surfaces):
            screen.surface.blit(surface,
                                ((screen.width * 0.1), (index * surface.get_height()) + (int(screen.height * 0.30))))

        subheading = Subheading("Scoreboard", screen.width * 0.1, screen.height * 0.26)


        # Display screen.surface, according to framerate
        pygame.display.update()
        fps_clock.tick(fps)
