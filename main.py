from turtle import Turtle, Screen
from player_turtle import PlayerTurtle
import time
from cars import Cars
from score import Score
import random
screen = Screen()
screen.title("The Turtle Crossing")
screen.setup(width=800, height=600)
screen.tracer(0)


# colors = ["black", "green", "red", "blue", "purple"]
timmy = PlayerTurtle()
timmy.start_position()
score = Score()
list_of_cars = []

# Control our turtle
screen.listen()
screen.onkey(timmy.move_up, "Up")
screen.onkey(timmy.move_down, "Down")

game_is_on = True


# Level of traffic
level_of_traffic = 160

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Cars moving forward
    for carr in list_of_cars:
        carr.move()
        # Check collision with a car
        if timmy.distance(carr) < 20:
            score.game_over()
            game_is_on = False

    # Generate a random number
    random_number = random.randint(0, level_of_traffic)

    # If the number is > then VAR, create a new car
    if random_number > 150:
        car = Cars()
        list_of_cars.append(car)

    # Check collision with top wall
    if timmy.ycor() > 260:

        timmy.is_in_the_end()
        score.add_points()
        level_of_traffic += 10

screen.exitonclick()