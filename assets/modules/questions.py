

class Questions:

    def __init__(self):
        self.get_questions()
        print(self.is_answer_correct(0,2))

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
            ]
        ]

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
