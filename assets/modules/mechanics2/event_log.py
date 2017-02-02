import pygame
from assets.modules.gui2.screen import *

from assets.modules.gui2.color_pallete import *

class Event_log():

    def __init__(self):
        self.log = [
            "[Game]:Let's play a game.", #17
        ]


    def add(self, event_item):
        self.log.append(event_item)
    def clear(self):
        self.log = [
            "[Game]:Welcome back!.", #17
        ]

    def create(self):
        list = self.log[-17:]
        log_surface = pygame.Surface((350, 315))
        log_surface = log_surface.convert()
        log_surface.fill(color_pallete.pink500)
        log_x = (screen.width * 0.1)
        log_y = 300

        log_item_x = (log_x + 173)
        log_item_y = (log_y + -175)

        log_font = pygame.font.Font("assets/fonts/roboto-mono-regular.ttf", 17)
        text_surfaces = [log_font.render(item, 1, (255, 255, 255)) for item in list]

        for index, surface in enumerate(text_surfaces):
            screen.surface.blit(surface,
                                (
                                    (log_item_y),
                                      (index * surface.get_height()) + (log_item_x))
                                )

event_log = Event_log()