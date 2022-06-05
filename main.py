from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score_board


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#122223")
screen.tracer(0)


snake = Snake()
snake.create_snake()
food = Food()
score_board = Score_board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


play = True
while play:
    screen.update()
    time.sleep(.1)

    snake.moving()

    if snake.head.distance(food) < 15:
        food.random_place()
        snake.new_part()
        score_board.increase_score()        


    # If snake touches an edge
    snake.touching_an_edge()
    if snake.touching_an_edge():
        score_board.reset()
        snake.reset()
        # play = False


    # snake.touching_the_body() first way:
    # for body_part in snake.snake_body:
    #     if body_part == snake.snake_body[0]:
    #         continue
    #     elif snake.head.distance(body_part) < 5:
    #         snake.game_over()
    #         play = False


    # snake.touching_the_body() second way:
    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 5:
            score_board.reset()
            snake.reset()
            # snake.game_over()
            # play = False

screen.exitonclick()