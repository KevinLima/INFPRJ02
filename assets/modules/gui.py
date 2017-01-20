import pygame

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.position = Position(x, y)
        self.width = width
        self.height = height

        self.hover = False
        self.color = color_pallete.red500
        self.action = False

        self.fontObj = pygame.font.Font(None, int(self.width * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.position.x, self.position.y)

    # Detect if hover, and if mousepressed
    def update_text(self):
        self.fontObj = pygame.font.Font(None, int(self.width * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.position.x, self.position.y)

    def track_mouse(self):
        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pressed1, mouse_pressed2, mouse_pressed3 = pygame.mouse.get_pressed()

        if (mouseX > self.position.x - self.width / 2 and mouseX < self.position.x + self.width / 2 and mouseY > self.position.y - self.height / 2 and mouseY < self.position.y + self.height / 2):
            self.hover = True
            self.color = color_pallete.grey800
            if (mouse_pressed1):
                self.color = color_pallete.red500
                self.action = not self.action
                ## ENTER AN ACTION HERE
        else:
            self.hover = False
            self.color = color_pallete.grey900
            self.action = False


class ColorPalette:
    def __init__(self):
        self.blue500 = (33, 150, 243)
        self.green500 = (76, 175, 80)
        self.grey50 = (250, 250, 250)
        self.grey800 = (66, 66, 66)
        self.grey900 = (33, 33, 33)
        self.indigo500 = (63, 81, 181)
        self.red500 = (244, 67, 54)

color_pallete = ColorPalette()

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def resolution(screen_width = 1280, screen_height = 720):
    if screen_width != 1280:
        screen_width = screen_width

    if screen_height != 720:
        screen_height = screen_height

    return screen_width, screen_height
