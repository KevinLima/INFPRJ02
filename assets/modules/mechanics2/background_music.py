# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Initialize PyGame
pygame.init()

# Status = "On" or "Off"
def background_music(status):
    if status == "On":
        background_music = pygame.mixer.music.load("assets/audio/background_music.mp3")
        pygame.mixer.music.play(-1)
    elif status == "Off":
        pygame.mixer.music.stop()
