from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)