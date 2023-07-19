import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# No matter how large the project is if you can break it into a small bite-sized chunks so you can tackle them
# And eventually you can tackle the whole project.

# TODO 1: (done)
#  Create a turtle player that starts at the bottom of the screen
#  and listen for the "Up" keypress to move the turtle north.
#  If you get stuck, check the video walkthrough in Step 3.

# TODO 2: (done)
#  Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
#  and move to the left edge of the screen.
#  No cars should be generated in the top and bottom 50px of the screen
#  (think of it as a safe zone for our little turtle).
#  Hint: generate a new car only every 6th time the game loop runs.
#  If you get stuck, check the video walkthrough in Step 4.

# TODO 3: (done)
#  Detect when the turtle player collides with a car and stop the game if this happens.
#  If you get stuck, check the video walkthrough in Step 5.

# TODO 4: (done)
#  Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
#  When this happens, return the turtle to the starting position and increase the speed of the cars.
#  Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.
#  If you get stuck, check the video walkthrough in Step 6.

# TODO 5: (done)
#  Create a scoreboard that keeps track of which level the user is on.
#  Every time the turtle player does a successful crossing, the level should increase.
#  When the turtle hits a car, GAME OVER should be displayed in the centre.
#  If you get stuck, check the video walkthrough in Step 7.


screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing")
screen.tracer(0)
screen.listen()

score_board = Scoreboard()

turtle = Player()
screen.onkey(turtle.move, "Up")

manage_cars = CarManager()
count = 0  # to generate cars every 6 iteration of the game loop

game_is_on = True
while game_is_on:

    # check if the player has crossed the street and made it
    if turtle.is_finished():
        turtle.reset_turtle()  # Take the turtle to the starting position
        manage_cars.increase_level()  # clear the old cars from the screen and increase the speed of the new cars
        score_board.update()  # increment the level on the scoreboard
    # increment the counter
    count += 1

    # in every 6 iteration generate a car and reset the counter
    if count == 6:
        manage_cars.generate_car()
        count = 0

    # detect if the turtle collides with a car
    for car in manage_cars.cars:
        if turtle.distance(car) < 40 and (car.xcor() - turtle.xcor()) < 20:  # that means the turtle collided with a car
            score_board.game_over()
            # print game over to the screen
            screen.update()
            time.sleep(1)
            game_is_on = False  # game over
            continue

    # move all the cars
    manage_cars.move()

    time.sleep(0.1)
    screen.update()
