from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(self.position())

    def position(self):
        x_cor = 0
        y_cor = 0
        is_on = True
        while is_on:
            x_cor += 20
            y_cor += 20
            return x_cor, y_cor