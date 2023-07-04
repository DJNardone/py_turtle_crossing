from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        reduce_traffic = random.randint(1, 6)
        if reduce_traffic == 1:
            start_y = random.randrange(-240, 250, 10)
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1.0, stretch_len=2.0, outline=1)
            new_car.goto(300, start_y)
            self.all_cars.append(new_car)

    def move(self):
        for c in self.all_cars:
            c.backward(STARTING_MOVE_DISTANCE)
