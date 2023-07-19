from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(self.move_speed)

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()  # to start the ball directing to the paddle who won the score
        self.x_move = 10
        self.y_move = 10

    def bounce_y(self):
        self.y_move *= -1.1

    def bounce_x(self):
        self.x_move *= -1.1

