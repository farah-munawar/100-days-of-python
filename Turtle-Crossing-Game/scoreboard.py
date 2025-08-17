from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.color("black")
        self.goto(0, 260)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 28, "bold"))
