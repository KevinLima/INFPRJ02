import pygame

class Button:
    def __init__(self, text, x, y, size):
        self.text = text
        self.position = Position(x, y)
        if size == "small":
            self.size = Size(screen.size.width * 0.125, screen.size.height * 0.05)
        elif size == "medium":
            self.size = Size(screen.size.width * 0.125, screen.size.height * 0.05)
        elif size == "large":
            self.size = Size(screen.size.width * 0.25, screen.size.height * 0.1)

        self.hover = False
        self.color = color_pallete.red500
        self.action = False

        self.fontObj = pygame.font.Font("roboto-regular.ttf", int(self.size.width * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.position.x, self.position.y)

    # Detect if hover, and if mousepressed
    def update_text(self):
        self.fontObj = pygame.font.Font(None, int(self.size.width * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.position.x, self.position.y)

    def track_mouse(self):
        # Get mouse values
        mouse_position_x, mouse_position_y = pygame.mouse.get_pos()
        mouse_pressed_1, mouse_pressed_2, mouse_pressed_3 = pygame.mouse.get_pressed()

        if (mouse_position_x > self.position.x - self.size.width * 0.5 and
                    mouse_position_x < self.position.x + self.size.width * 0.5 and
                    mouse_position_y > self.position.y - self.size.height * 0.5 and
                    mouse_position_y < self.position.y + self.size.height * 0.5):
            self.hover = True
            self.color = color_pallete.grey800
            if (mouse_pressed_1):
                self.color = color_pallete.red500
                self.action = not self.action
                ## ENTER AN ACTION HERE
        else:
            self.hover = False
            self.color = color_pallete.grey700
            self.action = False


class ColorPalette:
    def __init__(self):
        self.blue500 = (33, 150, 243)
        self.green500 = (76, 175, 80)
        self.grey50 = (250, 250, 250)
        self.grey700 = (97, 97, 97)
        self.grey800 = (66, 66, 66)
        self.grey900 = (33, 33, 33)
        self.indigo500 = (63, 81, 181)
        self.red500 = (244, 67, 54)

color_pallete = ColorPalette()

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Screen():
    def __init__(self):
        self.size = Size(1280, 720)
        self.screen = pygame.display.set_mode((self.size.width, self.size.height))

screen = Screen()


