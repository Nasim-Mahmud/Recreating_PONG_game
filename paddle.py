from turtle import Turtle

turtle1_position = [(350, 0), (350, 20), (350, 40)]
turtle2_position = [(-350, 0), (-350, 20), (-350, 40)]

UP = 90
MOVE = 20
DOWN = 270


class Paddle:
    def __init__(self):
        self.ggpaddle01 = []
        self.ggpaddle02 = []
        self.create_paddle(self.add_paddle_01, turtle1_position)
        self.create_paddle(self.add_paddle_02, turtle2_position)
        self.head01 = self.ggpaddle01[0]
        self.head02 = self.ggpaddle02[0]

    def create_paddle(self, paddle, pos):
        for position in pos:
            paddle(position)

    def add_paddle_01(self, pos):
        dino = Turtle("square")
        dino.penup()
        dino.fillcolor("white")
        dino.goto(pos)
        self.ggpaddle01.append(dino)

    def add_paddle_02(self, pos):
        dino = Turtle("square")
        dino.penup()
        dino.fillcolor("white")
        dino.goto(pos)
        self.ggpaddle02.append(dino)

    def move(self, paddles, head):
        for n in range(len(paddles) - 1, 0, -1):
            x_pos = paddles[n - 1].xcor()
            y_pos = paddles[n - 1].ycor()
            paddles[n].goto(x_pos, y_pos)
        head.forward(MOVE)

    # def move_01(self):
    #     for n in range(len(self.ggpaddle01)-1, 0, -1):
    #         x_pos = self.ggpaddle01[n-1].xcor()
    #         y_pos = self.ggpaddle01[n-1].ycor()
    #         self.ggpaddle01[n].goto(x_pos, y_pos)
    #     self.head01.forward(MOVE)

    # def move_02(self):
    #     for n in range(len(self.ggpaddle02)-1, 0, -1):
    #         x_pos = self.ggpaddle02[n-1].xcor()
    #         y_pos = self.ggpaddle02[n-1].ycor()
    #         self.ggpaddle02[n].goto(x_pos, y_pos)
    #     self.head02.forward(MOVE)

    def up_arrow(self):
        self.head01.setheading(UP)
        self.move(self.ggpaddle01, self.head01)

    def up_alph(self):
        self.head02.setheading(UP)
        self.move(self.ggpaddle02, self.head02)

    def down_arrow(self):
        self.head01.setheading(DOWN)
        self.move(self.ggpaddle01, self.head01)

    def down_alph(self):
        self.head02.setheading(DOWN)
        self.move(self.ggpaddle02, self.head02)
