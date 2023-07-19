from turtle import Screen
import time
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Yılan Oyunu")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
screen.update()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.down, "s")
isGameOn = True
while isGameOn:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increment_score()
    # detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
        score_board.update_board()
        snake.reset_snake()
        screen.update()
        time.sleep(0.5)
    # detect collision with the tail
    for segment in snake.segments:
        if snake.head.distance(segment) < 15 and segment != snake.head:
            score_board.update_board()
            snake.reset_snake()
            screen.update()
            time.sleep(0.5)

screen.exitonclick()
