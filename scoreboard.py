from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 370)
        self.color('white')
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))

    def game_over(self):
        timmy = Turtle()
        timmy.color('white')
        timmy.write('Game Over', align='center', font=('Arial', 35, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=('Arial', 24, 'normal'))
