import time
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
screen.onkey(paddle.up_arrow, "Up")
screen.onkey(paddle.down_arrow, "Down")
screen.onkey(paddle.up_alph, "w")
screen.onkey(paddle.down_alph, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # paddle.move()
screen.exitonclick()
