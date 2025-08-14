from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []

for position in starting_positions:
    t = Turtle('square')
    t.color('white')
    t.penup()
    t.goto(position)
    turtles.append(t)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for i in range(len(turtles) - 1, 0, -1):
        x = turtles[i - 1].xcor()
        y = turtles[i - 1].ycor()
        turtles[i].goto(x, y)

    turtles[0].forward(20)


screen.exitonclick()
