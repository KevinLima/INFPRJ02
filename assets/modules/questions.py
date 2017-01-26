from random import randint

class Questions:

    def __init__(self):
        self.get_questions()

    def get_questions(self):

        # Dummy questions
        self.question_list = [
            [
                0,  # ID
                "Entertainment",  # Category
                "Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd?",  # Question
                ["De Witte Aap",
                 "Het NRC",
                 "Café de Beurs"],  # Answers
                1  # Index of the correct answer
            ],
            [
                1,  # ID
                "Entertainment",  # Category
                "In welke bioscoop vindt het Wildlife Film Festival plaats?",  # Question
                ["Cinerama",
                 "Pathé de Kuip",
                 "Pathé Schouwburgplein"],  # Answers
                0  # Index of the correct answer
            ],
            [
                2,  # ID
                "Geography",  # Category
                "Rotterdam is de hoofdstad van Nederland. ",  # Question
                ["WAAR",
                 "NIET WAAR"],  # Answers
                1  # Index of the correct answer
            ]
        ]
        self.categories = [
            "Sports",
            "Geography",
            "Entertainment",
            "History"
        ]

        # List with al the used questions
        # Use self.used to add to this
        self.used_questions = []

    def is_answer_correct(self, question_id, answer_index):

        # Selects a question with question_id as first index
        question = next((x for x in self.question_list if x[0] == question_id), None)
        print(question)

        # Is there a question w/ that question id?
        if question is not None:
            # Is the answer_index (the answer the player chose), the same as the correct answer?
            if answer_index == question[4]:
                return True
            else:
                return False
        else:
            print("Can't find question")


    def get_question(self, category_name):
        if category_name in self.categories:
            # Get a list of questions that have the right category AND have not been used.
            question_candidates = [x for x in self.question_list if x[1] == category_name and x[0] not in self.used_questions]
            amount_of_questions = len(question_candidates)
            if amount_of_questions != 0:
                if amount_of_questions == 1:
                    return question_candidates[0]
                else:
                    # Get an random question from the list of candidates
                    return question_candidates[randint(0,(amount_of_questions -1))]
            else:
                print("No questions (left) in that category")

                # All the questions in this category have been used, try a different category
                return self.get_question(self.other_category(category_name))
        else:
            # Category that was provided does not match any in self.categories
            print("Can't find category")

    # Send the ID's of used questions here
    def used(self, question_id):
        self.used_questions.append(question_id)

    # This function return a diffrent category then you provided
    def other_category(self, category_name):
        categories = self.categories
        categories.remove(category_name)
        amount = len(categories)
        if amount != 0:
            return  categories[randint(0,(amount -1))]
        else:
            print("GAME OVER: all the questions have been used")
            #TODO: end the game

