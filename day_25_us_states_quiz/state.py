from turtle import Turtle


class State(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state, False, "center", ("Arial", 10, "normal"))

