from turtle import Turtle

class PlayerTurtle(Turtle):
    def __init__(self):
        super(PlayerTurtle, self).__init__()
        self.create_player()
        # self.goto(x_position, y_position)

    def create_player(self):
        self.color("green")
        self.shape("turtle")
        self.penup()

    def start_position(self):
        self.goto(0, -280)
        self.left(90)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def is_in_the_end(self):
        self.goto(0, -280)
        # move sped increase
        # add points to player
        # self.clear()

