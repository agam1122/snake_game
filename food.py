from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        print(random_x)
        print(random_y)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-350, 350)
        random_y = random.randint(-350, 350)
        self.goto(random_x, random_y)