from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

paddle_left = Paddle()
paddle_left.create_paddle()
paddle_left.move(-350, 0)

paddle_right = Paddle()
paddle_right.create_paddle()
paddle_right.move(350, 0)

game_ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_left.goup, "w")
screen.onkey(paddle_left.godown, "s")
screen.onkey(paddle_right.goup, "t")
screen.onkey(paddle_right.godown, "g")

game_on = True
while game_on:
    screen.update()
    time.sleep(game_ball.move_speed)
    game_ball.move()

    # detect collision with walls #

    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_yaxis()

    # detect collision with paddles #

    if (game_ball.distance(paddle_right) < 50 and game_ball.xcor() > 340) or (
            game_ball.distance(paddle_left) < 50 and game_ball.xcor() < -340):
        game_ball.bounce_xaxis()

    # scoreboard op(s) #

    if game_ball.xcor() > 380:
        game_ball.reset_position()
        scoreboard.left_point()

    if game_ball.xcor() < -380:
        game_ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
