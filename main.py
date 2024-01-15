import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard
import random

screen = Screen()
turtle = Turtle()
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

paddle_a = Paddle((-350, 0))
paddle_b = Paddle((350, 0))

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    # Keyboard bindings
    screen.listen()
    screen.onkeypress(paddle_a.paddle_up, "w")
    screen.onkeypress(paddle_a.paddle_down, "s")
    screen.onkeypress(paddle_b.paddle_up, "Up")
    screen.onkeypress(paddle_b.paddle_down, "Down")

    # Movement of ball
    ball.move()

    # Ball collision with wall
    ball.bounce_off_walls()
    if ball.distance(paddle_b) < 50 and ball.xcor() > 330 or ball.distance(paddle_a) < 50 and ball.xcor() < -330:
        ball.dx *= -1

    # Detect when ball misses paddles
    if ball.xcor() > 400:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreboard.a_score += 1
        scoreboard.update_scoreboard()


    if ball.xcor() < -400:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreboard.b_score += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
