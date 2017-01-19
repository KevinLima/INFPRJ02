import pygame

class Button:
    def __init__(self, text, x, y, width, height):

        self.text = text  # TEXT ON BUTTON
        self.posx = x  # X-POSITION -- CENTER OF THE RECT
        self.posy = y  # Y-POSITION -- CENTER OF THE RECT
        self.sizew = width  # WIDTH
        self.sizeh = height  # HEIGHT

        self.hover = False
        self.color = color_pallete.red500
        self.action = False

        self.fontObj = pygame.font.Font(None, int(self.sizew * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.posx, self.posy)

    # Detect if hover, and if mousepressed
    def update_text(self):
        self.fontObj = pygame.font.Font(None, int(self.sizew * 0.175))
        self.textSurfaceObj = self.fontObj.render(self.text, True, color_pallete.grey50, ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.posx, self.posy)

    def track_mouse(self):
        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pressed1, mouse_pressed2, mouse_pressed3 = pygame.mouse.get_pressed()

        if (mouseX > self.posx - self.sizew / 2 and mouseX < self.posx + self.sizew / 2 and mouseY > self.posy - self.sizeh / 2 and mouseY < self.posy + self.sizeh / 2):
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

def resolution(width = 1280, height = 720):
    if width != 1280:
        width = width

    if height != 720:
        height = height

    return width, height

color_pallete = ColorPalette()
