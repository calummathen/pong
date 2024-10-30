from turtle import Turtle, Screen

CENTRELINE_START = -250
CENTRELINE_END = 251
CENTRELINE_GAPS = 25
SCORE_COORDS = (0, 190)
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal",)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.color("white")
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0

    def current_scores(self):
        self.clear()
        self.goto(SCORE_COORDS)
        self.write(f"{self.player_1_score}     {self.player_2_score}", False, align=ALIGNMENT, font=FONT)

    def update_scores(self, player):
        if player == 1:
            self.player_1_score += 1
        elif player == 2:
            self.player_2_score += 1
        self.current_scores()
