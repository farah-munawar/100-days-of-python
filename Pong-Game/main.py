from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((250, 0))
l_paddle = Paddle((-250, 0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 230) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -230):
        ball.bounce_x()

    if ball.xcor() > 300:
        scoreboard.l_point()
        ball.reset_position()
    if ball.xcor() < -300:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
