from assets.modules.game import *
from assets.modules.screens.title_screen import *
from assets.modules.screens.question_screen import *
from assets.modules.screens.user_input_screen import *
from assets.modules.mechanics2.game_over import *
from assets.modules.screens.win_screen import *

pygame.init()

def main():
    # Uncomment te following line to demo the win screen
    # win_screen("John Doe")
    # print(question_screen("Sport"))
    #print(user_input_screen("Name?"))
    while True:
        title_screen()
        gameplay()

        if game_over.is_it_over == True:
            win_screen(game_over.winner_name, game_over.winner_score)


main()