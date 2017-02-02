# Import required modules
from assets.modules.game import *
from assets.modules.screens.title_screen import *
from assets.modules.screens.win_screen import *

pygame.init()


def main():
    # Uncomment te following line to demo the win screen
    #win_screen("John Doe", 999)
    # print(question_screen("Sport"))
    #print(user_input_screen("Name?"))

    # background_music = pygame.mixer.music.load("assets/audio/background_music.mp3")
    # pygame.mixer.music.play(-1)

    while True:
        title_screen()
        gameplay()

        if game_over.is_it_over == True:
            win_screen(game_over.winner_name, game_over.winner_score)

main()
