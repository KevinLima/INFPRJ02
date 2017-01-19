import pygame

class Button:
    def __init__(self, text, x, y, width, height):

        self.text = text  # TEXT ON BUTTON
        self.posx = x  # X-POSITION -- CENTER OF THE RECT
        self.posy = y  # Y-POSITION -- CENTER OF THE RECT
        self.sizew = width  # WIDTH
        self.sizeh = height  # HEIGHT

        self.hover = False
        self.color = (200, 0, 0)
        self.action = False

        self.fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.textSurfaceObj = self.fontObj.render(self.text, True, (255, 255, 255), ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.posx, self.posy)

    # Detect if hover, and if mousepressed
    def update_text(self):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 12)
        self.textSurfaceObj = self.fontObj.render(self.text, True, (255, 255, 255), ())
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.posx, self.posy)

    def track_mouse(self):
        # Get mouse values
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse_pressed1, mouse_pressed2, mouse_pressed3 = pygame.mouse.get_pressed()

        if (mouseX > self.posx - self.sizew / 2 and mouseX < self.posx + self.sizew / 2 and mouseY > self.posy - self.sizeh / 2 and mouseY < self.posy + self.sizeh / 2):
            self.hover = True
            self.color = (150, 0, 0)
            if (mouse_pressed1):
                self.color = (255, 0, 0)
                self.action = not self.action
                ## ENTER AN ACTION HERE
        else:
            self.hover = False
            self.color = (0, 0, 0)
            self.action = False


class ColorPalette:
    def __init__(self):
        self.blue500 = (33, 150, 243)
        self.green500 = (76, 175, 80)
        self.grey50 = (250, 250, 250)
        self.indigo500 = (63, 81, 181)
        self.red500 = (244, 67, 54)


color_pallete = ColorPalette()
