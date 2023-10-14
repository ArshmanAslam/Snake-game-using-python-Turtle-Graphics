from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('SNAKE GAME PYTHON')
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
# listening For Keyboard Inputs From user
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 14:
        score.score_cal()
        snake.extend()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() < -280 or snake.head.ycor() > 280:
        game = False
        score.game_over()

    for x in snake.snake_body[1:]:
        if snake.head.distance(x) < 10:
            score.game_over()
            game = False

screen.exitonclick()
