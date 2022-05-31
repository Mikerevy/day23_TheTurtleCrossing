from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 250)
        self.write("Score is: ", align="center", font=("Courier", 20, "normal"))
        self.goto(-200, 249)
        self.write(self.player_score, align="center", font=("Courier", 20, "normal"))

    def add_points(self):
        self.player_score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"Game over! Your score is: {self.player_score} ", align="center", font=("Courier", 20, "normal"))

