from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for y in POSITIONS:
            self.snakes(y)

    def snakes(self, y):
        new_snake = Turtle('square')
        new_snake.color('white')
        new_snake.penup()
        new_snake.goto(y)
        self.snake_body.append(new_snake)

    def extend(self):
        self.snakes(self.snake_body[-1].position())

    def move(self):
        for x in range(len(self.snake_body) - 1, 0, -1):
            xcor = self.snake_body[x - 1].xcor()
            ycor = self.snake_body[x - 1].ycor()
            self.snake_body[x].goto(xcor, ycor)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
