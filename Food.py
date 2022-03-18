import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.newfood()

    def newfood(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
