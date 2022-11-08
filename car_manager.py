from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.pu()
        self.color(choice(COLORS))
        self.goto(300, randint(-250, 300))

    def car_move(self, level):
        new_x = self.xcor() - (STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)
        self.goto(new_x, self.ycor())





