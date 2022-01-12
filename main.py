from turtle import Turtle, Screen
from board_settings import Board
from ball import Ball
import time
from paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

board = Board()
ball = Ball()
paddle_a = Paddle((-380, 0))
paddle_b = Paddle((380, 0))


screen.listen()
screen.onkey(paddle_a.move_up, "w")
screen.onkey(paddle_a.move_down, "s")
screen.onkey(paddle_b.move_up, "Up")
screen.onkey(paddle_b.move_down, "Down")



game_on = True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.distance(paddle_b) < 50 and ball.xcor() > 340:
        ball.bounce_pad()

    if ball.distance(paddle_a) < 50 and ball.xcor() < -340:
        ball.bounce_pad()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    elif ball.xcor() < -400:
        board.add_score_player_b()
        ball.home()


    elif ball.xcor() > 400:
        board.add_score_player_a()
        ball.home()
    if board.player_1_score == 5:
        board.player_1_win()
        game_on = False
    if board.player_2_score == 5:
        board.player_2_win()
        game_on = False





















screen.exitonclick()