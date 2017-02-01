from assets.modules.game import *
from assets.modules.screens.title_screen import *
from assets.modules.screens.question_screen import *

pygame.init()


def main():
    # Uncomment te following line to demo the win screen
    # win_screen("John Doe")
    print(question_screen("Sport"))
    title_screen()
    gameplay()

main()
