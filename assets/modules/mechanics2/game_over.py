from assets.modules.highscore import insertWinner
class Game_over():

    def __init__(self):
        self.is_it_over = False
        self.winner_name = ""
        self.winner_score = 0
    def its_over(self, name, score):
        self.winner_name = name
        self.winner_score = score
        insertWinner(self.winner_name, str(self.winner_score))
        self.is_it_over = True
    def clear(self):
        self.is_it_over = False
        self.winner_score = 0
        self.winner_name = ""

game_over = Game_over()