from turtle import Turtle
import random

# from paddle import Paddle

# paddle = Paddle()

# from main import paddle_a, paddle_b
#

turtle = Turtle()



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.dy = None
        self.dx = None
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

        self.set_random_direction()
    #
    def set_random_direction(self):
        # Randomly choose either 1 or -1 for x and y directions
        self.dx = random.choice([1, -1]) * 0.3  # Adjust the speed as needed
        self.dy = random.choice([1, -1]) * 0.3

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_off_walls(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1  # Reverse the y direction upon hitting the top or bottom walls
        # if self.xcor() > 330 and paddle.ycor() < self.ycor() < paddle.ycor()+5  or self.xcor() < -330 and paddle.ycor() < self.ycor() < paddle.ycor()+5:
        #     self.dx *= -1



            # turtle.color("WHITE")
            # turtle.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

