from turtle import Turtle
import random

direction = [1, -1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.x_move = 3
        self.y_move = self.random_start()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def random_start(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        random_direction = float(random.choice(direction)) * random.uniform(0.5, 1.2)
        return float(random_direction)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_contact(self):
        self.x_move *= -1
