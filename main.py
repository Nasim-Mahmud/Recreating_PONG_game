from turtle import Screen
from paddle import Paddle
from ball import Ball
# import time

screen = Screen()
ball = Ball()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")

game_is_on = True
while game_is_on:
    screen.update()
    paddle = Paddle()

screen.exitonclick()
