from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
level = screen.textinput(title= "Score", prompt= "What will be the highest score?")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

game_over = Turtle()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = False

if level:
    game_is_on = True
    print(type(level))

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #     Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #     Detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()

        scoreboard.update_l_point()


    #     Detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()

        scoreboard.update_r_point()

    if scoreboard.l_score == int(level):
        game_over.write("Game Over")
        game_is_on = False
    if scoreboard.r_score == int(level):
        print("Right side player wins")
        game_is_on = False

screen.exitonclick()
