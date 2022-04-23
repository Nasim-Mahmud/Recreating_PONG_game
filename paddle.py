from turtle import Turtle

turtle1_position = [(300, 0), (300, 20), (300, 40)]
turtle2_position = [(-300, 0), (-300, 20), (-300, 40)]

UP = 90
MOVE = 20
DOWN = 270


class Paddle:
    def __init__(self):
        self.ggpaddle01 = []
        self.ggpaddle02 = []
        self.create_paddle()
        self.head01 = self.ggpaddle01[0]
        self.head02 = self.ggpaddle02[0]

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
        self.ggpaddle01.append(dino)
        self.ggpaddle02.append(dino)

    def move(self):
        for n in range(len(self.ggpaddle01)-1, 0, -1):
            x_pos = self.ggpaddle01[n-1].xcor()
            y_pos = self.ggpaddle01[n-1].ycor()
            self.ggpaddle01[n].goto(x_pos, y_pos)
        self.head01.forward(MOVE)

        for n in range(len(self.ggpaddle02)-1, 0, -1):
            x_pos = self.ggpaddle02[n-1].xcor()
            y_pos = self.ggpaddle02[n-1].ycor()
            self.ggpaddle02[n].goto(x_pos, y_pos)
        self.head02.forward(MOVE)

    def up_arrow(self):
        self.head01.setheading(UP)
        self.move()

    def up_alph(self):
        self.head02.setheading(UP)
        self.move()

    def down_arrow(self):
        self.head01.setheading(DOWN)
        self.move()

    def down_alph(self):
        self.head02.setheading(DOWN)
        self.move()
