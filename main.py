from turtle import Turtle, Screen
from paddle import Paddle
# import time

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")

game_is_on = True
while game_is_on:
    screen.update()
    paddle = Paddle()
screen.exitonclick()
