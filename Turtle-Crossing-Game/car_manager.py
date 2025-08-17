import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SAFE_ZONE = 50
SCREEN_HALF_HEIGHT = 300
SCREEN_HALF_WIDTH = 300
CAR_HEIGHT = 20
CAR_WIDTH = 40
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT=2

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self._tick = 0  # used to spawn a new car every 6th loop

    def _random_y(self):
        return random.randint(-(SCREEN_HALF_HEIGHT - SAFE_ZONE), (SCREEN_HALF_HEIGHT - SAFE_ZONE))

    def _create_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.setheading(180)  # face left
        car.goto(SCREEN_HALF_WIDTH, self._random_y())  # spawn at right edge
        self.all_cars.append(car)

    def level_up(self):
        """Increase car speed when player reaches the finish line."""
        self.move_distance += MOVE_INCREMENT

    def maybe_create_car(self):
        """Create a new car only every 6th loop tick."""
        self._tick = (self._tick + 1) % 6
        if self._tick == 0:
            self._create_car()

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)

    def remove_offscreen(self):
        """Clean up cars that have exited the left side to keep the list small."""
        keep = []
        for car in self.all_cars:
            if car.xcor() > -(SCREEN_HALF_WIDTH + 20):
                keep.append(car)
            else:
                car.hideturtle()
        self.all_cars = keep

