from turtle import Turtle

CENTRELINE_START = -250
CENTRELINE_END = 251
CENTRELINE_GAPS = 25
SCORE_COORDS = (0, 190)


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.2)
        self.penup()
        self.color("white")
        self.hideturtle()

    def center_line(self):
        for y_pos in range(CENTRELINE_START, CENTRELINE_END, CENTRELINE_GAPS):
            self.goto(0, y_pos)
            self.stamp()
