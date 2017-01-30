from assets.modules.screens.win_screen import *
from assets.modules.screens.rules_screen import *
from assets.modules.screens.highscore_screen import *
from .menu import *
from .gui import *
from .mechanics import Dice, Player

# Import required modules
from assets.modules.gui2.screen import *

# Set fps
fps = 30  # frames per second setting
fps_clock = pygame.time.Clock()

# Initialize screen
pygame.display.set_caption("INFPRJ02")


class Space:
    def __init__(self, color):
        self.empty = True
        self.player = None
        self.color = color

    def occupy(self, player):
        self.empty = False
        self.player = player
    def vacate(self):
        self.empty = True
        self.player = None

    def __repr__(self):
        return "Space Obj\n Empty: {}\n Color: {}".format(self.empty, self.color)



#Grid
grid = []


for x in range(4):
    space = Space(color_pallete.grid_colors[x])
    xspace = Space(color_pallete.grid_colors[x])
    xspace.empty = False

    list = []
    for y in range(16):
        if y == 2:
            list.append(xspace)
        else:
            list.append(space)
    grid.append(list)

def create_grid():
    #Rect((left, top), (width, height)) -> Rect
    square = pygame.Surface((30,30))
    square = square.convert()

    square_x = 40
    square_y = 60

    square_font = pygame.font.Font(None, 30)



    for x in grid:
        for y in x:
            square.fill(y.color)
            if y.empty == False:
                square_text = square_font.render("P1", 1, (0,0,0))
                square_position = square_text.get_rect()
                square_position.centerx = (square_x + 15)
                square_position.centery = (square_y+ 15)

                screen.surface.blit(square, (square_x, square_y))
                screen.surface.blit(square_text, square_position)
            else:
                screen.surface.blit(square, (square_x, square_y))
            square_y += 40
        square_y = 60
        square_x += 40



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
    turn = 0
    number_of_players = 2

    # Initialize direction
    direction = 1

    # Initialize Players
    player_1 = Player("Player 1", color_pallete.green500, screen.width * 0.25,
                      screen.height * 0.75, screen.width * 0.0125,
                      screen.height * 0.05)
    player_2 = Player("Player 2", color_pallete.blue500, screen.width * 0.3,
                      screen.height * 0.75, screen.width * 0.0125,
                      screen.height * 0.05)


    # GAME
    background = pygame.Surface(screen.surface.get_size())
    background = background.convert()
    background.fill(color_pallete.purple500)

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

        screen.surface.blit(background, (0, 0))

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
        create_grid()

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
        pygame.draw.rect(screen.surface, player_1.color, (
        player_1.position.x - player_1.width * 0.5, player_1.position.y - player_1.height * 0.5, player_1.width, player_1.height))
        pygame.draw.rect(screen.surface, player_2.color, (
        player_2.position.x - player_2.width * 0.5, player_2.position.y - player_2.height * 0.5, player_2.width, player_2.height))
        # pygame.draw.rect(screen.surface, player_1.color, (200, 200, 100, 100))

        # Display screen.surface, according to framerate
        pygame.display.update()
        fps_clock.tick(fps)



