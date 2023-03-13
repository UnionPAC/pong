from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Init Left paddle (1 player game: CPU, 2 player game: Player 2)
left_paddle = Paddle((-350, 0))

# Init Right paddle (always Player 1)
right_paddle = Paddle((350, 0))

# Init Ball
ball = Ball()

# Init scoreboard
score = Score()

# Listen for key events
screen.listen()

# Player 1: User controls right paddle (right_paddle)
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# Player 2 or CPU: User controls left paddle (left_paddle)
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle miss
    if ball.xcor() > 380:
        score.left_point()
        ball.reset_pos()

    # Detect when l_paddle miss:
    if ball.xcor() < -380:
        score.right_point()
        ball.reset_pos()

screen.exitonclick()
