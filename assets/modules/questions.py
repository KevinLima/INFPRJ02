

class Questions:

    def __int__(self):
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
            ]
        ]

    def is_answer_correct(self, question_id, answer_id):
        question = next((y for x in self.question_list if ))
