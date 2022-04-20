from turtle import Turtle
turtle_position = [(0,0), (0, -20), (0, 40)]

class Paddle:
    def __init__(self):
        self.ggpaddle = []

    def add_paddle(self):
        dino = Turtle("square")
        dino.penup()
        dino.color("white")
        dino.goto()

