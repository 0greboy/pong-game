from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.a_score = 0
        self.b_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.a_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.b_score, align="center", font=("Courier", 80, "normal"))

    def a_point(self):
        self.a_score += 1