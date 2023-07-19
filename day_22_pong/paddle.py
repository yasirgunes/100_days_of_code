from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, s):
        super().__init__()
        self.way = s
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.move_up = False
        self.move_down = False
        if s == "left":
            self.goto(-450, 0)
        elif s == "right":
            self.goto(450, 0)
        else:
            print("You entered wrong direction! enter 'left' or 'right'")

    def up(self):
        self.move_up = True
        self.move_down = False
        # self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        # self.goto(self.xcor(), self.ycor() - 20)
        self.move_up = False
        self.move_down = True

    def stop(self):
        self.move_up = False
        self.move_down = False

    def move(self):
        if self.move_up:
            self.goto(self.xcor(), self.ycor() + 30)

        elif self.move_down:
            self.goto(self.xcor(), self.ycor() - 30)

    def reset(self):
        if self.way == "left":
            self.goto(-450, 0)
        elif self.way == "right":
            self.goto(450, 0)




