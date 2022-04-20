from turtle import Turtle

turtle_position = [(0, 0), (0, -20), (0, 40)]


class Paddle:
    def __init__(self):
        self.ggpaddle = []
        self.create_paddle()

    def create_paddle(self):
        for position in turtle_position:
            self.add_paddle(position)

    def add_paddle(self, pos):
        dino = Turtle("square")
        dino.penup()
        dino.fillcolor("white")
        dino.goto(pos)
        self.ggpaddle.append()
