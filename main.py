from assets.modules.game import *
from assets.modules.questions import Questions

pygame.init()


def main():
    # Uncomment te following line to demo the win screen
    #win_screen("John Doe")

    # Uncomment te following line to demo the highscore screen
    #highscore_screen()

    q = Questions()

    intro_menu()
    gameplay()

main()
