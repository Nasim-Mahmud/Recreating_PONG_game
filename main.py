from turtle import Screen
from paddle import Paddle
from ball import Ball

# import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
paddle = Paddle()
ball = Ball()
screen.tracer(0)

screen.listen()
screen.onkey(paddle.Up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    paddle = Paddle()
    paddle.move()
screen.exitonclick()
