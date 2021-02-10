from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up Main Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Instances

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
# Movement Paddle's

screen.listen()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


# Main Loop

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Bounce in the top and bottom wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Bounce with paddle
    if (ball.distance(l_paddle) < 50 and ball.xcor() < - 320) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_paddle()

    # Miss the paddle Right
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Miss the paddle Left
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
