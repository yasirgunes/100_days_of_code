from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        car = Turtle("square")
        car.shapesize(stretch_wid=2, stretch_len=1)
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(180)
        x_cor = 300
        y_cor = random.randint(-230, 230)
        car.goto(x_cor, y_cor)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            if car.xcor() < -340:
                car.hideturtle()
                self.cars.remove(car)
            car.forward(self.car_speed)

    def increase_level(self):
        for car in self.cars:  # delete the old cars from screen and from the cars list
            car.hideturtle()
            self.cars.remove(car)
        self.car_speed = self.car_speed + MOVE_INCREMENT  # update the speed

