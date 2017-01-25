from assets.modules.game import *

pygame.init()


def main():
    # Uncomment te following line to demo the win screen
    #win_screen("John Doe")

    # Uncomment te following line to demo the highscore screen
    #highscore_screen()

    intro_menu()
    gameplay()

main()
