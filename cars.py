from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super(Cars, self).__init__()
        self.random_y = random.randint(-100, 100)
        self.colors = ["black", "green", "red", "blue", "purple"]
        self.create_a_car()

    def create_a_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.color(random.choice(self.colors))
        self.goto(430, self.random_y)

    def move(self):
        new_x = self.xcor() - random.randint(10, 20)
        self.penup()
        self.goto(new_x, self.ycor())



