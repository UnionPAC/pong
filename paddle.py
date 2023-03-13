from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        # Create paddle appearance here
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(start_pos)

    def up(self):
        new_y = self.ycor() + 30
        current_x = self.xcor()
        self.goto(x=current_x, y=new_y)

    def down(self):
        new_y = self.ycor() - 30
        current_x = self.xcor()
        self.goto(x=current_x, y=new_y)
