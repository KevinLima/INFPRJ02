# Import PyGame & Sys modules
import pygame, sys
from pygame.locals import *

# Import required modules
from assets.modules.gui2.button import *
from assets.modules.gui2.color_pallete import *
from assets.modules.gui2.screen import *
from assets.modules.gui2.text import *
from assets.modules.screens.help_screen import *
from assets.modules.questions import *

# Initialize PyGame
pygame.init()

# Title screen
def question_screen(category):
    # Set background image
    screen.set_background_image("assets/images/background.png")

    # Assign get_question() to data list
    # data[0] = Question ID
    # data[1] = Category
    # data[2] = Question
    # data[3] = Correct answer
    # data[4] = Answers
    data = questions.get_question(category)

    question_list = data[2].split(" ")
    questions_list_lenght = len(question_list)

    if questions_list_lenght <= 7:
        question_line_1 = ""
        for x in question_list[0:6]:
            question_line_1 += x
            question_line_1 += " "

        # Draw question on screen
        question = Text999("{}: {}".format(data[0], question_line_1),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.2)

    elif questions_list_lenght > 7 and questions_list_lenght <= 14:
        question_line_1 = ""
        for x in question_list[0:6]:
            question_line_1 += x
            question_line_1 += " "

        question_line_2 = ""
        for x in question_list[7:13]:
            question_line_2 += x
            question_line_2 += " "

        # Draw question on screen
        question = Text999("{}: {}".format(data[0], question_line_1),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.2)


        question = Text999("       {}".format(question_line_2),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.3)

    elif questions_list_lenght > 14 and questions_list_lenght <= 21:
        question_line_1 = ""
        for x in question_list[0:6]:
            question_line_1 += x
            question_line_1 += " "

        question_line_2 = ""
        for x in question_list[7:13]:
            question_line_2 += x
            question_line_2 += " "

        question_line_3 = ""
        for x in question_list[13:20]:
            question_line_3 += x
            question_line_3 += " "

        # Draw question on screen
        question = Text999("{}: {}".format(data[0], question_line_1),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.2)


        question = Text999("       {}".format(question_line_2),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.3)

        question = Text999("       {}".format(question_line_3),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.4)

    else:
        question_line_1 = ""
        for x in question_list:
            question_line_1 += x
            question_line_1 += " "
        question = Text999("{}: {}".format(data[0], question_line_1),
                           "roboto-regular-bold", color_pallete.orange500,
                           screen.width * 0.0375, screen.width * 0.05,
                           screen.height * 0.2)

    # Get answers from data list
    answers = data[4]

    # Get correct answer from data list
    correct_answer = data[3]

    # Determine amount of answers in data list
    amount_of_answers = len(answers)

    if amount_of_answers == 2:
        return buttons_for_2_answers_(answers, correct_answer)

    elif amount_of_answers == 3:
        return buttons_for_3_answers_(answers, correct_answer)

    elif amount_of_answers == 4:
        return buttons_for_4_answers_(answers, correct_answer)

def buttons_for_2_answers_(answers, correct_answer):
    # Seperate answers into independent variables
    answer_a = answers[0]
    answer_b = answers[1]

    # Initialize buttons
    answer_a_button = Button999("A: {}".format(answer_a))
    answer_b_button = Button999("B: {}".format(answer_b))

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
                    return check_answer(answer_id, correct_answer)

                elif answer_b_button.obj.collidepoint(mouse):
                    answer_id = 2
                    return check_answer(answer_id, correct_answer)

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

def buttons_for_3_answers_(answers, correct_answer):
    # Seperate answers into independent variables
    answer_a = answers[0]
    answer_b = answers[1]
    answer_c = answers[2]

    # Initialize buttons
    answer_a_button = Button999("A: {}".format(answer_a))
    answer_b_button = Button999("B: {}".format(answer_b))
    answer_c_button = Button999("C: {}".format(answer_c))

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
                    return check_answer(answer_id, correct_answer)

                elif answer_b_button.obj.collidepoint(mouse):
                    answer_id = 2
                    return check_answer(answer_id, correct_answer)

                elif answer_c_button.obj.collidepoint(mouse):
                    answer_id = 3
                    return check_answer(answer_id, correct_answer)

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

def buttons_for_4_answers_(answers, correct_answer):
    # Seperate answers into independent variables
    answer_a = answers[0]
    answer_b = answers[1]
    answer_c = answers[2]
    answer_d = answers[3]

    # Initialize buttons
    answer_a_button = Button999("A: {}".format(answer_a))
    answer_b_button = Button999("B: {}".format(answer_b))
    answer_c_button = Button999("C: {}".format(answer_c))
    answer_d_button = Button999("D: {}".format(answer_d))

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
                    return check_answer(answer_id, correct_answer)

                elif answer_b_button.obj.collidepoint(mouse):
                    answer_id = 2
                    return check_answer(answer_id, correct_answer)

                elif answer_c_button.obj.collidepoint(mouse):
                    answer_id = 3
                    return check_answer(answer_id, correct_answer)

                elif answer_d_button.obj.collidepoint(mouse):
                    answer_id = 4
                    return check_answer(answer_id, correct_answer)

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

def check_answer(answer_id, correct_answer):
    if answer_id == correct_answer:
        return(True)
    else:
        return(False)
