from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


snake.create_snake()


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with walls
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 370 or snake.head.ycor() < -380:
        is_game_on = False
        scoreboard.game_over()

    # detect collisions with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


    screen.listen()


screen.exitonclick()
