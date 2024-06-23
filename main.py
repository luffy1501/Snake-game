import time
import turtle
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score
new_turtle = Turtle()
screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
snake.create_snake()
score = Score()


screen.listen()


screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")

running = True
while running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()>280 or snake.head.ycor() < -280:

        running = False
        score.end()
    for turtle in snake.all_turtle[1:]:

        if snake.head.distance(turtle) < 10:
            running = False
            score.end()

screen.exitonclick()