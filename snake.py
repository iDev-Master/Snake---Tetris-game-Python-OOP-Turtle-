from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)


MOVE_DISTANCE = 10
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
XCOOR = [0, -20, -40]
YCOOR = 0

class Snake:
    def __init__(self):
        # creating a snake and its parts of body
        self.snake_body = []
        
        
        # self.create_snake()
    def create_snake(self):
        for item in range(3):
            square = Turtle(shape="square")
            square.color("#fff")
            square.penup()
            square.goto(XCOOR[item], YCOOR)
            self.snake_body.append(square)
        self.head = self.snake_body[0]  



    def reset(self):
        for item in self.snake_body:
            item.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()

    
    # this code adds a new part to the snake, after that eats the food.
    def new_part(self): 
        square = Turtle(shape="square")
        square.color("#fff")
        square.penup()      
        self.snake_body.append(square)


    def moving(self):
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part-1].xcor()
            new_y = self.snake_body[body_part-1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def touching_an_edge(self):
        if (self.head.xcor() > 295) or (self.head.xcor() < -295) or (self.head.ycor() > 295) or (self.head.ycor() < -295):

            # self.game_over()
            # self.
            return True









    def game_over(self): 
        self.stop = Turtle()
        self.stop.hideturtle()
        self.stop.color("white")
        self.stop.write("Game over", align="center", font=("Arial", 20, "normal"))



