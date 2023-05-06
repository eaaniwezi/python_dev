from turtle import Turtle, Screen
import random
import turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle will win the race?")

turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_axis = -100

for color in turtle_color:
    turle = Turtle(shape="turtle")
    turle.color(color)
    turle.penup()
    turle.goto(x=-230, y=y_axis)
    y_axis += 50
    all_turtles.append(turle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turle in all_turtles:

        if turle.xcor() > 230:
            is_race_on = False
            screen.exitonclick()
            winning_color = turle.pencolor()
            if winning_color != user_bet:
                print(f"You lost!! {winning_color} won the race....")
            else:
                print(f"You guessed right!! {winning_color} won the race")

        rand_distance = random.randint(0, 10)
        turle.forward(rand_distance)
