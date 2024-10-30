from turtle import Turtle
import scorescreen

PADDLE_START = 380
UP = 90
DOWN = 270

class Paddles(Turtle):

    def __init__(self,player):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.setheading(UP)
        self.shapesize(stretch_wid=0.5, stretch_len=3)
        self.goto(player * PADDLE_START, 0)

    def up(self):
        if self.ycor() < scorescreen.CENTRELINE_END - 40:
            self.forward(20)
        else:
            pass

    def down(self):
        if self.ycor() > scorescreen.CENTRELINE_START + 40:
            self.backward(20)
        else:
            pass
