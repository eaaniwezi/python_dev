from snake import Snake
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()


    


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)

    snake.move()




screen.exitonclick()