
from turtle import Turtle, Screen
import random


list_shape = ["circle","turtle","arrow","square","triangle"]



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed(0)
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.color("green")
        self.score = 0

    def pop(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.shape(random.choice(list_shape))
        self.score +=1
        print(f"Your score is {self.score}!")
