import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

y_positions = [125, 75, 25, -25, -75, -125]
all_turtles = []

for i in range(6):
    t = Turtle(shape='turtle')
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)

        if racer.xcor() > 230:
            is_race_on = False
            winning_colour = racer.pencolor()
            if user_bet and winning_colour.lower() == user_bet.lower():
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_colour} turtle won.")

screen.exitonclick()
