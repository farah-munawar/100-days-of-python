import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
cars=CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(player.go_up,"Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.maybe_create_car()
    cars.move_cars()
    cars.remove_offscreen()
    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break
    if player.is_at_finish_line():
        player.goto_start()
        cars.level_up()
        scoreboard.increase_level()
screen.exitonclick()