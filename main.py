import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from score import score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.forward()

    if snake.segment[0].distance(food) < 15:
        food.newfood()
        scoreboard.score_increment()
        snake.atefood()

    if snake.segment[0].xcor() > 300 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor() > 300 or snake.segment[0].ycor() < -300:
        # print("Hit a wall")
        # is_game_on = False
        scoreboard.game_over()
        snake.new_game()

    for i in snake.segment[3:]:
        if snake.segment[0].distance(i) < 10:
            scoreboard.game_over()
            snake.new_game()


screen.exitonclick()
