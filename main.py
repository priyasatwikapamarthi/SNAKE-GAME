from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("SNAKE GAME🐍🐍")

screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game = True


while game:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()
    #Detect collision with food.
    if food.distance(snake.turtles[0]) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    #Detect collision with wall
    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-280 or snake.turtles[0].ycor()>280 or snake.turtles[0].ycor()<-280 :
        game = False
        score_board.game_over()
    #Detect collision with tail
    # if head collides with any segment in tail then trigger game over sequence
    for segments in snake.turtles[1:] :
        if snake.turtles[0].distance(segments) < 10 :
            game = False
            score_board.game_over()





screen.exitonclick()

