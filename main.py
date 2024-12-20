from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

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
game_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(0.5)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        if food.get_color() == "red":
            scoreboard.red_score()
        else:
            scoreboard.blue_score()
        food.refresh()
        snake.extend()

        if scoreboard.score % 20 == 0 and scoreboard.score > 0:
            game_speed *= 0.9

    if snake.head.xcor() > 300 :
        snake.head.goto(-300, snake.head.ycor())
    elif snake.head.xcor() < -300:
        snake.head.goto(300, snake.head.ycor())

    if snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()


    for any_segment in snake.segments[1:]:
       if snake.head.distance(any_segment) < 10:
           game_is_on = False
           scoreboard.game_over()


screen.exitonclick()
