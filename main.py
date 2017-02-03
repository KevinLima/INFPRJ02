# Import required modules
from assets.modules.game import *
from assets.modules.screens.title_screen import *
from assets.modules.screens.win_screen import *
from assets.modules.mechanics2.background_music import *

pygame.init()

def main():
    background_music("On")

    while True:
        title_screen()
        gameplay()

        if game_over.is_it_over == True:
            win_screen(game_over.winner_name, game_over.winner_score)

main()
