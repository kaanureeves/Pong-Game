from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed=0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_yaxis(self):
        self.y *= -1

    def bounce_xaxis(self):
        self.x *= -1
        self.move_speed *=0.9

    def reset_position(self):
        self.goto(0,0)
        self.bounce_xaxis()