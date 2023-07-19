from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-290, 250)
        self.color("gray")
        self.write(f"Level:{self.level}", False, "left", FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
