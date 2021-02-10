from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.settiltangle(90)
        self.setheading(90)
        self.goto(position[0], position[1])
        self.shapesize(stretch_wid=100/20, stretch_len=20/20)
        # the turtle is 20x20 pixels,we have to stretch x5 to get 100 height and 1x to get 20 width
        self.color("white")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
