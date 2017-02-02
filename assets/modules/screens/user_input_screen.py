# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.heading import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *

# Initialize PyGame
pygame.init()

# User input screen
def user_input_screen(question):
    # Set background image
    screen.set_background_image("assets/images/background.png")

    # Initialize back button
    back_button = Button999("Back", color_pallete.pink300, color_pallete.pink500)\

    #Draw question on screen above input field
    heading = Heading(question, screen.width * 0.1, screen.height * 0.24)
    # returns value user input
    return user_input_field()

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass

def display_box(message):
    fontobject = pygame.font.Font("assets/fonts/roboto-bold.ttf", int(screen.width * 0.05))
    pygame.draw.rect(screen.surface, color_pallete.pink500, (screen.width * 0.1, screen.height * 0.35, screen.width * 0.8, screen.height * 0.35), 0)
    if len(message) != 0:
        screen.surface.blit(fontobject.render(message, 1, color_pallete.grey50), (screen.width * 0.1, screen.height * 0.35))
    pygame.display.flip()

def user_input_field():
    current_string = []
    display_box("".join(current_string))

    while True:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box("".join(current_string))
    return "".join(current_string)

