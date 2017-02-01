# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *
from assets.modules.screens.help_screen import *
from assets.modules.screens.highscores_screen import *
from assets.modules.screens.rules_screen import *
from assets.modules.questions import *

# Initialize PyGame
pygame.init()

# Title screen
def question_screen(catagory):
    # Set background image
    screen.set_background_image("assets/images/question_screen_background.png")

    # Assign query to question variable
    question = questions.get_question(catagory)

    # Print question to screen
    question_text = Text999("{}: {}".format(question[0], question[2]), "roboto-regular-bold", color_pallete.orange500,
                            screen.width * 0.0375, screen.width * 0.05,
                            screen.height * 0.2)

    # Seperate answers from query
    answers = question[4]

    # Seperate correct answer from query
    correct_answer = question[3]

    print(correct_answer)

    # Print menu according to amount of answers
    amount_of_answers = 0

    for x in answers:
        amount_of_answers += 1

    if amount_of_answers != 0:
        if amount_of_answers == 2:
            answer_a = answers[0]
            answer_b = answers[1]

            # Initialize buttons
            answer_a_button = Button999("A: {}".format(answer_a), color_pallete.pink300, color_pallete.pink500)
            answer_b_button = Button999("B: {}".format(answer_b), color_pallete.pink300, color_pallete.pink500)

            # Set PyGame clock
            clock = pygame.time.Clock()

            # Title screen loop
            while True:
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if answer_a_button.obj.collidepoint(mouse):
                            answer_id = 1
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_b_button.obj.collidepoint(mouse):
                            answer_id = 2
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                # Draw buttons
                    answer_a_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.5,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.5))
                    answer_b_button.draw(screen, mouse, (screen.width * 0.05,
                                               screen.height * 0.6,
                                               screen.width * 0.75,
                                               screen.height * 0.075),
                                               (screen.width * 0.05,
                                                screen.height * 0.6))

                # Update PyGame screen
                pygame.display.update()
                clock.tick(30)

        elif amount_of_answers == 3:
            answer_a = answers[0]
            answer_b = answers[1]
            answer_c = answers[2]

            # Initialize buttons
            answer_a_button = Button999("A: {}".format(answer_a), color_pallete.pink300, color_pallete.pink500)
            answer_b_button = Button999("B: {}".format(answer_b), color_pallete.pink300, color_pallete.pink500)
            answer_c_button = Button999("C: {}".format(answer_c), color_pallete.pink300, color_pallete.pink500)

            # Set PyGame clock
            clock = pygame.time.Clock()

            # Title screen loop
            while True:
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if answer_a_button.obj.collidepoint(mouse):
                            answer_id = 1
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_b_button.obj.collidepoint(mouse):
                            answer_id = 2
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_c_button.obj.collidepoint(mouse):
                            answer_id = 3
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                # Draw buttons
                    answer_a_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.5,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.5))
                    answer_b_button.draw(screen, mouse, (screen.width * 0.05,
                                               screen.height * 0.6,
                                               screen.width * 0.75,
                                               screen.height * 0.075),
                                               (screen.width * 0.05,
                                                screen.height * 0.6))
                    answer_c_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.7,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.7))

                # Update PyGame screen
                pygame.display.update()
                clock.tick(30)

        elif amount_of_answers == 4:
            answer_a = answers[0]
            answer_b = answers[1]
            answer_c = answers[2]
            answer_d = answers[3]

            # Initialize buttons
            answer_a_button = Button999("A: {}".format(answer_a), color_pallete.pink300, color_pallete.pink500)
            answer_b_button = Button999("B: {}".format(answer_b), color_pallete.pink300, color_pallete.pink500)
            answer_c_button = Button999("C: {}".format(answer_c), color_pallete.pink300, color_pallete.pink500)
            answer_d_button = Button999("D: {}".format(answer_d), color_pallete.pink300, color_pallete.pink500)

            # Set PyGame clock
            clock = pygame.time.Clock()

            # Title screen loop
            while True:
                mouse = pygame.mouse.get_pos()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if answer_a_button.obj.collidepoint(mouse):
                            answer_id = 1
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_b_button.obj.collidepoint(mouse):
                            answer_id = 2
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_c_button.obj.collidepoint(mouse):
                            answer_id = 3
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                        elif answer_d_button.obj.collidepoint(mouse):
                            answer_id = 4
                            if answer_id == correct_answer:
                                return(True)
                            else:
                                return(False)

                # Draw buttons
                    answer_a_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.5,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.5))
                    answer_b_button.draw(screen, mouse, (screen.width * 0.05,
                                               screen.height * 0.6,
                                               screen.width * 0.75,
                                               screen.height * 0.075),
                                               (screen.width * 0.05,
                                                screen.height * 0.6))
                    answer_c_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.7,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.7))
                    answer_d_button.draw(screen, mouse, (screen.width * 0.05,
                                         screen.height * 0.8,
                                         screen.width * 0.75,
                                         screen.height * 0.075),
                                         (screen.width * 0.05,
                                          screen.height * 0.8))
                # Update PyGame screen
                pygame.display.update()
                clock.tick(30)

