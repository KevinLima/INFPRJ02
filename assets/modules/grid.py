import pygame
from assets.modules.gui2.color_pallete import *
from .gui2.screen import *
from .space import *

class Grid:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.grid = []
        for x in range(4):
            space = Space(color_pallete.grid_colors[x])
            list = []
            for y in range(16):
                list.append(space)
            self.grid.append(list)
        xsp = Space((255,255,255))
        xsp.occupy(p1)
        self.grid[0][2] = xsp

    def create_grid(self):
        # Rect((left, top), (width, height)) -> Rect
        square = pygame.Surface((30, 30))
        square = square.convert()

        square_x = 40
        square_y = 60

        square_font = pygame.font.Font(None, 30)
        self.remove_player(2, 0)

        for x in self.grid:
            for y in x:
                square.fill(y.color)
                if y.empty == False:
                    square_text = square_font.render(y.player.title, 1, (0, 0, 0))
                    square_position = square_text.get_rect()
                    square_position.centerx = (square_x + 15)
                    square_position.centery = (square_y + 15)

                    screen.surface.blit(square, (square_x, square_y))
                    screen.surface.blit(square_text, square_position)
                else:
                    screen.surface.blit(square, (square_x, square_y))
                square_y += 40
            square_y = 60
            square_x += 40


    def get_category(self, player):
        for x in self.grid:
            for y in x:
                if y.player == player:
                    return x


    def move_player(self, player, x, y):
        pass


    def remove_player(self, x_axis, y_axis):
        for x in self.grid:
            for y in x:
                if y.empty == False:
                    print(y.player)




    def insert_player(self, x, y):
        pass
