from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def move(self, xcor, ycor):
        self.goto(x=xcor, y=ycor)

    def goup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def godown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
