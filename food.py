import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.no_small_food = 0
        self.refresh()


    def refresh(self):
        rand_x = random.randint(-270,270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x , rand_y)
        self.no_small_food += 1

        if self.no_small_food % 3 == 0:
            self.shapesize(stretch_len=1, stretch_wid=1)
            self.color("red")
        else:
            self.shapesize(stretch_len=0.5, stretch_wid=0.5)
            self.color("blue")

    def get_color(self):
        """Returns the current color of the food."""
        return self.color()[0]
