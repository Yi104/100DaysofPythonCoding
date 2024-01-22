from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    # detect collision with the paddle
    if ball.distance(l_paddle)<50 and ball.xcor() < -320 or ball.distance(r_paddle)< 50 and ball.xcor() >320:
        ball.bounce_x()


    # detect ball missing on the paddle
    # r paddle misses
    if ball.xcor()>370:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor()<-370:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()