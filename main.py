from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen of the game
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

#snake created
snake = Snake()

#food created
food = Food()

#scoreboard created
scoreboard = Scoreboard()

#controlling the snake
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

#game started - snake is moving
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    if (snake.head.xcor() > 290 or snake.head.ycor() > 290 or
            snake.head.xcor() < -290 or snake.head.ycor() < -290):
        game_is_on = False
        scoreboard.game_over()

    for any_segment in snake.segments[1:]:
       if snake.head.distance(any_segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()