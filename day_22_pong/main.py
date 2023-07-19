import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=1000, height=800)
screen.tracer(0)

score_board = ScoreBoard()

l_paddle = Paddle("left")
r_paddle = Paddle("right")

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeyrelease(l_paddle.stop, "w")
screen.onkeyrelease(l_paddle.stop, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeyrelease(r_paddle.stop, "Up")
screen.onkeyrelease(r_paddle.stop, "Down")

ball = Ball()
ball.reset_ball()
game_over = False
screen.update()
time.sleep(0.5)
while not game_over:
    screen.update()
    ball.move()
    l_paddle.move()
    r_paddle.move()
    # detect missing the ball
    if ball.xcor() < -460 or ball.xcor() > 460:
        if ball.xcor() < -460:  # if the left paddle misses the ball
            score_board.right_score = score_board.right_score + 1
        elif ball.xcor() > 460:  # if the right paddle misses the ball
            score_board.left_score = score_board.left_score + 1
        score_board.update_board()
        ball.reset_ball()
        l_paddle.reset()
        r_paddle.reset()
        screen.update()
        time.sleep(0.5)  # reset the paddles and the balls to their inital position and wait for 0.5 second
    # detect collision with upper and lower walls
    if ball.ycor() > 390 or ball.ycor() < -390:
        ball.bounce_y()
    # detect collision with paddle
    if (ball.xcor() > 420 and ball.distance(r_paddle) < 50) or (ball.xcor() < -420 and ball.distance(l_paddle) < 50):
        ball.bounce_x()


screen.exitonclick()
