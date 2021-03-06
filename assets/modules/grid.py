import pygame
from assets.modules.gui2.color_pallete import *
from .gui2.screen import *
from .gui2.position import *
from .space import *

class Grid:

    def __init__(self, p1, p2):
        self.grid = []
        for x in range(4):
            list = []
            for y in range(16):
                space = Space(color_pallete.grid_colors[x])
                list.append(space)
            self.grid.append(list)


        # Setting up after new game
        p1_space = Space(color_pallete.grid_colors[(p1.coordinates.x)])
        p1_space.occupy(p1)
        p2_space = Space(color_pallete.grid_colors[(p2.coordinates.x)])
        p2_space.occupy(p2)
        self.insert_player(p1_space, p1.coordinates.x, p1.coordinates.y)
        self.insert_player(p2_space, p2.coordinates.x, p2.coordinates.y)


    # Creates a 2d list (4x16) of Space()
    def create_grid(self):
        # Rect((left, top), (width, height)) -> Rect
        square = pygame.Surface((30, 30))
        square = square.convert()

        square_x = 520
        square_y = 60

        square_font = pygame.font.Font(None, 30)

        for x in self.grid:
            for y in x:
                square.fill(y.color)
                if y.empty == False:
                    # This is the P1 or P2 text you see in the grid
                    square_text = square_font.render(y.player.title, 1, (0, 0, 0))
                    square_position = square_text.get_rect()

                    # The center of the a grid space
                    square_position.centerx = (square_x + 15)
                    square_position.centery = (square_y + 15)

                    screen.surface.blit(square, (square_x, square_y))
                    screen.surface.blit(square_text, square_position)
                else:
                    screen.surface.blit(square, (square_x, square_y))
                square_y += 40
            square_y = 60
            square_x += 40

    # Returns the index of the category
        # Use this index with the list of categories in the questions class
    def get_category(self, player):
        for x in self.grid:
            for y in x:
                if y.player == player:
                    return x

    # This function inserts the player in the new position and then deletes it from the old one
    # Use the x and y parameters to pass the amount of positions that the players moves
        # DO NOT use the parameters to give a position, only the change in position
        # You can use negative and positive numbers
    def move_player(self, player, x, y, other_player):

        new_x = player.coordinates.x + x
        new_y = player.coordinates.y + y
        # [0][1][2][3]
        new_x = self.loop_negative(new_x)
        new_x = self.loop_positive(new_x)

        if new_y < 0: new_y = 0
        if new_y > 15: new_y = 15

        if player.coordinates.x != new_x or player.coordinates.y != new_y:
            # Check if the position is occupied
            if self.grid[new_x][new_y].empty == True:
                self.grid[new_x][new_y].occupy(player)
                self.remove_player(player.coordinates.x, player.coordinates.y)
            else:
                bump_player = self.grid[new_x][new_y].player
                if new_y == 15:
                    if new_y == 0:
                        self.grid[1][15].occupy(bump_player)
                        other_player.coordinates = Position(1,15)
                    elif new_y == 3:
                        self.grid[2][15].occupy(bump_player)
                        other_player.coordinates = Position(2, 15)
                    else:
                        self.grid[new_x - 1][15].occupy(bump_player)
                        other_player.coordinates = Position(new_x - 1, 15)
                else:
                    self.grid[new_x][new_y + 1].occupy(bump_player)
                self.grid[new_x][new_y].occupy(player)
                self.remove_player(player.coordinates.x, player.coordinates.y)

        return (Position(new_x, new_y),
                Position(other_player.coordinates.x, other_player.coordinates.y))

    # This function is meant to "circle" the player around the grid
    def loop_negative(self, x):
        bl = True
        while (bl):
            if x < 0:
                x += 4
            else:
                bl = False
        return x

    # This function is meant to "circle" the player around the grid
    def loop_positive(self, x):
        bl = True
        while(bl):
            if x > 3:
                x -= 4
            else:
                bl = False
        return x

    # This is used to remove a player that has been inserted in a other position
    def remove_player(self, x, y):
        self.grid[x][y].vacate()


    # Only use this when the player is not yet on the grid
        # So at launch of gameplay()
    def insert_player(self, value, x, y):
        self.grid[x][y] = value
