from turtle import Turtle

turtle1_position = [(300, 0), (300, 20), (300, 40)]
turtle2_position = [(-300, 0), (-300, 20), (-300, 40)]

UP = 90

class Paddle:
    def __init__(self):
        self.ggpaddle = []
        self.create_paddle()
        self.head = self.ggpaddle[0]

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

    def move(self):
        for n in range(len(self.ggpaddle) -1, 0, -1):
            x_pos = self.ggpaddle[n-1].xcor()
            y_pos = self.ggpaddle[n - 1].ycor()
            self.ggpaddle[n].goto(x_pos, y_pos)
        self.head.forward(90)

    def Up(self):
        self.head.setheading(UP)