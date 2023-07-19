from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-10, 360)
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.write("Score", False, "center", ("Arial", 16, "normal"))
        self.goto(-10, 320)
        self.write(f"{self.left_score}\t\t{self.right_score}", False, "center", ("Arial", 20, "normal"))
        while self.ycor() > -360:
            self.goto(0, self.ycor() - 30)
            self.write("|", False, "center", ("Arial", 16, "normal"))

    def update_board(self):
        self.clear()
        self.goto(-10, 360)
        self.write("Score", False, "center", ("Arial", 16, "normal"))
        self.goto(-10, 320)
        self.write(f"{self.left_score}\t\t{self.right_score}", False, "center", ("Arial", 20, "normal"))
        while self.ycor() > -360:
            self.goto(0, self.ycor() - 30)
            self.write("|", False, "center", ("Arial", 16, "normal"))

