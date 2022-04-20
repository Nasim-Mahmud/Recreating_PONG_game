from turtle import Turtle

turtle1_position = [(300, 0), (300, 20), (300, 40)]
turtle2_position = [(-300, 0), (-300, 20), (-300, 40)]

class Paddle:
    def __init__(self):
        self.ggpaddle = []
        self.create_paddle()

    def create_paddle(self):
        for position in turtle1_position:
            self.add_paddle(position)
        for position in turtle2_position:
            self.add_paddle(position)

    def add_paddle(self, pos):
        dino = Turtle("square")
        dino.penup()
        dino.fillcolor("white")
        dino.goto(pos)
        self.ggpaddle.append(dino)
