from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.board()

    def board(self):
        self.write(f'Your Score : {self.score}', align='center', font=('Bold', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Bold', 20, 'normal'))

    def score_cal(self):
        self.score += 1
        self.clear()
        self.board()
