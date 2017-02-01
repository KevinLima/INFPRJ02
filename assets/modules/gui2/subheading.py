# Import PyGame & Sys modules

# Import required modules
from assets.modules.gui2.heading import *
from assets.modules.gui2.position import *
from assets.modules.gui2.screen import *

# Initialize PyGame
pygame.init()


class Subheading:
    def __init__(self, text, x, y):
        self.font = pygame.font.SysFont("assets/fonts/roboto-bold.ttf", int(screen.width * 0.03))
        self.text = self.font.render(text, 1, color_pallete.orange500)
        self.position = Position(x, y)
        screen.surface.blit(self.text, (self.position.x, self.position.y))
        pygame.display.update()
