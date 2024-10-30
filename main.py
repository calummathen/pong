from turtle import Turtle, Screen
from scorescreen import Score
from paddles import Paddles
from ball import Ball
from board import Board

screen = Screen()
score = Score()
board = Board()
ball = Ball()
player_1 = Paddles(-1)
player_2 = Paddles(1)

screen.tracer(0)
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")

# Create center line
board.center_line()
score.current_scores()


screen.update()
# screen.tracer(1)

screen.listen()
screen.onkey(player_2.up, "Up")
screen.onkey(player_2.down, "Down")
screen.onkey(player_1.up, "w")
screen.onkey(player_1.down, "s")

game_is_on = True

ball.random_start()

while game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 240 or ball.ycor() < -240:
        ball.wall_bounce()
    elif ball.distance(player_1.xcor(), player_1.ycor()) < 30 and ball.xcor() < -370 or ball.distance(player_2.xcor(), player_2.ycor()) < 30 and ball.xcor() > 370:
        ball.paddle_contact()
    elif ball.xcor() <= -400:
        score.update_scores(2)
        ball.random_start()
    elif ball.xcor() >= 400:
        score.update_scores(1)
        ball.random_start()

screen.exitonclick()
