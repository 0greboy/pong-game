from turtle import Turtle

PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
        self.speed(0)
        self.goto(position)


    def paddle_up(self):
        y = self.ycor()
        if y < 240:
            y += 20
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        if y > -240:
            y -= 20
        self.sety(y)


