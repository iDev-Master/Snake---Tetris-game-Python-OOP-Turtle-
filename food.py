from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("triangle")
        self.color("blue")
        self.shapesize(.7)
 

    def random_place(self):
        newx = random.randint(-280, 280)
        newy = random.randint(-280, 280)
        self.goto(newx, newy)




