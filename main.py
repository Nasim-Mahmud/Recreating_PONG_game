from turtle import Turtle, Screen
from paddle import Paddle
import time

paddle = Paddle()

screen = Screen()
screen.update()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.exitonclick()