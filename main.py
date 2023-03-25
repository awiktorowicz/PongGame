from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1280, height=720)
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_left = Paddle(-600, 0)
paddle_right = Paddle(600, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while (game_is_on):
    time.sleep(0.04)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 570 or ball.distance(paddle_left) < 50 and ball.xcor() < -570:
        ball.bounce_x()
    
    # Detect when paddle misses
    if ball.xcor() > 620:
        ball.reset_position()
        scoreboard.l_point()
        time.sleep(1)

    if ball.xcor() < -620:
        ball.reset_position()
        scoreboard.r_point()
        time.sleep(1)



screen.exitonclick()