from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Courier", 40, "bold"))
        self.goto(100, 240)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))

    def update_l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def update_r_point(self):
        self.r_score += 1
        self.update_scoreboard()
