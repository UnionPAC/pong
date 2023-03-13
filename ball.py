from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        # change y position to the inverse of w/e it currently is
        self.y_move *= -1

    def bounce_x(self):
        # change x position to the inverse of w/e it currently is
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()